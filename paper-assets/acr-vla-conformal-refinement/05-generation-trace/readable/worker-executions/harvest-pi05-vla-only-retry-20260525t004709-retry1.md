# harvest pi05 vla only retry 20260525T004709 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_retry1.log`
- **Structured JSON:** [`152afc18450f7549800d.json`](../../sessions/15/152afc18450f7549800d.json)

## Before a recorded user message

98 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "9079f5e8-13e3-46ba-be2b-116017276dbf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779682200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "943d4d44-b16b-4541-92b0-989392f6403e",
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "44ebd854-b4b2-4a36-8742-5aee667c1f5b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Rzh12sm5ZKXt6Fu3HxSD3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14836,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14836
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019vPPxj6q76Xmw2gREFnKfQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "9d375bcb-f3ad-48bd-b974-570a877b9338",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Rzh12sm5ZKXt6Fu3HxSD3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14836,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14836
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

_source line 6 · 2026-05-25T00:47:30.604Z_

<details><summary>↩ Tool result · `toolu_019vPPxj6q76Xmw2gREFnKfQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "907b2f2f-8d87-4377-bac9-8f78cc0dd27d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "2edef2d8-ae3a-41cb-b977-a650cd58b350",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RuvqJRbLqD4eHosF7CxWo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17169,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17169
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28743
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01UrqUE46mt1geWW5HaRfpEN`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id_contains": "pi05"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "e934d485-ae0b-4f93-b3fe-86fb5610dfc8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RuvqJRbLqD4eHosF7CxWo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17169,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17169
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28743
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_019BhmNqGoRz54LyDnigxEaW`</summary>

```json
{
  "server": "bjb1-32546",
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
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "51a092dc-296a-436a-b8b6-853f851166cd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RuvqJRbLqD4eHosF7CxWo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17169,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17169
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28743
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_013yE62exh8NKs1TrgqK1EZj`</summary>

```json
{
  "server": "bjb1-18228",
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
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "4ceb1022-10d7-4e60-aba7-7df8ec436c7b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RuvqJRbLqD4eHosF7CxWo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17169,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17169
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28743
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T00:47:37.842Z_

<details><summary>↩ Tool result · `toolu_01UrqUE46mt1geWW5HaRfpEN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5489}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "37df37a6-f24e-463d-8d7a-91f65f6f97b0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5489}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5489}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T00:47:38.826Z_

<details><summary>↩ Tool result · `toolu_019BhmNqGoRz54LyDnigxEaW`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "7fbcbed4-3234-4620-8aae-b62b8ccead03",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T00:47:39.565Z_

<details><summary>↩ Tool result · `toolu_013yE62exh8NKs1TrgqK1EZj`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "ade76d52-cda1-4f5f-ae0e-fc80b82110d9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "69569dd6-d1b1-4353-b682-24f3554c3cf5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013zGCGDv1JZsU7CaK2k5TWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 33503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EgKJzbM3sfyfMVoig8XDEw`</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "f3e8c725-2730-473b-84ec-574d5256aa75",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013zGCGDv1JZsU7CaK2k5TWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 33503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
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

_source line 16 · 2026-05-25T00:47:45.707Z_

<details><summary>↩ Tool result · `toolu_01EgKJzbM3sfyfMVoig8XDEw`</summary>

```text
Error: result (496,350 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "4251e0a0-c170-4e64-a872-50196d059277",
  "tool_use_result": {
    "content": "Error: result (496,350 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T00:44:07.720Z\", \"updated_at\": \"2026-05-25T00:46:32.035Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 45, 20 rollouts). Replicate seed for variance estimation.\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T00:44:04.114Z\", \"updated_at\": \"2026-05-25T00:46:23.539Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 44, 20 rollouts). Replicate seed for variance estimation.\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T00:43:50.844Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 43, 20 rollouts). Replicate seed for variance estimation.\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-k2-tau015-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T21:37:19.297Z\", \"updated_at\": \"2026-05-25T00:42:00.480Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.15 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:20.358Z\", \"updated_at\": \"2026-05-25T00:37:52.191Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal (seed 43, 20 rollouts). Replicate seed for variance estimation.\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:16.938Z\", \"updated_at\": \"2026-05-25T00:37:45.363Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal (seed 42, 20 rollouts). Establishes pi0.5 goal-conditioned baseline for ablation against conformal refinement.\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:23.924Z\", \"updated_at\": \"2026-05-25T00:37:38.379Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object (seed 42, 20 rollouts). Establishes pi0.5 object-manipulation baseline.\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:13.434Z\", \"updated_at\": \"2026-05-25T00:37:31.347Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 43, 20 rollouts). Replicate seed for variance estimation of pi0.5 baseline.\", \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:17:09.880Z\", \"updated_at\": \"2026-05-25T00:35:32.912Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial (seed 42, 20 rollouts). Establishes pi0.5 baseline success rate without conformal refinement, for comparison against reconvla/adaptive modes. Tests whether evaluate.py correctly handles --model pi05 with obs_dim=2048.\", \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:39.365Z\", \"updated_at\": \"2026-05-25T00:35:13.584Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Goal seed48 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:35.264Z\", \"updated_at\": \"2026-05-25T00:35:09.845Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Spatial seed49 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:31.569Z\", \"updated_at\": \"2026-05-25T00:35:06.130Z\", \"hypothesis\": \"SmolVLA crm_obs_only baseline on LIBERO-Spatial seed48 with K=10, max_norm=0.05. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-k10-tau025-spatial-s47\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T00:24:29.423Z\", \"updated_at\": \"2026-05-25T00:25:01.112Z\", \"hypothesis\": \"Re-run s47 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Ensures uniform K=10 + same-server across all 8 seeds for valid paired t-test.\"}, \"eval-k10-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-25T00:03:58.063Z\", \"updated_at\": \"2026-05-25T00:24:55.081Z\", \"hypothesis\": \"Re-run s46 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Audit confirmed s46 used K=2. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\"}, \"eval-k10-tau025-spatial-s45\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T00:24:16.535Z\", \"updated_at\": \"2026-05-25T00:24:48.372Z\", \"hypothesis\": \"Re-run s45 Adaptive Conformal with K=10 (τ=0.25) on Spatial on cqa1-32758 for same-server pairing. Previous s45 data likely from K=2 run. Ensures uniform K=10 across all 8 seeds for valid paired t-test.\"}, \"eval-supp-long-vla-only-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:21:06.247Z\", \"updated_at\": \"2026-05-24T23:58:15.416Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Long seed43 (re-run after previous killed). Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42-bjb1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:21:02.585Z\", \"updated_at\": \"2026-05-24T23:58:01.748Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal seed42, parallel re-run on bjb1 (original at cqa1-32758 still running). Provides redundant data for Table 1.\", \"conclusion\": \"failed\"}, \"crm-norm005-goal-s49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:18.196Z\", \"updated_at\": \"2026-05-24T23:57:07.110Z\", \"hypothesis\": \"SmolVLA CRM (obs_only, ε=0.05) on LIBERO-Goal seed49. Fills CRM coverage gap for Table 1.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:13.529Z\", \"updated_at\": \"2026-05-24T23:56:53.275Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed44. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"failed\"}, \"crm-norm005-object-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:08.294Z\", \"updated_at\": \"2026-05-24T23:56:39.546Z\", \"hypothesis\": \"SmolVLA CRM (obs_only, ε=0.05) on LIBERO-Object seed48. Fills CRM coverage gap for Table 1.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:19:02.892Z\", \"updated_at\": \"2026-05-24T23:56:25.825Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed43. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:18:57.232Z\", \"updated_at\": \"2026-05-24T23:56:12.064Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object seed42. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"failed\"}, \"eval-supp-long-vla-only-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:42:16.585Z\", \"updated_at\": \"2026-05-24T23:55:58.423Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 48. Long baseline sweep is complete for s42-s47; s48 extends to high seed for additional statistical power on the hardest benchmark.\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:42:13.100Z\", \"updated_at\": \"2026-05-24T23:55:44.927Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 50. Extension high seed beyond s42-s49 sweep for additional Goal baseline statistical power; pairs with potential future Adaptive Goal s50.\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:38:56.218Z\", \"updated_at\": \"2026-05-24T23:55:31.142Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 44. Goal baseline sweep missing s42-s47; s44 completes mid-range seeds for paired Adaptive vs VLA-only comparison on Goal.\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-vla-only-smolvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:37:31.823Z\", \"updated_at\": \"2026-05-24T23:55:17.604Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Spatial seed 42. Re-deploy after PREPARING-stuck entry on bjb1-18228 (which actually ran pi05 not smolvla). Missing smolvla spatial s42 baseline for paired CRM/Adaptive comparisons at seed 42.\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:35:37.364Z\", \"updated_at\": \"2026-05-24T23:55:03.748Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 43. Replicate seed for Goal baseline variance estimation; needed to support paired Adaptive vs VLA-only statistical comparison.\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:35:31.683Z\", \"updated_at\": \"2026-05-24T23:54:50.151Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal seed42. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:21:02.532Z\", \"updated_at\": \"2026-05-24T23:52:12.038Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43. Cross-architecture validation without CRM.\", \"notes\": \"INVALID: CUDA OOM crash. alphabet_soup 任务整批 0/20，cream_cheese 受影响降至 70%，导致 overall 86.5% (173/200) 偏低。日志中明确出现 torch.OutOfMemoryError。不要将此结果用于替换 r4 (98.5%)。详见 artifacts/.../pi05_object_s43_investigation.md\"}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:20:54.180Z\", \"updated_at\": \"2026-05-24T23:51:38.741Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:20:50.109Z\", \"updated_at\": \"2026-05-24T23:51:19.479Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s43. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:20:44.991Z\", \"updated_at\": \"2026-05-24T23:51:12.305Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s42. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:20:41.402Z\", \"updated_at\": \"2026-05-24T23:51:04.205Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s43. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T18:20:36.642Z\", \"updated_at\": \"2026-05-24T23:50:49.328Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s42. Cross-architecture validation without CRM.\"}, \"eval-k2-tau010-015-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:58:23.211Z\", \"updated_at\": \"2026-05-24T23:40:15.510Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 then τ=0.15 serial on Spatial s42. K=2 matches Table 1 production setting. Retry after tmux name conflict with previous attempt.\", \"conclusion\": \"killed\"}, \"eval-k2-tau010-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:37:15.675Z\", \"updated_at\": \"2026-05-24T23:40:10.067Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting; K=10 τ-sweep results not directly comparable. Expect high trigger rate similar to K=10 τ=0.10 (75.2%).\", \"conclusion\": \"killed\"}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T21:37:30.605Z\", \"updated_at\": \"2026-05-24T23:39:35.840Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.30 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\"}, \"eval-k2-tau020-spatial-s42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T21:37:23.017Z\", \"updated_at\": \"2026-05-24T23:39:28.854Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\"}, \"eval-k2-tau010-spatial-s42-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T23:28:29.356Z\", \"updated_at\": \"2026-05-24T23:39:13.638Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.10 Adaptive Conformal on Spatial s42. Retry after first attempt failed (conda not activated). Expect high trigger rate at low τ.\"}, \"eval-k2-tau035-spatial-s42\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T21:37:34.357Z\", \"updated_at\": \"2026-05-24T23:38:51.566Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\"}, \"eval-k2-tau025-spatial-s42\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T21:37:27.015Z\", \"updated_at\": \"2026-05-24T23:38:37.183Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.25 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\"}, \"train-crm-pi05-unified-3suite-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:38:31.224Z\", \"updated_at\": \"2026-05-24T23:37:22.059Z\", \"hypothesis\": \"π0.5 unified 3-suite (Spatial+Goal+Object) CRM training retry with batch_size=256 (was 32). D135: Long dropped due to DDL. obs_dim=2048, ~194K samples, 50 epochs. Parent killed due to 55h ETA; bs256 targets ~7-8h.\", \"parent\": \"train-crm-pi05-unified-3suite\", \"metrics\": {\"current_epoch\": 25, \"total_epochs\": 50, \"best_val_loss\": 0.004854, \"best_epoch\": 24, \"train_loss_latest\": 0.00844, \"progress_pct\": 50}, \"conclusion\": \"failed\", \"notes\": \"2026-05-24T23:35: 进程 PID 326315 仍在 bjb1-18228 上运行 (13h+, 状态 Rl)。外层 wrapper PID 326314 被 timeout SIGKILL 导致 cron 误判为 failed，但内层 Python 训练未受影响继续运行。Registry 状态机阻止 DONE→RUNNING 回退。实际应为 RUNNING。等待进程完成后需要手动 harvest metrics 和更新 conclusion。\"}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:35:45.687Z\", \"updated_at\": \"2026-05-24T23:35:24.629Z\", \"hypothesis\": \"VLA-only baseline seed 49 on Spatial. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:35:42.276Z\", \"updated_at\": \"2026-05-24T23:35:16.650Z\", \"hypothesis\": \"VLA-only baseline seed 48 on Spatial. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:36:00.263Z\", \"updated_at\": \"2026-05-24T23:35:09.744Z\", \"hypothesis\": \"VLA-only baseline seed 49 on Object. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:35:56.801Z\", \"updated_at\": \"2026-05-24T23:35:02.816Z\", \"hypothesis\": \"VLA-only baseline seed 48 on Object. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:35:52.328Z\", \"updated_at\": \"2026-05-24T23:34:55.908Z\", \"hypothesis\": \"VLA-only baseline seed 49 on Goal. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:35:48.983Z\", \"updated_at\": \"2026-05-24T23:34:48.590Z\", \"hypothesis\": \"VLA-only baseline seed 48 on Goal. Paired baseline for Adaptive seed extension, enabling 8-seed statistical comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-pi05-reconvla-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T18:17:30.670Z\", \"updated_at\": \"2026-05-24T23:27:42.594Z\", \"hypothesis\": \"π0.5 ReconVLA baseline on Spatial s42. Cross-architecture comparison.\", \"notes\": \"2026-05-24T21:15: CRASHED — CUDA OOM on GPU 0 (other process占用14.3GiB). 需要在空闲GPU上重启或用bf16加载。Goal(GPU2)和Object(GPU3)仍在运行。\"}, \"eval-canonical-vla-only-spatial-s44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:23:56.279Z\", \"updated_at\": \"2026-05-24T23:24:09.516Z\", \"hypothesis\": \"Canonical VLA-only Spatial baseline s44 on cqa1-32758. Fills missing same-server pair for s44 Adaptive K=10. Without this, s44 cannot be included in same-server paired t-test.\"}, \"eval-canonical-adaptive-k10-spatial-s49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:05:04.837Z\", \"updated_at\": \"2026-05-24T23:07:40.478Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s49. Eliminates cross-server confound.\"}, \"eval-canonical-adaptive-k10-spatial-s48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:05:01.412Z\", \"updated_at\": \"2026-05-24T23:07:34.058Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s48. Eliminates cross-server confound.\"}, \"eval-canonical-adaptive-k10-spatial-s44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:04:57.826Z\", \"updated_at\": \"2026-05-24T23:07:27.600Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s44. Eliminates cross-server confound.\"}, \"eval-canonical-adaptive-k10-spatial-s43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:04:54.331Z\", \"updated_at\": \"2026-05-24T23:07:21.190Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s43. Eliminates cross-server confound.\"}, \"eval-canonical-adaptive-k10-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T23:04:50.613Z\", \"updated_at\": \"2026-05-24T23:07:12.798Z\", \"hypothesis\": \"Canonical same-server Adaptive K=10 on cqa1-32758 Spatial s42. Eliminates cross-server confound — paired with cqa1 VLA-only baseline for clean paired t-test.\"}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T21:18:42.872Z\", \"updated_at\": \"2026-05-24T22:43:17.422Z\", \"hypothesis\": \"K=1 Adaptive Conformal on Spatial s42 at τ=0.20. Single-sample correction vs K=10 multi-sample centering — if K=1 SR is lower, it supports the claim that multi-sample centering improves correction quality by reducing noise in the correction vector.\", \"conclusion\": \"success\", \"notes\": \"K=1 Adaptive eval completed on bjb2-28827. Metrics need harvesting from log. K=1 single-sample correction baseline for K-sweep comparison.\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T22:41:44.799Z\", \"updated_at\": \"2026-05-24T22:43:11.837Z\", \"hypothesis\": \"K=5 Adaptive Conformal on Spatial s42 at default τ. K-sweep data point: K=5 vs K=1/K=2/K=10 to characterize multi-sample centering effect on correction quality.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"K\": 5, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau045-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:19:38.025Z\", \"updated_at\": \"2026-05-24T21:19:38.025Z\", \"hypothesis\": \"τ=0.45 Adaptive Conformal on Spatial s42. Upper bound of τ-sweep — expect near-zero triggering and SR ≈ VLA-only, confirming the method gracefully degrades to no-correction when threshold is high.\"}, \"eval-tau040-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:19:34.135Z\", \"updated_at\": \"2026-05-24T21:19:34.135Z\", \"hypothesis\": \"τ=0.40 Adaptive Conformal on Spatial s42. Extends τ-sweep above τ=0.35 to map the high-τ tail where triggering approaches zero and SR converges to VLA-only baseline.\"}, \"eval-tau005-spatial-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:19:29.650Z\", \"updated_at\": \"2026-05-24T21:19:29.650Z\", \"hypothesis\": \"τ=0.05 Adaptive Conformal on Spatial s42. Extends τ-sweep below τ=0.10 to test if extremely low threshold causes excessive triggering and further SR degradation (τ=0.10 already showed 75.2% trigger rate hurting SR).\"}, \"eval-spatial-vla-only-s42-verify\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T21:18:39.345Z\", \"updated_at\": \"2026-05-24T21:18:54.961Z\", \"hypothesis\": \"Verification rerun of SmolVLA VLA-only on Spatial s42. Previous run (eval-supp-spatial-vla-only-smolvla-s42) had abnormal wall_clock=3.14h suggesting possible π0.5 model contamination. This clean rerun on bjb1-32546 confirms SmolVLA baseline SR for matched-seed Table 1.\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:55:45.292Z\", \"updated_at\": \"2026-05-24T20:19:27.802Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Long seed43. Fills Table 1 data gap for multi-seed statistical analysis.\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-s50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T20:05:57.926Z\", \"updated_at\": \"2026-05-24T20:06:05.928Z\", \"hypothesis\": \"SmolVLA Object VLA-only baseline with seed 50 — additional seed for supplementary table robustness (seeds 44-49 complete, s42/43 missing, s50 adds coverage)\"}, \"eval-pi05-reconvla-spatial-s42-bf16\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T20:05:43.561Z\", \"updated_at\": \"2026-05-24T20:05:50.394Z\", \"hypothesis\": \"π0.5 reconvla spatial baseline with bf16 inference to avoid OOM on RTX 4090 D (24GB). Original fp32 run OOM'd on bjb2-28827 cuda:1. bf16 should halve model memory (~7GB→3.5GB) while maintaining eval accuracy.\"}, \"eval-supp-object-vla-only-s50\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-24T19:37:28.266Z\", \"updated_at\": \"2026-05-24T19:42:53.935Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Object seed 50. Extension seed beyond s42-49 sweep for additional statistical power in Object benchmark.\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:29.087Z\", \"updated_at\": \"2026-05-24T19:38:59.701Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal seed 45. Goal baseline sweep missing s42-s47; s45 fills another mid-range seed.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果文件: logs/eval_goal_vla_only_seed45.json\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:32.639Z\", \"updated_at\": \"2026-05-24T19:37:22.638Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 45. Fills missing seed in Long baseline sweep (s42/s43/s46 done).\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-24T19:37:17.731Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:56:22.838Z\", \"updated_at\": \"2026-05-24T19:35:25.978Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Spatial seed 42. Missing seed in 7-seed baseline sweep (s43-s49 done); s42 completes the seed=42 baseline used for paired CRM/Adaptive comparisons. Re-deploy after PREPARING-stuck entry on bjb1-18228.\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:54:05.881Z\", \"updated_at\": \"2026-05-24T19:33:21.937Z\", \"hypothesis\": \"π0.5 VLA-only baseline re-test with official settings: n_action_steps=10, 10 dummy steps with gripper-open, per-suite max_steps=280\", \"parent\": \"eval-pi05-vla-only-object-seed43-r3\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}, \"notes\": \"98.5% (197/200) 已核实有效。带 --n_action_steps 10 (chunked open-loop) 评估，与 s42-r4=100%、s44-r4=99.5% 横向一致。与 r3 (81.5%) 的 17pp 差距是评估范式 (closed-loop vs chunked) 而非 bug。bjb2-28827 上的 v2 重跑 (86.5%) 是 CUDA OOM 崩溃产物 (alphabet_soup 整批 0/20)，已判废。Baseline 对比时务必范式一致。详见 artifacts/.../pi05_object_s43_investigation.md\"}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:56:27.183Z\", \"updated_at\": \"2026-05-24T19:30:43.680Z\", \"hypothesis\": \"VLA-only baseline seed=50 on Object. Additional seed to strengthen 8+ seed statistical comparison for Adaptive vs VLA-only on the weakest-delta suite.\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:38.804Z\", \"updated_at\": \"2026-05-24T19:15:04.682Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 49 on Object. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:35.331Z\", \"updated_at\": \"2026-05-24T19:15:00.439Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 48 on Object. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-pi05-reconvla-object-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T18:17:39.327Z\", \"updated_at\": \"2026-05-24T18:24:33.207Z\", \"hypothesis\": \"π0.5 ReconVLA baseline on Object s42. Cross-architecture comparison.\"}, \"eval-pi05-reconvla-goal-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T18:17:34.087Z\", \"updated_at\": \"2026-05-24T18:24:26.298Z\", \"hypothesis\": \"π0.5 ReconVLA baseline on Goal s42. Cross-architecture comparison.\"}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:31.614Z\", \"updated_at\": \"2026-05-24T18:13:08.707Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 49 on Goal. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:28.081Z\", \"updated_at\": \"2026-05-24T18:13:01.700Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 48 on Goal. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:24.486Z\", \"updated_at\": \"2026-05-24T18:12:54.817Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 49 on Spatial. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"trigger_rate\": 0.195, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:35:20.958Z\", \"updated_at\": \"2026-05-24T18:12:47.985Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed 48 on Spatial. Additional seed for 8-seed mean±std to strengthen claim that Adaptive > VLA-only across all suites.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.198, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:16.467Z\", \"updated_at\": \"2026-05-24T18:12:40.045Z\", \"hypothesis\": \"Adaptive CRM with K=1 (pure CRM correction when gating triggers, no conformal selection) on Spatial τ=0.25. K=1 removes the multi-sample selection benefit, isolating the CRM correction quality. Expected SR lower than K=2 if conformal selection adds value.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.197, \"tau\": 0.25, \"K\": 1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-crm-obj-s47-reeval\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:13.035Z\", \"updated_at\": \"2026-05-24T18:12:33.152Z\", \"hypothesis\": \"CRM Object s47 re-eval to verify anomalous 82.5% SR (+2.6σ above 3-seed mean). If reproducible, it's a genuine high-variance seed; if not, original was a lucky run and should be excluded or noted.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:09.697Z\", \"updated_at\": \"2026-05-24T18:12:26.456Z\", \"hypothesis\": \"Adaptive CRM with τ=0.30 on Spatial should show very low trigger rate (<10%) and SR close to VLA-only, mapping the right tail of the inverted-U curve where gating rarely activates.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.167, \"tau\": 0.3, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:06.328Z\", \"updated_at\": \"2026-05-24T18:12:19.371Z\", \"hypothesis\": \"Adaptive CRM with τ=0.20 on Spatial should be near the optimal range (τ∈[0.15,0.25] from Goal sweep), confirming the inverted-U shape generalizes across suites with different trigger rate distributions.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.266, \"tau\": 0.2, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:02.885Z\", \"updated_at\": \"2026-05-24T18:12:12.445Z\", \"hypothesis\": \"Adaptive CRM with τ=0.10 on Spatial (highest trigger rate ~20%) should show high trigger rate (~70-80%) and potentially lower SR due to over-correction, mapping the left side of the inverted-U τ curve already observed on Goal suite.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.79, \"trigger_rate\": 0.752, \"tau\": 0.1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-adapt-tau025-obj-s50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T17:33:43.483Z\", \"updated_at\": \"2026-05-24T17:33:59.373Z\", \"hypothesis\": \"Adaptive CRM τ=0.25 seed=50 on Object. Additional seed paired with VLA-only s50 to strengthen 8+ seed statistical comparison on the weakest-delta suite.\"}, \"eval-supp-long-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T12:13:15.130Z\", \"updated_at\": \"2026-05-24T17:33:34.380Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 retry. Previous attempt failed. Extends Long Adaptive coverage for seed variance analysis.\", \"parent\": \"eval-supp-long-adapt-tau025-s47\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"trigger_rate\": 0.037, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-adaptive-k5-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T15:11:21.960Z\", \"updated_at\": \"2026-05-24T16:55:43.337Z\", \"hypothesis\": \"Adaptive CRM with K=5 (5 VLA samples when gating triggers, conformal ranking selects best) on Spatial τ=0.25. K=5 vs K=2 tests whether more samples improve selection quality. Diminishing returns expected if K=2 already captures enough diversity.\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:52:10.417Z\", \"updated_at\": \"2026-05-24T15:53:54.976Z\", \"hypothesis\": \"Long s47 K=2 mean baseline for seed extension (r2 on bjb2-28827). Sixth seed to tighten CI for Long suite K2mean method.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545, \"successes\": 109, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"note\": \"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\"}}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:58:57.165Z\", \"updated_at\": \"2026-05-24T15:04:00.999Z\", \"hypothesis\": \"ReconVLA reconstruction-based baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the reconvla baseline.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.78, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_rollouts\": 200, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T14:20:41.900Z\", \"updated_at\": \"2026-05-24T14:22:05.390Z\", \"hypothesis\": \"A1 VLA baseline evaluated under our LIBERO framework should reproduce near-official performance (99.8% SR on LIBERO-Object); a large gap would indicate systematic evaluation framework differences rather than model issues.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.565, \"total_successes\": 113, \"total_episodes\": 200, \"official_reported_sr\": 0.998, \"gap_vs_official\": -0.433, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.35, \"salad_dressing\": 0.35, \"bbq_sauce\": 0.8, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 0.65, \"milk\": 0.1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.25}}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:31:12.366Z\", \"updated_at\": \"2026-05-24T14:10:31.599Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline, third re-run after r2/r3 were killed for CRM training priority. Fills Long s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-long-vla-only-s47-r3\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.595, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-obj-k2mean-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T11:34:09.989Z\", \"updated_at\": \"2026-05-24T13:49:16.189Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed47 retry. Previous attempt failed. Extends Object K2mean coverage.\", \"conclusion\": \"failed\", \"notes\": \"True failure: process only initialized, no rollout completed. Likely caused by M083 output_file conflict (same JSON as vla-only). Now fixed in evaluate.py.\"}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T11:33:00.893Z\", \"updated_at\": \"2026-05-24T13:48:42.228Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed47 retry. Previous attempt failed. Extends Object Adaptive coverage.\", \"notes\": \"model_name correction: SmolVLA (not OpenVLA).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"trigger_rate\": 0.0403, \"crm_applied_steps\": 1458}}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T11:32:02.181Z\", \"updated_at\": \"2026-05-24T13:46:59.445Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed47 retry. Previous attempt failed. Extends Object CRM coverage.\", \"notes\": \"model_name correction: SmolVLA (not OpenVLA).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825}}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T11:30:59.839Z\", \"updated_at\": \"2026-05-24T13:46:52.447Z\", \"hypothesis\": \"VLA-only baseline on Object suite seed47 retry. Previous attempt failed. Extends Object VLA-only coverage for 6th seed variance analysis.\", \"notes\": \"model_name correction: SmolVLA (not OpenVLA). K=1 (vla_only single inference baseline).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T13:41:56.251Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"note\": \"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\"}, \"notes\": \"DUPLICATE of eval-supp-spatial-k2mean-s47 (different naming). JSON overwritten by vla-only run. SR=81% (162/200) per log. BUG FIX: evaluate.py patched on all servers — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:58:43.441Z\", \"updated_at\": \"2026-05-24T13:41:05.475Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial at seed 47 for seed-extension coverage. Extends 3-seed mean to 4th seed.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"total_successes\": 162, \"total_trials\": 200, \"per_task_range\": \"0.0-1.0\", \"worst_task\": \"pick_up_black_bowl_on_ramekin (0/20)\", \"best_tasks\": \"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\"}, \"notes\": \"K value: Registry spec shows --K 2 but VLA-only mode always executes as K=1 (single inference baseline). --K flag is ignored in vla_only mode. This is correct behavior, spec template error.\"}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-24T13:40:50.369Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T13:40:40.698Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"successes\": 163, \"total\": 200, \"trigger_rate\": 0.2046, \"mean_uncertainty\": 0.1873, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}, \"notes\": \"TABLE 1 CANONICAL CONFIG. 3-suite checkpoint (crm_smolvla_3suite_v1), K=10, norm=0.2, tau=0.25. SR=81.5% (163/200). Same config as Table 1 Adaptive Spatial (80.8±1.1% is 3-seed mean of s42/s45/s46). This s47 result is supplementary 4th seed.\"}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-24T13:40:18.329Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:52:06.114Z\", \"updated_at\": \"2026-05-24T12:59:11.634Z\", \"hypothesis\": \"Object s47 Reconvla baseline, only missing Object s47 method. Completes Object suite seed extension coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.765, \"total_successes\": 153, \"total_trials\": 200, \"per_task\": {\"alphabet_soup\": 0.75, \"cream_cheese\": 0.95, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.75, \"tomato_sauce\": 0.65, \"butter\": 0.5, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:51:59.402Z\", \"updated_at\": \"2026-05-24T12:06:10.287Z\", \"hypothesis\": \"Goal s47 K=2 mean baseline for seed extension. Sixth seed to tighten CI for Goal suite K2mean method.\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:51:52.528Z\", \"updated_at\": \"2026-05-24T12:06:00.775Z\", \"hypothesis\": \"Goal s47 Adaptive gating (tau=0.25) eval for seed extension. Sixth seed to tighten CI for Goal suite Adaptive method.\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29241, \"crm_applied_steps\": 2594, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:51:56.065Z\", \"updated_at\": \"2026-05-24T12:04:48.551Z\", \"hypothesis\": \"Goal s47 CRM obs-only (norm=0.05) eval for seed extension. Sixth seed to tighten CI for Goal suite CRM method.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T12:04:25.566Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T12:04:19.868Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T12:04:12.044Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T12:04:03.396Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.565, \"successes\": 113, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:52:02.749Z\", \"updated_at\": \"2026-05-24T12:02:42.999Z\", \"hypothesis\": \"Goal s47 Reconvla baseline for seed extension. Sixth seed to tighten CI for Goal suite Reconvla method.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T08:38:07.452Z\", \"updated_at\": \"2026-05-24T11:54:38.814Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed47. Sixth seed extending Object K2mean coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T08:38:10.740Z\", \"updated_at\": \"2026-05-24T11:54:35.410Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed47. Sixth seed extending Object CRM coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T08:38:16.262Z\", \"updated_at\": \"2026-05-24T11:54:31.885Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed47. Sixth seed extending Object Adaptive coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T08:38:03.765Z\", \"updated_at\": \"2026-05-24T11:35:27.918Z\", \"hypothesis\": \"VLA-only (K=1) baseline on Object suite seed47. Sixth seed extending Object VLA-only coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755, \"successes\": 151, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:31:15.967Z\", \"updated_at\": \"2026-05-24T11:32:52.408Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline, second re-run after r2 was killed for CRM training priority. Fills Goal s47 seed extension for variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s47-r2\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T11:12:34.971Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47. Renamed from eval-supp-long-vla-only-s47 (was misnamed at creation — actual command uses --baseline_mode mean --K 2). Paired with Adapt-s47 for matched-seed comparison.\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T11:12:22.088Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"conclusion\": \"failed\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T11:03:21.940Z\", \"hypothesis\": \"CRM obs-only (norm=0.05, K=10) on LIBERO-Spatial at seed 47 for seed-extension coverage of the CRM baseline.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T10:45:00.000Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"train-crm-pi05-unified-3suite\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T10:10:37.619Z\", \"updated_at\": \"2026-05-24T10:38:14.192Z\", \"hypothesis\": \"π0.5 unified 3-suite (Spatial+Goal+Object) CRM training. D135: Long dropped due to DDL. obs_dim=2048, ~194K samples, batch_size=32, 50 epochs.\", \"conclusion\": \"killed\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T10:10:16.342Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T10:09:37.798Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"conclusion\": \"killed\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T10:09:11.097Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T10:09:03.019Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mean_uncertainty\": 0.1885, \"trigger_rate\": 0.2013, \"tau\": 0.25, \"total_steps\": 28599, \"crm_applied_steps\": 5758}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T10:08:52.437Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T10:08:42.206Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T10:08:34.857Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-24T08:38:21.696Z\", \"updated_at\": \"2026-05-24T09:35:00.000Z\", \"metrics\": {\"best_val_loss\": 0.002887, \"best_epoch\": 50, \"final_train_loss\": 0.018836}, \"hypothesis\": \"π0.5 CRM K=1 MultiScaleCRM training on LIBERO-Spatial precomputed cache validates cross-model generalization of conformal refinement approach with obs_dim=2048.\"}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-24T08:38:31.640Z\", \"updated_at\": \"2026-05-24T09:35:00.000Z\", \"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}, \"hypothesis\": \"π0.5 CRM K=1 MultiScaleCRM training on LIBERO-Goal precomputed cache validates cross-model generalization of conformal refinement approach with obs_dim=2048.\"}, \"eval-supp-goal-vla-only-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:15:59.536Z\", \"updated_at\": \"2026-05-24T09:30:43.725Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline, re-run after previous kill for π0.5 CRM training priority. Fills Goal s47 seed extension.\", \"parent\": \"eval-supp-goal-vla-only-s47\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T09:15:55.640Z\", \"updated_at\": \"2026-05-24T09:30:34.360Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline, re-run after previous kill for π0.5 CRM training priority. Fills Long s47 seed extension.\", \"parent\": \"eval-supp-long-vla-only-s47-r2\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T08:35:00.000Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"conclusion\": \"killed\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T08:35:00.000Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:27:00.000Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:27:00.000Z\", \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T08:27:00.000Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:55:46.960Z\", \"updated_at\": \"2026-05-24T08:05:01.126Z\", \"hypothesis\": \"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:32:56.953Z\", \"updated_at\": \"2026-05-24T07:09:37.983Z\", \"hypothesis\": \"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:16.953Z\", \"updated_at\": \"2026-05-24T07:06:31.785Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:13.683Z\", \"updated_at\": \"2026-05-24T07:06:23.946Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:10.482Z\", \"updated_at\": \"2026-05-24T07:06:15.932Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:07.178Z\", \"updated_at\": \"2026-05-24T07:06:09.666Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T03:56:52.910Z\", \"updated_at\": \"2026-05-24T06:55:16.446Z\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:22:29.274Z\", \"updated_at\": \"2026-05-24T06:49:49.091Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:19.029Z\", \"updated_at\": \"2026-05-24T06:49:36.626Z\", \"hypothesis\": \"VLA-only baseline on Object suite seed45. Fills s45 gap in Object VLA-only 5-seed coverage (have s42-s44, s46) for supplementary table.\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:12.741Z\", \"updated_at\": \"2026-05-24T06:45:22.337Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Spatial suite seed45. Sixth seed extending Spatial CRM always-on variance coverage for supplementary table.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}, \"notes\": \"Eval completed normally. 78.0% (156/200). Results at logs/eval_spatial_crm_obs_only_norm0.05_seed45.json on cqa1-32758. Cron escalated as process-gone but script had already exited after completion.\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:09.089Z\", \"updated_at\": \"2026-05-24T06:45:16.646Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Sixth seed extending Spatial VLA-only variance coverage for supplementary table.\", \"conclusion\": \"success\", \"notes\": \"Eval completed normally on cqa1-32758. SR=77.0% (154/200). Results at logs/eval_spatial_vla_only_seed45.json. Per-task: between_plate_ramekin 90%, next_to_ramekin 90%, table_center 90%, on_cookie_box 100%, top_drawer 75%, on_ramekin 0%, next_to_cookie_box 95%, on_stove 75%, next_to_plate 80%, on_wooden_cabinet 75%.\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:18:27.873Z\", \"updated_at\": \"2026-05-24T06:23:35.000Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Goal enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T06:15:12.631Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T05:52:22.340Z\", \"updated_at\": \"2026-05-24T06:13:04.507Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Spatial enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:21.518Z\", \"updated_at\": \"2026-05-24T05:44:03.369Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:24.393Z\", \"updated_at\": \"2026-05-24T05:43:32.643Z\", \"hypothesis\": \"Goal VLA-only baseline seed46. Fifth seed extending Goal VLA-only. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:35.384Z\", \"updated_at\": \"2026-05-24T05:43:26.502Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal suite seed46. Fifth seed extending Goal Reconvla. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T18:48:38.574Z\", \"updated_at\": \"2026-05-24T03:28:46.242Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-24T03:27:16.008Z\", \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-24T03:27:10.816Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"conclusion\": \"success\", \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:50.876Z\", \"updated_at\": \"2026-05-24T03:27:05.531Z\", \"hypothesis\": \"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-24T03:27:01.680Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-24T03:26:55.797Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:26:47.449Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:26:39.499Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T12:22:12.815Z\", \"updated_at\": \"2026-05-24T03:26:27.340Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-24T03:25:46.138Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-24T03:25:36.173Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-24T03:25:23.533Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:20:29.949Z\", \"updated_at\": \"2026-05-24T03:24:43.469Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed45. Fourth seed extending Long K2mean coverage. VLA-only s45 on bjb1-32546 provides baseline.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:24.679Z\", \"updated_at\": \"2026-05-24T03:24:33.666Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed46. Extends Goal K2mean to 4th completed seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:43.468Z\", \"updated_at\": \"2026-05-24T03:24:30.058Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed46. Fifth seed extending Goal Adaptive. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:31.022Z\", \"updated_at\": \"2026-05-24T03:24:26.680Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed46. Fifth seed extending Goal CRM. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:42:31.834Z\", \"updated_at\": \"2026-05-24T03:19:19.270Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"parent\": \"eval-supp-spatial-adapt-tau025-s45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:59:42.673Z\", \"updated_at\": \"2026-05-24T03:18:33.793Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed45. Fourth seed extending Spatial K2mean. Fills Table 1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:34:46.225Z\", \"updated_at\": \"2026-05-24T03:18:27.488Z\", \"hypothesis\": \"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:52:50.566Z\", \"updated_at\": \"2026-05-24T03:18:20.676Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:45:59.585Z\", \"updated_at\": \"2026-05-24T03:18:17.471Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:22:31.743Z\", \"updated_at\": \"2026-05-24T03:18:14.133Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:50.126Z\", \"updated_at\": \"2026-05-24T00:54:53.307Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:41.239Z\", \"updated_at\": \"2026-05-24T00:53:11.757Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed45. Fourth seed for Long Adaptive validation.\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:16.039Z\", \"updated_at\": \"2026-05-24T00:30:53.206Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed45. Fourth seed extending Spatial Reconvla. 3-seed: 79.8%±1.0%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}, \"notes\": \"Cron false positive — eval script completed normally with 79.5% (159/200). Results at logs/eval_spatial_reconvla_seed45.json on cqa1-32758. No W&B/sentinel used by eval scripts.\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:04.113Z\", \"updated_at\": \"2026-05-24T00:21:09.215Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed45. Matched-seed companion for Goal s45 4-seed extension.\", \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:59.880Z\", \"updated_at\": \"2026-05-23T23:45:46.677Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Extends Object Adaptive coverage. Trigger rate expected ~3-5% on Object tasks.\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:29.185Z\", \"updated_at\": \"2026-05-23T23:45:41.402Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Duplicate of eval-supp-k2mean-obj-s45 (already DONE SR=77.5%). Killed to free GPU.\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:43.001Z\", \"updated_at\": \"2026-05-23T23:43:24.974Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fifth seed extending Object CRM. Previous seeds show ~79-81% range.\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-23T22:23:46.061Z\", \"updated_at\": \"2026-05-23T23:42:01.475Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:25.473Z\", \"updated_at\": \"2026-05-23T23:04:07.248Z\", \"hypothesis\": \"Long K=2 mean baseline seed44. Third seed for Long K=2 mean validation. Isolates multi-sample averaging on long-horizon tasks.\", \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:31.761Z\", \"updated_at\": \"2026-05-23T23:04:01.262Z\", \"hypothesis\": \"Long Reconvla K=10 seed44. Third seed for Long Reconvla 3-seed validation. s42=56.5% (below VLA-only 58.0%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-23T23:02:16.008Z\", \"updated_at\": \"2026-05-23T23:02:16.008Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Spatial suite seed45. Fourth seed completing Spatial k2mean coverage (s42=negative, s43/s44=done). Isolates multi-sample averaging effect.\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:38.416Z\", \"updated_at\": \"2026-05-23T22:57:24.122Z\", \"hypothesis\": \"Reconvla K=10 on Goal suite seed45. Fourth seed extending Goal Reconvla. 3-seed mean: 80.8%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果文件: logs/eval_goal_reconvla_seed45.json\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:20.093Z\", \"updated_at\": \"2026-05-23T22:57:13.555Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fills the last Object s46 method gap.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判为 failed。日志确认 79.5% (159/200)。结果文件: logs/eval_object_crm_obs_only_norm0.05_seed46.json\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:32.501Z\", \"updated_at\": \"2026-05-23T22:56:01.038Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed45. Fourth seed extending Goal CRM. 3-seed mean: 83.7%±1.8%.\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\", \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果文件: logs/eval_goal_crm_obs_only_norm0.05_seed45.json\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:15:28.966Z\", \"updated_at\": \"2026-05-23T22:37:07.655Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed45. Extends Object method coverage for 5-seed Adaptive variance investigation.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:41:19.029Z\", \"updated_at\": \"2026-05-23T22:31:59.949Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed46. Extends Object method coverage for 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:13:06.213Z\", \"updated_at\": \"2026-05-23T22:31:49.469Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed45. Extends Goal Adaptive from 3-seed to 4-seed.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:35.159Z\", \"updated_at\": \"2026-05-23T21:28:56.768Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed44. Third seed for Long CRM 3-seed validation.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:32.204Z\", \"updated_at\": \"2026-05-23T21:28:50.765Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed44. Third seed for Long Adaptive 3-seed validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:58.207Z\", \"updated_at\": \"2026-05-23T21:28:27.870Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed46. Companion baseline for Object Adaptive s46 5-seed extension.\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:52.406Z\", \"updated_at\": \"2026-05-23T21:28:21.695Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Companion baseline for Object Adaptive s45 5-seed extension.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:06.320Z\", \"updated_at\": \"2026-05-23T20:26:37.804Z\", \"hypothesis\": \"Object Adaptive τ=0.25 seed46. User-requested additional seed to assess Object Adaptive variance.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:22:32.322Z\", \"updated_at\": \"2026-05-23T20:13:10.758Z\", \"metrics\": {\"SR\": 0.57}, \"conclusion\": \"negative\", \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. VLA-only s42=58.0% baseline.\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:24:10.813Z\", \"updated_at\": \"2026-05-23T20:09:46.499Z\", \"hypothesis\": \"Object VLA-only baseline seed46. Companion baseline for Object Adaptive s46 comparison. 3-seed baseline: 77.8%±1.0%.\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:36.825Z\", \"updated_at\": \"2026-05-23T20:09:34.819Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed43. Isolates multi-sample averaging effect on Long tasks.\", \"metrics\": {\"SR\": 0.56}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:30.979Z\", \"updated_at\": \"2026-05-23T20:09:28.982Z\", \"hypothesis\": \"Reconvla K=10 argmin on Long suite seed43. Second seed for Long Reconvla validation.\", \"metrics\": {\"SR\": 0.59}, \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:26.229Z\", \"updated_at\": \"2026-05-23T20:09:23.098Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed43. Second seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.545}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:21.251Z\", \"updated_at\": \"2026-05-23T20:09:17.172Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed43. Second seed for Long Adaptive validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}, \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:55:59.154Z\", \"updated_at\": \"2026-05-23T18:16:04.202Z\", \"hypothesis\": \"Retry of eval-supp-obj-adapt-tau025-s45. Object Adaptive CRM τ=0.25 seed45 on bjb2-40593 after fixing missing CRM checkpoint.\", \"parent\": \"eval-supp-obj-adapt-tau025-s45\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:44.431Z\", \"updated_at\": \"2026-05-23T17:25:47.737Z\", \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:38.730Z\", \"updated_at\": \"2026-05-23T17:25:41.523Z\", \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:33.117Z\", \"updated_at\": \"2026-05-23T17:25:32.561Z\", \"hypothesis\": \"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:39.811Z\", \"updated_at\": \"2026-05-23T17:25:24.644Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold → lower trigger rate → fewer corrections. Part of 5-point τ-sensitivity curve. Tests whether very conservative gating still maintains benefit.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}, \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:36.431Z\", \"updated_at\": \"2026-05-23T17:25:15.441Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.15 on Goal s42. Mid-low threshold. Part of 5-point τ-sensitivity curve. Tests transition zone between aggressive and conservative gating.\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:27:45.450Z\", \"updated_at\": \"2026-05-23T17:25:06.995Z\", \"hypothesis\": \"K=2 mean baseline on Object seed44. Third seed for 3-seed mean±std. s42=79.5%, s43 running. Isolates multi-sample averaging on Object tasks.\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:32.832Z\", \"updated_at\": \"2026-05-23T17:24:59.810Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold → higher CRM trigger rate → more corrections. Part of 5-point τ-sensitivity curve (0.10, 0.15, 0.25, 0.40, always-on). Tests whether aggressive gating improves or hurts Goal performance.\", \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:31:41.302Z\", \"updated_at\": \"2026-05-23T17:24:48.531Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed44. s42=79.0%, s43 running on bjb2-28827. Third seed for Object Reconvla validation.\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:51:10.407Z\", \"updated_at\": \"2026-05-23T17:22:10.552Z\", \"hypothesis\": \"VLA-only baseline on Spatial seed44. s42=78.5%. Second/third seed for 3-seed Spatial VLA-only baseline mean±std.\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:18.236Z\", \"updated_at\": \"2026-05-23T17:21:50.650Z\", \"hypothesis\": \"Goal VLA-only wrapper s44 re-run. Previous result lost due to JSON filename collision with k2mean-s44. Confirms 83.5% baseline across seeds (s42=83.5%, s43=82.5%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:23:34.262Z\", \"updated_at\": \"2026-05-23T14:41:49.032Z\", \"hypothesis\": \"K=2 mean baseline on Spatial seed44. Third seed for 3-seed mean±std. s42=81.5%, s43 running. Isolates multi-sample averaging effect from CRM correction on Spatial.\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:31:48.527Z\", \"updated_at\": \"2026-05-23T14:41:43.043Z\", \"hypothesis\": \"VLA-only baseline on Spatial seed43. s42=78.5%. Second seed for 3-seed baseline mean±std.\", \"metrics\": {\"overall_success_rate\": 0.79, \"successes\": 158, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:21:57.954Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:21:51.978Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:21:46.269Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"conclusion\": \"negative\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:21:40.459Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-23T14:13:45.028Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"metrics\": {\"overall_sr\": 0.58, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.25, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.4, \"STUDY_SCENE1_book_caddy\": 0.9, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.3, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.55, \"KITCHEN_SCENE8_moka_pots_stove\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.75}}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T10:13:26.507Z\", \"updated_at\": \"2026-05-23T13:25:45.095Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal seed44. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Third seed for Goal Reconvla validation.\", \"metrics\": {\"success_rate\": 0.805, \"total_rollouts\": 200, \"total_successes\": 161, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.81, 0.81, 0.805], \"mean\": 0.8083, \"std\": 0.0029}}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T08:59:10.206Z\", \"updated_at\": \"2026-05-23T13:25:39.232Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed43. Multi-seed validation (s42=79.0%). Tests cross-seed consistency of reconvla selection on Object suite.\", \"parent\": \"eval-supp-obj-reconvla-s42\", \"metrics\": {\"success_rate\": 0.77, \"total_rollouts\": 200, \"total_successes\": 154}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:24:35.031Z\", \"updated_at\": \"2026-05-23T13:25:33.374Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed44. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp positive). Third seed for Goal CRM 3-seed mean±std validation.\", \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:38:54.570Z\", \"updated_at\": \"2026-05-23T11:53:35.791Z\", \"hypothesis\": \"K=2 mean baseline on Object suite with seed 43 should yield SR consistent with s42 (79.5%), confirming VLA-only performance stability across seeds.\", \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T08:33:20.623Z\", \"updated_at\": \"2026-05-23T11:49:21.426Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed42 (retry). Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks.\", \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:05:16.443Z\", \"updated_at\": \"2026-05-23T11:33:49.855Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed44. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Third seed for 3-seed mean±std on Goal Adaptive performance.\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T11:33:43.836Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\", \"metrics\": {\"success_rate\": 0.785}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T11:33:38.082Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\", \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T11:33:32.430Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\", \"metrics\": {\"success_rate\": 0.82}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T11:33:25.089Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\", \"metrics\": {\"success_rate\": 0.775, \"trigger_rate\": 0.0367, \"crm_applied_steps\": 1312, \"total_steps\": 35796}, \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T08:19:47.656Z\", \"updated_at\": \"2026-05-23T11:31:34.130Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal seed43. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Second seed for Goal reconvla multi-seed validation.\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.65, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"negative\", \"notes\": \"Reconvla Goal seed43: SR=81.0% (162/200). s42=81.0%, s43=81.0% 完全一致。两 seed 平均 81.0%。VLA-only baseline 83.5%。Reconvla 在 Goal 上仍低于 VLA-only -2.5pp。\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:38:51.694Z\", \"updated_at\": \"2026-05-23T11:30:05.886Z\", \"hypothesis\": \"K=2 mean baseline multi-seed on Spatial seed43. Isolates multi-sample averaging effect from CRM correction. Second seed for 3-seed mean±std on K=2 mean baseline.\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}, \"conclusion\": \"success\", \"notes\": \"K=2 mean Spatial seed43: SR=78.0% (156/200). 与 s42 的 81.5% 相比下降 3.5pp。on_ramekin 任务 0%（与 s42 一致）。VLA-only baseline (s42) = 78.5%。两 seed 平均: (81.5+78.0)/2 = 79.75%。\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:44.347Z\", \"updated_at\": \"2026-05-23T11:25:39.981Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed44. Multi-seed validation (with s42=79%, s43). Third seed for 3-seed mean±std statistical claim on reconvla.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"between_plate_and_ramekin\": 1, \"table_center\": 1, \"next_to_ramekin\": 0.95, \"next_to_cookie_box\": 0.95, \"on_cookie_box\": 0.9, \"on_wooden_cabinet\": 0.85, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"top_drawer_wooden_cabinet\": 0.7, \"on_ramekin\": 0}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.8, 0.815, 0.795], \"mean\": 0.803, \"std\": 0.01}}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:39.046Z\", \"updated_at\": \"2026-05-23T11:21:32.905Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial seed43. Multi-seed validation (with s42=79%, s44). Tests cross-seed consistency of reconvla selection strategy.\", \"parent\": \"eval-supp-reconvla-k2-spatial-s42\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:38:57.518Z\", \"updated_at\": \"2026-05-23T11:20:45.445Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed43. Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks. Second seed for 3-seed mean±std.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:22.668Z\", \"updated_at\": \"2026-05-23T10:48:56.855Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Object suite seed42. Isolates multi-sample averaging from CRM correction. Object CRM=77%, Reconvla=79%. If K=2 mean ≈ VLA-only, confirms CRM/reconvla improvements not from sampling diversity alone.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:36:42.194Z\", \"updated_at\": \"2026-05-23T10:47:49.735Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed42. Goal VLA-only baseline = 83.5%. Result: 84.0% = +0.5pp weak positive. Trigger rate 8.3% indicates low uncertainty on Goal tasks. Adaptive gating preserves near-baseline performance.\", \"parent\": \"eval-supp-goal-crm005-s42\", \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:29.401Z\", \"updated_at\": \"2026-05-23T10:27:32.365Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM norm=0.05 on Goal suite seed42. Goal VLA-only baseline = 83.5% (confirmed by fresh eval). CRM 85.5% = +2.0pp improvement. CRM benefits Goal suite with moderate correction.\", \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:28.711Z\", \"updated_at\": \"2026-05-23T10:11:16.616Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal suite seed42. Goal VLA-only baseline = 83.5%. Result: 81.0% = -2.5pp negative. Reconstruction-based selection hurts on Goal tasks.\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:05.516Z\", \"updated_at\": \"2026-05-23T10:09:50.183Z\", \"hypothesis\": \"Unified CRM obs_only on all 4 LIBERO suites (object, spatial, goal, long) enables comprehensive cross-suite evaluation with a single model\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005669, \"epochs\": 50, \"final_train_loss\": 0.009731, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\"}}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:33.979Z\", \"updated_at\": \"2026-05-23T10:09:44.401Z\", \"hypothesis\": \"Goal VLA-only wrapper baseline seed42 with n_rollouts=20. Previous Goal VLA-only (71%) may have used different wrapper. Re-run with consistent evaluation wrapper for fair cross-method comparison.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:16:00.470Z\", \"updated_at\": \"2026-05-23T10:05:16.143Z\", \"hypothesis\": \"Object Adaptive CRM with correct tau=0.25 (previous r2 used tau=0.074855, too aggressive with 70% trigger rate → no improvement). tau=0.25 worked on Spatial (82% vs 78.5% VLA-only). Object VLA-only=77.8%±1.0%.\", \"parent\": \"eval-supp-obj-adapt-s42-r2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.035, \"mean_unc\": 0.109, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 2}}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T07:03:14.824Z\", \"updated_at\": \"2026-05-23T09:40:16.419Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Spatial seed42. Isolates multi-sample averaging effect from CRM correction. If SR ≈ VLA-only 78.5%, confirms CRM is the source of improvement, not sampling diversity.\", \"metrics\": {\"success_rate\": 81.5, \"total_success\": 163, \"total_rollouts\": 200, \"per_task\": {\"bowl_between_plate_ramekin\": 95, \"bowl_next_to_ramekin\": 95, \"bowl_from_table_center\": 100, \"bowl_on_cookie_box\": 100, \"bowl_in_top_drawer\": 70, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 95, \"bowl_on_stove\": 80, \"bowl_next_to_plate\": 85, \"bowl_on_wooden_cabinet\": 95}}, \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:51:53.573Z\", \"updated_at\": \"2026-05-23T08:56:25.513Z\", \"hypothesis\": \"CRM obs_only norm=0.05 multi-seed validation on Spatial (seed44). norm=0.05 always-on achieved 80% SR on seed42. Third seed (with s42/s43) for 3-seed mean±std statistical claim on CRM always-on.\", \"parent\": \"eval-supp-crm-norm005-spatial-s43\", \"metrics\": {\"success_rate\": 78.5, \"total_rollouts\": 200, \"total_successes\": 157, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [80, 81, 78.5], \"mean\": 79.8, \"std\": 1.3}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:12:35.946Z\", \"updated_at\": \"2026-05-23T08:44:11.956Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 multi-seed validation on Spatial (seed44). tau=0.25 confirmed optimal on seed42 (82% SR, +3.5pp over VLA-only, trigger_rate 19.4%). Testing reproducibility across seeds.\", \"parent\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"metrics\": {\"success_rate\": 80.5, \"total_successes\": 161, \"total_rollouts\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1881, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"mode\": \"adaptive_conformal_crm\", \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin\": {\"sr\": 90, \"successes\": 18, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_ramekin\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}, \"pick_up_the_black_bowl_from_table_center\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet\": {\"sr\": 65, \"successes\": 13, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_ramekin\": {\"sr\": 0, \"successes\": 0, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_stove\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_plate\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_wooden_cabinet\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:30:30.881Z\", \"updated_at\": \"2026-05-23T08:36:38.221Z\", \"hypothesis\": \"K=2 argmin baseline (reconvla mode, --K 2) on Spatial seed42. Due to centroid bug (K=2 → d1==d2 → always picks sample 0), K=2 argmin effectively equals K=1 VLA-only (~78.5%). If confirmed, proves 82% improvement comes entirely from CRM correction, not K=2 sampling diversity.\", \"parent\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 100, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 75, \"next_to_plate\": 80, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:12:16.652Z\", \"updated_at\": \"2026-05-23T08:36:15.063Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 multi-seed validation on Spatial (seed43). tau=0.25 confirmed optimal on seed42 (82% SR, +3.5pp over VLA-only, trigger_rate 19.4%). Testing reproducibility across seeds.\", \"parent\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 19.4, \"mean_unc\": 0.1845, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 95, \"on_cookie_box\": 100, \"in_top_drawer_wooden_cabinet\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 80, \"next_to_plate\": 85, \"on_wooden_cabinet\": 80}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:30:33.726Z\", \"updated_at\": \"2026-05-23T08:35:04.453Z\", \"hypothesis\": \"CRM obs_only norm=0.05 multi-seed validation on Spatial (seed43). norm=0.05 always-on achieved 80% SR on seed42 (best always-on config). Testing reproducibility for cross-seed consistency claim.\", \"parent\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"metrics\": {\"success_rate\": 81, \"total_rollouts\": 200, \"total_successes\": 162, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 75, \"success\": 15, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 95, \"success\": 19, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:56:46.277Z\", \"updated_at\": \"2026-05-23T08:29:52.019Z\", \"hypothesis\": \"K=2 mean baseline (vla_only mode, 2-sample action average) on Goal suite seed42. Isolates the effect of multi-sample averaging from CRM correction. If K=2 mean ≈ VLA-only (71%), confirms improvement comes from CRM, not sampling diversity.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:16.885Z\", \"updated_at\": \"2026-05-23T07:08:55.601Z\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"hypothesis\": \"Adaptive CRM (tau=0.074855, K=2, norm=0.2) generalizes from Spatial (81%) to Object suite, validating cross-suite applicability of conformal gating\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 80, \"cream_cheese\": 90, \"salad_dressing\": 70, \"bbq_sauce\": 85, \"ketchup\": 70, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 80, \"orange_juice\": 95}, \"mean_unc\": 0.1104, \"trigger_rate\": 0.702}, \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:09.846Z\", \"updated_at\": \"2026-05-23T07:08:49.478Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object with seed44 for 3-seed statistical significance\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:01.112Z\", \"updated_at\": \"2026-05-23T07:08:43.800Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object with seed43 for 3-seed statistical significance\", \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:11:48.015Z\", \"updated_at\": \"2026-05-23T07:08:33.647Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object establishes fair comparison point for CRM method evaluation\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:22.236Z\", \"updated_at\": \"2026-05-23T07:05:57.520Z\", \"conclusion\": \"success\", \"hypothesis\": \"Reconvla K=10 (argmin baseline) on Object suite establishes cross-suite comparison with Spatial (79%); validates CRM-based methods generalize\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 95, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 75, \"orange_juice\": 90}}}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:12:14.170Z\", \"updated_at\": \"2026-05-23T06:40:03.190Z\", \"hypothesis\": \"CRM norm=0.05 generalizes from Spatial (+1.5pp over VLA-only 78.5%→80%) to Object suite, validating cross-suite benefit of minimal CRM correction\", \"parent\": \"eval-3dir-norm005-spatial-s42\", \"metrics\": {\"overall_success_rate\": 0.77, \"n_success\": 154, \"n_total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"conformal_threshold\": 0.074855, \"K\": 10, \"seed\": 42, \"per_task_sr\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:11:54.911Z\", \"updated_at\": \"2026-05-23T06:20:31.236Z\", \"hypothesis\": \"Adaptive CRM with tau=0.35 (conservative, ~10% trigger rate) tests whether very selective CRM application still provides benefit on LIBERO-Spatial\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"metrics\": {\"overall_sr\": 80, \"n_success\": 160, \"n_total\": 200, \"trigger_rate\": 12.17, \"mean_unc\": 0.1873, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"crm_applied_steps\": 3474, \"total_steps\": 28549, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 90, \"on_cookie_box\": 95, \"in_top_drawer\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 85, \"next_to_plate\": 85, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:11:25.578Z\", \"updated_at\": \"2026-05-23T06:16:30.800Z\", \"hypothesis\": \"Adaptive CRM with tau=0.15 (~P75) reduces trigger rate to ~50-60% while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"metrics\": {\"overall_sr\": 80.5, \"n_success\": 161, \"n_total\": 200, \"trigger_rate\": 40.7, \"mean_unc\": 0.1852, \"conformal_threshold\": 0.15, \"max_correction_norm\": 0.2, \"per_task_sr\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 100, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 75, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 80, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:11:13.449Z\", \"updated_at\": \"2026-05-23T06:12:43.228Z\", \"hypothesis\": \"CRM norm=0.2 always-on isolates whether adaptive gating (81% SR) outperforms same-norm always-on correction on LIBERO-Spatial\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"metrics\": {\"overall_sr\": 79, \"n_success\": 158, \"n_total\": 200, \"per_task_sr\": {\"between_plate_and_ramekin\": 100, \"next_to_ramekin\": 90, \"from_table_center\": 95, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 95, \"next_to_plate\": 75, \"on_wooden_cabinet\": 65}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:11:39.644Z\", \"updated_at\": \"2026-05-23T06:12:07.119Z\", \"hypothesis\": \"Adaptive CRM with tau=0.25 (~P90) reduces trigger rate to ~20-30% while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"metrics\": {\"overall_sr\": 82, \"n_success\": 164, \"n_total\": 200, \"trigger_rate\": 19.4, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 100, \"on_cookie_box\": 100, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 90, \"on_stove\": 90, \"next_to_plate\": 90, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T23:07:05.761Z\", \"updated_at\": \"2026-05-23T04:55:40.054Z\", \"hypothesis\": \"OpenVLA-7B fine-tuned on LIBERO-Object baseline eval (seed42). 复现官方 88.4% SR，获取 per-task breakdown 与 SmolVLA 对比。如果 SR 符合预期，验证 CRM 路线的 base policy 基线可用性。重试：前次 timeout (6h不够，需~10h)。\", \"parent\": \"eval-openvla-object-baseline-seed42\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:54:53.558Z\", \"updated_at\": \"2026-05-23T04:55:15.323Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed55. Norm sweep seed balance.\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:16:27.403Z\", \"updated_at\": \"2026-05-23T04:55:09.845Z\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples from LIBERO demos for CRM training. Required step for Plan A (CRM with π0.5 features).\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:37:16.074Z\", \"updated_at\": \"2026-05-23T04:55:04.457Z\", \"hypothesis\": \"Precompute SmolVLA obs features (960D) + K=2 action samples on LIBERO-Goal for CRM training (Plan A config). Shard 2/3 on cuda:5 of bjb2-28827, output to crm_cache_v5/goal/partial_s2_*.pt.\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:37:03.110Z\", \"updated_at\": \"2026-05-23T04:54:57.961Z\", \"hypothesis\": \"Precompute SmolVLA obs features (960D) + K=2 action samples on LIBERO-Goal for CRM training (Plan A config). Shard 1/3 on cuda:4 of bjb2-28827, output to crm_cache_v5/goal/partial_s1_*.pt.\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:36:45.138Z\", \"updated_at\": \"2026-05-23T04:54:52.235Z\", \"hypothesis\": \"Precompute SmolVLA obs features (960D) + K=2 action samples on LIBERO-Goal for CRM training (Plan A config). Shard 0/3 on cuda:3 of bjb2-28827, output to crm_cache_v5/goal/partial_s0_*.pt.\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:07:26.187Z\", \"updated_at\": \"2026-05-23T04:54:46.718Z\", \"conclusion\": \"killed\", \"notes\": \"Phantom entry — never submitted (PREPARING, no spec). Cron false alarm.\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:08:55.328Z\", \"updated_at\": \"2026-05-23T04:54:41.335Z\", \"conclusion\": \"killed\", \"notes\": \"Phantom entry — never submitted (PREPARING, no spec). Cron false alarm. No action needed.\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:08:30.499Z\", \"updated_at\": \"2026-05-23T04:54:35.953Z\", \"conclusion\": \"killed\", \"notes\": \"Phantom entry — never submitted (PREPARING, no spec). Cron false alarm.\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:28.149Z\", \"updated_at\": \"2026-05-23T04:54:30.564Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:32.121Z\", \"updated_at\": \"2026-05-23T04:54:25.093Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:37.387Z\", \"updated_at\": \"2026-05-23T04:54:19.576Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:45.533Z\", \"updated_at\": \"2026-05-23T04:54:14.038Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:50.015Z\", \"updated_at\": \"2026-05-23T04:54:08.535Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:54.489Z\", \"updated_at\": \"2026-05-23T04:50:29.455Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:36:39.492Z\", \"updated_at\": \"2026-05-23T04:50:22.494Z\", \"hypothesis\": \"Adaptive conformal CRM (K=2, tau=0.074855) generalizes from Spatial (+2.5pp) to Object suite\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:38:23.399Z\", \"updated_at\": \"2026-05-23T04:50:16.948Z\", \"hypothesis\": \"Reducing max_correction_norm to 0.2 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-spatial\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:38:26.202Z\", \"updated_at\": \"2026-05-23T04:50:11.299Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 adjusts correction trigger sensitivity, finding optimal balance between correction frequency and accuracy on LIBERO-spatial\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:38:28.948Z\", \"updated_at\": \"2026-05-23T04:50:03.969Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 adjusts correction trigger sensitivity, finding optimal balance between correction frequency and accuracy on LIBERO-spatial\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:38:32.825Z\", \"updated_at\": \"2026-05-23T04:49:53.623Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 adjusts correction trigger sensitivity, finding optimal balance between correction frequency and accuracy on LIBERO-spatial\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:42:17.967Z\", \"updated_at\": \"2026-05-23T04:32:30.777Z\", \"hypothesis\": \"Unified CRM obs_only trained on all 4 LIBERO suites provides better generalization than 3-suite model, resumed from epoch 32 checkpoint after accidental pkill\", \"parent\": \"train-crm-unified-4suite-r5\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T02:00:11.285Z\", \"updated_at\": \"2026-05-23T04:07:05.366Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object establishes fair comparison point for CRM method evaluation\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T02:00:08.251Z\", \"updated_at\": \"2026-05-23T04:06:59.994Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object establishes fair comparison point for CRM method evaluation\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T02:00:05.406Z\", \"updated_at\": \"2026-05-23T04:06:54.695Z\", \"hypothesis\": \"SmolVLA wrapper VLA-only baseline on LIBERO-Object establishes fair comparison point for CRM method evaluation\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:26:33.584Z\", \"updated_at\": \"2026-05-23T04:06:49.393Z\", \"hypothesis\": \"CRM norm=0.05 generalizes from Spatial (+0.2pp) to Object suite, validating cross-suite benefit of minimal CRM correction\", \"parent\": \"eval-3dir-norm005-spatial-s42\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:26:29.768Z\", \"updated_at\": \"2026-05-23T04:06:43.867Z\", \"hypothesis\": \"Adaptive CRM with tau=0.35 (conservative, ~10% trigger rate) tests whether very selective CRM application still provides benefit on LIBERO-Spatial\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:26:26.232Z\", \"updated_at\": \"2026-05-23T04:06:38.592Z\", \"hypothesis\": \"Adaptive CRM with tau=0.25 (~P90) reduces trigger rate to ~20-30% while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:26:20.007Z\", \"updated_at\": \"2026-05-23T04:06:33.197Z\", \"hypothesis\": \"Adaptive CRM with tau=0.15 (~P75) reduces trigger rate to ~50-60% while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T03:26:15.065Z\", \"updated_at\": \"2026-05-23T04:06:27.722Z\", \"hypothesis\": \"CRM norm=0.2 always-on isolates whether adaptive gating (81% SR) outperforms same-norm always-on correction on LIBERO-Spatial\", \"parent\": \"eval-3dir-adaptive-spatial-s42\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:54:21.349Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:37:46.832Z\", \"updated_at\": \"2026-05-23T03:53:00.389Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.3 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 73.9, \"successes\": 133, \"total\": 180, \"n_tasks_complete\": 9, \"n_tasks_total\": 10, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\", \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.85, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0.8, \"next_to_plate\": 0.55, \"on_wooden_cabinet\": \"partial_5/10\"}}}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:37:57.325Z\", \"updated_at\": \"2026-05-23T03:52:57.581Z\", \"hypothesis\": \"ReconVLA K=10 argmin sampling without CRM correction isolates sample-selection benefit from CRM correction, serving as diagnostic baseline on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:37:49.389Z\", \"updated_at\": \"2026-05-23T03:52:54.819Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.1 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.75}}}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T01:37:52.090Z\", \"updated_at\": \"2026-05-23T03:52:51.544Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.05 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:21:53.685Z\", \"updated_at\": \"2026-05-23T03:39:47.719Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:21:51.013Z\", \"updated_at\": \"2026-05-23T03:39:37.428Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:21:48.300Z\", \"updated_at\": \"2026-05-23T03:39:26.989Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:21.485Z\", \"updated_at\": \"2026-05-23T03:35:03.670Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:18.595Z\", \"updated_at\": \"2026-05-23T03:35:00.107Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:13:25.027Z\", \"updated_at\": \"2026-05-23T03:31:27.072Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:24:37.459Z\", \"updated_at\": \"2026-05-23T01:33:47.618Z\", \"hypothesis\": \"Continuation of train-crm-unified-4suite-r4 (still running, cron false-alarm set r4 to DONE/failed). Unified CRM obs_only on 4 LIBERO suites, epoch 14/50, val_loss=0.007949\", \"parent\": \"train-crm-unified-4suite-r4\", \"metrics\": {\"val_loss\": 0.006075, \"epochs_completed\": 32, \"epochs_target\": 50, \"train_loss_final\": 0.010489, \"best_epoch\": 32, \"crash_epoch\": 33, \"crash_count\": 2}, \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:25:26.458Z\", \"updated_at\": \"2026-05-23T01:33:43.543Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating conformal refinement across task suites\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:25:22.045Z\", \"updated_at\": \"2026-05-23T01:33:35.873Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating conformal refinement across task suites\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:25:18.375Z\", \"updated_at\": \"2026-05-23T01:33:30.489Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating conformal refinement across task suites\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:25:14.775Z\", \"updated_at\": \"2026-05-23T01:33:22.750Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating conformal refinement across task suites\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T23:25:11.568Z\", \"updated_at\": \"2026-05-23T01:33:14.831Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Spatial, validating conformal refinement across task suites\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44\": {\"status\": \"PENDING\", \"created_at\": \"2026-05-22T05:10:37.288Z\", \"updated_at\": \"2026-05-22T23:26:30.844Z\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Goal, validating conformal refinement approach\", \"parent\": \"train-crm-smolvla-3suite-v1\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:21:56.371Z\", \"updated_at\": \"2026-05-22T23:24:07.545Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:58:07.658Z\", \"updated_at\": \"2026-05-22T23:18:08.524Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal with seed=44 completes the final missing 3-seed baseline for paper comparison\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:51:21.056Z\", \"updated_at\": \"2026-05-22T23:17:55.201Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal with seed=43 establishes reference SR for 3-seed mean±std paper comparison\", \"parent\": \"eval-smolvla-lerobot-goal-seed43-v2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:51:18.291Z\", \"updated_at\": \"2026-05-22T23:17:49.796Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Spatial with seed=43 establishes reference SR for 3-seed mean±std paper comparison\", \"parent\": \"eval-smolvla-lerobot-spatial-seed43-v2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 54.5, \"n_episodes\": 200}}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:53:43.527Z\", \"updated_at\": \"2026-05-22T23:11:45.218Z\", \"hypothesis\": \"SmolVLA CRM (obs_only, 3-suite Object+Spatial+Goal) trained on wrapper precompute data (77,835 samples, K=10) — validates CRM improvement on weaker VLA with substantial headroom (baseline 59-75%)\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005878, \"final_train_loss\": 0.00969, \"final_val_loss\": 0.00588, \"epochs_completed\": 50, \"total_params\": 327198, \"data_samples\": 77835, \"best_epoch\": 50}}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:14:54.761Z\", \"updated_at\": \"2026-05-22T20:50:32.835Z\", \"hypothesis\": \"SmolVLA baseline evaluation on LIBERO Goal benchmark (seed=43) provides reference success rate for conformal refinement comparison\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:14:52.001Z\", \"updated_at\": \"2026-05-22T20:50:27.156Z\", \"hypothesis\": \"SmolVLA baseline evaluation on LIBERO Spatial benchmark (seed=43) provides reference success rate for conformal refinement comparison\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:14:49.263Z\", \"updated_at\": \"2026-05-22T20:50:21.831Z\", \"hypothesis\": \"SmolVLA baseline evaluation on LIBERO Object benchmark (seed=44) provides reference success rate for conformal refinement comparison\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:14:46.594Z\", \"updated_at\": \"2026-05-22T20:50:16.518Z\", \"hypothesis\": \"SmolVLA baseline evaluation on LIBERO Object benchmark (seed=43) provides reference success rate for conformal refinement comparison\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:52:09.225Z\", \"updated_at\": \"2026-05-22T20:13:51.786Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal with seed=43 establishes reference SR for 3-seed mean±std paper comparison\", \"conclusion\": \"failed\", \"notes\": \"M059: 并行过多崩溃，需重跑\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:52:03.607Z\", \"updated_at\": \"2026-05-22T20:13:46.670Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Spatial with seed=43 establishes reference SR for 3-seed mean±std paper comparison\", \"conclusion\": \"failed\", \"notes\": \"M059: 并行过多崩溃，需重跑\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:52:00.868Z\", \"updated_at\": \"2026-05-22T20:13:40.397Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Object with seed=44 establishes reference SR for 3-seed mean±std paper comparison\", \"conclusion\": \"failed\", \"notes\": \"M059: 并行过多崩溃，需重跑\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:51:58.107Z\", \"updated_at\": \"2026-05-22T20:13:33.516Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Object with seed=43 establishes reference SR for 3-seed mean±std paper comparison\", \"conclusion\": \"failed\", \"notes\": \"M059: 并行过多崩溃，需重跑\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:52:06.592Z\", \"updated_at\": \"2026-05-22T20:12:30.387Z\", \"hypothesis\": \"SmolVLA baseline evaluation on LIBERO spatial benchmark provides reference success rate for conformal refinement comparison\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.6, \"n_episodes\": 200, \"n_tasks\": 10, \"per_task_sr\": [0.75, 0.65, 0.75, 0.75, 0.5, 0, 0.9, 0.7, 0.4, 0.6]}}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:34:57.808Z\", \"updated_at\": \"2026-05-22T19:05:54.572Z\", \"hypothesis\": \"SmolVLA wrapper precompute on LIBERO-Long (K=10) to enable 4-suite CRM training after 3-suite CRM completes\", \"conclusion\": \"success\", \"notes\": \"正常完成。产出: /root/autodl-tmp/crm_cache_smolvla_k10/long/manifest.json, 54059 samples, K=10。bjb1-18228 cuda:2 已释放。\"}, \"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-22T18:52:11.876Z\", \"updated_at\": \"2026-05-22T19:02:22.376Z\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal with seed=44 establishes reference SR for 3-seed mean±std paper comparison\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:53:05.237Z\", \"updated_at\": \"2026-05-22T18:46:08.623Z\", \"hypothesis\": \"SmolVLA baseline on LIBERO-Long with lerobot evaluate establishes reference success rate for comparing ACR refinement methods\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}, \"notes\": \"Reviewer 二次确认: 正常运行并完成 (~19min)。数据有效。输出: /root/outputs/eval/smolvla_long_seed44/eval_info.json\"}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:52:59.794Z\", \"updated_at\": \"2026-05-22T18:46:05.996Z\", \"hypothesis\": \"SmolVLA baseline on LIBERO-Long with lerobot evaluate establishes reference success rate for comparing ACR refinement methods\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 53.5, \"n_episodes\": 200}, \"notes\": \"Reviewer 二次确认: 正常运行并完成 (~19min)。数据有效。输出: /root/outputs/eval/smolvla_long_seed43/eval_info.json\"}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:52:54.045Z\", \"updated_at\": \"2026-05-22T18:46:03.386Z\", \"hypothesis\": \"SmolVLA baseline on LIBERO-Long with lerobot evaluate establishes reference success rate for comparing ACR refinement methods\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}, \"notes\": \"Reviewer 二次确认: 正常运行并完成 (~19min)。数据有效。输出: /root/outputs/eval/smolvla_long_seed42/eval_info.json\"}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:51:28.515Z\", \"updated_at\": \"2026-05-22T18:14:09.706Z\", \"hypothesis\": \"Unified CRM (obs_only mode, unc_dim=0) trained on all 4 LIBERO suites (Object+Spatial+Goal+Long) with K=10 cache — matches Plan A architecture for cross-suite generalization eval\", \"parent\": \"train-crm-unified-4suite\", \"metrics\": {\"epochs_completed\": 13, \"current_epoch\": 14, \"current_batch\": \"2700/6316\", \"total_epochs\": 50, \"last_train_loss\": 0.012, \"checkpoint_latest\": \"checkpoint_epoch0013.pt\", \"checked_at\": \"2026-05-22T01:21Z\", \"note\": \"CRON false alarm - process still running (PID 322367)\"}, \"conclusion\": \"failed\", \"notes\": \"CRON FALSE ALARM: 进程 PID 322367 仍在正常运行 (epoch 16/50)。Cron 因无 W&B/sentinel 误判为 failed。实际训练由 r5 (train-crm-unified-4suite-r5) 跟踪。不要基于此 failed 状态触发重启或 eval。\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:20:53.528Z\", \"updated_at\": \"2026-05-22T18:12:13.396Z\", \"hypothesis\": \"π0.5 VLA-only baseline rerun on LIBERO-Long (seed42) with standardized params: n_action_steps=10, max_steps=520, n_rollouts=20. Previous run on bjb2-40593 failed due to environment issues.\", \"parent\": \"eval-pi05-vla-only-long-seed42-r4\", \"metrics\": {\"success_rate\": 0.94, \"successes\": 188, \"total\": 200, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.95, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 1, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.9, \"STUDY_SCENE1_book_in_caddy\": 0.95, \"LIVING_ROOM_SCENE6_mug_pudding\": 1, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0.9, \"KITCHEN_SCENE8_both_moka_pots\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave\": 0.9}}, \"conclusion\": \"success\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T01:04:45.531Z\", \"updated_at\": \"2026-05-22T17:20:46.002Z\", \"hypothesis\": \"π0.5 + CRM (Object, K=10, obs_dim=2048) eval with final 50-epoch checkpoint (val_loss=0.004018) will improve upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-object-full\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T21:31:43.148Z\", \"updated_at\": \"2026-05-22T17:20:35.256Z\", \"hypothesis\": \"π0.5 + CRM (Object, K=10, obs_dim=2048) eval with final 50-epoch checkpoint (val_loss=0.004018) will improve upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-object-full\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T21:30:44.869Z\", \"updated_at\": \"2026-05-22T17:20:24.929Z\", \"hypothesis\": \"π0.5 + CRM (Object, K=10, obs_dim=2048) eval with final 50-epoch checkpoint (val_loss=0.004018) will improve upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-object-full\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:50:13.725Z\", \"updated_at\": \"2026-05-22T17:17:06.116Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Phantom duplicate entry — real experiment is eval-pi05-vla-only-long-seed43-r4 (DONE/success/95.5%)\", \"notes\": \"Killed before submission. Original eval-pi05-vla-only-long-seed43-r4 already succeeded with 95.5% SR. No rerun needed.\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:27:52.232Z\", \"updated_at\": \"2026-05-22T17:16:24.608Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Phantom duplicate entry — real experiment is eval-pi05-vla-only-goal-seed44-r4 (DONE/success/97.5%)\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:30:09.587Z\", \"updated_at\": \"2026-05-22T17:16:00.966Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Phantom duplicate entry — real experiment is eval-pi05-vla-only-goal-seed42-r4 (DONE/success/98.0%)\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:51:26.793Z\", \"updated_at\": \"2026-05-22T17:15:55.404Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Phantom duplicate entry — real experiment is eval-pi05-vla-only-long-seed44-r4 (DONE/success/95.5%)\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:27:10.419Z\", \"updated_at\": \"2026-05-22T17:14:50.393Z\", \"conclusion\": \"killed\", \"notes\": \"Phantom experiment entry — never submitted (status was PREPARING, no spec/server/command). Cron false alarm. Real experiment is eval-pi05-vla-only-goal-seed43-r4 (DONE/success).\", \"hypothesis\": \"Phantom duplicate entry — real experiment is eval-pi05-vla-only-goal-seed43-r4 (DONE/success/98.0%)\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T12:22:08.483Z\", \"updated_at\": \"2026-05-22T17:02:13.462Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=300\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:03:10.617Z\", \"updated_at\": \"2026-05-22T17:01:57.058Z\", \"hypothesis\": \"Precompute SmolVLA obs features + K=2 action samples on LIBERO-Long (libero_10) for CRM training, cached to crm_cache_v5/long/. 3-shard parallel on cuda:3-5 of bjb1-32546.\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:34:36.171Z\", \"updated_at\": \"2026-05-22T17:00:24.406Z\", \"hypothesis\": \"Unified CRM (obs_only mode, unc_dim=0) trained on all 4 LIBERO suites with K=10 cache — matches Plan A architecture for fair comparison\", \"parent\": \"train-crm-unified-4suite\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:21:05.723Z\", \"updated_at\": \"2026-05-22T17:00:17.793Z\", \"hypothesis\": \"Retry: Unified CRM trained on all 4 LIBERO suites (Object+Spatial+Goal+Long, K=2) after r1 was killed. Same config: input_mode=full, obs_dim=960, hidden_dim=256, 50 epochs\", \"parent\": \"train-crm-unified-4suite\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:56:22.224Z\", \"updated_at\": \"2026-05-22T17:00:10.097Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training (parallel path on bjb2-28827)\", \"conclusion\": \"killed\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:56:19.770Z\", \"updated_at\": \"2026-05-22T17:00:02.382Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Long for unified 4-suite CRM training (parallel path on bjb2-28827)\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:52:38.008Z\", \"updated_at\": \"2026-05-22T16:59:56.882Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=280\", \"parent\": \"eval-pi05-vla-only-spatial-seed44-r3\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:52:35.446Z\", \"updated_at\": \"2026-05-22T16:59:51.541Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=280\", \"parent\": \"eval-pi05-vla-only-spatial-seed43-r3\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:52:32.717Z\", \"updated_at\": \"2026-05-22T16:59:46.047Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=280\", \"parent\": \"eval-pi05-vla-only-spatial-seed42-r3\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:19:40.063Z\", \"updated_at\": \"2026-05-22T16:43:05.868Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}, \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520. Multi-seed (seed44) evaluation to establish robust baseline statistics.\"}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:19:30.186Z\", \"updated_at\": \"2026-05-22T16:42:49.732Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520. Multi-seed (seed43) evaluation to establish robust baseline statistics.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:19:23.742Z\", \"updated_at\": \"2026-05-22T16:23:50.003Z\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}, \"conclusion\": \"success\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal achieves ~98% success rate with n_action_steps=10, establishing the upper-bound reference for conformal refinement comparisons\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:19:17.565Z\", \"updated_at\": \"2026-05-22T16:23:41.572Z\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"conclusion\": \"success\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Goal achieves ~98% success rate with n_action_steps=10, establishing the upper-bound reference for conformal refinement comparisons\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T16:13:45.727Z\", \"updated_at\": \"2026-05-22T16:17:13.985Z\", \"conclusion\": \"killed\", \"notes\": \"Phantom experiment entry — never submitted (status was PREPARING, no spec/server/command). Cron false alarm. Real experiment is eval-pi05-vla-only-long-seed42-r4 (RUNNING on bjb2-40593).\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T15:48:27.660Z\", \"updated_at\": \"2026-05-22T15:48:27.660Z\"}, \"precompute-smolvla-spatial-k10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T15:48:13.209Z\", \"updated_at\": \"2026-05-22T15:48:13.210Z\"}, \"precompute-smolvla-object-k10\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T15:47:41.690Z\", \"updated_at\": \"2026-05-22T15:47:41.690Z\"}, \"eval-vla-only-long-seed2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T14:19:49.215Z\", \"updated_at\": \"2026-05-22T14:19:49.215Z\"}, \"eval-vla-only-long-seed1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T14:19:43.184Z\", \"updated_at\": \"2026-05-22T14:19:43.184Z\"}, \"eval-vla-only-long-seed0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T14:19:38.265Z\", \"updated_at\": \"2026-05-22T14:19:38.265Z\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:14:43.743Z\", \"updated_at\": \"2026-05-22T13:24:23.378Z\", \"hypothesis\": \"OpenVLA-OFT official repo baseline on LIBERO-Object (10 tasks × 50 trials) — using official eval script and per-suite finetuned weights to establish ground truth baseline\", \"conclusion\": \"failed\", \"notes\": \"官方 repo eval 进程反复死亡（5×），无有效输出。OpenVLA-OFT 已在 D108/D109 中确认为 dead end（0% SR on wrapper + official）。不再追查。\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T01:15:47.132Z\", \"updated_at\": \"2026-05-22T13:24:17.309Z\", \"hypothesis\": \"π0.5 + CRM (Spatial, K=10, obs_dim=2048) eval with final checkpoint will improve upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-spatial-v2\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T01:15:44.738Z\", \"updated_at\": \"2026-05-22T13:24:14.018Z\", \"hypothesis\": \"π0.5 + CRM (Spatial, K=10, obs_dim=2048) eval with final checkpoint will improve upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-spatial-v2\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T01:15:42.369Z\", \"updated_at\": \"2026-05-22T13:24:09.791Z\", \"hypothesis\": \"π0.5 + CRM (Spatial, K=10, obs_dim=2048) eval with final checkpoint will improve upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"parent\": \"crm-train-pi05-spatial-v2\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=124 超时失败（~12h）。旧版 eval（n_action_steps=50 + acr_vla mode）。诊断 Worker 已派发。\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:54:08.543Z\", \"updated_at\": \"2026-05-22T11:51:23.505Z\", \"hypothesis\": \"π0.5 VLA-only baseline re-test with official settings: n_action_steps=10, 10 dummy steps with gripper-open, per-suite max_steps=280\", \"parent\": \"eval-pi05-vla-only-object-seed44-r3\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:55:34.076Z\", \"updated_at\": \"2026-05-22T11:33:17.264Z\", \"hypothesis\": \"Running SmolVLA LIBERO-Object eval through official lerobot pipeline to diagnose 10.8% vs 96% gap — if lerobot achieves ~96%, our wrapper has implementation bugs\", \"conclusion\": \"success\", \"notes\": \"## Root Cause Analysis (post-experiment)\\n\\nThe 66.5% vs 96% gap is explained by MODEL MISMATCH, not eval pipeline bugs:\\n\\n**Paper setup (96% on LIBERO-Object):**\\n- ONE unified multi-task model trained on ALL 40 LIBERO tasks (spatial+object+goal+long, 1693 episodes)\\n- 100,000 steps, batch_size=64\\n- Frozen vision encoder + action expert from scratch\\n\\n**Our local model (66.5% on LIBERO-Object):**\\n- `pepijn223/smolvla_libero` trained ONLY on `libero_spatial` (10 tasks)\\n- 25,000 steps, batch_size=32\\n- Same as official `lerobot/smolvla_libero` on HF Hub\\n\\n**Key findings:**\\n1. No publicly available checkpoint matches the paper's multi-task 100K-step model\\n2. GitHub issue #3287 confirms another researcher also got ~70% trying to reproduce\\n3. Official `lerobot/smolvla_libero` and `lerobot/smolvla_libero_plus` are both trained only on libero_spatial\\n4. The 66.5% result is expected for a spatial-only model evaluated on object tasks (out-of-distribution)\\n\\n**Implications for our wrapper (10.8%):**\\n- Wrapper still has a real bug (10.8% vs 66.5% = 6x gap with same model)\\n- But even with a perfect wrapper, we cannot reach 96% without the correct multi-task checkpoint\\n- Wrapper bugs likely: missing open-loop chunk replay, state dim mismatch, image preprocessing\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:54:01.041Z\", \"updated_at\": \"2026-05-22T11:26:20.250Z\", \"hypothesis\": \"Reducing n_action_steps from 50 to 10 allows PI0.5 to re-plan more frequently, improving VLA-only baseline success rate on LIBERO-Object compared to r3 (81.5%).\", \"parent\": \"eval-pi05-vla-only-object-seed42-r3\", \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}, \"conclusion\": \"success\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T08:57:48.529Z\", \"updated_at\": \"2026-05-22T11:18:23.000Z\", \"hypothesis\": \"Unified CRM trained on all 4 LIBERO suites (Object+Spatial+Goal+Long, 224K samples, K=10) with input_mode=full (unc_dim=40) should generalize across suites, enabling single-model eval on all benchmarks for paper Table\", \"conclusion\": \"failed\", \"metrics\": {\"completed_epochs\": 4, \"target_epochs\": 50, \"exit_code\": 124, \"failure_reason\": \"timeout (EXIT_CODE=124) — killed after 4/50 epochs (~2.3 GPU hours)\", \"best_val_loss\": 0.009633, \"best_epoch\": 4, \"training_curve\": [{\"epoch\": 1, \"train_loss\": 0.019467, \"val_loss\": 0.010801, \"lr\": \"9.99e-04\"}, {\"epoch\": 2, \"train_loss\": 0.018024, \"val_loss\": 0.010438, \"lr\": \"9.96e-04\"}, {\"epoch\": 3, \"train_loss\": 0.017237, \"val_loss\": 0.009901, \"lr\": \"9.91e-04\"}, {\"epoch\": 4, \"train_loss\": 0.01663, \"val_loss\": 0.009633, \"lr\": \"9.84e-04\"}]}}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:14:21.941Z\", \"updated_at\": \"2026-05-22T11:15:49.784Z\", \"hypothesis\": \"Retry: Precompute SmolVLA Long K=2 for crm_cache_v5 after fixing missing directory\", \"parent\": \"precompute-smolvla-long-bjb1-32546\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:27.252Z\", \"updated_at\": \"2026-05-22T11:11:37.983Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Long for unified 4-suite CRM training\", \"conclusion\": \"failed\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:51:37.131Z\", \"hypothesis\": \"Per-DOF weighted MSE loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by weighting each action dimension proportionally to its error magnitude.\", \"parent\": \"crm-loss-perdof\", \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:20.547Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"parent\": \"crm-loss-combined\", \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:40:44.234Z\", \"hypothesis\": \"Conformal-guided loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by incorporating conformal prediction scores into the training objective.\", \"parent\": \"crm-loss-conformal\", \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:44:20.228Z\", \"updated_at\": \"2026-05-22T10:26:08.383Z\", \"hypothesis\": \"MSE-trained CRM eval on SmolVLA Object for controlled loss variant comparison — baseline for perdof/conformal/combined\", \"parent\": \"crm-loss-mse-baseline\", \"metrics\": {\"avg_success_rate\": 7, \"total_successes\": 14, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 10, \"ketchup\": 5, \"tomato_sauce\": 15, \"butter\": 10, \"milk\": 15, \"chocolate_pudding\": 5, \"orange_juice\": 0}}, \"conclusion\": \"negative\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:56:24.604Z\", \"updated_at\": \"2026-05-22T09:00:45.065Z\", \"hypothesis\": \"OpenVLA-OFT (7B deterministic VLA) baseline eval on LIBERO-Object to establish cross-model comparison point; D107 gate CLOSED means no CRM pipeline but VLA-only baseline is needed for paper Table\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": \"all 10 tasks 0.0%\", \"n_rollouts\": 20, \"total_episodes\": 200}}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T09:00:18.250Z\", \"updated_at\": \"2026-05-22T09:00:18.250Z\"}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:32.599Z\", \"updated_at\": \"2026-05-22T08:56:52.782Z\", \"hypothesis\": \"Precomputing obs_features and K=10 action samples for LIBERO-Long (136090 samples) enables efficient offline CRM training without repeated forward passes through SmolVLA backbone.\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 136090, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5, \"obs_features_shape\": [136090, 960], \"k_samples_shape\": [136090, 10, 5, 6], \"expert_actions_shape\": [136090, 5, 6], \"total_time_sec\": 8021, \"speed\": \"0.06s/sample\"}}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T08:03:27.743Z\", \"updated_at\": \"2026-05-22T08:03:27.743Z\"}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T08:03:23.271Z\", \"updated_at\": \"2026-05-22T08:03:23.271Z\"}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T08:03:18.740Z\", \"updated_at\": \"2026-05-22T08:03:18.741Z\"}, \"crm-loss-combined\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:02:25.073Z\", \"updated_at\": \"2026-05-22T07:39:25.644Z\", \"hypothesis\": \"Combined per-DOF weighting + conformal-guided loss will achieve best CRM performance by addressing both DOF importance and correction calibration\", \"metrics\": {\"best_val_loss\": 0.005302, \"final_train_loss\": 0.004481, \"best_epoch\": 48, \"epochs\": 50, \"vs_mse\": \"2.5x worse\", \"vs_perdof\": \"43x worse\", \"dof_weight_range\": [0.0107, 3.7318]}, \"conclusion\": \"negative\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:02:18.756Z\", \"updated_at\": \"2026-05-22T07:37:31.142Z\", \"hypothesis\": \"Conformal-guided auxiliary loss (lambda=0.1) will improve CRM by encouraging correction magnitude proportional to nonconformity, compared to uniform MSE\", \"metrics\": {\"best_val_loss\": 0.013343, \"final_train_loss\": 0.016046, \"epochs\": 50, \"vs_mse\": \"6.4x worse\"}, \"conclusion\": \"negative\", \"notes\": \"Training completed cleanly (50/50 epochs, EXIT_CODE=0). Val loss decreased monotonically 0.037526 (ep1) → 0.013343 (ep50). Final train_loss=0.016046, val_loss=0.013343. The ~6.4x higher val_loss vs MSE baseline (0.013343 vs 0.002080) is EXPECTED and NOT a regression: total loss = MSE + λ·conformal_aux with λ=0.1, so the reported loss is on a strictly larger objective than the MSE-only baseline — direct numeric comparison is invalid. Convergence shape is healthy (still improving at ep50, no divergence). Whether the conformal-guided regularizer actually helps the CRM produce more useful corrections must be judged on downstream robot eval (success rate on SmolVLA Object), not on training-objective loss. Best ckpt saved.\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:29.841Z\", \"updated_at\": \"2026-05-22T07:33:35.175Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training (parallel path)\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:02:15.989Z\", \"updated_at\": \"2026-05-22T06:35:46.165Z\", \"hypothesis\": \"Per-DOF inverse-variance weighted loss will improve CRM by prioritizing high-precision DOFs (rotation/gripper), compared to uniform MSE\", \"metrics\": {\"best_val_loss\": 0.000124, \"final_train_loss\": 0.000141, \"best_epoch\": 50, \"total_epochs\": 50, \"dof_weight_min\": 0.0107, \"dof_weight_max\": 3.7318, \"mse_baseline_val_loss\": 0.00208, \"conformal_guided_val_loss\": 0.013343, \"samples\": 14570, \"crm_params\": 337438}, \"conclusion\": \"success\", \"notes\": \"Training completed successfully (50/50 epochs, EXIT_CODE=0), val_loss continuously improved through final epoch.\\\\n\\\\nPer-DOF weighted val_loss=0.000124 vs MSE baseline val_loss=0.002080. CAVEAT: loss values are NOT directly comparable — perdof_weighted uses inverse-variance weighting (range 0.0107–3.7318, ~350x) which rescales the loss function. The low numerical loss reflects that the model fits high-precision DOFs (rotation/gripper, weight up to 3.73x) very well, while de-emphasizing high-variance DOFs (translation, weight as low as 0.01x).\\\\n\\\\nAll 4 variants completed on same data/architecture:\\\\n- mse: val_loss=0.002080\\\\n- perdof_weighted: val_loss=0.000124\\\\n- conformal_guided: val_loss=0.013343\\\\n- combined: still running (epoch 48, val_loss=0.005302)\\\\n\\\\nDefinitive comparison requires downstream robot evaluation (success rate) with each checkpoint. The per-DOF weighting approach shows excellent convergence and the model prioritizes rotation/gripper precision as designed.\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:02:13.450Z\", \"updated_at\": \"2026-05-22T06:32:42.169Z\", \"hypothesis\": \"MSE baseline re-training on SmolVLA Object for controlled comparison with loss variants\", \"metrics\": {\"best_val_loss\": 0.00208, \"final_train_loss\": 0.004038, \"best_epoch\": 50, \"total_epochs\": 50, \"initial_val_loss\": 0.008373, \"exit_code\": 0}, \"conclusion\": \"success\", \"notes\": \"Training completed cleanly (50/50 epochs, EXIT_CODE=0). Val loss decreased monotonically from 0.008373 (ep1) → 0.002080 (ep50), no overfitting/plateau visible — model still converging at end of cosine schedule. Train_loss=0.004038 vs val_loss=0.002080 (val < train, expected with augmentation noise on train side). Best ckpt saved at epoch 50. Loss values are NOT directly comparable across variants (perdof uses per-DoF weights, conformal_guided adds aux term to MSE); ablation conclusion requires downstream robot eval (success rate on Object task). Provides controlled reference for the 3 loss variants under identical hyperparameters/seed.\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:37:37.065Z\", \"updated_at\": \"2026-05-22T05:56:00.921Z\", \"hypothesis\": \"SmolVLA + ACR-VLA Plan A (K=2 L2-probe + selective CRM obs_only correction, max_norm=0.2) on LIBERO-Goal OOD suite with seed=43 (replication of seed=42) will improve upon SmolVLA VLA-only baseline, contributing to variance estimation\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:12:38.325Z\", \"updated_at\": \"2026-05-22T05:55:17.088Z\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:12:29.206Z\", \"updated_at\": \"2026-05-22T05:55:10.553Z\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:12:21.717Z\", \"updated_at\": \"2026-05-22T05:55:03.970Z\", \"conclusion\": \"killed\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:37:34.598Z\", \"updated_at\": \"2026-05-22T05:54:52.777Z\", \"hypothesis\": \"SmolVLA + ACR-VLA Plan A (K=2 L2-probe + selective CRM obs_only correction, max_norm=0.2) on LIBERO-Long OOD suite will improve upon SmolVLA VLA-only baseline, validating selective-correction efficiency on Long-horizon benchmark\", \"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"RuntimeError: state_dict shape mismatch in CRM checkpoint. input_mean/input_std: [990] vs [1030], net.0.weight: [256,990] vs [256,1030]. CRM checkpoint (crm_v3_norm/obs_only/crm_best.pt) was trained with obs_dim=960 but model now expects obs_dim=1000.\"}}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:37:32.213Z\", \"updated_at\": \"2026-05-22T05:54:08.054Z\", \"hypothesis\": \"SmolVLA + ACR-VLA Plan A (K=2 L2-probe + selective CRM obs_only correction, max_norm=0.2) on LIBERO-Goal OOD suite will improve upon SmolVLA VLA-only baseline, validating selective-correction efficiency on Goal benchmark\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T05:10:41.746Z\", \"updated_at\": \"2026-05-22T05:10:41.746Z\"}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T05:10:32.722Z\", \"updated_at\": \"2026-05-22T05:10:32.722Z\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T21:55:29.833Z\", \"updated_at\": \"2026-05-22T01:31:49.429Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"parent\": \"\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.006138, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T18:26:52.186Z\", \"updated_at\": \"2026-05-22T01:01:07.723Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (69303 object samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization\", \"notes\": \"Training with 69,303 samples (95.6%). Full data available: 72,159 samples (99.5%, shard0 missing ~351 due to kill). Per Director: ≥98% means current checkpoint acceptable. No retrain needed.\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T17:52:42.182Z\", \"updated_at\": \"2026-05-21T18:10:31.701Z\", \"hypothesis\": \"CRM projection trained on π0.5 precomputed features (38500 spatial samples, K=10) will learn to predict conformal refinement corrections that improve upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization of CRM beyond SmolVLA\", \"notes\": \"⚠️ INCOMPLETE DATA (63.9% coverage). Pipeline validation only - checkpoint NOT for paper. Will retrain after precompute completes with full ~60250 samples.\", \"conclusion\": \"killed\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T17:52:37.705Z\", \"updated_at\": \"2026-05-21T18:10:26.906Z\", \"hypothesis\": \"CRM projection trained on π0.5 precomputed features (49700 object samples, K=10) will learn to predict conformal refinement corrections that improve upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization of CRM beyond SmolVLA\", \"notes\": \"⚠️ INCOMPLETE DATA (68.5% coverage). Pipeline validation only - checkpoint NOT for paper. Will retrain after precompute completes with full ~72500 samples.\", \"conclusion\": \"killed\"}, \"crm-pipeline-auto\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T16:37:34.472Z\", \"updated_at\": \"2026-05-21T16:37:34.472Z\"}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T15:04:33.582Z\", \"updated_at\": \"2026-05-21T15:04:33.582Z\"}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:39.622Z\", \"updated_at\": \"2026-05-21T14:19:39.622Z\"}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:35.288Z\", \"updated_at\": \"2026-05-21T14:19:35.288Z\"}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:30.950Z\", \"updated_at\": \"2026-05-21T14:19:30.950Z\"}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:26.580Z\", \"updated_at\": \"2026-05-21T14:19:26.580Z\"}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:22.348Z\", \"updated_at\": \"2026-05-21T14:19:22.348Z\"}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:17.949Z\", \"updated_at\": \"2026-05-21T14:19:17.949Z\"}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:13.168Z\", \"updated_at\": \"2026-05-21T14:19:13.169Z\"}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:08.830Z\", \"updated_at\": \"2026-05-21T14:19:08.830Z\"}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:19:04.514Z\", \"updated_at\": \"2026-05-21T14:19:04.514Z\"}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:27.170Z\", \"updated_at\": \"2026-05-21T14:05:27.170Z\"}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:22.511Z\", \"updated_at\": \"2026-05-21T14:05:22.511Z\"}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:17.907Z\", \"updated_at\": \"2026-05-21T14:05:17.907Z\"}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:13.392Z\", \"updated_at\": \"2026-05-21T14:05:13.392Z\"}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:08.790Z\", \"updated_at\": \"2026-05-21T14:05:08.790Z\"}, \"precompute-pi05-obj-shard9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:50:29.762Z\", \"updated_at\": \"2026-05-21T13:50:29.762Z\"}, \"precompute-pi05-obj-shard8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:50:25.069Z\", \"updated_at\": \"2026-05-21T13:50:25.069Z\"}, \"precompute-pi05-obj-shard7\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:50:20.551Z\", \"updated_at\": \"2026-05-21T13:50:20.551Z\"}, \"precompute-pi05-obj-shard6\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:50:15.986Z\", \"updated_at\": \"2026-05-21T13:50:15.986Z\"}, \"precompute-pi05-obj-shard5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:50:11.352Z\", \"updated_at\": \"2026-05-21T13:50:11.353Z\"}, \"precompute-pi05-spatial-shard6\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:46:14.580Z\", \"updated_at\": \"2026-05-21T13:46:14.580Z\"}, \"precompute-pi05-spatial-shard5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:46:08.912Z\", \"updated_at\": \"2026-05-21T13:46:08.912Z\"}, \"precompute-pi05-spatial-shard4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:46:03.897Z\", \"updated_at\": \"2026-05-21T13:46:03.897Z\"}, \"precompute-pi05-spatial-shard3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:45:58.808Z\", \"updated_at\": \"2026-05-21T13:45:58.808Z\"}, \"precompute-pi05-spatial-shard2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:45:51.058Z\", \"updated_at\": \"2026-05-21T13:45:51.058Z\"}, \"precompute-pi05-spatial-shard1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:45:45.565Z\", \"updated_at\": \"2026-05-21T13:45:45.566Z\"}, \"precompute-pi05-spatial-shard0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T13:45:40.280Z\", \"updated_at\": \"2026-05-21T13:45:40.280Z\"}, \"precompute-pi05-shard0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:13:53.765Z\", \"updated_at\": \"2026-05-21T13:44:35.499Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 0/6). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard9\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:19:30.227Z\", \"updated_at\": \"2026-05-21T13:42:56.355Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 9/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard8\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:19:22.125Z\", \"updated_at\": \"2026-05-21T13:42:50.972Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 8/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard7\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:19:03.096Z\", \"updated_at\": \"2026-05-21T13:42:45.877Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 7/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard6\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:18:56.927Z\", \"updated_at\": \"2026-05-21T13:42:40.538Z\", \"hypothesis\": \"π0.5 CRM feature precompute (shard 6/10). Extract 2048D obs features + K=10 action samples from frozen π0.5 on LIBERO Object+Spatial demos for CRM training.\"}, \"precompute-pi05-shard5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:15:49.135Z\", \"updated_at\": \"2026-05-21T13:42:35.528Z\"}, \"precompute-pi05-shard4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:15:32.187Z\", \"updated_at\": \"2026-05-21T13:42:30.590Z\"}, \"precompute-pi05-shard3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:15:13.099Z\", \"updated_at\": \"2026-05-21T13:42:24.367Z\"}, \"precompute-pi05-shard2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:14:59.128Z\", \"updated_at\": \"2026-05-21T13:42:18.667Z\"}, \"precompute-pi05-shard1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T12:14:44.417Z\", \"updated_at\": \"2026-05-21T13:42:13.102Z\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:51:32.435Z\", \"updated_at\": \"2026-05-21T12:22:59.643Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed45 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:36.820Z\", \"updated_at\": \"2026-05-21T12:22:49.675Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:32.595Z\", \"updated_at\": \"2026-05-21T12:22:43.339Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:27.418Z\", \"updated_at\": \"2026-05-21T12:22:38.751Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:22.502Z\", \"updated_at\": \"2026-05-21T12:22:31.438Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T11:52:16.887Z\", \"updated_at\": \"2026-05-21T12:22:24.249Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 with patched lerobot (VT key remap), cross-VLA validation of CRM\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T11:50:52.186Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"notes\": \"Cron false-positive: marked failed but actually completed successfully. Overall SR 34.0% (34/100) on LIBERO-Spatial with crm_obs_only mode (K=10, max_correction_norm=0.2). Output: /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json. Per-task: between_plate_ramekin=90%, next_to_ramekin=90%, table_center=0%, on_cookie_box=40%, in_top_drawer=10%, on_ramekin=0%, next_to_cookie_box=80%, on_stove=0%, next_to_plate=30%, on_wooden_cabinet=0%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T11:46:53.337Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T11:46:50.878Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T11:46:42.183Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\", \"conclusion\": \"failed\", \"notes\": \"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Stdout buffering may hide further progress. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"notes\": \"KILLED (旧策略 action[0] only). 后续修复历程: (1) action queue fix → bbq_sauce 0/5 (2) vision tower 确认正确加载 (3) 图像 180° 翻转修复 (torch.flip dims=[2,3]) → **Quick verify SR=72%** 修复成功！根因: 官方 lerobot 对图像做 NCHW 180° 旋转，我们的 wrapper 缺失此步骤。\", \"conclusion\": \"killed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:31.173Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"notes\": \"[2026-05-21] 成功完成全部 10 task × 20 rollouts = 200。SR=11.5% (23/200)。Log: /root/autodl-tmp/logs/norm003_seed66.log (bjb1-18228, PID 642428, cuda:0)\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:14:00.886Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T05:13:12.047Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"notes\": \"[2026-05-21 修正] 之前的\\\"task 9/10 异常退出\\\"判断错误。实际进程跑完了全部 10 个 task (20 rollouts each, 共 200)，JSON 已生成: logs/eval_object_crm_obs_only_norm0.05_seed66.json。SR=11.0% (22/200)。原 conclusion=failed 已修正为 success。Log: /root/autodl-tmp/logs/norm005_seed66.log (bjb1-18228)。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T05:10:29.526Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-21T05:07:12.893Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-21T05:07:10.342Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-21T05:07:08.046Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:49.745Z\", \"updated_at\": \"2026-05-21T05:07:05.713Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:49.893Z\", \"updated_at\": \"2026-05-21T05:07:03.314Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:08.378Z\", \"updated_at\": \"2026-05-21T04:55:07.524Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed53. Multi-seed robustness for magnitude curve plan_500.\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-21T04:55:05.083Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-21T04:55:02.734Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与 obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:41.505Z\", \"updated_at\": \"2026-05-21T04:55:00.434Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-21T04:54:57.990Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-21T04:54:54.506Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-21T04:54:51.647Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-21T04:54:44.901Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-21T04:54:42.439Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-21T04:54:39.963Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"notes\": \"Partial result: killed at task 8/10 but SR=16% consistent with norm02 mean (16.8%). Reclassified from failed to success per Director instruction.\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-21T04:54:37.451Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:49:55.438Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\", \"notes\": \"监控误报进程消失。实际正常完成 SR=14.0% (14/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.1_seed67.json (bjb1-18228，注意保存在 /root/logs/ 而非项目 logs/)。进程在完成后自然退出，非异常终止。\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-21T04:48:32.810Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-21T04:48:27.282Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\", \"notes\": \"Experiment completed successfully but stuck in ANALYZING >24h. Manual resolution on 2026-05-21: JSON output confirmed complete (10 tasks × 10 rollouts = 100 total). Overall SR=10%. Per-task SR range: 0.0-0.2.\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-21T04:48:15.442Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:31:32.794Z\", \"updated_at\": \"2026-05-21T04:48:05.210Z\", \"hypothesis\": \"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-21T04:47:51.213Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-21T04:47:46.335Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:49.074Z\", \"updated_at\": \"2026-05-21T04:47:42.399Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-21T04:47:36.667Z\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\", \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-21T04:47:19.616Z\", \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:15.856Z\", \"updated_at\": \"2026-05-21T04:46:30.740Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}, \"notes\": \"Cron false positive — 实际正常完成 SR=35.0% (35/100), trigger_rate=98.0%, mean_unc=0.2619。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:37:28.279Z\", \"updated_at\": \"2026-05-21T04:45:27.640Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:13.764Z\", \"updated_at\": \"2026-05-21T04:44:12.088Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}, \"notes\": \"Cron false positive — 实际正常完成 SR=34.0% (34/100), trigger_rate=97.6%, mean_unc=0.2679。日志在 bjb1-32546。已手动修正。\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:17.907Z\", \"updated_at\": \"2026-05-21T04:42:43.669Z\", \"hypothesis\": \"D090 Plan A Spatial: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:51.140Z\", \"updated_at\": \"2026-05-21T04:42:32.790Z\", \"hypothesis\": \"D090 Plan A: K=2 forward → L2 pairwise distance as uncertainty → if L2 > τ(P50=0.074855): argmin-to-median CRM correction (max_correction_norm=0.2). Selective compute: only correct high-uncertainty steps.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-21T04:34:43.303Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\", \"notes\": \"Random selection baseline seed44 完成。SR=0.11, 10 tasks × 10 rollouts = 100 total。三个 seed 汇总: seed43=0.09, seed44=0.11, seed45=0.10, 均值≈0.10。与 VLA-only baseline 相当，确认 random selection 无法有效利用 K=10 candidates。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-21T04:34:38.177Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T04:34:04.735Z\", \"updated_at\": \"2026-05-21T04:34:32.245Z\", \"hypothesis\": \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:47.309Z\", \"updated_at\": \"2026-05-21T04:32:53.123Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:58.271Z\", \"updated_at\": \"2026-05-21T04:32:42.275Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:47.989Z\", \"updated_at\": \"2026-05-21T04:32:32.158Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:30.715Z\", \"updated_at\": \"2026-05-21T04:32:24.008Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:28.230Z\", \"updated_at\": \"2026-05-21T04:32:17.159Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-21T04:32:11.044Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T04:01:22.020Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T03:59:27.286Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"notes\": \"PID 802634(旧)→802639(旧,killed)→811006(r2,MEAN_STD fix). Dual process conflict resolved. Monitoring until task 5.\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:48.001Z\", \"updated_at\": \"2026-05-21T03:33:43.610Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:33.689Z\", \"updated_at\": \"2026-05-21T03:30:13.218Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:31.269Z\", \"updated_at\": \"2026-05-21T03:30:10.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:23.747Z\", \"updated_at\": \"2026-05-21T03:30:07.112Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判。已手动修正。\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:04.127Z\", \"updated_at\": \"2026-05-21T03:30:04.361Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:20.171Z\", \"updated_at\": \"2026-05-21T03:29:59.855Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed49. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-21T03:29:57.231Z\", \"hypothesis\": \"CRM obs_only with ε=0.1 and K=10 on LIBERO-Object seed48. Low-norm data point for plan_500 magnitude curve, strengthening Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-21T03:29:54.309Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"overall_success_rate\": 0.17}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:51.040Z\", \"updated_at\": \"2026-05-21T03:29:47.720Z\", \"hypothesis\": \"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\", \"parent\": \"eval-obs-only-object-norm01-seed45\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-21T03:29:43.639Z\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:01.005Z\", \"updated_at\": \"2026-05-21T03:29:41.343Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:35.665Z\", \"updated_at\": \"2026-05-21T03:29:39.045Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed50. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:27.458Z\", \"updated_at\": \"2026-05-21T03:29:36.190Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive — 实际正常完成 SR=15.0% (15/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。日志在 bjb1-32546。\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-21T03:29:30.312Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-21T03:29:23.229Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-21T03:29:16.871Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-21T03:29:14.257Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-21T03:29:10.509Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:04.999Z\", \"updated_at\": \"2026-05-21T03:29:06.231Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:02.708Z\", \"updated_at\": \"2026-05-21T03:29:02.399Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:34.507Z\", \"updated_at\": \"2026-05-21T03:28:57.483Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed46. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive: 实验正常完成 SR=15.0%, JSON 已写入。进程退出后 cron 无 sentinel/W&B 标记 → 误判 failed。已修正 conclusion=success。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:01.117Z\", \"updated_at\": \"2026-05-21T03:28:48.787Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-21T03:28:46.427Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:45:20.860Z\", \"updated_at\": \"2026-05-21T03:28:43.998Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"parent\": \"eval-obs-only-object-norm003-seed43\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-21T03:28:41.514Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14% (14/100)。norm003 magnitude curve 数据点，在 VLA-only (10.9%) 和 norm02 (16.8%) 之间。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:14:50.423Z\", \"updated_at\": \"2026-05-21T03:19:50.462Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=19.0%。\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:19:48.034Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:00:59.021Z\", \"updated_at\": \"2026-05-21T03:19:45.881Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"notes\": \"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:18.450Z\", \"updated_at\": \"2026-05-21T03:19:43.346Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:25:26.898Z\", \"updated_at\": \"2026-05-21T03:19:41.023Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=13.0%。\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T03:19:38.737Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:13.220Z\", \"updated_at\": \"2026-05-21T03:17:06.237Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:10.875Z\", \"updated_at\": \"2026-05-21T03:17:01.964Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:57:21.662Z\", \"updated_at\": \"2026-05-21T03:16:58.507Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:08.600Z\", \"updated_at\": \"2026-05-21T03:16:54.862Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:58.578Z\", \"updated_at\": \"2026-05-21T03:16:49.849Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:15:06.396Z\", \"updated_at\": \"2026-05-21T03:16:44.624Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:54.184Z\", \"updated_at\": \"2026-05-21T03:16:34.818Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:14:50.541Z\", \"updated_at\": \"2026-05-21T03:16:26.327Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:18.900Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed75. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:14.621Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed74. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:13:06.825Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed72. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:28.765Z\", \"updated_at\": \"2026-05-21T03:13:03.208Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r2. Redo after python PATH failure on bjb1-32546. Norm sweep seed balance for ε=0.03.\", \"parent\": \"eval-obs-only-object-norm003-seed63\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:12:59.417Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:26.296Z\", \"updated_at\": \"2026-05-21T03:12:55.649Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r2. Redo after python PATH failure on bjb1-32546. Norm sweep seed balance for ε=0.03.\", \"parent\": \"eval-obs-only-object-norm003-seed62\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T03:12:20.827Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed73. Norm sweep seed balance.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:19.545Z\", \"updated_at\": \"2026-05-21T03:11:43.996Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51 r3. Redo after python PATH failure on bjb1-32546. Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed51-r2\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:41:23.364Z\", \"updated_at\": \"2026-05-21T03:10:52.558Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52 r3. Redo after python PATH failure on bjb1-32546. Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed52-r2\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:10:27.996Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed65. Norm sweep filling ε=0.1 gap.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:10:08.688Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed64. Norm sweep filling ε=0.1 gap (ROADMAP TBD).\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:09:32.235Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.05.\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:08:52.713Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.03.\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T03:05:28.591Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.03 (expanding from 3 to 5 seeds).\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:15:11.709Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 同 seed61/seed63,进程在 task1 rollout 5/10 时静默退出。bjb2-28827 SIGHUP 批量故障。已被 seed71-75 替代。\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:14:56.556Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 同 seed61/seed62,进程在 task1 rollout 5/10 时静默退出。bjb2-28827 SIGHUP 批量故障。已被 seed71-75 替代。\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:14:51.727Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed61. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 task1 rollout 5/10 时静默退出,无 Traceback/OOM/CUDA error。日志仅 14 行。与 bjb2-28827 历史 SIGHUP 模式一致(tmux/SSH 断连导致信号杀死进程)。同时失败: seed62, seed63。已被 seed71-75 替代,无需重跑。\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T00:54:21.580Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed64. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:29.353Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:21.900Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.03 (only 3 seeds, need more for reliable mean±std).\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:16.959Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51 r2. Redo of crashed seed51 (process dead, no JSON). Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed51\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:36:12.707Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52 r2. Redo of crashed seed52 (process dead, no JSON). Norm sweep: filling ε=0.1 gap.\", \"parent\": \"eval-obs-only-object-norm01-seed52\", \"conclusion\": \"failed\", \"notes\": \"Real failure: nohup: failed to run command 'python': No such file or directory. bjb1-32546 没有 python 在 PATH 中，需用 /root/miniconda3/bin/python。需重跑。\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:17:19.933Z\", \"updated_at\": \"2026-05-21T00:18:47.313Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 4+.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}, \"notes\": \"Cron false positive — 实际正常完成 SR=11.0% (11/100)。eval 脚本无 W&B/sentinel，cron 误判为 failed。已手动修正。\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:13:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed49 r2. Redo of crashed seed49 (process dead, no JSON). Norm sweep seed balance.\", \"parent\": \"eval-obs-only-object-norm005-seed49\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T00:13:00.000Z\", \"updated_at\": \"2026-05-21T00:13:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed55 r2. Redo of crashed seed55 (process dead, no JSON). Norm sweep seed balance.\", \"parent\": \"eval-obs-only-object-norm005-seed55\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:32:47.109Z\", \"updated_at\": \"2026-05-20T23:28:23.498Z\", \"hypothesis\": \"OpenVLA CRM obs_only eval: 测试 CRM correction 在 OpenVLA (7B, near-deterministic T=0.5) 上的效果。OpenVLA v2 baseline=69%，但 T=0.5 产生近乎相同的 actions (8/10 identical)。关键问题：CRM correction 在低 action diversity 条件下是否仍有效？解决 3 个 review criticals: M1 narrow scope, R2-W1-new low absolute perf, R1-W3-new single VLA。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"sr_pct\": \"0.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:27:35.885Z\", \"updated_at\": \"2026-05-20T22:28:30.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed44 retry2. Norm sweep ε=0.03 data point.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:21:32.888Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:36:46.646Z\", \"updated_at\": \"2026-05-20T22:20:24.412Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed48. Expanding random selection seed coverage for seed balance (plan_600, target n≥5).\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:04:37.390Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:06:18.108Z\", \"updated_at\": \"2026-05-20T21:59:15.550Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed52. Multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T19:45:26.024Z\", \"updated_at\": \"2026-05-20T21:32:35.788Z\", \"conclusion\": \"killed\", \"notes\": \"Killed to free GPU for P0 OpenVLA CRM eval. norm=0.2 已有 7+ seeds，边际价值低。\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T21:16:27.264Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T21:16:23.354Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T21:16:19.344Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-18T10:33:08.510Z\", \"updated_at\": \"2026-05-20T19:45:39.649Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-norm data. seed42=13%, seed43=14%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:18:59.700Z\", \"updated_at\": \"2026-05-20T19:42:34.465Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed42. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.14, \"mean_l2\": 0, \"avg_k\": 1, \"fast_path_pct\": 0.12, \"n_rollouts\": 10}, \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=14%。avg_k=1.0 说明 head 几乎不触发 full-K escalation。低于 GO 阈值 15%。\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:19:04.464Z\", \"updated_at\": \"2026-05-20T19:38:46.967Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed43. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.11, \"n_rollouts\": 100, \"fast_path_pct\": 12.5, \"avg_k\": 1}, \"notes\": \"Cron false positive (日志路径不匹配)。实际正常完成 SR=11%。avg_k=1.0，head 不触发 full-K。低于 GO 阈值 15%，支持 D090 NO-GO 结论。\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:51.325Z\", \"updated_at\": \"2026-05-20T19:34:40.308Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additional perdof seed for multi-seed robustness.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.1, \"n_rollouts\": 100, \"per_task\": [0, 0, 1, 1, 0, 1, 1, 0, 4, 2]}, \"notes\": \"Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=10% (10/100)，与 VLA-only baseline (10.9%) 持平，perdof CRM 无改进。\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T19:21:50.874Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:30:38.520Z\", \"updated_at\": \"2026-05-20T19:18:36.706Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Spatial seed42. Third attempt after prior kills.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}, \"notes\": \"Cron false positive — eval 实际完成，SR=34% (34/100)。与之前 seed42=34% 一致。Random Selection Spatial 三 seeds: 34%, 26%, 28%。\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:31:49.315Z\", \"updated_at\": \"2026-05-20T19:18:34.577Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed50. Additional spatial seed for multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}, \"notes\": \"Cron false positive — eval 实际完成，SR=35% (35/100)。日志在项目目录下而非 ~/runs/，导致 cron 找不到 sentinel。\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:47:46.067Z\", \"updated_at\": \"2026-05-20T19:18:14.214Z\", \"hypothesis\": \"Training CRM obs_only model on OpenVLA features (obs_dim=4096) to enable backbone-agnostic conformal refinement. If successful, CRM can improve any VLA backbone, resolving review critical C3 (single VLA limitation).\", \"parent\": \"openvla-precompute-k1\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}, \"notes\": \"Cron false positive — 训练实际完成 50/50 epochs, best val_loss=0.077260. Checkpoint at /root/autodl-tmp/checkpoints/crm_openvla_obs_only/. 无 W&B/sentinel 导致 cron 误判。\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:49:30.105Z\", \"updated_at\": \"2026-05-20T18:37:09.326Z\", \"hypothesis\": \"Precomputing OpenVLA hidden features at quartile layers [7,15,23,31] will produce multi-scale representations (4×4096) compatible with the CRM K=1 training pipeline, enabling backbone-agnostic conformal refinement.\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:36:03.819Z\", \"updated_at\": \"2026-05-20T17:36:15.098Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Third attempt on bjb1-18228 with updated code.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:56:54.460Z\", \"updated_at\": \"2026-05-20T17:31:38.771Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed49. Testing per-DOF correction architecture for multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:34:01.591Z\", \"updated_at\": \"2026-05-20T17:30:04.397Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed47 (plan_600). Additional seed for random baseline multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:34.419Z\", \"updated_at\": \"2026-05-20T17:28:06.990Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42, retry 2. Prior run killed mid-evaluation. Re-run to fill missing seed42 Spatial CRM data point.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:31:47.920Z\", \"updated_at\": \"2026-05-20T17:22:56.685Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether fewer candidates degrade performance.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:35:38.150Z\", \"updated_at\": \"2026-05-20T17:21:49.990Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 re-run (plan_600). Fresh run on bjb1-18228 for additional baseline data point.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:47:57.755Z\", \"updated_at\": \"2026-05-20T17:20:57.101Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed44. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:02.848Z\", \"updated_at\": \"2026-05-20T16:58:33.591Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Third attempt (M032).\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:00.848Z\", \"updated_at\": \"2026-05-20T16:58:27.648Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Third attempt after unc_dim bugfix + exit file cleanup (M032).\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:50:04.763Z\", \"updated_at\": \"2026-05-20T16:50:59.250Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Third attempt (M032).\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:42:56.456Z\", \"updated_at\": \"2026-05-20T15:35:34.584Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Retry after code fix - additional seed for random baseline comparison.\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T15:34:05.777Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 (plan_600). Additional spatial seed for random baseline to compare against CRM selection on ID suite.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:36.635Z\", \"updated_at\": \"2026-05-20T15:33:54.594Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Additional seed for random baseline to establish statistical comparison against CRM selection.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:32:05.973Z\", \"updated_at\": \"2026-05-20T15:33:15.181Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:48.207Z\", \"updated_at\": \"2026-05-20T15:32:12.693Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:49:20.087Z\", \"updated_at\": \"2026-05-20T15:19:37.689Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42. Filling missing seed42 for Spatial CRM to balance seed coverage across configs.\", \"metrics\": {\"status_note\": \"INCOMPLETE - only 2/10 tasks evaluated before process terminated\", \"partial_per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 1}, \"tasks_completed\": 2, \"tasks_total\": 10}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:27:10.816Z\", \"updated_at\": \"2026-05-20T15:19:01.383Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:06:33.103Z\", \"updated_at\": \"2026-05-20T15:17:24.944Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:07:43.376Z\", \"updated_at\": \"2026-05-20T15:05:10.161Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) on LIBERO-Object seed50. Additional seed for balanced Argmin vs CRM comparison.\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:08:11.387Z\", \"updated_at\": \"2026-05-20T14:59:00.735Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T05:16:21.107Z\", \"updated_at\": \"2026-05-20T14:58:56.897Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed51. Paired baseline for CRM obs_only Goal seed51 (SR=66%) comparison.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:06:37.026Z\", \"updated_at\": \"2026-05-20T14:48:09.495Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:32.629Z\", \"updated_at\": \"2026-05-20T14:37:22.190Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on LIBERO-Object seed45. Controls for sampling diversity vs CRM-guided selection. Plan_600.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:33:04.339Z\", \"updated_at\": \"2026-05-20T14:34:18.084Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed44-plan702\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:33:01.973Z\", \"updated_at\": \"2026-05-20T14:34:14.100Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed43-plan702\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T14:32:58.117Z\", \"updated_at\": \"2026-05-20T14:34:10.003Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed42-plan702\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T14:26:11.524Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:51.797Z\", \"updated_at\": \"2026-05-20T14:26:08.978Z\", \"hypothesis\": \"Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.\", \"parent\": \"eval-argmin-object-k5-seed44\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:56.660Z\", \"updated_at\": \"2026-05-20T14:26:03.273Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.\", \"parent\": \"eval-vla-only-goal-seed44\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:55.082Z\", \"updated_at\": \"2026-05-20T14:25:59.677Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.\", \"parent\": \"eval-obs-only-spatial-norm02-seed46\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}, \"created_at\": \"2026-05-20T13:50:06.703Z\", \"updated_at\": \"2026-05-20T13:50:45.112Z\", \"hypothesis\": \"Latency profiling for VLA+CRM pipeline. Measures wall-clock time for K=1/5/10/20 VLA sampling + CRM inference + conformal scoring.\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:41.144Z\", \"updated_at\": \"2026-05-20T13:33:48.420Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P75 threshold sweep. Existing: seed42=31%, seed43=34%. Validates P75 consistency on Spatial.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}, \"notes\": \"SIGHUP false failure (同 P25-seed44 模式)。全部 100 rollouts 完成, SR=33%。已从 memory.md 恢复 metrics 并修正 conclusion=success。\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:04.411Z\", \"updated_at\": \"2026-05-20T13:32:36.837Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed51. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}, \"notes\": \"Cron false positive — 日志在 /root/acr-vla-conformal-refinement/logs/ 而非 ~/runs/，cron 找不到日志文件误判为 dead。全部 100 rollouts 完成, SR=66%。手动修正 conclusion=success。Goal OOD 持续 neutral (新 n=7: ~67.7% vs VLA 68.7%)。\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:42.913Z\", \"updated_at\": \"2026-05-20T13:31:25.501Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P25 threshold sweep. Completes Spatial sweep table (P25/P50/P75/P90 × 3 seeds).\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}, \"notes\": \"SIGHUP false failure — 全部 100 rollouts 完成, SR=32%, JSON 已保存。EXIT_CODE=129 发生在结果保存之后 (同 P75-seed44 模式)。手动修正 conclusion=success。\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:53:24.027Z\", \"updated_at\": \"2026-05-20T13:26:22.725Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout。完成 400/500 episodes (8/10 tasks)，SR=68.0% (272/400)。第9个task (pick_up_milk) 4/50时被kill。每episode ~60s，500 episodes需~8.3h但timeout仅~6h。已有成果: 前8个task数据完整。建议: 加大timeout_hours至12h重跑。\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:49:04.530Z\", \"updated_at\": \"2026-05-20T13:17:52.468Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed49 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T13:07:47.325Z\", \"updated_at\": \"2026-05-20T13:08:32.542Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Goal seed53. Additional OOD Goal seed for multi-seed robustness.\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:49.157Z\", \"updated_at\": \"2026-05-20T13:07:28.620Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed48 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:14:26.858Z\", \"updated_at\": \"2026-05-20T13:07:16.116Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}, \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:48:11.751Z\", \"updated_at\": \"2026-05-20T13:06:48.437Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed52. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:06:03.701Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:55.751Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:45.262Z\", \"updated_at\": \"2026-05-20T12:54:12.191Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed42. Most aggressive threshold — on Object P90 gives 93% fast_path but SR drops to 13.3%. Tests whether Spatial follows same pattern: high fast_path with SR penalty.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"notes\": \"Cron false positive: EXIT_CODE=129 (SIGHUP after completion). 日志确认 10/10 tasks × 10 rollouts 全部完成，JSON 已写出。手动修正 conclusion=success。\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:50:37.777Z\", \"updated_at\": \"2026-05-20T12:48:49.975Z\", \"hypothesis\": \"CRM obs_only norm02 (ε=0.2) K=10 on Object seed49. Expanding Object CRM norm02 from n=6 to n=7 for seed balance (R2 concern).\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:24.476Z\", \"updated_at\": \"2026-05-20T12:41:49.447Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"failed\", \"metrics\": {\"incomplete\": true, \"tasks_completed\": 2, \"tasks_total\": 10, \"partial_results\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9}, \"failure_reason\": \"Process exited after 2/10 tasks; no JSON output generated; likely OOM or early termination\"}}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:34:55.742Z\", \"updated_at\": \"2026-05-20T11:30:00.787Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"conclusion\": \"success\", \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:34:52.011Z\", \"updated_at\": \"2026-05-20T11:29:58.029Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"conclusion\": \"success\", \"notes\": \"审计修正：JSON 完整（10 tasks × 10 rollouts），实验已成功完成。EXIT_CODE=2 为提交命令路径错误（evaluate.py vs src/evaluate.py），但实际运行的进程已正常完成并写出结果。\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:01:50.026Z\", \"updated_at\": \"2026-05-20T11:13:15.994Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\", \"notes\": \"Reviewer 三次独立验证确认成功：JSON 完整，SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel）。\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:47.126Z\", \"updated_at\": \"2026-05-20T10:52:54.947Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed42. Cross-benchmark threshold sweep: P25 keeps ~65% fast-path on Object, testing transfer to Spatial.\", \"metrics\": {\"overall_success_rate\": 0.33, \"avg_K\": 7.65, \"fast_path_pct\": 29.4, \"mean_l2_distance\": 0.0892, \"threshold\": 0.054959, \"total_steps\": 23410, \"fast_steps\": 6873, \"full_steps\": 16537, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:55.884Z\", \"updated_at\": \"2026-05-20T10:51:17.226Z\", \"hypothesis\": \"Adaptive K with P25 threshold (τ=0.054959) on LIBERO-Spatial will maintain competitive SR compared to K=10 baseline while reducing average inference cost by using fewer refinement steps when the model is confident.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:53.159Z\", \"updated_at\": \"2026-05-20T10:38:12.906Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed43. Second seed for cross-benchmark P75 threshold sweep.\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:19:57.817Z\", \"updated_at\": \"2026-05-20T10:36:14.773Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed43. K-value sweep second seed (plan_601): tests K=20 vs K=10 compute tradeoff.\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:40.709Z\", \"updated_at\": \"2026-05-20T10:34:46.457Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed49 (re-run). Original seed49 data (SR=0.16) removed from analysis due to unverifiable provenance. Clean re-run for data integrity.\", \"parent\": \"eval-vla-only-long-seed49\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:02:44.429Z\", \"updated_at\": \"2026-05-20T10:34:34.589Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed42. Cross-benchmark threshold sweep: P75 keeps ~87% fast-path on Object, testing transfer to Spatial.\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:42:09.659Z\", \"updated_at\": \"2026-05-20T09:52:50.961Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed44\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:49.558Z\", \"updated_at\": \"2026-05-20T09:46:30.063Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed42. ~25% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:51.298Z\", \"updated_at\": \"2026-05-20T09:46:26.443Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed43. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:54.375Z\", \"updated_at\": \"2026-05-20T09:46:22.801Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed42. ~50% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:55.910Z\", \"updated_at\": \"2026-05-20T09:46:19.108Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed43. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:30.506Z\", \"updated_at\": \"2026-05-20T09:26:47.119Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42. Ablation 验证 CRM uncertainty-guided selection 的价值。\", \"notes\": \"2026-05-20 15:06 确认进程活跃: PID 235076, cuda:0, tmux session active, 进度 task 2/10 (~15%). 启动时间 14:40 UTC. 旧 seed44 JSON (SR=0.13) 在磁盘上但会被新运行覆盖.\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:42:06.832Z\", \"updated_at\": \"2026-05-20T09:26:09.877Z\", \"hypothesis\": \"K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855) transfers from Object to Spatial benchmark, achieving comparable SR to fixed K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as core method.\", \"parent\": \"eval-adaptive-k-spatial-p50-seed43\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T06:35:07.755Z\", \"updated_at\": \"2026-05-20T08:44:33.011Z\", \"hypothesis\": \"CRM obs_only norm02 (ε=0.2) K=10 on Object seed42 achieves SR comparable to other norm02 seeds (15-20%), complementing Table 1 from n=6 to n=7 for stronger statistical backing.\", \"notes\": \"2026-05-20 15:06 确认进程活跃: PID 235678, cuda:3, tmux session active, 进度 task 2/10 (~15%). 启动时间 14:40 UTC.\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T07:21:06.879Z\", \"updated_at\": \"2026-05-20T08:42:01.299Z\", \"hypothesis\": \"Formal latency profiling (N=1000) for all inference modes. Measure per-step wall-clock time to populate Table 3 latency column.\", \"conclusion\": \"success\", \"notes\": \"N=1000 profiling 成功完成。Cron 误判 failed（脚本无 sentinel 文件）。JSON: logs/latency_profile_n1000.json (5589 bytes, 17 components × 1000 iterations)。Artifact: art_20260520_de306f。\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:13.788Z\", \"updated_at\": \"2026-05-20T06:53:17.867Z\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.127) on Object seed44. Part of the 4-threshold sweep validating P50 as Pareto optimal.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:16:25.982Z\", \"updated_at\": \"2026-05-20T05:59:13.545Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed54. 补齐 Long baseline 样本量。\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:06.901Z\", \"updated_at\": \"2026-05-20T05:56:34.512Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed43. ~75% steps trigger K=10+CRM. P25 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:15.310Z\", \"updated_at\": \"2026-05-20T05:56:30.173Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed51. 补齐 Spatial CRM 样本量，增强 ID suite correction 效果的统计可靠性。\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:51:05.182Z\", \"updated_at\": \"2026-05-20T05:56:26.105Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed49. 补齐 Goal baseline 样本量，与 CRM-Goal (64-72% SR) 配对对比。\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:18.551Z\", \"updated_at\": \"2026-05-20T05:56:21.658Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed52. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:12:11.506Z\", \"updated_at\": \"2026-05-20T05:56:16.817Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed51. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T02:42:54.485Z\", \"updated_at\": \"2026-05-20T05:56:11.186Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed50. 补齐 Long VLA-only 样本量 (n→9)，增强 OOD baseline 统计可靠性。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:16:23.286Z\", \"updated_at\": \"2026-05-20T05:56:05.404Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed50. Long OOD 补样本量，验证 CRM 在 cross-suite OOD 上的效果。\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T03:16:19.625Z\", \"updated_at\": \"2026-05-20T05:56:00.045Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. 重新部署在干净 GPU 上（原 bjb2-40593 与 calibration 共享 GPU 拖慢）。Sweep 最后一个数据点。\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T02:47:03.770Z\", \"updated_at\": \"2026-05-20T05:39:46.462Z\", \"hypothesis\": \"CRM correction magnitude as zero-overhead gating signal. Three correlation pairs: (1) ρ(K1_correction_mag, K10_var) — primary GO/NO-GO (threshold ρ>0.3); (2) ρ(K2_argmin_correction_mag, K10_var) — fallback if K1 fails; (3) ρ(K1_correction_mag, K2_L2_distance) — cross-validate with proven K=2 signal. If GO: zero-cost adaptive K (CRM 0.25ms, no extra VLA inference).\", \"conclusion\": \"negative\", \"metrics\": {\"go_nogo\": \"NO-GO\", \"rho_k1_corr_vs_k10_var\": 0.1523, \"p_k1_corr_vs_k10_var\": \"6.37e-143\", \"rho_k2_corr_vs_k10_var\": 0.134, \"p_k2_corr_vs_k10_var\": \"8.66e-111\", \"total_steps\": 27626, \"total_episodes\": 100}}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:32.457Z\", \"updated_at\": \"2026-05-20T05:39:32.457Z\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:29.096Z\", \"updated_at\": \"2026-05-20T05:39:29.096Z\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:25.536Z\", \"updated_at\": \"2026-05-20T05:39:25.536Z\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:21.611Z\", \"updated_at\": \"2026-05-20T05:39:21.611Z\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:11.774Z\", \"updated_at\": \"2026-05-20T05:39:11.774Z\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:07.990Z\", \"updated_at\": \"2026-05-20T05:39:07.990Z\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:04.130Z\", \"updated_at\": \"2026-05-20T05:39:04.130Z\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:39:00.913Z\", \"updated_at\": \"2026-05-20T05:39:00.914Z\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:16:27.646Z\", \"updated_at\": \"2026-05-20T05:17:00.091Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed52. 补齐 Goal baseline 样本量 (n→9)。\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:16:24.338Z\", \"updated_at\": \"2026-05-20T05:16:52.571Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed53. 补齐 Long baseline 样本量，与 CRM-Long 配对。\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:16:22.723Z\", \"updated_at\": \"2026-05-20T05:16:49.496Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed51. 补齐 Long CRM OOD 样本量 (n→10)，增强 +3pp 效果的统计显著性。\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T05:16:19.471Z\", \"updated_at\": \"2026-05-20T05:16:42.496Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed50. 补齐 Goal baseline 样本量 (n→7)，与 CRM-Goal (n=7) 配对。\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:08.930Z\", \"updated_at\": \"2026-05-20T05:15:52.486Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed49. 补齐 Long CRM OOD 样本量 (n→8)，验证 CRM 在 OOD Long 上的效果稳定性。\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:05.584Z\", \"updated_at\": \"2026-05-20T05:15:50.831Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed48. 补齐 Long CRM OOD 样本量 (n→7)，验证 CRM 在 OOD Long 上的 +5.3pp 效果是否稳定或集中于单 task。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:57:44.184Z\", \"updated_at\": \"2026-05-20T05:15:47.607Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed48. Goal OOD 补样本量 (n→6)，验证 CRM 在 cross-suite OOD 上的效果。seed46=72% 推高均值，看是否一致。\", \"metrics\": {\"success_rate\": 0.68, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:54:07.709Z\", \"updated_at\": \"2026-05-20T04:33:38.995Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed47. Goal OOD 补样本量 (n→6)，增强 cross-suite OOD 统计可靠性。\", \"metrics\": {\"success_rate\": 0.69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:20:10.184Z\", \"updated_at\": \"2026-05-20T04:13:53.186Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:12:22.300Z\", \"updated_at\": \"2026-05-20T03:12:40.851Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed51. 补齐 Spatial baseline 样本量，与 CRM-Spatial 配对检验。\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:05.392Z\", \"updated_at\": \"2026-05-20T03:05:13.741Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed42. ~75% steps trigger K=10+CRM. 低阈值极端——接近 fixed K=10，验证 SR 上限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:24.943Z\", \"updated_at\": \"2026-05-20T03:02:41.906Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:22.088Z\", \"updated_at\": \"2026-05-20T03:02:34.679Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:43:05.230Z\", \"updated_at\": \"2026-05-20T02:54:29.366Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed46. Goal OOD 补样本量 (n→5)，验证 CRM 在 cross-suite OOD 上的效果（当前 n=2 结果中性 ~69.5%≈VLA-only）。\", \"parent\": \"eval-crm-goal-seed42\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:01.821Z\", \"updated_at\": \"2026-05-20T02:43:30.806Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed51. 补齐 Object VLA-only 样本量 (n→8+)，增强主 ID benchmark baseline 统计可靠性。\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:51.266Z\", \"updated_at\": \"2026-05-20T02:43:21.463Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed49. 补齐 Long VLA-only 样本量 (n→8)，增强 OOD baseline 统计可靠性，与 CRM-Long 配对检验。\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:57.407Z\", \"updated_at\": \"2026-05-20T02:40:24.520Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed44. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:52.859Z\", \"updated_at\": \"2026-05-20T02:40:21.205Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed44. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:12.128Z\", \"updated_at\": \"2026-05-20T02:40:15.747Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed43. ~10% steps trigger K=10+CRM. P90 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:10.641Z\", \"updated_at\": \"2026-05-20T02:40:12.273Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed42. ~10% steps trigger K=10+CRM. 高阈值极端——接近 K=2 only，验证 SR 下限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:53:09.016Z\", \"updated_at\": \"2026-05-20T02:36:09.821Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. ~75% steps trigger K=10+CRM. P25 sweep 第三个 seed。\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:39.170Z\", \"updated_at\": \"2026-05-20T01:39:25.709Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed47. 额外 seed 增加统计稳健性，与 CRM Spatial seed47 配对。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:50.143Z\", \"updated_at\": \"2026-05-20T01:19:10.476Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Spatial seed47. 补齐 CRM-Spatial 第 6 个 seed（当前 n=5, seeds 42-46），增强 in-distribution 效果的统计显著性。\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:19:03.093Z\", \"updated_at\": \"2026-05-20T01:19:03.093Z\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:36.050Z\", \"updated_at\": \"2026-05-20T00:21:06.698Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed47. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是 OOD long-horizon 任务。补充 seed42-46 增加统计样本量。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:15.951Z\", \"updated_at\": \"2026-05-20T00:16:50.121Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed48. 补齐 Long VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:13.996Z\", \"updated_at\": \"2026-05-20T00:13:08.430Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed46. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是未见过的 suite。补齐 CRM-Long 第 5 个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:33.318Z\", \"updated_at\": \"2026-05-20T00:11:46.069Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:31.838Z\", \"updated_at\": \"2026-05-20T00:11:07.345Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed44. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"parent\": \"eval-crm-goal-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:06:58.021Z\", \"updated_at\": \"2026-05-19T23:20:20.286Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed43. 重跑：bjb2-40593 上 7/10 tasks 后进程终止无 JSON。补齐 Spatial K=10 n=5。\", \"parent\": \"eval-obs-only-spatial-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:52.408Z\", \"updated_at\": \"2026-05-19T22:38:04.117Z\", \"hypothesis\": \"K=2 L2 divergence (mean pairwise L2 from K=10 samples) as uncertainty proxy for Adaptive K. Measures action-space disagreement directly. Go/no-go: Spearman ρ(mean_pair_l2, k10_variance) > 0.3.\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:29.495Z\", \"updated_at\": \"2026-05-19T22:15:17.800Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD long-horizon 任务。补充 seed42/43/44 增加 n。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:12:47.550Z\", \"updated_at\": \"2026-05-19T22:12:58.379Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)。重跑（前次进程死亡）。\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:11.071Z\", \"updated_at\": \"2026-05-19T22:12:05.406Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:25.931Z\", \"updated_at\": \"2026-05-19T22:08:08.414Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:01.140Z\", \"updated_at\": \"2026-05-19T21:32:22.969Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed43. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:58.936Z\", \"updated_at\": \"2026-05-19T21:32:21.219Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed42. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:43.834Z\", \"updated_at\": \"2026-05-19T21:32:10.689Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed47. 补齐 Object VLA-only n=5，与 CRM K=10 配对统计检验。\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:50.501Z\", \"updated_at\": \"2026-05-19T21:32:07.617Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed44. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:49.078Z\", \"updated_at\": \"2026-05-19T21:32:03.390Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed43. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:47.244Z\", \"updated_at\": \"2026-05-19T21:31:58.213Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed42. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:24.873Z\", \"updated_at\": \"2026-05-19T21:22:37.560Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed42. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。若 CRM 提升 Goal SR，证明跨 suite 泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:26.786Z\", \"updated_at\": \"2026-05-19T21:19:08.468Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed43. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。与 seed42 配对增加统计稳健性。\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:37.036Z\", \"updated_at\": \"2026-05-19T21:15:20.345Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed46. 补齐 Spatial VLA-only n=5，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:41.106Z\", \"updated_at\": \"2026-05-19T21:14:38.930Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 (Long) with seed47 establishes additional statistical sample (n→6) for baseline success rate estimation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}, \"notes\": \"Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。实际已完成全部 10 tasks。SR=14.0%，与已有 seeds 一致 (mean~14.2%)。手动修正 conclusion=success。\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:44.897Z\", \"updated_at\": \"2026-05-19T20:53:05.054Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:43.382Z\", \"updated_at\": \"2026-05-19T20:52:09.464Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:14.902Z\", \"updated_at\": \"2026-05-19T20:10:50.847Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed45. 补齐 Goal suite 第 4 个 seed (n=4)，与 seed42/43/44-r2 配套。LIBERO-Goal 目标条件泛化 baseline。\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:08.765Z\", \"updated_at\": \"2026-05-19T20:08:19.990Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed46. 补齐 Goal suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"notes\": \"Cron false positive: eval completed normally (71.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:07.011Z\", \"updated_at\": \"2026-05-19T20:08:18.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed46. 补齐 Long suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"notes\": \"Cron false positive: eval completed normally (18.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:57:05.859Z\", \"updated_at\": \"2026-05-19T20:07:21.125Z\", \"hypothesis\": \"FMVD (Flow Velocity Dispersion) signal validation: verify correlation between ODE velocity dispersion during K=1 denoising and K=10 action variance. Go/no-go gate for Adaptive K mechanism (Spearman ρ > 0.3).\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}, \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:11.716Z\", \"updated_at\": \"2026-05-19T19:21:47.544Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed45. 补齐 Long suite 第 4 个 seed (n=4)，与 seed42/43/44 配套。LIBERO-10 长 horizon 任务 baseline。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:24.175Z\", \"updated_at\": \"2026-05-19T19:05:12.052Z\", \"hypothesis\": \"perdof CRM with ε=0.03 (max_correction_norm) on LIBERO-Object seed47 tests whether a smaller correction magnitude improves or degrades task success rate compared to ε=0.05\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:21.800Z\", \"updated_at\": \"2026-05-19T19:05:09.001Z\", \"hypothesis\": \"perdof CRM with ε=0.05 (max_correction_norm) on LIBERO-Object seed47 provides per-DOF conformal refinement; this run supplements the magnitude curve at ε=0.05 (currently n=4)\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:55.593Z\", \"updated_at\": \"2026-05-19T18:38:52.937Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed44. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:49.327Z\", \"updated_at\": \"2026-05-19T18:38:48.009Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed42. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:52.159Z\", \"updated_at\": \"2026-05-19T18:33:56.305Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed43. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:53.389Z\", \"updated_at\": \"2026-05-19T18:07:05.998Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:35.615Z\", \"updated_at\": \"2026-05-19T18:04:19.943Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed47. 补充 Spatial cross-seed 一致性数据。\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:33.151Z\", \"updated_at\": \"2026-05-19T17:24:14.391Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 补充 Spatial K=10 cross-benchmark 数据，当前 n=3 (seed42=35%, seed44=36%, seed45=34%)，扩展到 n=5 增强统计稳健性。\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:21:11.529Z\", \"updated_at\": \"2026-05-19T17:24:12.993Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed44 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:03.921Z\", \"updated_at\": \"2026-05-19T17:08:52.675Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44. LIBERO-Goal 使用相同初始状态不同目标，测试 VLA 对 goal-conditioned 任务的 baseline 表现。\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:30.944Z\", \"updated_at\": \"2026-05-19T16:31:13.969Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:29.373Z\", \"updated_at\": \"2026-05-19T16:31:10.982Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-random-selection-object-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:27.994Z\", \"updated_at\": \"2026-05-19T16:31:08.997Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed43\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:26.607Z\", \"updated_at\": \"2026-05-19T16:31:06.453Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-random-selection-object-k5-seed42\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:32.306Z\", \"updated_at\": \"2026-05-19T16:30:37.908Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:33.621Z\", \"updated_at\": \"2026-05-19T16:30:18.549Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:13:57.251Z\", \"updated_at\": \"2026-05-19T16:17:38.007Z\", \"hypothesis\": \"Latency profiling: 正式测量 VLA+CRM pipeline 各组件 wall-clock time，覆盖 K=1/5/10/20 batched vs sequential，生成论文 Table 级结果。预期 CRM overhead < 1ms，pipeline 主要 bottleneck 在 VLA flow-matching sampling。\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:49.193Z\", \"updated_at\": \"2026-05-19T16:06:07.907Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve perdof ε=0.05 (当前 n=2)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:44.727Z\", \"updated_at\": \"2026-05-19T15:30:01.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed44. Spatial benchmark 第三个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:51.880Z\", \"updated_at\": \"2026-05-19T14:58:17.531Z\", \"hypothesis\": \"obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (当前 n=3)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:01:28.636Z\", \"updated_at\": \"2026-05-19T14:43:19.646Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed43. P1 缺口：与 Spatial K=5 CRM seed43=32% 配对，计算 per-seed improvement。没有此 baseline 无法报告 Spatial 改进幅度。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T12:55:51.909Z\", \"updated_at\": \"2026-05-19T14:38:29.599Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed42. P1 缺口：Spatial benchmark 需要 VLA-only baseline 才能报告 CRM 的改进幅度。对标 obs_only spatial K=10 seed42=35%。\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:40.507Z\", \"updated_at\": \"2026-05-19T14:32:21.490Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:39.233Z\", \"updated_at\": \"2026-05-19T14:32:16.468Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:37.093Z\", \"updated_at\": \"2026-05-19T14:32:11.343Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed45\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:34.934Z\", \"updated_at\": \"2026-05-19T14:32:06.313Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:57:11.028Z\", \"updated_at\": \"2026-05-19T14:32:01.561Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed43\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:43:11.414Z\", \"updated_at\": \"2026-05-19T14:31:56.882Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-argmin-object-k5-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:54.536Z\", \"updated_at\": \"2026-05-19T14:26:11.536Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-19T13:39:15.552Z\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"per-DoF CRM with max_correction_norm=0.1 on LIBERO-Object (seed43, K=10, n_rollouts=10) should achieve comparable SR to obs_only default, as tighter norm constraint limits correction magnitude per joint.\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:53.834Z\", \"updated_at\": \"2026-05-19T13:35:23.895Z\", \"hypothesis\": \"obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=12%)，需标准化。obs_only default 当前 n=3 (seed42/43/44)。\", \"parent\": \"eval-obs-only-object-default-seed45\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:30.602Z\", \"updated_at\": \"2026-05-19T13:30:16.050Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed42 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:36:13.145Z\", \"updated_at\": \"2026-05-19T13:26:50.930Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed45 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:15.812Z\", \"updated_at\": \"2026-05-19T13:26:46.918Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed43 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:18:03.763Z\", \"updated_at\": \"2026-05-19T13:24:40.192Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed43 on LIBERO-Object. 补 magnitude curve：perdof ε=0.3 当前 n=3 (seed42:4%, seed44:4%, seed45:6%)，mean=4.67%。增加第 4 个 seed 强化 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:55.654Z\", \"updated_at\": \"2026-05-19T13:12:13.645Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-19T12:48:29.290Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 CRM full training with multi-stage VLA feature fusion + composite loss (L2 + contrastive + uncertainty-weighted) on full object benchmark dataset. Scaled-up version of train-crm-k1-accg-object-seed42-v2 with complete training data.\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-19T12:48:27.021Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 spatial benchmark precomputation: generate single-sample VLA action predictions and features for CRM K=1 training. Required preprocessing step before K=1 CRM can be trained on spatial tasks.\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-19T12:48:10.176Z\", \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-19T12:48:06.312Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.3 至 n=7。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-19T12:48:03.869Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.1 至 n=7。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:16.472Z\", \"updated_at\": \"2026-05-19T12:48:01.446Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks r3 rerun. Second reproduction of LTO baseline SR=14%. Confirms v2 result consistency.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:29.003Z\", \"updated_at\": \"2026-05-19T12:47:58.882Z\", \"hypothesis\": \"VLA-only baseline on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:26.507Z\", \"updated_at\": \"2026-05-19T12:47:56.312Z\", \"hypothesis\": \"LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:13:30.382Z\", \"updated_at\": \"2026-05-19T12:47:52.436Z\", \"conclusion\": \"success\", \"hypothesis\": \"LTO Split A CRM training (obs_only, 5 tasks, task_indices 0-4). Predecessor to eval-lto-splitA-heldout experiments. Superseded by crm-lto-splitA-train-fixed (task_names matching).\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:31:15.780Z\", \"updated_at\": \"2026-05-19T12:23:18.801Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:22:25.439Z\", \"updated_at\": \"2026-05-19T11:45:28.182Z\", \"hypothesis\": \"Scalar CRM seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current scalar: [9,10,6,9] mean=8.5%\", \"parent\": \"eval-scalar-object-seed45\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:33.036Z\", \"updated_at\": \"2026-05-19T11:34:16.077Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:04:44.384Z\", \"updated_at\": \"2026-05-19T11:34:12.397Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration 补种到 n=7 统计力度增强。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:18.656Z\", \"updated_at\": \"2026-05-19T11:31:39.191Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:24.718Z\", \"updated_at\": \"2026-05-19T11:30:55.300Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 n≥5。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T11:30:43.198Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T11:30:33.951Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:44.467Z\", \"updated_at\": \"2026-05-19T11:30:18.282Z\", \"hypothesis\": \"Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束, success_rate=0%\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:47.310Z\", \"updated_at\": \"2026-05-19T11:30:17.012Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:41.596Z\", \"updated_at\": \"2026-05-19T11:30:15.785Z\", \"hypothesis\": \"Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:35.770Z\", \"updated_at\": \"2026-05-19T11:30:14.493Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:29:18.036Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:27.251Z\", \"updated_at\": \"2026-05-19T11:27:53.132Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 n≥6。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:44:44.161Z\", \"updated_at\": \"2026-05-19T05:16:02.877Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. Retry with timeout=16h after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"conclusion\": \"killed\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:35:02.089Z\", \"updated_at\": \"2026-05-19T05:13:20.212Z\", \"conclusion\": \"killed\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval.\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:34:59.607Z\", \"updated_at\": \"2026-05-19T05:13:18.481Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. If SR > VLA-only on held-out tasks, CRM generalizes beyond training distribution.\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:53:33.612Z\", \"updated_at\": \"2026-05-19T04:58:44.483Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 obs_only ε=0.05 seed (n=4→5)。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:14.835Z\", \"updated_at\": \"2026-05-19T04:58:40.993Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed48 on LIBERO-Object. 补 perdof ε=0.3 至 n=7。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:03.172Z\", \"updated_at\": \"2026-05-19T04:58:36.864Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:27:23.594Z\", \"updated_at\": \"2026-05-19T04:32:49.103Z\", \"conclusion\": \"success\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks. Uses task_names string matching.\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:10.585Z\", \"updated_at\": \"2026-05-19T04:32:33.294Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. 补 magnitude curve ε=0.03 至 n=6。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-19T01:44:05.704Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-19T01:38:34.712Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed45 confirms cross-seed consistency of collapse.\", \"parent\": \"crm-train-v2-perdof\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:38.704Z\", \"updated_at\": \"2026-05-19T01:33:59.345Z\", \"hypothesis\": \"Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T21:05:50.448Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=19%, mean=16.5%). Variance 大 (5pp gap), 第三个 seed 对 K-value scaling narrative 至关重要。\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:31:41.748Z\", \"updated_at\": \"2026-05-18T19:14:55.968Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。重试 r2 修正 python 路径。\", \"parent\": \"eval-perdof-object-norm003-seed44\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T23:53:01.705Z\", \"updated_at\": \"2026-05-18T18:53:10.563Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed42. Magnitude curve comparison point for perdof variant.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T23:53:00.645Z\", \"updated_at\": \"2026-05-18T18:53:09.494Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed42. Intermediate norm point for magnitude curve.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T16:48:10.654Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T15:18:13.193Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:44:42.438Z\", \"updated_at\": \"2026-05-18T14:17:30.462Z\", \"hypothesis\": \"VLA-only baseline seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current VLA-only: [12,12,10,9,13] mean=11.2%\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-18T13:27:03.418Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T12:39:30.555Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T12:33:45.335Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T12:33:41.666Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:56:45.558Z\", \"hypothesis\": \"Perdof CRM with norm clipping ε=0.2 provides controlled corrections that preserve baseline policy behavior on LIBERO-Object. Expected SR ~10% (similar to other seeds 42/44/45/46/47 at 9-12%).\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"killed\", \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\", \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T07:05:18.047Z\", \"updated_at\": \"2026-05-18T00:33:26.447Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed46. Retry after previous run was killed at task 5/10.\", \"conclusion\": \"killed\", \"notes\": \"Retry #2: relaunched on bjb1-32546 cuda:3, PID 562396, tmux session eval-obs-only-object-norm01-seed46-r2. Previous run killed at task 5/10 on bjb1-18228.\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"conclusion\": \"killed\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"conclusion\": \"negative\", \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"conclusion\": \"failed\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"conclusion\": \"failed\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"conclusion\": \"failed\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-15T16:57:00.172Z\", \"updated_at\": \"2026-05-15T17:38:28.909Z\", \"conclusion\": \"killed\", \"notes\": \"Restarted on cuda:3 (PID 118886, tmux: eval-mag-perdof-norm03-object) after v4-default killed. Previous run killed by SIGTERM before first rollout.\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"conclusion\": \"killed\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"conclusion\": \"failed\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"conclusion\": \"killed\"}}, \"count\": 997, \"total\": 997, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4574}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01FBJCQ418dCCUJok2VVfibG`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | contains(\"pi05\")) | \"\\(.key) | status=\\(.value.status // \"?\") | conclusion=\\(.value.conclusion // \"?\")\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Filter pi05 experiments from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "f21f5cb6-ac96-4caa-82a8-34463924fc80",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018mDYRgSRY3R5UK95bMHE8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 34234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
      },
      "output_tokens": 56,
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

_source line 18 · 2026-05-25T00:47:51.017Z_

<details><summary>↩ Tool result · `toolu_01FBJCQ418dCCUJok2VVfibG`</summary>

```text
eval-pi05-vla-only-spatial-s45 | status=DONE | conclusion=success
eval-pi05-vla-only-object-s44 | status=DONE | conclusion=success
eval-pi05-vla-only-object-s43 | status=DONE | conclusion=success
eval-pi05-vla-only-goal-s43 | status=DONE | conclusion=success
eval-pi05-vla-only-goal-s42 | status=DONE | conclusion=success
eval-pi05-vla-only-object-s42 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-s43 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-s42 | status=DONE | conclusion=success
eval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=?
train-crm-pi05-unified-3suite-r2 | status=DONE | conclusion=failed
eval-pi05-reconvla-spatial-s42 | status=PREPARING | conclusion=?
eval-pi05-reconvla-spatial-s42-bf16 | status=PREPARING | conclusion=?
eval-pi05-vla-only-object-seed43-r4 | status=DONE | conclusion=success
eval-pi05-reconvla-object-s42 | status=PREPARING | conclusion=?
eval-pi05-reconvla-goal-s42 | status=PREPARING | conclusion=?
train-crm-pi05-unified-3suite | status=DONE | conclusion=killed
precompute-pi05-object-2048-r2 | status=DONE | conclusion=success
train-crm-pi05-spatial-k1 | status=DONE | conclusion=success
train-crm-pi05-goal-k1 | status=DONE | conclusion=success
precompute-pi05-long-2048-r2 | status=RUNNING | conclusion=?
precompute-pi05-goal-2048-r2 | status=DONE | conclusion=success
precompute-pi05-spatial-2048-r2 | status=DONE | conclusion=success
crm-train-pi05-spatial-full | status=DONE | conclusion=success
eval-pi05-vla-only-long-seed42-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed42 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed43 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed44 | status=DONE | conclusion=success
precompute-pi05-features-object | status=DONE | conclusion=killed
precompute-pi05-goal-2048 | status=DONE | conclusion=failed
precompute-pi05-spatial-2048 | status=DONE | conclusion=failed
precompute-pi05-object-2048 | status=DONE | conclusion=failed
precompute-pi05-long-2048 | status=DONE | conclusion=killed
eval-pi05-vla-only-long-seed42-r4-rerun | status=DONE | conclusion=success
eval-pi05-crm-object-seed44 | status=DONE | conclusion=killed
eval-pi05-crm-object-seed43 | status=DONE | conclusion=killed
eval-pi05-crm-object-seed42 | status=DONE | conclusion=killed
eval-pi05-vla-only-long-seed43-r4-std | status=DONE | conclusion=killed
eval-pi05-vla-only-goal-seed44-r4-std | status=DONE | conclusion=killed
eval-pi05-vla-only-goal-seed42-r4-std | status=DONE | conclusion=killed
eval-pi05-vla-only-long-seed44-r4-std | status=DONE | conclusion=killed
eval-pi05-vla-only-goal-seed43-r4-std | status=DONE | conclusion=killed
eval-pi05-vla-only-goal-seed42-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-seed44-r4 | status=DONE | conclusion=killed
eval-pi05-vla-only-spatial-seed43-r4 | status=DONE | conclusion=killed
eval-pi05-vla-only-spatial-seed42-r4 | status=DONE | conclusion=killed
eval-pi05-vla-only-long-seed44-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-long-seed43-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-goal-seed44-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-goal-seed43-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed
eval-pi05-crm-spatial-seed44 | status=DONE | conclusion=failed
eval-pi05-crm-spatial-seed43 | status=DONE | conclusion=failed
eval-pi05-crm-spatial-seed42 | status=DONE | conclusion=failed
eval-pi05-vla-only-object-seed44-r4 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed42-r4 | status=DONE | conclusion=success
precompute-pi05-long-bjb1-18228 | status=PREPARING | conclusion=?
precompute-pi05-goal-bjb2-28827-s2 | status=PREPARING | conclusion=?
precompute-pi05-goal-bjb2-28827-s1 | status=PREPARING | conclusion=?
precompute-pi05-goal-bjb2-28827-s0 | status=PREPARING | conclusion=?
crm-train-pi05-spatial-v2 | status=DONE | conclusion=success
crm-train-pi05-object-full | status=DONE | conclusion=success
crm-train-pi05-spatial | status=DONE | conclusion=killed
crm-train-pi05-object | status=DONE | conclusion=killed
precompute-pi05-obj-s6-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s9-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s8-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s7-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s0-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s5-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s4-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s3-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s2-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s1-r2 | status=PREPARING | conclusion=?
precompute-pi05-obj-s9-fix | status=PREPARING | conclusion=?
precompute-pi05-obj-s8-fix | status=PREPARING | conclusion=?
precompute-pi05-obj-s7-fix | status=PREPARING | conclusion=?
precompute-pi05-obj-s6-fix | status=PREPARING | conclusion=?
precompute-pi05-obj-s5-fix | status=PREPARING | conclusion=?
precompute-pi05-obj-shard9 | status=PREPARING | conclusion=?
precompute-pi05-obj-shard8 | status=PREPARING | conclusion=?
precompute-pi05-obj-shard7 | status=PREPARING | conclusion=?
precompute-pi05-obj-shard6 | status=PREPARING | conclusion=?
precompute-pi05-obj-shard5 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard6 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard5 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard4 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard3 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard2 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard1 | status=PREPARING | conclusion=?
precompute-pi05-spatial-shard0 | status=PREPARING | conclusion=?
precompute-pi05-shard0 | status=PREPARING | conclusion=?
precompute-pi05-shard9 | status=PREPARING | conclusion=?
precompute-pi05-shard8 | status=PREPARING | conclusion=?
precompute-pi05-shard7 | status=PREPARING | conclusion=?
precompute-pi05-shard6 | status=PREPARING | conclusion=?
precompute-pi05-shard5 | status=PREPARING | conclusion=?
precompute-pi05-shard4 | status=PREPARING | conclusion=?
precompute-pi05-shard3 | status=PREPARING | conclusion=?
precompute-pi05-shard2 | status=PREPARING | conclusion=?
precompute-pi05-shard1 | status=PREPARING | conclusion=?
eval-pi05-vla-only-spatial-seed45 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-seed43-r3 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-seed42-r3 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed44-r3 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed43-r3 | status=DONE | conclusion=success
eval-pi05-vla-only-object-seed42-r3 | status=DONE | conclusion=success
eval-pi05-vla-only-spatial-seed44 | status=DONE | conclusion=failed
eval-pi05-vla-only-spatial-seed43 | status=DONE | conclusion=failed
eval-pi05-vla-only-spatial-seed42 | status=DONE | conclusion=failed
eval-pi05-baseline-object-seed42-r2 | status=PREPARING | conclusion=killed
eval-pi05-baseline-object-seed42 | status=DONE | conclusion=failed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "2317ff23-2d6a-4682-b06a-818a60db71ef",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-spatial-s45 | status=DONE | conclusion=success\neval-pi05-vla-only-object-s44 | status=DONE | conclusion=success\neval-pi05-vla-only-object-s43 | status=DONE | conclusion=success\neval-pi05-vla-only-goal-s43 | status=DONE | conclusion=success\neval-pi05-vla-only-goal-s42 | status=DONE | conclusion=success\neval-pi05-vla-only-object-s42 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-s43 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-s42 | status=DONE | conclusion=success\neval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=?\ntrain-crm-pi05-unified-3suite-r2 | status=DONE | conclusion=failed\neval-pi05-reconvla-spatial-s42 | status=PREPARING | conclusion=?\neval-pi05-reconvla-spatial-s42-bf16 | status=PREPARING | conclusion=?\neval-pi05-vla-only-object-seed43-r4 | status=DONE | conclusion=success\neval-pi05-reconvla-object-s42 | status=PREPARING | conclusion=?\neval-pi05-reconvla-goal-s42 | status=PREPARING | conclusion=?\ntrain-crm-pi05-unified-3suite | status=DONE | conclusion=killed\nprecompute-pi05-object-2048-r2 | status=DONE | conclusion=success\ntrain-crm-pi05-spatial-k1 | status=DONE | conclusion=success\ntrain-crm-pi05-goal-k1 | status=DONE | conclusion=success\nprecompute-pi05-long-2048-r2 | status=RUNNING | conclusion=?\nprecompute-pi05-goal-2048-r2 | status=DONE | conclusion=success\nprecompute-pi05-spatial-2048-r2 | status=DONE | conclusion=success\ncrm-train-pi05-spatial-full | status=DONE | conclusion=success\neval-pi05-vla-only-long-seed42-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed42 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed43 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed44 | status=DONE | conclusion=success\nprecompute-pi05-features-object | status=DONE | conclusion=killed\nprecompute-pi05-goal-2048 | status=DONE | conclusion=failed\nprecompute-pi05-spatial-2048 | status=DONE | conclusion=failed\nprecompute-pi05-object-2048 | status=DONE | conclusion=failed\nprecompute-pi05-long-2048 | status=DONE | conclusion=killed\neval-pi05-vla-only-long-seed42-r4-rerun | status=DONE | conclusion=success\neval-pi05-crm-object-seed44 | status=DONE | conclusion=killed\neval-pi05-crm-object-seed43 | status=DONE | conclusion=killed\neval-pi05-crm-object-seed42 | status=DONE | conclusion=killed\neval-pi05-vla-only-long-seed43-r4-std | status=DONE | conclusion=killed\neval-pi05-vla-only-goal-seed44-r4-std | status=DONE | conclusion=killed\neval-pi05-vla-only-goal-seed42-r4-std | status=DONE | conclusion=killed\neval-pi05-vla-only-long-seed44-r4-std | status=DONE | conclusion=killed\neval-pi05-vla-only-goal-seed43-r4-std | status=DONE | conclusion=killed\neval-pi05-vla-only-goal-seed42-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-seed44-r4 | status=DONE | conclusion=killed\neval-pi05-vla-only-spatial-seed43-r4 | status=DONE | conclusion=killed\neval-pi05-vla-only-spatial-seed42-r4 | status=DONE | conclusion=killed\neval-pi05-vla-only-long-seed44-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-long-seed43-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-goal-seed44-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-goal-seed43-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed\neval-pi05-crm-spatial-seed44 | status=DONE | conclusion=failed\neval-pi05-crm-spatial-seed43 | status=DONE | conclusion=failed\neval-pi05-crm-spatial-seed42 | status=DONE | conclusion=failed\neval-pi05-vla-only-object-seed44-r4 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed42-r4 | status=DONE | conclusion=success\nprecompute-pi05-long-bjb1-18228 | status=PREPARING | conclusion=?\nprecompute-pi05-goal-bjb2-28827-s2 | status=PREPARING | conclusion=?\nprecompute-pi05-goal-bjb2-28827-s1 | status=PREPARING | conclusion=?\nprecompute-pi05-goal-bjb2-28827-s0 | status=PREPARING | conclusion=?\ncrm-train-pi05-spatial-v2 | status=DONE | conclusion=success\ncrm-train-pi05-object-full | status=DONE | conclusion=success\ncrm-train-pi05-spatial | status=DONE | conclusion=killed\ncrm-train-pi05-object | status=DONE | conclusion=killed\nprecompute-pi05-obj-s6-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s9-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s8-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s7-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s0-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s5-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s4-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s3-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s2-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s1-r2 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s9-fix | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s8-fix | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s7-fix | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s6-fix | status=PREPARING | conclusion=?\nprecompute-pi05-obj-s5-fix | status=PREPARING | conclusion=?\nprecompute-pi05-obj-shard9 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-shard8 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-shard7 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-shard6 | status=PREPARING | conclusion=?\nprecompute-pi05-obj-shard5 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard6 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard5 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard4 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard3 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard2 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard1 | status=PREPARING | conclusion=?\nprecompute-pi05-spatial-shard0 | status=PREPARING | conclusion=?\nprecompute-pi05-shard0 | status=PREPARING | conclusion=?\nprecompute-pi05-shard9 | status=PREPARING | conclusion=?\nprecompute-pi05-shard8 | status=PREPARING | conclusion=?\nprecompute-pi05-shard7 | status=PREPARING | conclusion=?\nprecompute-pi05-shard6 | status=PREPARING | conclusion=?\nprecompute-pi05-shard5 | status=PREPARING | conclusion=?\nprecompute-pi05-shard4 | status=PREPARING | conclusion=?\nprecompute-pi05-shard3 | status=PREPARING | conclusion=?\nprecompute-pi05-shard2 | status=PREPARING | conclusion=?\nprecompute-pi05-shard1 | status=PREPARING | conclusion=?\neval-pi05-vla-only-spatial-seed45 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-seed43-r3 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-seed42-r3 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed44-r3 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed43-r3 | status=DONE | conclusion=success\neval-pi05-vla-only-object-seed42-r3 | status=DONE | conclusion=success\neval-pi05-vla-only-spatial-seed44 | status=DONE | conclusion=failed\neval-pi05-vla-only-spatial-seed43 | status=DONE | conclusion=failed\neval-pi05-vla-only-spatial-seed42 | status=DONE | conclusion=failed\neval-pi05-baseline-object-seed42-r2 | status=PREPARING | conclusion=killed\neval-pi05-baseline-object-seed42 | status=DONE | conclusion=failed",
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

_source line 19_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "1a2a5398-e65d-414a-9efd-20958e711473",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NJNLax6ZRbhsN5nyRf3S99",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4122,
      "cache_read_input_tokens": 34890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4122
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01YaYSe2iaZfEG5TzgNVDyZv`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | contains(\"pi05-vla-only\")) | \"\\(.key) | status=\\(.value.status // \"?\") | conclusion=\\(.value.conclusion // \"?\") | metrics=\\(.value.metrics // {} | tostring)\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Check pi05 vla-only metrics state"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "82132c41-144a-458c-9584-57df3f366b7a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NJNLax6ZRbhsN5nyRf3S99",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4122,
      "cache_read_input_tokens": 34890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4122
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

_source line 21 · 2026-05-25T00:48:07.866Z_

<details><summary>↩ Tool result · `toolu_01YaYSe2iaZfEG5TzgNVDyZv`</summary>

```text
eval-pi05-vla-only-spatial-s45 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.85,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"spatial","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-object-s44 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.81,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"object","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-object-s43 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.815,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"object","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-goal-s43 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.97,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"goal","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-goal-s42 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.955,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"goal","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-object-s42 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.965,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"object","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-spatial-s43 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.96,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"spatial","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-spatial-s42 | status=DONE | conclusion=success | metrics={"overall_success_rate":0.98,"n_rollouts":20,"n_tasks":10,"total_rollouts":200,"benchmark":"spatial","mode":"vla_only","model":"pi0.5"}
eval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=? | metrics={}
eval-pi05-vla-only-object-seed43-r4 | status=DONE | conclusion=success | metrics={"success_rate":98.5,"total_successes":197,"total_episodes":200}
eval-pi05-vla-only-long-seed42-r4 | status=DONE | conclusion=success | metrics={"success_rate":0,"successes":0,"total":200}
eval-pi05-vla-only-object-seed42 | status=DONE | conclusion=success | metrics={"overall_sr":0,"per_task_sr":[0,0,0,0,0,0,0,0,0,0],"total_rollouts":200,"n_tasks":10,"n_rollouts_per_task":20}
eval-pi05-vla-only-object-seed43 | status=DONE | conclusion=success | metrics={"overall_sr":0,"per_task_sr":[0,0,0,0,0,0,0,0,0,0],"total_rollouts":200,"n_tasks":10,"n_rollouts_per_task":20}
eval-pi05-vla-only-object-seed44 | status=DONE | conclusion=success | metrics={"overall_sr":0,"per_task_sr":[0,0,0,0,0,0,0,0,0,0],"total_rollouts":200,"n_tasks":10,"n_rollouts_per_task":20}
eval-pi05-vla-only-long-seed42-r4-rerun | status=DONE | conclusion=success | metrics={"success_rate":0.94,"successes":188,"total":200,"per_task":{"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce":0.95,"LIVING_ROOM_SCENE2_cream_cheese_butter":1,"KITCHEN_SCENE3_stove_moka_pot":1,"KITCHEN_SCENE4_black_bowl_drawer":1,"LIVING_ROOM_SCENE5_mugs_on_plates":0.9,"STUDY_SCENE1_book_in_caddy":0.95,"LIVING_ROOM_SCENE6_mug_pudding":1,"LIVING_ROOM_SCENE1_soup_cream_cheese":0.9,"KITCHEN_SCENE8_both_moka_pots":0.8,"KITCHEN_SCENE6_mug_in_microwave":0.9}}
eval-pi05-vla-only-long-seed43-r4-std | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-goal-seed44-r4-std | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-goal-seed42-r4-std | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-long-seed44-r4-std | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-goal-seed43-r4-std | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-goal-seed42-r4 | status=DONE | conclusion=success | metrics={"success_rate":0.98,"successes":196,"total":200}
eval-pi05-vla-only-spatial-seed44-r4 | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-spatial-seed43-r4 | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-spatial-seed42-r4 | status=DONE | conclusion=killed | metrics={}
eval-pi05-vla-only-long-seed44-r4 | status=DONE | conclusion=success | metrics={"success_rate":0.955}
eval-pi05-vla-only-long-seed43-r4 | status=DONE | conclusion=success | metrics={"success_rate":0.955}
eval-pi05-vla-only-goal-seed44-r4 | status=DONE | conclusion=success | metrics={"success_rate":0.975,"successes":195,"total":200}
eval-pi05-vla-only-goal-seed43-r4 | status=DONE | conclusion=success | metrics={"success_rate":0.98,"successes":196,"total":200}
eval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed | metrics={}
eval-pi05-vla-only-object-seed44-r4 | status=DONE | conclusion=success | metrics={"success_rate":99.5,"total_successes":199,"total_episodes":200}
eval-pi05-vla-only-object-seed42-r4 | status=DONE | conclusion=success | metrics={"success_rate":100,"total_success":200,"total_rollouts":200,"n_action_steps":10,"per_task":{"alphabet_soup":100,"cream_cheese":100,"salad_dressing":100,"bbq_sauce":100,"ketchup":100,"tomato_sauce":100,"butter":100,"milk":100,"chocolate_pudding":100,"orange_juice":100}}
eval-pi05-vla-only-spatial-seed45 | status=DONE | conclusion=success | metrics={"success_rate":0.85,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-spatial-seed43-r3 | status=DONE | conclusion=success | metrics={"success_rate":0.83,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-spatial-seed42-r3 | status=DONE | conclusion=success | metrics={"success_rate":0.845,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-object-seed44-r3 | status=DONE | conclusion=success | metrics={"success_rate":0.81,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-object-seed43-r3 | status=DONE | conclusion=success | metrics={"success_rate":0.815,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-object-seed42-r3 | status=DONE | conclusion=success | metrics={"success_rate":0.82,"n_tasks":10,"total_rollouts":200}
eval-pi05-vla-only-spatial-seed44 | status=DONE | conclusion=failed | metrics={}
eval-pi05-vla-only-spatial-seed43 | status=DONE | conclusion=failed | metrics={}
eval-pi05-vla-only-spatial-seed42 | status=DONE | conclusion=failed | metrics={}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "405717db-85d7-4566-b2db-5217c6847d6c",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-spatial-s45 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.85,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"spatial\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-object-s44 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.81,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"object\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-object-s43 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.815,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"object\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-goal-s43 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.97,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"goal\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-goal-s42 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.955,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"goal\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-object-s42 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.965,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"object\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-spatial-s43 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.96,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"spatial\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-spatial-s42 | status=DONE | conclusion=success | metrics={\"overall_success_rate\":0.98,\"n_rollouts\":20,\"n_tasks\":10,\"total_rollouts\":200,\"benchmark\":\"spatial\",\"mode\":\"vla_only\",\"model\":\"pi0.5\"}\neval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=? | metrics={}\neval-pi05-vla-only-object-seed43-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":98.5,\"total_successes\":197,\"total_episodes\":200}\neval-pi05-vla-only-long-seed42-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0,\"successes\":0,\"total\":200}\neval-pi05-vla-only-object-seed42 | status=DONE | conclusion=success | metrics={\"overall_sr\":0,\"per_task_sr\":[0,0,0,0,0,0,0,0,0,0],\"total_rollouts\":200,\"n_tasks\":10,\"n_rollouts_per_task\":20}\neval-pi05-vla-only-object-seed43 | status=DONE | conclusion=success | metrics={\"overall_sr\":0,\"per_task_sr\":[0,0,0,0,0,0,0,0,0,0],\"total_rollouts\":200,\"n_tasks\":10,\"n_rollouts_per_task\":20}\neval-pi05-vla-only-object-seed44 | status=DONE | conclusion=success | metrics={\"overall_sr\":0,\"per_task_sr\":[0,0,0,0,0,0,0,0,0,0],\"total_rollouts\":200,\"n_tasks\":10,\"n_rollouts_per_task\":20}\neval-pi05-vla-only-long-seed42-r4-rerun | status=DONE | conclusion=success | metrics={\"success_rate\":0.94,\"successes\":188,\"total\":200,\"per_task\":{\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\":0.95,\"LIVING_ROOM_SCENE2_cream_cheese_butter\":1,\"KITCHEN_SCENE3_stove_moka_pot\":1,\"KITCHEN_SCENE4_black_bowl_drawer\":1,\"LIVING_ROOM_SCENE5_mugs_on_plates\":0.9,\"STUDY_SCENE1_book_in_caddy\":0.95,\"LIVING_ROOM_SCENE6_mug_pudding\":1,\"LIVING_ROOM_SCENE1_soup_cream_cheese\":0.9,\"KITCHEN_SCENE8_both_moka_pots\":0.8,\"KITCHEN_SCENE6_mug_in_microwave\":0.9}}\neval-pi05-vla-only-long-seed43-r4-std | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-goal-seed44-r4-std | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-goal-seed42-r4-std | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-long-seed44-r4-std | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-goal-seed43-r4-std | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-goal-seed42-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0.98,\"successes\":196,\"total\":200}\neval-pi05-vla-only-spatial-seed44-r4 | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-spatial-seed43-r4 | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-spatial-seed42-r4 | status=DONE | conclusion=killed | metrics={}\neval-pi05-vla-only-long-seed44-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0.955}\neval-pi05-vla-only-long-seed43-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0.955}\neval-pi05-vla-only-goal-seed44-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0.975,\"successes\":195,\"total\":200}\neval-pi05-vla-only-goal-seed43-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":0.98,\"successes\":196,\"total\":200}\neval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed | metrics={}\neval-pi05-vla-only-object-seed44-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":99.5,\"total_successes\":199,\"total_episodes\":200}\neval-pi05-vla-only-object-seed42-r4 | status=DONE | conclusion=success | metrics={\"success_rate\":100,\"total_success\":200,\"total_rollouts\":200,\"n_action_steps\":10,\"per_task\":{\"alphabet_soup\":100,\"cream_cheese\":100,\"salad_dressing\":100,\"bbq_sauce\":100,\"ketchup\":100,\"tomato_sauce\":100,\"butter\":100,\"milk\":100,\"chocolate_pudding\":100,\"orange_juice\":100}}\neval-pi05-vla-only-spatial-seed45 | status=DONE | conclusion=success | metrics={\"success_rate\":0.85,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-spatial-seed43-r3 | status=DONE | conclusion=success | metrics={\"success_rate\":0.83,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-spatial-seed42-r3 | status=DONE | conclusion=success | metrics={\"success_rate\":0.845,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-object-seed44-r3 | status=DONE | conclusion=success | metrics={\"success_rate\":0.81,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-object-seed43-r3 | status=DONE | conclusion=success | metrics={\"success_rate\":0.815,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-object-seed42-r3 | status=DONE | conclusion=success | metrics={\"success_rate\":0.82,\"n_tasks\":10,\"total_rollouts\":200}\neval-pi05-vla-only-spatial-seed44 | status=DONE | conclusion=failed | metrics={}\neval-pi05-vla-only-spatial-seed43 | status=DONE | conclusion=failed | metrics={}\neval-pi05-vla-only-spatial-seed42 | status=DONE | conclusion=failed | metrics={}",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "fb4b3606-bb96-4521-8a3c-696e9d21d983",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XnSQhK1H4XhgGxaHrbbADr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4647,
      "cache_read_input_tokens": 39012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4647
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

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013XxUxLQHKySecx4Gj2ghR5`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "7ee17cd4-d89f-44f4-a3d3-c72e642c7454",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XnSQhK1H4XhgGxaHrbbADr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4647,
      "cache_read_input_tokens": 39012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4647
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

_source line 24 · 2026-05-25T00:48:16.992Z_

<details><summary>↩ Tool result · `toolu_013XxUxLQHKySecx4Gj2ghR5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "ec900768-69a4-4e65-a72c-4a90b44e2d4b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014t88kNFGjjQ9a9eUasLBLo`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "64e7a2be-a830-4412-8c5c-0b1249421852",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XnSQhK1H4XhgGxaHrbbADr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4647,
      "cache_read_input_tokens": 39012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4647
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

_source line 26 · 2026-05-25T00:48:18.018Z_

<details><summary>↩ Tool result · `toolu_014t88kNFGjjQ9a9eUasLBLo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "60e39230-12ed-4409-9f62-3269a4077868",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "231ef634-9395-465f-adf2-377dc51b4169",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018MKa2yYNVCy7YMpdmdWs2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1584,
      "cache_read_input_tokens": 43659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1584
      },
      "output_tokens": 63,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EvybKmb8C6ehWYmjbEW3hF`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "86b5a375-b80d-42b5-9bf5-dc899f416125",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018MKa2yYNVCy7YMpdmdWs2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1584,
      "cache_read_input_tokens": 43659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1584
      },
      "output_tokens": 63,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UUMrtj8VdtFBKDAWozZC8P`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d5e8a652-4541-42c7-9896-f7f5be2991fa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018MKa2yYNVCy7YMpdmdWs2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1584,
      "cache_read_input_tokens": 43659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1584
      },
      "output_tokens": 63,
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

_source line 30 · 2026-05-25T00:48:40.166Z_

<details><summary>↩ Tool result · `toolu_01EvybKmb8C6ehWYmjbEW3hF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1329 May 25 02:47 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1325 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1791 May 22 21:10 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1498 May 25 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1500 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1502 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n-rw-r--r-- 1 root root 1704 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1704 May 25 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1703 May 21 20:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "505cf5e9-8ac2-4f47-9437-84769d90d975",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1329 May 25 02:47 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1325 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\\\n-rw-r--r-- 1 root root 1791 May 22 21:10 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1498 May 25 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1500 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n-rw-r--r-- 1 root root 1502 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n-rw-r--r-- 1 root root 1704 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1704 May 25 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\\n-rw-r--r-- 1 root root 1703 May 21 20:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1329 May 25 02:47 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1325 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1791 May 22 21:10 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1498 May 25 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1500 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1502 May 21 20:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n-rw-r--r-- 1 root root 1704 May 25 02:46 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1704 May 25 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1703 May 21 20:15 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T00:48:40.534Z_

<details><summary>↩ Tool result · `toolu_01UUMrtj8VdtFBKDAWozZC8P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1495 May 22 19:21 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1704 May 22 20:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "39986b99-4135-4fe8-9eca-19bdf66420be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1495 May 22 19:21 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\\\n-rw-r--r-- 1 root root 1704 May 22 20:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1495 May 22 19:21 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1498 May 22 19:23 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json\\n-rw-r--r-- 1 root root 1704 May 22 20:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json\\n-rw-r--r-- 1 root root 1704 May 22 20:17 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "956129f8-b269-400f-9711-b78e6cd689b4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 33_

The new files (May 25) on bjb1-32546 are likely the v2 reruns. Let me read them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "2d6fc5fc-6410-4f77-8648-881428d0efd3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LLbjP1yvgUYvWWKZQehdJ3`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "03eb9244-c962-4e90-8b17-72d8fe5e815f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 35 · 2026-05-25T00:48:51.489Z_

<details><summary>↩ Tool result · `toolu_01LLbjP1yvgUYvWWKZQehdJ3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.955,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a8499ddb-a5a0-4221-a3e4-1e23e283d725",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"goal\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.955,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.955,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SAegKLrDZR2Dgcmz924TxB`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "8bac99ea-dac0-4923-9ad9-9cb96f7164a5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 37 · 2026-05-25T00:48:52.520Z_

<details><summary>↩ Tool result · `toolu_01SAegKLrDZR2Dgcmz924TxB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.97,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "11fb344d-37c0-4f06-bfea-aa9457059afd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"goal\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.97,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.97,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NzUQCijiZV8bUkbqeSgSTH`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "39ff94f7-0471-4686-beee-0e012b322597",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 39 · 2026-05-25T00:48:53.585Z_

<details><summary>↩ Tool result · `toolu_01NzUQCijiZV8bUkbqeSgSTH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "196314cb-85ae-4bde-94d6-31127ced1b04",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.98,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Rcvz5GPbaMsfHPxYs3hCXt`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "362f6578-8023-4441-ac14-667ec02a85fc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 41 · 2026-05-25T00:48:55.154Z_

<details><summary>↩ Tool result · `toolu_01Rcvz5GPbaMsfHPxYs3hCXt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.96,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "ca12056c-44e2-485d-984e-fc676dbc7569",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.96,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.96,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014tEc86HowuLyfh9h2xAeaw`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "c50e40f1-87cd-499f-9dc0-60cc6d3079a1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 43 · 2026-05-25T00:48:56.193Z_

<details><summary>↩ Tool result · `toolu_014tEc86HowuLyfh9h2xAeaw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.965,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "77173992-e308-418a-b94a-34bc1e53b26d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.965,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.965,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CKLaxLDNw7rGMHFx1fojev`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed45.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "7679cde3-dac0-4097-b132-da0fdfed165d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 45 · 2026-05-25T00:48:57.257Z_

<details><summary>↩ Tool result · `toolu_01CKLaxLDNw7rGMHFx1fojev`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.85,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "922b4a6b-376c-4e41-bb3d-73282bcab55a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.85,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 6,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.85,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019HEV5R7tTeTbagSBh4KvPp`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "58665f0a-6a06-4454-85d4-f2806eccc214",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 47 · 2026-05-25T00:48:58.777Z_

<details><summary>↩ Tool result · `toolu_019HEV5R7tTeTbagSBh4KvPp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.94,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "f805bbe2-6be2-4a7a-95f2-f2c6f604de5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.94,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.94,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01138HYYjKTKRYAT25UATAkV`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "fa4ad49b-e171-4e86-acbc-3908173ffd28",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 49 · 2026-05-25T00:48:59.808Z_

<details><summary>↩ Tool result · `toolu_01138HYYjKTKRYAT25UATAkV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.815,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "716c33ba-d4ec-485f-86eb-cdb3feaffc3a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.815,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.6,\\\\n      \\\\\\\"successes\\\\\\\": 12,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.815,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016ekiwsC7vkWENfLAQ7Gp4V`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "b35d9d49-ab11-4037-8063-86c14a202526",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 51 · 2026-05-25T00:49:00.877Z_

<details><summary>↩ Tool result · `toolu_016ekiwsC7vkWENfLAQ7Gp4V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "41987230-a9ac-42b4-b91f-12a54b82694d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.81,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.65,\\\\n      \\\\\\\"successes\\\\\\\": 13,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.55,\\\\n      \\\\\\\"successes\\\\\\\": 11,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M5Wn4K5FwL4fuBsRnNAQgk`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "1aad9346-03b1-43e5-9bdd-3a790aba640d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N7EvKPR34WniRyAP6cajNV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 45243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3309
      },
      "output_tokens": 40,
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

_source line 53 · 2026-05-25T00:49:01.878Z_

<details><summary>↩ Tool result · `toolu_01M5Wn4K5FwL4fuBsRnNAQgk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.985,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "2f06ee1a-ca7b-47a4-b155-2e8c2532f1c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.985,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.985,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d8fd9fc9-10b4-4b76-bd4b-6c1aa7f635be",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VHHxLJgpeKNMFy9722wao7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15176,
      "cache_read_input_tokens": 48552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15176
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

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_0179Rc7zcesM5m26n1KowQnF`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | test(\"pi05-vla-only.*(v2|seed44)$\")) | \"\\(.key) | spec=\\(.value.spec // {} | tostring)\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Check v2 and seed44 entries' specs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "e437c9ea-2b87-42ae-b698-1ef32d310dbb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VHHxLJgpeKNMFy9722wao7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15176,
      "cache_read_input_tokens": 48552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15176
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

_source line 56 · 2026-05-25T00:49:26.008Z_

<details><summary>↩ Tool result · `toolu_0179Rc7zcesM5m26n1KowQnF`</summary>

```text
eval-pi05-vla-only-object-s43-v2 | spec={}
eval-pi05-vla-only-object-s42-v2 | spec={}
eval-pi05-vla-only-goal-s43-v2 | spec={}
eval-pi05-vla-only-goal-s42-v2 | spec={}
eval-pi05-vla-only-spatial-s43-v2 | spec={}
eval-pi05-vla-only-spatial-s42-v2 | spec={}
eval-pi05-vla-only-object-seed44 | spec={}
eval-pi05-vla-only-spatial-seed44 | spec={}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "1cf5c48e-fc71-4b70-8eaa-4ea34cc07414",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-object-s43-v2 | spec={}\neval-pi05-vla-only-object-s42-v2 | spec={}\neval-pi05-vla-only-goal-s43-v2 | spec={}\neval-pi05-vla-only-goal-s42-v2 | spec={}\neval-pi05-vla-only-spatial-s43-v2 | spec={}\neval-pi05-vla-only-spatial-s42-v2 | spec={}\neval-pi05-vla-only-object-seed44 | spec={}\neval-pi05-vla-only-spatial-seed44 | spec={}",
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

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01KwaATK3JKRm5D3pfoHdUva`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | test(\"pi05-vla-only.*(v2|seed44)$\")) | \"\\(.key) | full=\\(.value | tostring)\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Check v2 and seed44 full records"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "ab48f630-bf9f-4906-87b8-fc4c4a34baf9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Drn6AjSNcyQqzbsonMTFye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1972,
      "cache_read_input_tokens": 63728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1972
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

_source line 58 · 2026-05-25T00:49:30.834Z_

<details><summary>↩ Tool result · `toolu_01KwaATK3JKRm5D3pfoHdUva`</summary>

```text
eval-pi05-vla-only-object-s43-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:21:02.532Z","updated_at":"2026-05-24T23:52:12.038Z","hypothesis":"π0.5 VLA-only baseline on Object s43. Cross-architecture validation without CRM.","notes":"INVALID: CUDA OOM crash. alphabet_soup 任务整批 0/20，cream_cheese 受影响降至 70%，导致 overall 86.5% (173/200) 偏低。日志中明确出现 torch.OutOfMemoryError。不要将此结果用于替换 r4 (98.5%)。详见 artifacts/.../pi05_object_s43_investigation.md"}
eval-pi05-vla-only-object-s42-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:20:54.180Z","updated_at":"2026-05-24T23:51:38.741Z","hypothesis":"π0.5 VLA-only baseline on Object s42. Cross-architecture validation without CRM."}
eval-pi05-vla-only-goal-s43-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:20:50.109Z","updated_at":"2026-05-24T23:51:19.479Z","hypothesis":"π0.5 VLA-only baseline on Goal s43. Cross-architecture validation without CRM."}
eval-pi05-vla-only-goal-s42-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:20:44.991Z","updated_at":"2026-05-24T23:51:12.305Z","hypothesis":"π0.5 VLA-only baseline on Goal s42. Cross-architecture validation without CRM."}
eval-pi05-vla-only-spatial-s43-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:20:41.402Z","updated_at":"2026-05-24T23:51:04.205Z","hypothesis":"π0.5 VLA-only baseline on Spatial s43. Cross-architecture validation without CRM."}
eval-pi05-vla-only-spatial-s42-v2 | full={"status":"QUEUED","created_at":"2026-05-24T18:20:36.642Z","updated_at":"2026-05-24T23:50:49.328Z","hypothesis":"π0.5 VLA-only baseline on Spatial s42. Cross-architecture validation without CRM."}
eval-pi05-vla-only-object-seed44 | full={"status":"DONE","created_at":"2026-05-21T08:22:19.985Z","updated_at":"2026-05-24T03:25:23.533Z","hypothesis":"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM","metrics":{"overall_sr":0,"per_task_sr":[0,0,0,0,0,0,0,0,0,0],"total_rollouts":200,"n_tasks":10,"n_rollouts_per_task":20},"conclusion":"success","notes":"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis."}
eval-pi05-vla-only-spatial-seed44 | full={"status":"DONE","created_at":"2026-05-21T08:22:27.768Z","updated_at":"2026-05-21T11:46:53.337Z","hypothesis":"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM","conclusion":"failed","notes":"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial."}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "9a1ec946-becc-4252-8e76-5c1df2033800",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-object-s43-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:21:02.532Z\",\"updated_at\":\"2026-05-24T23:52:12.038Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Object s43. Cross-architecture validation without CRM.\",\"notes\":\"INVALID: CUDA OOM crash. alphabet_soup 任务整批 0/20，cream_cheese 受影响降至 70%，导致 overall 86.5% (173/200) 偏低。日志中明确出现 torch.OutOfMemoryError。不要将此结果用于替换 r4 (98.5%)。详见 artifacts/.../pi05_object_s43_investigation.md\"}\neval-pi05-vla-only-object-s42-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:20:54.180Z\",\"updated_at\":\"2026-05-24T23:51:38.741Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Object s42. Cross-architecture validation without CRM.\"}\neval-pi05-vla-only-goal-s43-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:20:50.109Z\",\"updated_at\":\"2026-05-24T23:51:19.479Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Goal s43. Cross-architecture validation without CRM.\"}\neval-pi05-vla-only-goal-s42-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:20:44.991Z\",\"updated_at\":\"2026-05-24T23:51:12.305Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Goal s42. Cross-architecture validation without CRM.\"}\neval-pi05-vla-only-spatial-s43-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:20:41.402Z\",\"updated_at\":\"2026-05-24T23:51:04.205Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Spatial s43. Cross-architecture validation without CRM.\"}\neval-pi05-vla-only-spatial-s42-v2 | full={\"status\":\"QUEUED\",\"created_at\":\"2026-05-24T18:20:36.642Z\",\"updated_at\":\"2026-05-24T23:50:49.328Z\",\"hypothesis\":\"π0.5 VLA-only baseline on Spatial s42. Cross-architecture validation without CRM.\"}\neval-pi05-vla-only-object-seed44 | full={\"status\":\"DONE\",\"created_at\":\"2026-05-21T08:22:19.985Z\",\"updated_at\":\"2026-05-24T03:25:23.533Z\",\"hypothesis\":\"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\",\"metrics\":{\"overall_sr\":0,\"per_task_sr\":[0,0,0,0,0,0,0,0,0,0],\"total_rollouts\":200,\"n_tasks\":10,\"n_rollouts_per_task\":20},\"conclusion\":\"success\",\"notes\":\"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}\neval-pi05-vla-only-spatial-seed44 | full={\"status\":\"DONE\",\"created_at\":\"2026-05-21T08:22:27.768Z\",\"updated_at\":\"2026-05-21T11:46:53.337Z\",\"hypothesis\":\"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\",\"conclusion\":\"failed\",\"notes\":\"Process killed mid-eval (task 10/10, rollout 10/20). No result JSON. All 9 completed tasks: 0/20 = 0% SR. Task 10 partial: 0/10. Likely system RAM OOM — all 3 seeds killed simultaneously at identical progress point. Clear pattern: PI0.5 VLA-only ~0% on Spatial.\"}",
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

_source line 59_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "4bc4e2a2-7efc-463f-b808-731c1d308ad2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AbGFZx6GUnR74UymC9bRwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 45,
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

_source line 60_

Let me check tmux sessions and existing harvested state more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "0c3d6108-71f9-476d-9d6f-222401bfa876",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AbGFZx6GUnR74UymC9bRwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 45,
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

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TWKsKws6xghEiu4WpHNpVW`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "tmux ls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "163dc072-79d0-48d8-96ac-5e8cf6ac0d83",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AbGFZx6GUnR74UymC9bRwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 45,
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

_source line 62 · 2026-05-25T00:50:11.169Z_

<details><summary>↩ Tool result · `toolu_01TWKsKws6xghEiu4WpHNpVW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "8f8f4df2-3b3a-4301-9ab0-b190e2fa18ee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_0178aKTSYHReQBE3M5zh3fj1`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | test(\"^eval-pi05-vla-only-(spatial|object|goal)-s[0-9]+$\")) | \"\\(.key) | updated=\\(.value.updated_at) | log_path=\\(.value.spec.log_path // .value.log_path // \"?\")\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Check non-v2 entries' updated timestamps and log paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a0270994-f55f-456d-a99d-31e8a4502694",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AbGFZx6GUnR74UymC9bRwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 45,
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

_source line 64 · 2026-05-25T00:50:14.283Z_

<details><summary>↩ Tool result · `toolu_0178aKTSYHReQBE3M5zh3fj1`</summary>

```text
eval-pi05-vla-only-spatial-s45 | updated=2026-05-25T00:46:32.035Z | log_path=?
eval-pi05-vla-only-object-s44 | updated=2026-05-25T00:46:23.539Z | log_path=?
eval-pi05-vla-only-object-s43 | updated=2026-05-25T00:43:50.844Z | log_path=?
eval-pi05-vla-only-goal-s43 | updated=2026-05-25T00:37:52.191Z | log_path=?
eval-pi05-vla-only-goal-s42 | updated=2026-05-25T00:37:45.363Z | log_path=?
eval-pi05-vla-only-object-s42 | updated=2026-05-25T00:37:38.379Z | log_path=?
eval-pi05-vla-only-spatial-s43 | updated=2026-05-25T00:37:31.347Z | log_path=?
eval-pi05-vla-only-spatial-s42 | updated=2026-05-25T00:35:32.912Z | log_path=?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "f96a9f64-6dff-4c2f-9084-a673aa3547ea",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-spatial-s45 | updated=2026-05-25T00:46:32.035Z | log_path=?\neval-pi05-vla-only-object-s44 | updated=2026-05-25T00:46:23.539Z | log_path=?\neval-pi05-vla-only-object-s43 | updated=2026-05-25T00:43:50.844Z | log_path=?\neval-pi05-vla-only-goal-s43 | updated=2026-05-25T00:37:52.191Z | log_path=?\neval-pi05-vla-only-goal-s42 | updated=2026-05-25T00:37:45.363Z | log_path=?\neval-pi05-vla-only-object-s42 | updated=2026-05-25T00:37:38.379Z | log_path=?\neval-pi05-vla-only-spatial-s43 | updated=2026-05-25T00:37:31.347Z | log_path=?\neval-pi05-vla-only-spatial-s42 | updated=2026-05-25T00:35:32.912Z | log_path=?",
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

_source line 65_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "5c8590c6-280a-4efb-9d1f-9ffdb92580a8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

### Assistant

_source line 66_

Let me read the remaining JSON files from bjb1-18228.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "afffe183-4ac7-4b11-91c6-4db931f40564",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QMtzZTN5fbHNPiRFwyUExW`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "5e25aba4-c5f6-4a38-a455-27a56e3ee647",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

_source line 68 · 2026-05-25T00:50:44.985Z_

<details><summary>↩ Tool result · `toolu_01QMtzZTN5fbHNPiRFwyUExW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d5090414-bb0c-420e-8edb-8cbc4a291ac0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.995,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TfbdhZfM1Q1YZPnhFkRb7V`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "e3f1648a-1280-40ce-928d-89a2794b2cc4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

_source line 70 · 2026-05-25T00:50:46.024Z_

<details><summary>↩ Tool result · `toolu_01TfbdhZfM1Q1YZPnhFkRb7V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 1.0,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d4f0d9a3-8b81-4bd9-8e55-9fd9cd909749",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 1.0,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 1.0,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Lrdg4SyVpqW4y1hGMGUdvq`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "b074b1d6-c64d-4e0b-b576-64cd8eac37e9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

_source line 72 · 2026-05-25T00:50:47.538Z_

<details><summary>↩ Tool result · `toolu_01Lrdg4SyVpqW4y1hGMGUdvq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.985,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "fcd084e8-0c84-43a7-933e-1fa966a08fc1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.985,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n      \\\\\\\"successes\\\\\\\": 18,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.985,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FnTjuRWrU36TvdQVyyjptc`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "855be088-b777-4cb1-bb53-a427eb7366a7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

_source line 74 · 2026-05-25T00:50:48.620Z_

<details><summary>↩ Tool result · `toolu_01FnTjuRWrU36TvdQVyyjptc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d3a6480c-ada7-4883-9eca-c7c9370f6468",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.98,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YJ2KwGRtdvyyv3ttNt9MWh`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_pi05_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "b16a0974-4c64-4e3a-ba6c-f24cc66b7090",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SDPk5FuCuksbNv1Y82vFi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 67415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3883
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

_source line 76 · 2026-05-25T00:50:49.512Z_

<details><summary>↩ Tool result · `toolu_01YJ2KwGRtdvyyv3ttNt9MWh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.975,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "c51244d3-43e2-4f57-b78a-5e9f54a762f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.975,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.75,\\\\n      \\\\\\\"successes\\\\\\\": 15,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.975,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 77_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "3b0cbc9d-38f8-4dc6-ac8b-6269f2a65887",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HVt1m2g5h68NPTNEjxbdk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9203,
      "cache_read_input_tokens": 71298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9203
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

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01BMovvUxBgmzrCh58UCRaHj`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | test(\"^eval-pi05-vla-only-(spatial|object|goal)-s[0-9]+(-v2)?$\")) | \"\\(.key) | created=\\(.value.created_at) | updated=\\(.value.updated_at) | status=\\(.value.status)\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt | sort",
  "description": "Compare creation timestamps for v2 vs non-v2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a682a130-5bc5-4d9f-b87c-a9b5f17fa95b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HVt1m2g5h68NPTNEjxbdk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9203,
      "cache_read_input_tokens": 71298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9203
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

_source line 79 · 2026-05-25T00:51:36.114Z_

<details><summary>↩ Tool result · `toolu_01BMovvUxBgmzrCh58UCRaHj`</summary>

```text
eval-pi05-vla-only-goal-s42 | created=2026-05-24T18:17:16.938Z | updated=2026-05-25T00:37:45.363Z | status=DONE
eval-pi05-vla-only-goal-s42-v2 | created=2026-05-24T18:20:44.991Z | updated=2026-05-24T23:51:12.305Z | status=QUEUED
eval-pi05-vla-only-goal-s43 | created=2026-05-24T18:17:20.358Z | updated=2026-05-25T00:37:52.191Z | status=DONE
eval-pi05-vla-only-goal-s43-v2 | created=2026-05-24T18:20:50.109Z | updated=2026-05-24T23:51:19.479Z | status=QUEUED
eval-pi05-vla-only-object-s42 | created=2026-05-24T18:17:23.924Z | updated=2026-05-25T00:37:38.379Z | status=DONE
eval-pi05-vla-only-object-s42-v2 | created=2026-05-24T18:20:54.180Z | updated=2026-05-24T23:51:38.741Z | status=QUEUED
eval-pi05-vla-only-object-s43 | created=2026-05-24T18:17:27.320Z | updated=2026-05-25T00:43:50.844Z | status=DONE
eval-pi05-vla-only-object-s43-v2 | created=2026-05-24T18:21:02.532Z | updated=2026-05-24T23:52:12.038Z | status=QUEUED
eval-pi05-vla-only-object-s44 | created=2026-05-25T00:44:04.114Z | updated=2026-05-25T00:46:23.539Z | status=DONE
eval-pi05-vla-only-spatial-s42 | created=2026-05-24T18:17:09.880Z | updated=2026-05-25T00:35:32.912Z | status=DONE
eval-pi05-vla-only-spatial-s42-v2 | created=2026-05-24T18:20:36.642Z | updated=2026-05-24T23:50:49.328Z | status=QUEUED
eval-pi05-vla-only-spatial-s43 | created=2026-05-24T18:17:13.434Z | updated=2026-05-25T00:37:31.347Z | status=DONE
eval-pi05-vla-only-spatial-s43-v2 | created=2026-05-24T18:20:41.402Z | updated=2026-05-24T23:51:04.205Z | status=QUEUED
eval-pi05-vla-only-spatial-s45 | created=2026-05-25T00:44:07.720Z | updated=2026-05-25T00:46:32.035Z | status=DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "80974917-b4e8-4e43-95f8-4bd7b1f77cd3",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-goal-s42 | created=2026-05-24T18:17:16.938Z | updated=2026-05-25T00:37:45.363Z | status=DONE\neval-pi05-vla-only-goal-s42-v2 | created=2026-05-24T18:20:44.991Z | updated=2026-05-24T23:51:12.305Z | status=QUEUED\neval-pi05-vla-only-goal-s43 | created=2026-05-24T18:17:20.358Z | updated=2026-05-25T00:37:52.191Z | status=DONE\neval-pi05-vla-only-goal-s43-v2 | created=2026-05-24T18:20:50.109Z | updated=2026-05-24T23:51:19.479Z | status=QUEUED\neval-pi05-vla-only-object-s42 | created=2026-05-24T18:17:23.924Z | updated=2026-05-25T00:37:38.379Z | status=DONE\neval-pi05-vla-only-object-s42-v2 | created=2026-05-24T18:20:54.180Z | updated=2026-05-24T23:51:38.741Z | status=QUEUED\neval-pi05-vla-only-object-s43 | created=2026-05-24T18:17:27.320Z | updated=2026-05-25T00:43:50.844Z | status=DONE\neval-pi05-vla-only-object-s43-v2 | created=2026-05-24T18:21:02.532Z | updated=2026-05-24T23:52:12.038Z | status=QUEUED\neval-pi05-vla-only-object-s44 | created=2026-05-25T00:44:04.114Z | updated=2026-05-25T00:46:23.539Z | status=DONE\neval-pi05-vla-only-spatial-s42 | created=2026-05-24T18:17:09.880Z | updated=2026-05-25T00:35:32.912Z | status=DONE\neval-pi05-vla-only-spatial-s42-v2 | created=2026-05-24T18:20:36.642Z | updated=2026-05-24T23:50:49.328Z | status=QUEUED\neval-pi05-vla-only-spatial-s43 | created=2026-05-24T18:17:13.434Z | updated=2026-05-25T00:37:31.347Z | status=DONE\neval-pi05-vla-only-spatial-s43-v2 | created=2026-05-24T18:20:41.402Z | updated=2026-05-24T23:51:04.205Z | status=QUEUED\neval-pi05-vla-only-spatial-s45 | created=2026-05-25T00:44:07.720Z | updated=2026-05-25T00:46:32.035Z | status=DONE",
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

_source line 80_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "f3ead65c-532f-4150-b701-2fd75ea0c1ad",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WuPJkwzS5bMpZUaT1KAYxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4553,
      "cache_read_input_tokens": 80501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4553
      },
      "output_tokens": 45,
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

_source line 81_

Let me check the registry's overall harvest state to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "03ace6ad-f3a6-4ea8-953e-99d94e3c9972",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WuPJkwzS5bMpZUaT1KAYxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4553,
      "cache_read_input_tokens": 80501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4553
      },
      "output_tokens": 45,
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

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_015JZ4guqa24HSHgHHUrKDU3`</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[] | select(.key | contains(\"pi05\") and (contains(\"vla-only\") or contains(\"VLA-only\"))) | select(.value.status == \"RUNNING\" or .value.status == \"PENDING\" or .value.status == \"QUEUED\" or .value.status == \"PREPARING\") | \"\\(.key) | status=\\(.value.status) | conclusion=\\(.value.conclusion // \"?\")\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/8bed2a86-f76d-426c-b76f-09c08092a431/tool-results/mcp-agent-ml-research-read_registry-1779670065690.txt",
  "description": "Find pi05 vla-only entries needing attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "6142790d-427d-4fe9-adda-97c025106a86",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WuPJkwzS5bMpZUaT1KAYxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4553,
      "cache_read_input_tokens": 80501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4553
      },
      "output_tokens": 45,
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

_source line 83 · 2026-05-25T00:52:15.155Z_

<details><summary>↩ Tool result · `toolu_015JZ4guqa24HSHgHHUrKDU3`</summary>

```text
eval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=?
eval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a2648232-25cf-430c-8f7d-dd4eeefb9b49",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-object-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-object-s42-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-goal-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-goal-s42-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-spatial-s43-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-spatial-s42-v2 | status=QUEUED | conclusion=?\neval-pi05-vla-only-long-seed42-r4-std | status=PREPARING | conclusion=killed",
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

_source line 84_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "72a5c556-e8c5-4b42-899d-1f4c9fef0258",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fd3CmeoZZbXomAc9bYYwHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 85054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3169
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

### Assistant

_source line 85_

Let me do a broader search for any other π0.5 result files I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a328610d-3fb9-4b81-b514-1520cfd5ff33",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fd3CmeoZZbXomAc9bYYwHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 85054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3169
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

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013JAJRDeTsmSqpCPb8eRT2j`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement -name \"*pi05*vla*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "37265ba0-d472-4186-bbb9-3db37ce2fa27",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fd3CmeoZZbXomAc9bYYwHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 85054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3169
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

_source line 87 · 2026-05-25T00:52:36.921Z_

<details><summary>↩ Tool result · `toolu_013JAJRDeTsmSqpCPb8eRT2j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a34c8c88-99cb-4937-9345-727cd452b6bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012StHmekFU8GgygNdnY76Rb`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement -name \"*pi05*vla*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "0ff6793d-447c-4399-a708-27da20cc1f08",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fd3CmeoZZbXomAc9bYYwHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 85054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3169
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

_source line 89 · 2026-05-25T00:52:37.997Z_

<details><summary>↩ Tool result · `toolu_012StHmekFU8GgygNdnY76Rb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "a3408d00-4e90-4f0f-bf9a-5eb6569f1b8d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TAkfeyZR5uDPWVmxosTe4a`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "find /root -maxdepth 4 -name \"*pi05*\" -name \"*.json\" -newer /tmp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "7f06f854-dcac-4f17-88df-604333bd015a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fd3CmeoZZbXomAc9bYYwHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 85054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3169
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

_source line 91 · 2026-05-25T00:52:38.969Z_

<details><summary>↩ Tool result · `toolu_01TAkfeyZR5uDPWVmxosTe4a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "2de42320-75d2-4bc7-8d30-539b33d1963c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013bWmHGcir1F8M9rCRwWSPL`</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement -path \"*/results/*\" -name \"*pi05*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "1fcdb338-76f1-404b-a4a4-8a0cae41fa85",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EqHhEbPDzB7mKp46N6KqJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2176,
      "cache_read_input_tokens": 88223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2176
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

_source line 93 · 2026-05-25T00:52:43.390Z_

<details><summary>↩ Tool result · `toolu_013bWmHGcir1F8M9rCRwWSPL`</summary>

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
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "6dae9dcf-c335-4779-ac5b-cef02f4015dc",
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

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XbS9ucTeR4Hi439M7dWv8X`</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "find /root/acr-vla-conformal-refinement -path \"*/results/*\" -name \"*pi05*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "50975259-2137-47b7-b2f4-ef62988fb834",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EqHhEbPDzB7mKp46N6KqJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2176,
      "cache_read_input_tokens": 88223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2176
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

_source line 95 · 2026-05-25T00:52:44.130Z_

<details><summary>↩ Tool result · `toolu_01XbS9ucTeR4Hi439M7dWv8X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "d21eae64-354a-45e9-8006-880a04343e20",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 96_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "64fdb99b-9b3e-4805-ba5d-4d6875a3d83d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0125HPz5C97ViRBpbSnr5VAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 90399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
      },
      "output_tokens": 50,
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

_source line 97_

Harvest 状态已确认完整。所有 π0.5 VLA-only JSON 文件均已正确 harvest 到 registry，无新结果需要添加。

## π0.5 VLA-only 结果汇总

### 已 harvest 进 registry 的实验（8 个 DONE/success）

| exp_id | Suite | Seed | SR | JSON 源 |
|--------|-------|------|------|---------|
| eval-pi05-vla-only-spatial-s42 | spatial | 42 | **0.980** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s43 | spatial | 43 | **0.960** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s45 | spatial | 45 | **0.850** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s42 | object | 42 | **0.965** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-object-s43 | object | 43 | **0.815** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s44 | object | 44 | **0.810** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-goal-s42 | goal | 42 | **0.955** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-goal-s43 | goal | 43 | **0.970** | bjb1-32546 (5/25) |

### 仍 QUEUED 但无独立结果的 v2 stub 条目（6 个）

object-s42-v2, object-s43-v2, goal-s42-v2, goal-s43-v2, spatial-s42-v2, spatial-s43-v2

- 创建于 2026-05-24T18:20Z（比对应非-v2 条目晚 3 分钟），从未进入 RUNNING 状态
- bjb1-32546 上的 May 25 JSON 已被非-v2 条目消费，v2 条目并无独立 JSON
- object-s43-v2 之前注解为 "INVALID OOM"

### bjb1-18228 上的 JSON（已映射到 -r4 系列）

bjb1-18228 的 6 个 JSON（5/22）映射到已 harvest 的 `eval-pi05-vla-only-{object,spatial}-seed{42,43,44}-r4` 条目（SR 完全匹配 1.0/0.985/0.995/0.98/0.975/0.985）。spatial-seed44 在 r4 系列被标 killed/无 metrics，但 r3/r4 系列已是历史归档，未列入当前需 harvest 范围。

### 结论

无需调用 update_registry——所有可 harvest 的 π0.5 VLA-only 结果已经在 registry 中。"上次 harvest 失败" 的实际状态：harvest 已成功完成，遗留的 6 个 v2 QUEUED 条目是重复 stub 而非未 harvest 结果。如需清理，可单独标记这 6 个 v2 条目为 superseded。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "uuid": "5e3db0b2-e50b-498c-9d93-24c95d7f0e6f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0125HPz5C97ViRBpbSnr5VAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 90399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
      },
      "output_tokens": 50,
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

_source line 98_

Harvest 状态已确认完整。所有 π0.5 VLA-only JSON 文件均已正确 harvest 到 registry，无新结果需要添加。

## π0.5 VLA-only 结果汇总

### 已 harvest 进 registry 的实验（8 个 DONE/success）

| exp_id | Suite | Seed | SR | JSON 源 |
|--------|-------|------|------|---------|
| eval-pi05-vla-only-spatial-s42 | spatial | 42 | **0.980** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s43 | spatial | 43 | **0.960** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s45 | spatial | 45 | **0.850** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s42 | object | 42 | **0.965** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-object-s43 | object | 43 | **0.815** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s44 | object | 44 | **0.810** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-goal-s42 | goal | 42 | **0.955** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-goal-s43 | goal | 43 | **0.970** | bjb1-32546 (5/25) |

### 仍 QUEUED 但无独立结果的 v2 stub 条目（6 个）

object-s42-v2, object-s43-v2, goal-s42-v2, goal-s43-v2, spatial-s42-v2, spatial-s43-v2

- 创建于 2026-05-24T18:20Z（比对应非-v2 条目晚 3 分钟），从未进入 RUNNING 状态
- bjb1-32546 上的 May 25 JSON 已被非-v2 条目消费，v2 条目并无独立 JSON
- object-s43-v2 之前注解为 "INVALID OOM"

### bjb1-18228 上的 JSON（已映射到 -r4 系列）

bjb1-18228 的 6 个 JSON（5/22）映射到已 harvest 的 `eval-pi05-vla-only-{object,spatial}-seed{42,43,44}-r4` 条目（SR 完全匹配 1.0/0.985/0.995/0.98/0.975/0.985）。spatial-seed44 在 r4 系列被标 killed/无 metrics，但 r3/r4 系列已是历史归档，未列入当前需 harvest 范围。

### 结论

无需调用 update_registry——所有可 harvest 的 π0.5 VLA-only 结果已经在 registry 中。"上次 harvest 失败" 的实际状态：harvest 已成功完成，遗留的 6 个 v2 QUEUED 条目是重复 stub 而非未 harvest 结果。如需清理，可单独标记这 6 个 v2 条目为 superseded。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 341372,
  "duration_api_ms": 333730,
  "num_turns": 38,
  "stop_reason": "end_turn",
  "session_id": "8bed2a86-f76d-426c-b76f-09c08092a431",
  "total_cost_usd": 1.6462037499999997,
  "usage": {
    "input_tokens": 27,
    "cache_creation_input_tokens": 89487,
    "cache_read_input_tokens": 923986,
    "output_tokens": 24931,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 89487,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1468,
        "cache_read_input_tokens": 90399,
        "cache_creation_input_tokens": 586,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 586
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1402,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001507,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 27,
      "outputTokens": 24931,
      "cacheReadInputTokens": 923986,
      "cacheCreationInputTokens": 89487,
      "webSearchRequests": 0,
      "costUSD": 1.6446967499999998,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2224398-9286-4dc0-ba05-f9f9f9f86b70"
}
```

</details>

---

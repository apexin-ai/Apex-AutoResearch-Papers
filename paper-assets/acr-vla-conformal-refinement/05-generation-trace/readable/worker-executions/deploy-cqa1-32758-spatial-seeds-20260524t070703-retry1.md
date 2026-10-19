# deploy cqa1 32758 spatial seeds 20260524T070703 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-spatial-seeds_20260524T070703_retry1.log`
- **Structured JSON:** [`fc37eba4505c12e24b29.json`](../../sessions/fc/fc37eba4505c12e24b29.json)

## Before a recorded user message

34 recorded events

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
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
  "uuid": "80431515-ccde-4efa-b00b-b95cd2b368e3",
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
    "resetsAt": 1779610200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c32a2055-f336-4c16-b4ad-d9a2e7b91317",
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209"
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "b1e3157a-dee1-4662-a285-24e375bbb62f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Gof8CnPwg9gCRaUekvAXpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15338,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15338
      },
      "output_tokens": 0,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VHpb5K1nPKexPiaMmELieL`</summary>

```json
{
  "query": "select:read_registry,update_registry,ssh_read_only,ssh_execute,detect_image",
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "2e322597-0f90-4a80-982d-247f33aeacc2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Gof8CnPwg9gCRaUekvAXpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15338,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15338
      },
      "output_tokens": 0,
      "service_tier": "standard",
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

_source line 6 · 2026-05-24T07:07:23.638Z_

<details><summary>↩ Tool result · `toolu_01VHpb5K1nPKexPiaMmELieL`</summary>

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "5e060088-8384-498b-8985-2356c350f7c8",
  "tool_use_result": {
    "matches": [],
    "query": "select:read_registry,update_registry,ssh_read_only,ssh_execute,detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Shpgx3yGmSrzAC5JF48ADb`</summary>

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "fbb104c5-0dff-4f8d-b37e-d0d591febb46",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01W3949r3BpYBQGFbH11ictb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 31579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 8 · 2026-05-24T07:07:26.726Z_

<details><summary>↩ Tool result · `toolu_01Shpgx3yGmSrzAC5JF48ADb`</summary>

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "002480c2-6650-41c7-aea2-92ed5e6885b8",
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

_source line 9_

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "474bdbba-50a5-47ee-b250-556b959f8f72",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01W2UB5kdMTh4Av6nET2ivvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17804,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17804
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29166
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EdCEcUv1P9LCaH4heef5t1`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id_prefix": "eval-supp-goal"
  },
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "3b6aad2e-c057-42fc-a876-1565d2c3129a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01W2UB5kdMTh4Av6nET2ivvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17804,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17804
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29166
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CC2L43TPV4z3TkqAsFJrSE`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id_prefix": "eval-supp-spatial"
  },
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "deb82e50-286a-495c-adb0-6c83e981d7b3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01W2UB5kdMTh4Av6nET2ivvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17804,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17804
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29166
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T07:07:33.180Z_

<details><summary>↩ Tool result · `toolu_01EdCEcUv1P9LCaH4heef5t1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0515}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "c0b0868c-f680-4617-8648-e1684874d509",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0515}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0515}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T07:07:36.969Z_

<details><summary>↩ Tool result · `toolu_01CC2L43TPV4z3TkqAsFJrSE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7623}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "a0f48e36-f6a8-4ebf-8d03-8dcbf2cf0183",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.7623}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7623}}"
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "7de40bb8-4a40-411e-a1e6-da579f8c40de",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JUpWs39HFaGpBdN5CPhZjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 34138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 614
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0166axsa8iHpDWoHrSix7KFT`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "841d3774-2485-4d34-b8b6-30c8cd7d0d1f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JUpWs39HFaGpBdN5CPhZjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 34138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 614
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

_source line 16 · 2026-05-24T07:07:41.928Z_

<details><summary>↩ Tool result · `toolu_0166axsa8iHpDWoHrSix7KFT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:07:37.003Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:16.953Z\", \"updated_at\": \"2026-05-24T07:06:31.785Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:13.683Z\", \"updated_at\": \"2026-05-24T07:06:23.946Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:10.482Z\", \"updated_at\": \"2026-05-24T07:06:15.932Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:07.178Z\", \"updated_at\": \"2026-05-24T07:06:09.666Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T03:56:52.910Z\", \"updated_at\": \"2026-05-24T06:55:16.446Z\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:22:29.274Z\", \"updated_at\": \"2026-05-24T06:49:49.091Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:19.029Z\", \"updated_at\": \"2026-05-24T06:49:36.626Z\", \"hypothesis\": \"VLA-only baseline on Object suite seed45. Fills s45 gap in Object VLA-only 5-seed coverage (have s42-s44, s46) for supplementary table.\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:12.741Z\", \"updated_at\": \"2026-05-24T06:45:22.337Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Spatial suite seed45. Sixth seed extending Spatial CRM always-on variance coverage for supplementary table.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}, \"notes\": \"Eval completed normally. 78.0% (156/200). Results at logs/eval_spatial_crm_obs_only_norm0.05_seed45.json on cqa1-32758. Cron escalated as process-gone but script had already exited after completion.\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:09.089Z\", \"updated_at\": \"2026-05-24T06:45:16.646Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Sixth seed extending Spatial VLA-only variance coverage for supplementary table.\", \"conclusion\": \"success\", \"notes\": \"Eval completed normally on cqa1-32758. SR=77.0% (154/200). Results at logs/eval_spatial_vla_only_seed45.json. Per-task: between_plate_ramekin 90%, next_to_ramekin 90%, table_center 90%, on_cookie_box 100%, top_drawer 75%, on_ramekin 0%, next_to_cookie_box 95%, on_stove 75%, next_to_plate 80%, on_wooden_cabinet 75%.\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:32:56.953Z\", \"updated_at\": \"2026-05-24T06:33:34.726Z\", \"hypothesis\": \"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T06:33:29.735Z\", \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T06:33:25.524Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T06:33:17.189Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:46.960Z\", \"updated_at\": \"2026-05-24T06:33:11.821Z\", \"hypothesis\": \"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\", \"conclusion\": \"failed\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:18:27.873Z\", \"updated_at\": \"2026-05-24T06:23:35.000Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Goal enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"conclusion\": \"success\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T06:15:12.631Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T05:52:22.340Z\", \"updated_at\": \"2026-05-24T06:13:04.507Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Spatial enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:21.518Z\", \"updated_at\": \"2026-05-24T05:44:03.369Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:24.393Z\", \"updated_at\": \"2026-05-24T05:43:32.643Z\", \"hypothesis\": \"Goal VLA-only baseline seed46. Fifth seed extending Goal VLA-only. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:35.384Z\", \"updated_at\": \"2026-05-24T05:43:26.502Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal suite seed46. Fifth seed extending Goal Reconvla. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T18:48:38.574Z\", \"updated_at\": \"2026-05-24T03:28:46.242Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-24T03:27:16.008Z\", \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-24T03:27:10.816Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"conclusion\": \"success\", \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:50.876Z\", \"updated_at\": \"2026-05-24T03:27:05.531Z\", \"hypothesis\": \"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-24T03:27:01.680Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-24T03:26:55.797Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:26:47.449Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:26:39.499Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T12:22:12.815Z\", \"updated_at\": \"2026-05-24T03:26:27.340Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-24T03:25:46.138Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-24T03:25:36.173Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-24T03:25:23.533Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:20:29.949Z\", \"updated_at\": \"2026-05-24T03:24:43.469Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed45. Fourth seed extending Long K2mean coverage. VLA-only s45 on bjb1-32546 provides baseline.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:24.679Z\", \"updated_at\": \"2026-05-24T03:24:33.666Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed46. Extends Goal K2mean to 4th completed seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:43.468Z\", \"updated_at\": \"2026-05-24T03:24:30.058Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed46. Fifth seed extending Goal Adaptive. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:31.022Z\", \"updated_at\": \"2026-05-24T03:24:26.680Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed46. Fifth seed extending Goal CRM. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:42:31.834Z\", \"updated_at\": \"2026-05-24T03:19:19.270Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"parent\": \"eval-supp-spatial-adapt-tau025-s45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:59:42.673Z\", \"updated_at\": \"2026-05-24T03:18:33.793Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed45. Fourth seed extending Spatial K2mean. Fills Table 1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:34:46.225Z\", \"updated_at\": \"2026-05-24T03:18:27.488Z\", \"hypothesis\": \"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:52:50.566Z\", \"updated_at\": \"2026-05-24T03:18:20.676Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:45:59.585Z\", \"updated_at\": \"2026-05-24T03:18:17.471Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:22:31.743Z\", \"updated_at\": \"2026-05-24T03:18:14.133Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:50.126Z\", \"updated_at\": \"2026-05-24T00:54:53.307Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:41.239Z\", \"updated_at\": \"2026-05-24T00:53:11.757Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed45. Fourth seed for Long Adaptive validation.\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:32.639Z\", \"updated_at\": \"2026-05-24T00:53:04.280Z\", \"hypothesis\": \"Long VLA-only baseline seed45. Fourth seed for Long baseline. s42=58.0%, s43=59.5%, s44=56.5%.\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:16.039Z\", \"updated_at\": \"2026-05-24T00:30:53.206Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed45. Fourth seed extending Spatial Reconvla. 3-seed: 79.8%±1.0%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}, \"notes\": \"Cron false positive — eval script completed normally with 79.5% (159/200). Results at logs/eval_spatial_reconvla_seed45.json on cqa1-32758. No W&B/sentinel used by eval scripts.\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:04.113Z\", \"updated_at\": \"2026-05-24T00:21:09.215Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed45. Matched-seed companion for Goal s45 4-seed extension.\", \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:59.880Z\", \"updated_at\": \"2026-05-23T23:45:46.677Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Extends Object Adaptive coverage. Trigger rate expected ~3-5% on Object tasks.\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:29.185Z\", \"updated_at\": \"2026-05-23T23:45:41.402Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Duplicate of eval-supp-k2mean-obj-s45 (already DONE SR=77.5%). Killed to free GPU.\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:43.001Z\", \"updated_at\": \"2026-05-23T23:43:24.974Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fifth seed extending Object CRM. Previous seeds show ~79-81% range.\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-23T22:23:46.061Z\", \"updated_at\": \"2026-05-23T23:42:01.475Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:25.473Z\", \"updated_at\": \"2026-05-23T23:04:07.248Z\", \"hypothesis\": \"Long K=2 mean baseline seed44. Third seed for Long K=2 mean validation. Isolates multi-sample averaging on long-horizon tasks.\", \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:31.761Z\", \"updated_at\": \"2026-05-23T23:04:01.262Z\", \"hypothesis\": \"Long Reconvla K=10 seed44. Third seed for Long Reconvla 3-seed validation. s42=56.5% (below VLA-only 58.0%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-23T23:02:16.008Z\", \"updated_at\": \"2026-05-23T23:02:16.008Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Spatial suite seed45. Fourth seed completing Spatial k2mean coverage (s42=negative, s43/s44=done). Isolates multi-sample averaging effect.\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:38.416Z\", \"updated_at\": \"2026-05-23T22:57:24.122Z\", \"hypothesis\": \"Reconvla K=10 on Goal suite seed45. Fourth seed extending Goal Reconvla. 3-seed mean: 80.8%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果文件: logs/eval_goal_reconvla_seed45.json\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:29.087Z\", \"updated_at\": \"2026-05-23T22:57:20.913Z\", \"hypothesis\": \"Goal VLA-only baseline seed45. Fourth seed extending Goal baseline. Matched-seed companion for Goal Adaptive s45.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果文件: logs/eval_goal_vla_only_seed45.json\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:20.093Z\", \"updated_at\": \"2026-05-23T22:57:13.555Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fills the last Object s46 method gap.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判为 failed。日志确认 79.5% (159/200)。结果文件: logs/eval_object_crm_obs_only_norm0.05_seed46.json\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:32.501Z\", \"updated_at\": \"2026-05-23T22:56:01.038Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed45. Fourth seed extending Goal CRM. 3-seed mean: 83.7%±1.8%.\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\", \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果文件: logs/eval_goal_crm_obs_only_norm0.05_seed45.json\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:15:28.966Z\", \"updated_at\": \"2026-05-23T22:37:07.655Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed45. Extends Object method coverage for 5-seed Adaptive variance investigation.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:41:19.029Z\", \"updated_at\": \"2026-05-23T22:31:59.949Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed46. Extends Object method coverage for 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:13:06.213Z\", \"updated_at\": \"2026-05-23T22:31:49.469Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed45. Extends Goal Adaptive from 3-seed to 4-seed.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:35.159Z\", \"updated_at\": \"2026-05-23T21:28:56.768Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed44. Third seed for Long CRM 3-seed validation.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:32.204Z\", \"updated_at\": \"2026-05-23T21:28:50.765Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed44. Third seed for Long Adaptive 3-seed validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:58.207Z\", \"updated_at\": \"2026-05-23T21:28:27.870Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed46. Companion baseline for Object Adaptive s46 5-seed extension.\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:52.406Z\", \"updated_at\": \"2026-05-23T21:28:21.695Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Companion baseline for Object Adaptive s45 5-seed extension.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:06.320Z\", \"updated_at\": \"2026-05-23T20:26:37.804Z\", \"hypothesis\": \"Object Adaptive τ=0.25 seed46. User-requested additional seed to assess Object Adaptive variance.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:55:45.292Z\", \"updated_at\": \"2026-05-23T20:21:04.060Z\", \"hypothesis\": \"VLA-only baseline on Long suite seed43. Duplicate deployment on bjb2-28827; primary results already harvested from cqa1 (SR=59.5%).\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:22:32.322Z\", \"updated_at\": \"2026-05-23T20:13:10.758Z\", \"metrics\": {\"SR\": 0.57}, \"conclusion\": \"negative\", \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. VLA-only s42=58.0% baseline.\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:24:10.813Z\", \"updated_at\": \"2026-05-23T20:09:46.499Z\", \"hypothesis\": \"Object VLA-only baseline seed46. Companion baseline for Object Adaptive s46 comparison. 3-seed baseline: 77.8%±1.0%.\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-23T20:09:40.603Z\", \"hypothesis\": \"Long VLA-only baseline seed44. Second seed for Long baseline. s42=58.0%.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:36.825Z\", \"updated_at\": \"2026-05-23T20:09:34.819Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed43. Isolates multi-sample averaging effect on Long tasks.\", \"metrics\": {\"SR\": 0.56}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:30.979Z\", \"updated_at\": \"2026-05-23T20:09:28.982Z\", \"hypothesis\": \"Reconvla K=10 argmin on Long suite seed43. Second seed for Long Reconvla validation.\", \"metrics\": {\"SR\": 0.59}, \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:26.229Z\", \"updated_at\": \"2026-05-23T20:09:23.098Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed43. Second seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.545}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:21.251Z\", \"updated_at\": \"2026-05-23T20:09:17.172Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed43. Second seed for Long Adaptive validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}, \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:55:59.154Z\", \"updated_at\": \"2026-05-23T18:16:04.202Z\", \"hypothesis\": \"Retry of eval-supp-obj-adapt-tau025-s45. Object Adaptive CRM τ=0.25 seed45 on bjb2-40593 after fixing missing CRM checkpoint.\", \"parent\": \"eval-supp-obj-adapt-tau025-s45\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:44.431Z\", \"updated_at\": \"2026-05-23T17:25:47.737Z\", \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:38.730Z\", \"updated_at\": \"2026-05-23T17:25:41.523Z\", \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:33.117Z\", \"updated_at\": \"2026-05-23T17:25:32.561Z\", \"hypothesis\": \"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:39.811Z\", \"updated_at\": \"2026-05-23T17:25:24.644Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold → lower trigger rate → fewer corrections. Part of 5-point τ-sensitivity curve. Tests whether very conservative gating still maintains benefit.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}, \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:36.431Z\", \"updated_at\": \"2026-05-23T17:25:15.441Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.15 on Goal s42. Mid-low threshold. Part of 5-point τ-sensitivity curve. Tests transition zone between aggressive and conservative gating.\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:27:45.450Z\", \"updated_at\": \"2026-05-23T17:25:06.995Z\", \"hypothesis\": \"K=2 mean baseline on Object seed44. Third seed for 3-seed mean±std. s42=79.5%, s43 running. Isolates multi-sample averaging on Object tasks.\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:32.832Z\", \"updated_at\": \"2026-05-23T17:24:59.810Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold → higher CRM trigger rate → more corrections. Part of 5-point τ-sensitivity curve (0.10, 0.15, 0.25, 0.40, always-on). Tests whether aggressive gating improves or hurts Goal performance.\", \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:31:41.302Z\", \"updated_at\": \"2026-05-23T17:24:48.531Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed44. s42=79.0%, s43 running on bjb2-28827. Third seed for Object Reconvla validation.\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:51:10.407Z\", \"updated_at\": \"2026-05-23T17:22:10.552Z\", \"hypothesis\": \"VLA-only baseline on Spatial seed44. s42=78.5%. Second/third seed for 3-seed Spatial VLA-only baseline mean±std.\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:18.236Z\", \"updated_at\": \"2026-05-23T17:21:50.650Z\", \"hypothesis\": \"Goal VLA-only wrapper s44 re-run. Previous result lost due to JSON filename collision with k2mean-s44. Confirms 83.5% baseline across seeds (s42=83.5%, s43=82.5%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:23:34.262Z\", \"updated_at\": \"2026-05-23T14:41:49.032Z\", \"hypothesis\": \"K=2 mean baseline on Spatial seed44. Third seed for 3-seed mean±std. s42=81.5%, s43 running. Isolates multi-sample averaging effect from CRM correction on Spatial.\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}}, \"count\": 100, \"total\": 881, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9561}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "c9bd985b-1f87-44a0-a1fe-b2225c1de62e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-24T07:07:37.003Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:07:37.003Z\\\", \\\"hypothesis\\\": \\\"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\\\"}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:16.953Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:31.785Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:13.683Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:23.946Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:10.482Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:15.932Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:07.178Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:09.666Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:23.532Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:05:36.964Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\\\"}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T03:56:52.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:55:16.446Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.765, \\\"successes\\\": 153, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb2-40593\\\", \\\"json_file\\\": \\\"eval_object_crm_obs_only_norm0.05_seed45.json\\\"}, \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:52:08.968Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\"}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:52:05.630Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\"}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:51:27.049Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\"}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:48:57.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:52.276Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\"}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:48:54.415Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:44.120Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\\\"}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:48:50.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:37.107Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\\\"}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:48:46.040Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:30.794Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\"}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:22:29.274Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:49.091Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-obj-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:27:19.029Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:36.626Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Object suite seed45. Fills s45 gap in Object VLA-only 5-seed coverage (have s42-s44, s46) for supplementary table.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.76}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T21:31:12.741Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:45:22.337Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Spatial suite seed45. Sixth seed extending Spatial CRM always-on variance coverage for supplementary table.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.78, \\\"successes\\\": 156, \\\"total\\\": 200, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 1, \\\"next_to_ramekin\\\": 1, \\\"table_center\\\": 0.9, \\\"on_cookie_box\\\": 1, \\\"top_drawer_cabinet\\\": 0.7, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.95, \\\"on_stove\\\": 0.8, \\\"next_to_plate\\\": 0.75, \\\"on_wooden_cabinet\\\": 0.7}}, \\\"notes\\\": \\\"Eval completed normally. 78.0% (156/200). Results at logs/eval_spatial_crm_obs_only_norm0.05_seed45.json on cqa1-32758. Cron escalated as process-gone but script had already exited after completion.\\\"}, \\\"eval-supp-spatial-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T21:31:09.089Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:45:16.646Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed45. Sixth seed extending Spatial VLA-only variance coverage for supplementary table.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Eval completed normally on cqa1-32758. SR=77.0% (154/200). Results at logs/eval_spatial_vla_only_seed45.json. Per-task: between_plate_ramekin 90%, next_to_ramekin 90%, table_center 90%, on_cookie_box 100%, top_drawer 75%, on_ramekin 0%, next_to_cookie_box 95%, on_stove 75%, next_to_plate 80%, on_wooden_cabinet 75%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.77, \\\"successes\\\": 154, \\\"total\\\": 200}}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:34:20.287Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:38:39.651Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\\\"}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:32:56.953Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:33:34.726Z\\\", \\\"hypothesis\\\": \\\"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\\\"}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T03:23:24.189Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:33:29.735Z\\\", \\\"hypothesis\\\": \\\"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T00:55:40.981Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:33:25.524Z\\\", \\\"hypothesis\\\": \\\"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T00:55:34.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:33:17.189Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T00:55:46.960Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:33:11.821Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:18:31.140Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\"}, \\\"precompute-pi05-goal-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T06:18:27.873Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:35.000Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Goal enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-24T06:18:24.705Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:31.677Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\"}, \\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T00:32:53.028Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:15:12.631Z\\\", \\\"hypothesis\\\": \\\"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 60.5, \\\"successes\\\": 121, \\\"total\\\": 200, \\\"source\\\": \\\"reviewer_manual_check\\\"}}, \\\"precompute-pi05-spatial-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T05:52:22.340Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:13:04.507Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Spatial enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\"}, \\\"precompute-smolvla-goal-bjb1-32546\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T06:35:21.518Z\\\", \\\"updated_at\\\": \\\"2026-05-24T05:44:03.369Z\\\", \\\"hypothesis\\\": \\\"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-supp-goal-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:02:24.393Z\\\", \\\"updated_at\\\": \\\"2026-05-24T05:43:32.643Z\\\", \\\"hypothesis\\\": \\\"Goal VLA-only baseline seed46. Fifth seed extending Goal VLA-only. s42-s45 mean ~84%. Completes 5-seed coverage.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.83, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:02:35.384Z\\\", \\\"updated_at\\\": \\\"2026-05-24T05:43:26.502Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Goal suite seed46. Fifth seed extending Goal Reconvla. s42-s45 mean ~83%. Completes 5-seed coverage.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-pi05-spatial-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T18:48:38.574Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:28:46.242Z\\\", \\\"hypothesis\\\": \\\"CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.006138, \\\"epochs_completed\\\": 50, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\\\"}}, \\\"eval-obs-only-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T12:43:42.283Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:16.008Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\\\", \\\"parent\\\": \\\"eval-obs-only-spatial\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"successes\\\": 0, \\\"total\\\": 100}}, \\\"eval-perdof-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T13:27:53.154Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:10.816Z\\\", \\\"hypothesis\\\": \\\"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\\\", \\\"parent\\\": \\\"eval-mag-perdof-norm003-object\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 11, \\\"successes\\\": 11, \\\"total\\\": 100}}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T10:44:50.876Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:05.531Z\\\", \\\"hypothesis\\\": \\\"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 34, \\\"successes\\\": 34, \\\"total\\\": 100}}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T13:50:21.016Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:01.680Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 36, \\\"successes\\\": 36, \\\"total\\\": 100, \\\"fast_path\\\": 81.5, \\\"avg_k\\\": 3.5, \\\"mean_l2\\\": 0.0885}}, \\\"eval-supp-goal-vla-only-wrapper-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:34:16.215Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:55.797Z\\\", \\\"hypothesis\\\": \\\"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 82, \\\"successes\\\": 164, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:12:57.615Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:47.449Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 59, \\\"successes\\\": 118, \\\"total\\\": 200}}, \\\"eval-supp-spatial-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:41:52.628Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:39.499Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80, \\\"successes\\\": 160, \\\"total\\\": 200}}, \\\"eval-supp-obj-crm-norm005-s46\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-24T03:25:56.315Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:33.701Z\\\", \\\"hypothesis\\\": \\\"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.795, \\\"successes\\\": 159, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T12:22:12.815Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:27.340Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"successes\\\": 0, \\\"total\\\": 200}}, \\\"eval-supp-reconvla-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T22:37:18.110Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:15.872Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"successes\\\": 156, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1\\\"}}, \\\"eval-pi05-vla-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:14.823Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:46.138Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\\\"}, \\\"eval-pi05-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:17.435Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:36.173Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\\\"}, \\\"eval-pi05-vla-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T08:22:19.985Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:23.533Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"total_rollouts\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\\\"}, \\\"eval-supp-long-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:20:29.949Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:43.469Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed45. Fourth seed extending Long K2mean coverage. VLA-only s45 on bjb1-32546 provides baseline.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.56, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}}, \\\"eval-supp-goal-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:06:24.679Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:33.666Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Goal suite seed46. Extends Goal K2mean to 4th completed seed for variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.825, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}}, \\\"eval-supp-goal-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:02:43.468Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:30.058Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal suite seed46. Fifth seed extending Goal Adaptive. s42-s45 mean ~84%. Completes 5-seed coverage.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.835, \\\"trigger_rate\\\": 0.0909, \\\"tau\\\": 0.25, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}}, \\\"eval-supp-goal-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:06:31.022Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:26.680Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Goal suite seed46. Fifth seed extending Goal CRM. s42-s45 mean ~83%. Completes 5-seed coverage.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"source\\\": \\\"json_harvest_bjb2-28827\\\"}}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:42:31.834Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:19:19.270Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\\\", \\\"parent\\\": \\\"eval-supp-spatial-adapt-tau025-s45\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"trigger_rate\\\": 20, \\\"mean_unc\\\": 0.1863}}, \\\"eval-supp-spatial-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T22:59:42.673Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:33.793Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed45. Fourth seed extending Spatial K2mean. Fills Table 1 gap.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80, \\\"successes\\\": 160, \\\"total\\\": 200}}, \\\"eval-supp-spatial-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T00:34:46.225Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:27.488Z\\\", \\\"hypothesis\\\": \\\"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80.5, \\\"successes\\\": 161, \\\"total\\\": 200}}, \\\"eval-supp-spatial-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T00:52:50.566Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:20.676Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80, \\\"successes\\\": 160, \\\"total\\\": 200}}, \\\"eval-supp-spatial-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:45:59.585Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:17.471Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 80, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"trigger_rate\\\": 19.9, \\\"mean_unc\\\": 0.1846}}, \\\"eval-supp-spatial-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T00:22:31.743Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:14.133Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 81, \\\"successes\\\": 162, \\\"total\\\": 200}}, \\\"eval-supp-long-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:12:50.126Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:54:53.307Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.605, \\\"successes\\\": 121, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:12:41.239Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:53:11.757Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed45. Fourth seed for Long Adaptive validation.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.6, \\\"successes\\\": 120, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:12:32.639Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:53:04.280Z\\\", \\\"hypothesis\\\": \\\"Long VLA-only baseline seed45. Fourth seed for Long baseline. s42=58.0%, s43=59.5%, s44=56.5%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.575, \\\"successes\\\": 115, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T21:31:16.039Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:30:53.206Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Spatial suite seed45. Fourth seed extending Spatial Reconvla. 3-seed: 79.8%±1.0%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 79.5, \\\"successes\\\": 159, \\\"total\\\": 200}, \\\"notes\\\": \\\"Cron false positive — eval script completed normally with 79.5% (159/200). Results at logs/eval_spatial_reconvla_seed45.json on cqa1-32758. No W&B/sentinel used by eval scripts.\\\"}, \\\"eval-supp-goal-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T21:31:04.113Z\\\", \\\"updated_at\\\": \\\"2026-05-24T00:21:09.215Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Goal suite seed45. Matched-seed companion for Goal s45 4-seed extension.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.81, \\\"per_task\\\": {\\\"open_the_middle_drawer_of_the_cabinet\\\": 0.7, \\\"put_the_bowl_on_the_stove\\\": 0.95, \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.85, \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.6, \\\"put_the_bowl_on_top_of_the_cabinet\\\": 0.95, \\\"push_the_plate_to_the_front_of_the_stove\\\": 0.95, \\\"put_the_cream_cheese_in_the_bowl\\\": 0.55, \\\"turn_on_the_stove\\\": 0.95, \\\"put_the_bowl_on_the_plate\\\": 0.9, \\\"put_the_wine_bottle_on_the_rack\\\": 0.7}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-adapt-tau025-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:26:59.880Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:45:46.677Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object suite seed45. Extends Object Adaptive coverage. Trigger rate expected ~3-5% on Object tasks.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.78}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T22:37:29.185Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:45:41.402Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Object suite seed45. Duplicate of eval-supp-k2mean-obj-s45 (already DONE SR=77.5%). Killed to free GPU.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-crm-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T23:41:43.001Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:43:24.974Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Object suite seed46. Fifth seed extending Object CRM. Previous seeds show ~79-81% range.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.795, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0.8, \\\"cream_cheese\\\": 0.7, \\\"salad_dressing\\\": 0.75, \\\"bbq_sauce\\\": 0.8, \\\"ketchup\\\": 0.7, \\\"tomato_sauce\\\": 0.75, \\\"butter\\\": 0.75, \\\"milk\\\": 0.85, \\\"chocolate_pudding\\\": 0.95, \\\"orange_juice\\\": 0.9}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"created_at\\\": \\\"2026-05-23T22:23:46.061Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:42:01.475Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-k2mean-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:26:25.473Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:04:07.248Z\\\", \\\"hypothesis\\\": \\\"Long K=2 mean baseline seed44. Third seed for Long K=2 mean validation. Isolates multi-sample averaging on long-horizon tasks.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"SR\\\": 0.545, \\\"successes\\\": 109, \\\"total\\\": 200}}, \\\"eval-supp-long-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:26:31.761Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:04:01.262Z\\\", \\\"hypothesis\\\": \\\"Long Reconvla K=10 seed44. Third seed for Long Reconvla 3-seed validation. s42=56.5% (below VLA-only 58.0%).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.57, \\\"successes\\\": 114, \\\"total\\\": 200}}, \\\"eval-supp-k2mean-spatial-s45\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-23T23:02:16.008Z\\\", \\\"updated_at\\\": \\\"2026-05-23T23:02:16.008Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline (vla_only, 2-sample average) on Spatial suite seed45. Fourth seed completing Spatial k2mean coverage (s42=negative, s43/s44=done). Isolates multi-sample averaging effect.\\\"}, \\\"eval-supp-goal-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:28:38.416Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:24.122Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Goal suite seed45. Fourth seed extending Goal Reconvla. 3-seed mean: 80.8%±0.3%.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.855}, \\\"notes\\\": \\\"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果文件: logs/eval_goal_reconvla_seed45.json\\\"}, \\\"eval-supp-goal-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:28:29.087Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:20.913Z\\\", \\\"hypothesis\\\": \\\"Goal VLA-only baseline seed45. Fourth seed extending Goal baseline. Matched-seed companion for Goal Adaptive s45.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.835}, \\\"notes\\\": \\\"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果文件: logs/eval_goal_vla_only_seed45.json\\\"}, \\\"eval-supp-crm-norm005-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:12:20.093Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:13.555Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Object suite seed46. Fills the last Object s46 method gap.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.795}, \\\"notes\\\": \\\"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判为 failed。日志确认 79.5% (159/200)。结果文件: logs/eval_object_crm_obs_only_norm0.05_seed46.json\\\"}, \\\"eval-supp-goal-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:28:32.501Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:56:01.038Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Goal suite seed45. Fourth seed extending Goal CRM. 3-seed mean: 83.7%±1.8%.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 81, \\\"successes\\\": 162, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果文件: logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\\"}, \\\"eval-supp-crm-norm005-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T18:15:28.966Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:37:07.655Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Object suite seed45. Extends Object method coverage for 5-seed Adaptive variance investigation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.765}}, \\\"eval-supp-reconvla-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T18:41:19.029Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:31:59.949Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object suite seed46. Extends Object method coverage for 5-seed variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200}}, \\\"eval-supp-goal-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T20:13:06.213Z\\\", \\\"updated_at\\\": \\\"2026-05-23T22:31:49.469Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Goal suite seed45. Extends Goal Adaptive from 3-seed to 4-seed.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.81, \\\"successes\\\": 162, \\\"total\\\": 200, \\\"trigger_rate\\\": 0.094, \\\"mean_unc\\\": 0.1493}}, \\\"eval-supp-long-crm-norm005-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:44:35.159Z\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:56.768Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 always-on on Long suite seed44. Third seed for Long CRM 3-seed validation.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-adapt-tau025-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:44:32.204Z\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:50.765Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed44. Third seed for Long Adaptive 3-seed validation. Long VLA-only s42=58.0%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.56, \\\"trigger_rate\\\": 0.049}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-k2mean-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:56:58.207Z\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:27.870Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Object suite seed46. Companion baseline for Object Adaptive s46 5-seed extension.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.765}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:56:52.406Z\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:21.695Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Object suite seed45. Companion baseline for Object Adaptive s45 5-seed extension.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.775}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:27:06.320Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:26:37.804Z\\\", \\\"hypothesis\\\": \\\"Object Adaptive τ=0.25 seed46. User-requested additional seed to assess Object Adaptive variance.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.775}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:55:45.292Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:21:04.060Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Long suite seed43. Duplicate deployment on bjb2-28827; primary results already harvested from cqa1 (SR=59.5%).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-k2mean-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:22:32.322Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:13:10.758Z\\\", \\\"metrics\\\": {\\\"SR\\\": 0.57}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. VLA-only s42=58.0% baseline.\\\"}, \\\"eval-supp-obj-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:24:10.813Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:46.499Z\\\", \\\"hypothesis\\\": \\\"Object VLA-only baseline seed46. Companion baseline for Object Adaptive s46 comparison. 3-seed baseline: 77.8%±1.0%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.79}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:41.287Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:40.603Z\\\", \\\"hypothesis\\\": \\\"Long VLA-only baseline seed44. Second seed for Long baseline. s42=58.0%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-k2mean-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:36.825Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:34.819Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed43. Isolates multi-sample averaging effect on Long tasks.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.56}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:30.979Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:28.982Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Long suite seed43. Second seed for Long Reconvla validation.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.59}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-crm-norm005-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:26.229Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:23.098Z\\\", \\\"hypothesis\\\": \\\"CRM norm=0.05 always-on on Long suite seed43. Second seed for Long CRM validation.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.545}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-adapt-tau025-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:21.251Z\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:17.172Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed43. Second seed for Long Adaptive validation. Long VLA-only s42=58.0%.\\\", \\\"metrics\\\": {\\\"SR\\\": 0.58, \\\"trigger_rate\\\": 0.045}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-adapt-tau025-s45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T17:55:59.154Z\\\", \\\"updated_at\\\": \\\"2026-05-23T18:16:04.202Z\\\", \\\"hypothesis\\\": \\\"Retry of eval-supp-obj-adapt-tau025-s45. Object Adaptive CRM τ=0.25 seed45 on bjb2-40593 after fixing missing CRM checkpoint.\\\", \\\"parent\\\": \\\"eval-supp-obj-adapt-tau025-s45\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-supp-long-crm-norm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T09:56:44.431Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:47.737Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.565}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-long-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T09:56:38.730Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:41.523Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.59, \\\"trigger_rate\\\": 0.039, \\\"tau\\\": 0.25, \\\"crm_applied_steps\\\": 2785, \\\"total_steps\\\": 71980}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T09:56:33.117Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:32.561Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.565}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-ablation-tau040-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T13:06:39.811Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:24.644Z\\\", \\\"hypothesis\\\": \\\"τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold → lower trigger rate → fewer corrections. Part of 5-point τ-sensitivity curve. Tests whether very conservative gating still maintains benefit.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.835, \\\"trigger_rate\\\": 0.012, \\\"tau\\\": 0.4, \\\"crm_applied_steps\\\": 346, \\\"total_steps\\\": 28165}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-ablation-tau015-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T13:06:36.431Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:15.441Z\\\", \\\"hypothesis\\\": \\\"τ-sweep ablation: τ=0.15 on Goal s42. Mid-low threshold. Part of 5-point τ-sensitivity curve. Tests transition zone between aggressive and conservative gating.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.85, \\\"trigger_rate\\\": 0.339, \\\"tau\\\": 0.15, \\\"crm_applied_steps\\\": 9590, \\\"total_steps\\\": 28273}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-k2mean-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:27:45.450Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:06.995Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Object seed44. Third seed for 3-seed mean±std. s42=79.5%, s43 running. Isolates multi-sample averaging on Object tasks.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.75, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0.7, \\\"cream_cheese\\\": 0.7, \\\"salad_dressing\\\": 0.8, \\\"bbq_sauce\\\": 0.8, \\\"ketchup\\\": 0.85, \\\"tomato_sauce\\\": 0.7, \\\"butter\\\": 0.55, \\\"milk\\\": 0.7, \\\"chocolate_pudding\\\": 0.75, \\\"orange_juice\\\": 0.95}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-ablation-tau010-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T13:06:32.832Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:24:59.810Z\\\", \\\"hypothesis\\\": \\\"τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold → higher CRM trigger rate → more corrections. Part of 5-point τ-sensitivity curve (0.10, 0.15, 0.25, 0.40, always-on). Tests whether aggressive gating improves or hurts Goal performance.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.81, \\\"trigger_rate\\\": 0.739, \\\"tau\\\": 0.1, \\\"crm_applied_steps\\\": 22170, \\\"total_steps\\\": 29984}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-supp-obj-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:31:41.302Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:24:48.531Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 argmin on Object seed44. s42=79.0%, s43 running on bjb2-28827. Third seed for Object Reconvla validation.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.76, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0.65, \\\"cream_cheese\\\": 0.7, \\\"salad_dressing\\\": 0.7, \\\"bbq_sauce\\\": 0.95, \\\"ketchup\\\": 0.9, \\\"tomato_sauce\\\": 0.7, \\\"butter\\\": 0.75, \\\"milk\\\": 0.6, \\\"chocolate_pudding\\\": 0.7, \\\"orange_juice\\\": 0.95}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:51:10.407Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:22:10.552Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial seed44. s42=78.5%. Second/third seed for 3-seed Spatial VLA-only baseline mean±std.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.785, \\\"successes\\\": 157, \\\"total\\\": 200, \\\"per_task\\\": {\\\"between_plate_ramekin\\\": 0.9, \\\"next_to_ramekin\\\": 0.95, \\\"table_center\\\": 0.95, \\\"on_cookie_box\\\": 1, \\\"top_drawer\\\": 0.75, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 1, \\\"on_stove\\\": 0.8, \\\"next_to_plate\\\": 0.8, \\\"on_wooden_cabinet\\\": 0.7}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T14:36:18.236Z\\\", \\\"updated_at\\\": \\\"2026-05-23T17:21:50.650Z\\\", \\\"hypothesis\\\": \\\"Goal VLA-only wrapper s44 re-run. Previous result lost due to JSON filename collision with k2mean-s44. Confirms 83.5% baseline across seeds (s42=83.5%, s43=82.5%).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.85, \\\"successes\\\": 170, \\\"total\\\": 200, \\\"per_task\\\": {\\\"open_middle_drawer\\\": 0.85, \\\"put_bowl_stove\\\": 0.95, \\\"wine_bottle_cabinet\\\": 0.85, \\\"open_top_drawer_bowl\\\": 0.7, \\\"bowl_on_cabinet\\\": 0.9, \\\"push_plate_stove\\\": 0.9, \\\"cream_cheese_bowl\\\": 0.65, \\\"turn_on_stove\\\": 1, \\\"bowl_on_plate\\\": 0.95, \\\"wine_bottle_rack\\\": 0.75}}}, \\\"eval-supp-k2mean-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T11:23:34.262Z\\\", \\\"updated_at\\\": \\\"2026-05-23T14:41:49.032Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial seed44. Third seed for 3-seed mean±std. s42=81.5%, s43 running. Isolates multi-sample averaging effect from CRM correction on Spatial.\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"successes\\\": 162, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 100, \\\"total\\\": 881, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9561}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:07:37.003Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:16.953Z\", \"updated_at\": \"2026-05-24T07:06:31.785Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:13.683Z\", \"updated_at\": \"2026-05-24T07:06:23.946Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:10.482Z\", \"updated_at\": \"2026-05-24T07:06:15.932Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:34:07.178Z\", \"updated_at\": \"2026-05-24T07:06:09.666Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\", \"conclusion\": \"killed\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T03:56:52.910Z\", \"updated_at\": \"2026-05-24T06:55:16.446Z\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:22:29.274Z\", \"updated_at\": \"2026-05-24T06:49:49.091Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:19.029Z\", \"updated_at\": \"2026-05-24T06:49:36.626Z\", \"hypothesis\": \"VLA-only baseline on Object suite seed45. Fills s45 gap in Object VLA-only 5-seed coverage (have s42-s44, s46) for supplementary table.\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:12.741Z\", \"updated_at\": \"2026-05-24T06:45:22.337Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Spatial suite seed45. Sixth seed extending Spatial CRM always-on variance coverage for supplementary table.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}, \"notes\": \"Eval completed normally. 78.0% (156/200). Results at logs/eval_spatial_crm_obs_only_norm0.05_seed45.json on cqa1-32758. Cron escalated as process-gone but script had already exited after completion.\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:09.089Z\", \"updated_at\": \"2026-05-24T06:45:16.646Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Sixth seed extending Spatial VLA-only variance coverage for supplementary table.\", \"conclusion\": \"success\", \"notes\": \"Eval completed normally on cqa1-32758. SR=77.0% (154/200). Results at logs/eval_spatial_vla_only_seed45.json. Per-task: between_plate_ramekin 90%, next_to_ramekin 90%, table_center 90%, on_cookie_box 100%, top_drawer 75%, on_ramekin 0%, next_to_cookie_box 95%, on_stove 75%, next_to_plate 80%, on_wooden_cabinet 75%.\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:32:56.953Z\", \"updated_at\": \"2026-05-24T06:33:34.726Z\", \"hypothesis\": \"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T06:33:29.735Z\", \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T06:33:25.524Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T06:33:17.189Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"conclusion\": \"failed\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:55:46.960Z\", \"updated_at\": \"2026-05-24T06:33:11.821Z\", \"hypothesis\": \"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\", \"conclusion\": \"failed\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T06:18:27.873Z\", \"updated_at\": \"2026-05-24T06:23:35.000Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Goal enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"conclusion\": \"success\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T06:15:12.631Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T05:52:22.340Z\", \"updated_at\": \"2026-05-24T06:13:04.507Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Spatial enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:35:21.518Z\", \"updated_at\": \"2026-05-24T05:44:03.369Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:24.393Z\", \"updated_at\": \"2026-05-24T05:43:32.643Z\", \"hypothesis\": \"Goal VLA-only baseline seed46. Fifth seed extending Goal VLA-only. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:35.384Z\", \"updated_at\": \"2026-05-24T05:43:26.502Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal suite seed46. Fifth seed extending Goal Reconvla. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T18:48:38.574Z\", \"updated_at\": \"2026-05-24T03:28:46.242Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-24T03:27:16.008Z\", \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-24T03:27:10.816Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"conclusion\": \"success\", \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:44:50.876Z\", \"updated_at\": \"2026-05-24T03:27:05.531Z\", \"hypothesis\": \"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-24T03:27:01.680Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-24T03:26:55.797Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:26:47.449Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:26:39.499Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T12:22:12.815Z\", \"updated_at\": \"2026-05-24T03:26:27.340Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-24T03:25:46.138Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-24T03:25:36.173Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-24T03:25:23.533Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:20:29.949Z\", \"updated_at\": \"2026-05-24T03:24:43.469Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed45. Fourth seed extending Long K2mean coverage. VLA-only s45 on bjb1-32546 provides baseline.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:24.679Z\", \"updated_at\": \"2026-05-24T03:24:33.666Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed46. Extends Goal K2mean to 4th completed seed for variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:02:43.468Z\", \"updated_at\": \"2026-05-24T03:24:30.058Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed46. Fifth seed extending Goal Adaptive. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:06:31.022Z\", \"updated_at\": \"2026-05-24T03:24:26.680Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed46. Fifth seed extending Goal CRM. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:42:31.834Z\", \"updated_at\": \"2026-05-24T03:19:19.270Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"parent\": \"eval-supp-spatial-adapt-tau025-s45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:59:42.673Z\", \"updated_at\": \"2026-05-24T03:18:33.793Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed45. Fourth seed extending Spatial K2mean. Fills Table 1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:34:46.225Z\", \"updated_at\": \"2026-05-24T03:18:27.488Z\", \"hypothesis\": \"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:52:50.566Z\", \"updated_at\": \"2026-05-24T03:18:20.676Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:45:59.585Z\", \"updated_at\": \"2026-05-24T03:18:17.471Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T00:22:31.743Z\", \"updated_at\": \"2026-05-24T03:18:14.133Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:50.126Z\", \"updated_at\": \"2026-05-24T00:54:53.307Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:41.239Z\", \"updated_at\": \"2026-05-24T00:53:11.757Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed45. Fourth seed for Long Adaptive validation.\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:32.639Z\", \"updated_at\": \"2026-05-24T00:53:04.280Z\", \"hypothesis\": \"Long VLA-only baseline seed45. Fourth seed for Long baseline. s42=58.0%, s43=59.5%, s44=56.5%.\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:16.039Z\", \"updated_at\": \"2026-05-24T00:30:53.206Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed45. Fourth seed extending Spatial Reconvla. 3-seed: 79.8%±1.0%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}, \"notes\": \"Cron false positive — eval script completed normally with 79.5% (159/200). Results at logs/eval_spatial_reconvla_seed45.json on cqa1-32758. No W&B/sentinel used by eval scripts.\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T21:31:04.113Z\", \"updated_at\": \"2026-05-24T00:21:09.215Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed45. Matched-seed companion for Goal s45 4-seed extension.\", \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:59.880Z\", \"updated_at\": \"2026-05-23T23:45:46.677Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Extends Object Adaptive coverage. Trigger rate expected ~3-5% on Object tasks.\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T22:37:29.185Z\", \"updated_at\": \"2026-05-23T23:45:41.402Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Duplicate of eval-supp-k2mean-obj-s45 (already DONE SR=77.5%). Killed to free GPU.\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T23:41:43.001Z\", \"updated_at\": \"2026-05-23T23:43:24.974Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fifth seed extending Object CRM. Previous seeds show ~79-81% range.\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-23T22:23:46.061Z\", \"updated_at\": \"2026-05-23T23:42:01.475Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:25.473Z\", \"updated_at\": \"2026-05-23T23:04:07.248Z\", \"hypothesis\": \"Long K=2 mean baseline seed44. Third seed for Long K=2 mean validation. Isolates multi-sample averaging on long-horizon tasks.\", \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:26:31.761Z\", \"updated_at\": \"2026-05-23T23:04:01.262Z\", \"hypothesis\": \"Long Reconvla K=10 seed44. Third seed for Long Reconvla 3-seed validation. s42=56.5% (below VLA-only 58.0%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-23T23:02:16.008Z\", \"updated_at\": \"2026-05-23T23:02:16.008Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Spatial suite seed45. Fourth seed completing Spatial k2mean coverage (s42=negative, s43/s44=done). Isolates multi-sample averaging effect.\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:38.416Z\", \"updated_at\": \"2026-05-23T22:57:24.122Z\", \"hypothesis\": \"Reconvla K=10 on Goal suite seed45. Fourth seed extending Goal Reconvla. 3-seed mean: 80.8%±0.3%.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果文件: logs/eval_goal_reconvla_seed45.json\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:29.087Z\", \"updated_at\": \"2026-05-23T22:57:20.913Z\", \"hypothesis\": \"Goal VLA-only baseline seed45. Fourth seed extending Goal baseline. Matched-seed companion for Goal Adaptive s45.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果文件: logs/eval_goal_vla_only_seed45.json\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:12:20.093Z\", \"updated_at\": \"2026-05-23T22:57:13.555Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fills the last Object s46 method gap.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判为 failed。日志确认 79.5% (159/200)。结果文件: logs/eval_object_crm_obs_only_norm0.05_seed46.json\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:28:32.501Z\", \"updated_at\": \"2026-05-23T22:56:01.038Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed45. Fourth seed extending Goal CRM. 3-seed mean: 83.7%±1.8%.\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\", \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果文件: logs/eval_goal_crm_obs_only_norm0.05_seed45.json\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:15:28.966Z\", \"updated_at\": \"2026-05-23T22:37:07.655Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed45. Extends Object method coverage for 5-seed Adaptive variance investigation.\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:41:19.029Z\", \"updated_at\": \"2026-05-23T22:31:59.949Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed46. Extends Object method coverage for 5-seed variance analysis.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T20:13:06.213Z\", \"updated_at\": \"2026-05-23T22:31:49.469Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed45. Extends Goal Adaptive from 3-seed to 4-seed.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:35.159Z\", \"updated_at\": \"2026-05-23T21:28:56.768Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed44. Third seed for Long CRM 3-seed validation.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:44:32.204Z\", \"updated_at\": \"2026-05-23T21:28:50.765Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed44. Third seed for Long Adaptive 3-seed validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:58.207Z\", \"updated_at\": \"2026-05-23T21:28:27.870Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed46. Companion baseline for Object Adaptive s46 5-seed extension.\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:56:52.406Z\", \"updated_at\": \"2026-05-23T21:28:21.695Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Companion baseline for Object Adaptive s45 5-seed extension.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:27:06.320Z\", \"updated_at\": \"2026-05-23T20:26:37.804Z\", \"hypothesis\": \"Object Adaptive τ=0.25 seed46. User-requested additional seed to assess Object Adaptive variance.\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:55:45.292Z\", \"updated_at\": \"2026-05-23T20:21:04.060Z\", \"hypothesis\": \"VLA-only baseline on Long suite seed43. Duplicate deployment on bjb2-28827; primary results already harvested from cqa1 (SR=59.5%).\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:22:32.322Z\", \"updated_at\": \"2026-05-23T20:13:10.758Z\", \"metrics\": {\"SR\": 0.57}, \"conclusion\": \"negative\", \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. VLA-only s42=58.0% baseline.\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:24:10.813Z\", \"updated_at\": \"2026-05-23T20:09:46.499Z\", \"hypothesis\": \"Object VLA-only baseline seed46. Companion baseline for Object Adaptive s46 comparison. 3-seed baseline: 77.8%±1.0%.\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-23T20:09:40.603Z\", \"hypothesis\": \"Long VLA-only baseline seed44. Second seed for Long baseline. s42=58.0%.\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:36.825Z\", \"updated_at\": \"2026-05-23T20:09:34.819Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed43. Isolates multi-sample averaging effect on Long tasks.\", \"metrics\": {\"SR\": 0.56}, \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:30.979Z\", \"updated_at\": \"2026-05-23T20:09:28.982Z\", \"hypothesis\": \"Reconvla K=10 argmin on Long suite seed43. Second seed for Long Reconvla validation.\", \"metrics\": {\"SR\": 0.59}, \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:26.229Z\", \"updated_at\": \"2026-05-23T20:09:23.098Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed43. Second seed for Long CRM validation.\", \"metrics\": {\"SR\": 0.545}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:21.251Z\", \"updated_at\": \"2026-05-23T20:09:17.172Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed43. Second seed for Long Adaptive validation. Long VLA-only s42=58.0%.\", \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}, \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T17:55:59.154Z\", \"updated_at\": \"2026-05-23T18:16:04.202Z\", \"hypothesis\": \"Retry of eval-supp-obj-adapt-tau025-s45. Object Adaptive CRM τ=0.25 seed45 on bjb2-40593 after fixing missing CRM checkpoint.\", \"parent\": \"eval-supp-obj-adapt-tau025-s45\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:44.431Z\", \"updated_at\": \"2026-05-23T17:25:47.737Z\", \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:38.730Z\", \"updated_at\": \"2026-05-23T17:25:41.523Z\", \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:56:33.117Z\", \"updated_at\": \"2026-05-23T17:25:32.561Z\", \"hypothesis\": \"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:39.811Z\", \"updated_at\": \"2026-05-23T17:25:24.644Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold → lower trigger rate → fewer corrections. Part of 5-point τ-sensitivity curve. Tests whether very conservative gating still maintains benefit.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.012, \"tau\": 0.4, \"crm_applied_steps\": 346, \"total_steps\": 28165}, \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:36.431Z\", \"updated_at\": \"2026-05-23T17:25:15.441Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.15 on Goal s42. Mid-low threshold. Part of 5-point τ-sensitivity curve. Tests transition zone between aggressive and conservative gating.\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:27:45.450Z\", \"updated_at\": \"2026-05-23T17:25:06.995Z\", \"hypothesis\": \"K=2 mean baseline on Object seed44. Third seed for 3-seed mean±std. s42=79.5%, s43 running. Isolates multi-sample averaging on Object tasks.\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:06:32.832Z\", \"updated_at\": \"2026-05-23T17:24:59.810Z\", \"hypothesis\": \"τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold → higher CRM trigger rate → more corrections. Part of 5-point τ-sensitivity curve (0.10, 0.15, 0.25, 0.40, always-on). Tests whether aggressive gating improves or hurts Goal performance.\", \"metrics\": {\"overall_sr\": 0.81, \"trigger_rate\": 0.739, \"tau\": 0.1, \"crm_applied_steps\": 22170, \"total_steps\": 29984}, \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:31:41.302Z\", \"updated_at\": \"2026-05-23T17:24:48.531Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed44. s42=79.0%, s43 running on bjb2-28827. Third seed for Object Reconvla validation.\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:51:10.407Z\", \"updated_at\": \"2026-05-23T17:22:10.552Z\", \"hypothesis\": \"VLA-only baseline on Spatial seed44. s42=78.5%. Second/third seed for 3-seed Spatial VLA-only baseline mean±std.\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T14:36:18.236Z\", \"updated_at\": \"2026-05-23T17:21:50.650Z\", \"hypothesis\": \"Goal VLA-only wrapper s44 re-run. Previous result lost due to JSON filename collision with k2mean-s44. Confirms 83.5% baseline across seeds (s42=83.5%, s43=82.5%).\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T11:23:34.262Z\", \"updated_at\": \"2026-05-23T14:41:49.032Z\", \"hypothesis\": \"K=2 mean baseline on Spatial seed44. Third seed for 3-seed mean±std. s42=81.5%, s43 running. Isolates multi-sample averaging effect from CRM correction on Spatial.\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}}, \"count\": 100, \"total\": 881, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9561}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "7519cf85-8aef-47b9-9f89-2bd095779ba2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RgWStDLejzfyLLHaA3mGMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23822,
      "cache_read_input_tokens": 34752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23822
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

Spatial s45/s46 已全部 DONE，Goal s45/s46 也已全部 DONE。看 registry 还发现：4 个 Spatial RUNNING 条目 (timestamps 06:48) 像是已部署但状态不明的。先查服务器实际状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "32c73ca8-8f4e-4381-a45f-5f1092ef91e3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RgWStDLejzfyLLHaA3mGMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23822,
      "cache_read_input_tokens": 34752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23822
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BB3kmGGZbNTdDSDx96HVwN`</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "2994b5e1-144a-4bbe-b856-0a2adbf97ceb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RgWStDLejzfyLLHaA3mGMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23822,
      "cache_read_input_tokens": 34752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23822
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Rd8ceJPhdzCNdvDLmiEUcK`</summary>

```json
{
  "server": "cqa1-32758",
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "80f32071-147d-4890-9b1b-2ec800645083",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RgWStDLejzfyLLHaA3mGMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23822,
      "cache_read_input_tokens": 34752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23822
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 21 · 2026-05-24T07:08:11.286Z_

<details><summary>↩ Tool result · `toolu_01BB3kmGGZbNTdDSDx96HVwN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n3, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n4, NVIDIA GeForce RTX 4090 D, 6548 MiB, 30 %\\n5, NVIDIA GeForce RTX 4090 D, 6548 MiB, 38 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "ef82e06a-487d-4ba3-afed-f667e418ff35",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\\\n1, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\\\n2, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\\\n3, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\\\n4, NVIDIA GeForce RTX 4090 D, 6548 MiB, 30 %\\\\n5, NVIDIA GeForce RTX 4090 D, 6548 MiB, 38 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.08}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n3, NVIDIA GeForce RTX 4090 D, 1 MiB, 0 %\\n4, NVIDIA GeForce RTX 4090 D, 6548 MiB, 30 %\\n5, NVIDIA GeForce RTX 4090 D, 6548 MiB, 38 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T07:08:11.306Z_

<details><summary>↩ Tool result · `toolu_01Rd8ceJPhdzCNdvDLmiEUcK`</summary>

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "b0d5fb91-7555-49b7-9001-cf1fcc8eef38",
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JhFioYPWgMoBq3WggnboD7`</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "tmux ls 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "1a57463c-7558-4d02-bbab-7c97a3569b09",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KnuSN1c6rJpYfdmK14drZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 58574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
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

_source line 24 · 2026-05-24T07:08:14.678Z_

<details><summary>↩ Tool result · `toolu_01JhFioYPWgMoBq3WggnboD7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"long-adapt-s47: 1 windows (created Sun May 24 14:35:42 2026)\\nlong-vla-s47: 1 windows (created Sun May 24 14:35:45 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "fb6a9fcb-b425-40f7-8365-508499c8df14",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"long-adapt-s47: 1 windows (created Sun May 24 14:35:42 2026)\\\\nlong-vla-s47: 1 windows (created Sun May 24 14:35:45 2026)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"long-adapt-s47: 1 windows (created Sun May 24 14:35:42 2026)\\nlong-vla-s47: 1 windows (created Sun May 24 14:35:45 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WPpoji3ngaUDz2eC42DvgX`</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "ls /root/autodl-tmp/checkpoints/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "b167d649-118e-4334-a731-5cc2ec643a55",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KnuSN1c6rJpYfdmK14drZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 58574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
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

_source line 26 · 2026-05-24T07:08:14.971Z_

<details><summary>↩ Tool result · `toolu_01WPpoji3ngaUDz2eC42DvgX`</summary>

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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "f0662e99-ecee-4ba6-a0d1-b7af9a46b1c7",
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "db215a81-72bf-4a42-9f6c-22e72e9fd655",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MUn3BvMTn6nuJnqe4FW8Nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 61430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GiMMULXtoafuWdaaBTod1A`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "983ba2f7-7ee0-429d-8660-ffd7f9a55475",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MUn3BvMTn6nuJnqe4FW8Nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 61430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

_source line 29 · 2026-05-24T07:08:23.838Z_

<details><summary>↩ Tool result · `toolu_01GiMMULXtoafuWdaaBTod1A`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "4489e7dc-708c-47be-ac81-410315b322d8",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Tq9QmDzGBHJZXWJvMWzhbF`</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "ls /root/autodl-tmp/checkpoints/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "63e648ae-2ac3-4638-8cef-300a3ad3d9b3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MUn3BvMTn6nuJnqe4FW8Nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 61430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
      },
      "output_tokens": 79,
      "service_tier": "standard",
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

_source line 31 · 2026-05-24T07:08:25.047Z_

<details><summary>↩ Tool result · `toolu_01Tq9QmDzGBHJZXWJvMWzhbF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"crm_smolvla_3suite_v1\\ncrm_unified_4suite_r4\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "a6bc1da4-d819-4afa-9a75-ed7a6298fcda",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"crm_smolvla_3suite_v1\\\\ncrm_unified_4suite_r4\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"crm_smolvla_3suite_v1\\ncrm_unified_4suite_r4\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
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
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "61c283d8-9e6e-4cdb-97f2-f625d23775ef",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EQ47ev6jsrZAFuoiHdXDRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4228,
      "cache_read_input_tokens": 62222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4228
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

_source line 33_

GPU 0-3 都空闲，只剩 long-adapt-s47 和 long-vla-s47 两个 tmux session 在 GPU 4/5。

但任务描述与 registry 现状不符——**Spatial s45/s46 已全部 DONE**（包括 vla-only/reconvla/k2mean/crm-norm005/adapt-tau025），Goal s45/s46 也全部 DONE。

Registry 中 4 个 06:48 时间戳的 RUNNING Spatial 条目（`eval-supp-vla-only-spatial-s45/s46`, `eval-supp-crm-norm005-spatial-s45`, `eval-supp-adapt-tau025-spatial-s45`）和已 DONE 的 `eval-supp-spatial-*-s45/s46` 是命名重复，GPU 也空闲——这些都是孤儿条目。

**Spatial 已有完整 5-seed 覆盖 (s42–s46)**。下一步合理选项可能是 Spatial s47（与正在跑的 Long s47 并列扩到 6-seed），目前只有 `eval-supp-spatial-crm-norm005-s47` RUNNING，缺 vla-only / k2mean / reconvla / adapt-tau025 共 4 个——恰好 4 张 GPU。

请确认要部署的实验集，我倾向以下方案：

**Spatial s47 sixth-seed 扩展**（4 张 GPU 各跑一个）：
- GPU 0: spatial-vla-only-s47
- GPU 1: spatial-k2mean-s47
- GPU 2: spatial-reconvla-s47
- GPU 3: spatial-adapt-tau025-s47

要这样跑吗？还是有别的意图（例如部署其他 suite/seed）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "uuid": "e829e3bb-c156-4f86-8591-6afde6a8568b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EQ47ev6jsrZAFuoiHdXDRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4228,
      "cache_read_input_tokens": 62222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4228
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

_source line 34_

GPU 0-3 都空闲，只剩 long-adapt-s47 和 long-vla-s47 两个 tmux session 在 GPU 4/5。

但任务描述与 registry 现状不符——**Spatial s45/s46 已全部 DONE**（包括 vla-only/reconvla/k2mean/crm-norm005/adapt-tau025），Goal s45/s46 也全部 DONE。

Registry 中 4 个 06:48 时间戳的 RUNNING Spatial 条目（`eval-supp-vla-only-spatial-s45/s46`, `eval-supp-crm-norm005-spatial-s45`, `eval-supp-adapt-tau025-spatial-s45`）和已 DONE 的 `eval-supp-spatial-*-s45/s46` 是命名重复，GPU 也空闲——这些都是孤儿条目。

**Spatial 已有完整 5-seed 覆盖 (s42–s46)**。下一步合理选项可能是 Spatial s47（与正在跑的 Long s47 并列扩到 6-seed），目前只有 `eval-supp-spatial-crm-norm005-s47` RUNNING，缺 vla-only / k2mean / reconvla / adapt-tau025 共 4 个——恰好 4 张 GPU。

请确认要部署的实验集，我倾向以下方案：

**Spatial s47 sixth-seed 扩展**（4 张 GPU 各跑一个）：
- GPU 0: spatial-vla-only-s47
- GPU 1: spatial-k2mean-s47
- GPU 2: spatial-reconvla-s47
- GPU 3: spatial-adapt-tau025-s47

要这样跑吗？还是有别的意图（例如部署其他 suite/seed）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 104645,
  "duration_api_ms": 97573,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "fe0fd9c0-8ab6-4ccb-b273-c92da18d1209",
  "total_cost_usd": 0.74393675,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 65643,
    "cache_read_input_tokens": 315270,
    "output_tokens": 6963,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65643,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 6,
        "output_tokens": 2877,
        "cache_read_input_tokens": 62222,
        "cache_creation_input_tokens": 4228,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4228
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1743,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001848,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 22,
      "outputTokens": 6963,
      "cacheReadInputTokens": 315270,
      "cacheCreationInputTokens": 65643,
      "webSearchRequests": 0,
      "costUSD": 0.7420887500000001,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a42064a8-5ca4-4e4f-ae83-56a48b435717"
}
```

</details>

---

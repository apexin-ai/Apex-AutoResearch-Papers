# audit table1 goal object provenance r2 20260525T021436 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 116
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log`
- **Structured JSON:** [`0cc23d45f0fcca4049db.json`](../../sessions/0c/0cc23d45f0fcca4049db.json)

## Before a recorded user message

116 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
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
  "uuid": "fa9eed34-8fe0-4459-a163-23b00dc8bf2b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779682200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ad2103dd-d3c3-4df1-a926-9242a12a8a78",
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c"
}
```

---

### Assistant

_source line 3_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "3ea9a7f5-113e-4365-a6ab-782d0c02e6ca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011VUb1RPJG6QWKQz9zs3D2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15227,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15227
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

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UwHoEkACgupTHECMxrPQy7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e2f5ecf5-983f-4b63-9c06-e7de37561acc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011VUb1RPJG6QWKQz9zs3D2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15227,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15227
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

_source line 5 · 2026-05-25T02:14:52.217Z_

<details><summary>↩ Tool result · `toolu_01UwHoEkACgupTHECMxrPQy7`</summary>

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "efcc400d-6e3b-4793-8fe3-6d23d065ceae",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 6_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b274f549-9a28-48df-8add-18f65674b1b5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018eXxqPNkSqxiMDRVkJn7ts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16908,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16908
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28922
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019fJDXX2ioneWU2zfxFs2C5`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "conclusion": "success"
  },
  "fields": [
    "exp_id",
    "name",
    "server",
    "status",
    "conclusion",
    "metrics",
    "tags",
    "config"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "1d5802bf-9b9f-4abc-954e-4781282115ab",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018eXxqPNkSqxiMDRVkJn7ts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16908,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16908
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28922
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T02:15:04.037Z_

<details><summary>↩ Tool result · `toolu_019fJDXX2ioneWU2zfxFs2C5`</summary>

```text
Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "40864965-5dd6-4b5e-a437-78eb4acb10be",
  "tool_use_result": {
    "content": "Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.805, \"trigger_rate\": 0.262, \"mean_unc\": 0.1862}}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.8, \"success\": 160, \"total\": 200, \"mean_unc\": 0.1924, \"trigger_rate\": 0.169}}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"K\": 5, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"trigger_rate\": 0.195, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.198, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.197, \"tau\": 0.25, \"K\": 1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-crm-obj-s47-reeval\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.167, \"tau\": 0.3, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.266, \"tau\": 0.2, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.79, \"trigger_rate\": 0.752, \"tau\": 0.1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545, \"successes\": 109, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"note\": \"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\"}}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.78, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_rollouts\": 200, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.595, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"trigger_rate\": 0.0403, \"crm_applied_steps\": 1458}}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825}}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"note\": \"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\"}}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"total_successes\": 162, \"total_trials\": 200, \"per_task_range\": \"0.0-1.0\", \"worst_task\": \"pick_up_black_bowl_on_ramekin (0/20)\", \"best_tasks\": \"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"successes\": 163, \"total\": 200, \"trigger_rate\": 0.2046, \"mean_uncertainty\": 0.1873, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.765, \"total_successes\": 153, \"total_trials\": 200, \"per_task\": {\"alphabet_soup\": 0.75, \"cream_cheese\": 0.95, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.75, \"tomato_sauce\": 0.65, \"butter\": 0.5, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29241, \"crm_applied_steps\": 2594, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.565, \"successes\": 113, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755, \"successes\": 151, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mean_uncertainty\": 0.1885, \"trigger_rate\": 0.2013, \"tau\": 0.25, \"total_steps\": 28599, \"crm_applied_steps\": 5758}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.002887, \"best_epoch\": 50, \"final_train_loss\": 0.018836}}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.76}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.78}, \"conclusion\": \"success\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.795}}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.765}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.775}, \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.79}, \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.76, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.7, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.9, \"tomato_sauce\": 0.7, \"butter\": 0.75, \"milk\": 0.6, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.95}}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.785, \"successes\": 157, \"total\": 200, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.79, \"successes\": 158, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.58, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.25, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.4, \"STUDY_SCENE1_book_caddy\": 0.9, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.3, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0.55, \"KITCHEN_SCENE8_moka_pots_stove\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.75}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.77, \"total_rollouts\": 200, \"total_successes\": 154}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}, \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_episodes\": 200, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"per_task\": {\"between_plate_and_ramekin\": 1, \"table_center\": 1, \"next_to_ramekin\": 0.95, \"next_to_cookie_box\": 0.95, \"on_cookie_box\": 0.9, \"on_wooden_cabinet\": 0.85, \"on_stove\": 0.8, \"next_to_plate\": 0.8, \"top_drawer_wooden_cabinet\": 0.7, \"on_ramekin\": 0}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.8, 0.815, 0.795], \"mean\": 0.803, \"std\": 0.01}}}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.85}}}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005669, \"epochs\": 50, \"final_train_loss\": 0.009731, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/\"}}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.035, \"mean_unc\": 0.109, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 2}}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 78.5, \"total_rollouts\": 200, \"total_successes\": 157, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}}, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [80, 81, 78.5], \"mean\": 79.8, \"std\": 1.3}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80.5, \"total_successes\": 161, \"total_rollouts\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1881, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"mode\": \"adaptive_conformal_crm\", \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin\": {\"sr\": 90, \"successes\": 18, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_ramekin\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}, \"pick_up_the_black_bowl_from_table_center\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet\": {\"sr\": 65, \"successes\": 13, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_ramekin\": {\"sr\": 0, \"successes\": 0, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_cookie_box\": {\"sr\": 100, \"successes\": 20, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_stove\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_next_to_the_plate\": {\"sr\": 80, \"successes\": 16, \"rollouts\": 20}, \"pick_up_the_black_bowl_on_the_wooden_cabinet\": {\"sr\": 95, \"successes\": 19, \"rollouts\": 20}}}, \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 100, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 75, \"next_to_plate\": 80, \"on_wooden_cabinet\": 85}}}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 80, \"trigger_rate\": 19.4, \"mean_unc\": 0.1845, \"total_rollouts\": 200, \"total_successes\": 160, \"per_task\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 95, \"on_cookie_box\": 100, \"in_top_drawer_wooden_cabinet\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 80, \"next_to_plate\": 85, \"on_wooden_cabinet\": 80}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 81, \"total_rollouts\": 200, \"total_successes\": 162, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"next_to_ramekin\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"from_table_center\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_cookie_box\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"in_top_drawer_wooden_cabinet\": {\"sr\": 75, \"success\": 15, \"total\": 20}, \"on_ramekin\": {\"sr\": 0, \"success\": 0, \"total\": 20}, \"next_to_cookie_box\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"on_stove\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"next_to_plate\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"on_wooden_cabinet\": {\"sr\": 95, \"success\": 19, \"total\": 20}}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 95, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 75, \"orange_juice\": 90}}}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.77, \"n_success\": 154, \"n_total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"conformal_threshold\": 0.074855, \"K\": 10, \"seed\": 42, \"per_task_sr\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80, \"n_success\": 160, \"n_total\": 200, \"trigger_rate\": 12.17, \"mean_unc\": 0.1873, \"conformal_threshold\": 0.35, \"max_correction_norm\": 0.2, \"crm_applied_steps\": 3474, \"total_steps\": 28549, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 100, \"from_table_center\": 90, \"on_cookie_box\": 95, \"in_top_drawer\": 70, \"on_ramekin\": 0, \"next_to_cookie_box\": 95, \"on_stove\": 85, \"next_to_plate\": 85, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 80.5, \"n_success\": 161, \"n_total\": 200, \"trigger_rate\": 40.7, \"mean_unc\": 0.1852, \"conformal_threshold\": 0.15, \"max_correction_norm\": 0.2, \"per_task_sr\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 100, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 75, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 95, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 90, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 80, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 85}}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 79, \"n_success\": 158, \"n_total\": 200, \"per_task_sr\": {\"between_plate_and_ramekin\": 100, \"next_to_ramekin\": 90, \"from_table_center\": 95, \"on_cookie_box\": 95, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 100, \"on_stove\": 95, \"next_to_plate\": 75, \"on_wooden_cabinet\": 65}}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 82, \"n_success\": 164, \"n_total\": 200, \"trigger_rate\": 19.4, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_and_ramekin\": 95, \"next_to_ramekin\": 95, \"from_table_center\": 100, \"on_cookie_box\": 100, \"in_top_drawer\": 75, \"on_ramekin\": 0, \"next_to_cookie_box\": 90, \"on_stove\": 90, \"next_to_plate\": 90, \"on_wooden_cabinet\": 85}}, \"conclusion\": \"success\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 54.5, \"n_episodes\": 200}}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.005878, \"final_train_loss\": 0.00969, \"final_val_loss\": 0.00588, \"epochs_completed\": 50, \"total_params\": 327198, \"data_samples\": 77835, \"best_epoch\": 50}}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.6, \"n_episodes\": 200, \"n_tasks\": 10, \"per_task_sr\": [0.75, 0.65, 0.75, 0.75, 0.5, 0, 0.9, 0.7, 0.4, 0.6]}}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 53.5, \"n_episodes\": 200}}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 49.5, \"n_episodes\": 200}}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.94, \"successes\": 188, \"total\": 200, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.95, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 1, \"KITCHEN_SCENE3_stove_moka_pot\": 1, \"KITCHEN_SCENE4_black_bowl_drawer\": 1, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.9, \"STUDY_SCENE1_book_in_caddy\": 0.95, \"LIVING_ROOM_SCENE6_mug_pudding\": 1, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0.9, \"KITCHEN_SCENE8_both_moka_pots\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave\": 0.9}}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.955}}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}, \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 136090, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5, \"obs_features_shape\": [136090, 960], \"k_samples_shape\": [136090, 10, 5, 6], \"expert_actions_shape\": [136090, 5, 6], \"total_time_sec\": 8021, \"speed\": \"0.06s/sample\"}}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.000124, \"final_train_loss\": 0.000141, \"best_epoch\": 50, \"total_epochs\": 50, \"dof_weight_min\": 0.0107, \"dof_weight_max\": 3.7318, \"mse_baseline_val_loss\": 0.00208, \"conformal_guided_val_loss\": 0.013343, \"samples\": 14570, \"crm_params\": 337438}, \"conclusion\": \"success\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.00208, \"final_train_loss\": 0.004038, \"best_epoch\": 50, \"total_epochs\": 50, \"initial_val_loss\": 0.008373, \"exit_code\": 0}, \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.006138, \"best_epoch\": 50, \"total_epochs\": 50}}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.85, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.83, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.845, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.34, \"per_task_sr\": [0.9, 0.9, 0, 0.4, 0.1, 0, 0.8, 0, 0.3, 0], \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10}}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-40593\", \"metrics\": {\"overall_success_rate\": 0.1}, \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12}, \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.16}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"server\": \"bjb2-28827\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"server\": \"bjb1-32546\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"server\": \"bjb1-18228\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 534, \"total\": 534, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.033}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_012dXikzAFNtaPEwEW8jSit5`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# Filter for goal and object experiments\nfor exp in data:\n    name = exp.get('name', '').lower()\n    tags = ' '.join(exp.get('tags', [])).lower() if isinstance(exp.get('tags'), list) else ''\n    if 'goal' in name or 'object' in name or 'goal' in tags or 'object' in tags:\n        print(json.dumps({\n            'exp_id': exp.get('exp_id'),\n            'name': exp.get('name'),\n            'server': exp.get('server'),\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'tags': exp.get('tags'),\n            'config': exp.get('config')\n        }, ensure_ascii=False))\n\"\n",
  "description": "Parse registry and filter Goal/Object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "7252770a-78a5-4787-a010-c7833c56797a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Datdb9B29GADfCgRrJ2nhQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 33242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 10 · 2026-05-25T02:15:10.923Z_

<details><summary>↩ Tool result · reported error · `toolu_012dXikzAFNtaPEwEW8jSit5`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    name = exp.get('name', '').lower()
           ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "df2b6536-bcab-4024-8170-adf12bea6903",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    name = exp.get('name', '').lower()\n           ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_015eBgbuEdr3hPSvTY2NxZFD`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt | head -c 3000",
  "description": "Inspect registry result structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "88eb40d5-18f4-4d87-a4f0-b5ce964f246e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JdMvmFNwMn8whwGBibA2p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 34000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 621
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 12 · 2026-05-25T02:15:14.450Z_

<details><summary>↩ Tool result · `toolu_015eBgbuEdr3hPSvTY2NxZFD`</summary>

```text
{"success": true, "data": {"experiments": {"eval-k2-tau020-spatial-s42": {"status": "DONE", "conclusion": "success", "metrics": {"SR": 0.805, "trigger_rate": 0.262, "mean_unc": 0.1862}}, "eval-k2-tau030-spatial-s42": {"status": "DONE", "conclusion": "success", "metrics": {"SR": 0.8, "success": 160, "total": 200, "mean_unc": 0.1924, "trigger_rate": 0.169}}, "eval-pi05-vla-only-spatial-s45": {"status": "DONE", "metrics": {"overall_success_rate": 0.85, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "spatial", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-object-s44": {"status": "DONE", "metrics": {"overall_success_rate": 0.81, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-object-s43": {"status": "DONE", "metrics": {"overall_success_rate": 0.815, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-goal-s43": {"status": "DONE", "metrics": {"overall_success_rate": 0.97, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-goal-s42": {"status": "DONE", "metrics": {"overall_success_rate": 0.955, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-object-s42": {"status": "DONE", "metrics": {"overall_success_rate": 0.965, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-spatial-s43": {"status": "DONE", "metrics": {"overall_success_rate": 0.96, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "spatial", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-pi05-vla-only-spatial-s42": {"status": "DONE", "metrics": {"overall_success_rate": 0.98, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "spatial", "mode": "vla_only", "model": "pi0.5"}, "conclusion": "success"}, "eval-supp-crm-norm005-goal-s48": {"status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.8, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "crm_obs_only", "max_correction_norm": 0.05, "K": 10}}, "eval-supp-crm-norm005-spatial-s49": {"status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.785, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "spatial", "mode": "crm_obs_only", "max_correction_norm": 0.05, "K": 10}}, "eval-supp-crm-norm005-spatial-s48": {"status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.78, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "spatial", "mode
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6caaddd1-d9e7-4ed7-a0fc-d570f45b9e0d",
  "tool_use_result": {
    "stdout": "{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.805, \"trigger_rate\": 0.262, \"mean_unc\": 0.1862}}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.8, \"success\": 160, \"total\": 200, \"mean_unc\": 0.1924, \"trigger_rate\": 0.169}}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode",
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

_source line 13_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "68947193-cf23-4d62-9368-2780921002d1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014ABSuaMNhCUcdExoP4HsHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 34621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01BGsAp1HZ8aTA2gMZNK6emC`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\n# Filter for goal and object experiments\nfor exp_id, exp in exps.items():\n    name = exp_id.lower()\n    metrics = exp.get('metrics', {})\n    benchmark = metrics.get('benchmark', '').lower() if isinstance(metrics, dict) else ''\n    if 'goal' in name or 'object' in name or benchmark in ('goal', 'object'):\n        out = {\n            'exp_id': exp_id,\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': metrics,\n            'server': exp.get('server'),\n            'tags': exp.get('tags'),\n        }\n        print(json.dumps(out, ensure_ascii=False))\n\" | head -200\n",
  "description": "Extract Goal/Object experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e78dc75f-c817-42be-8f6a-b7a053a968b5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014ABSuaMNhCUcdExoP4HsHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 34621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 15 · 2026-05-25T02:15:26.237Z_

<details><summary>↩ Tool result · `toolu_01BGsAp1HZ8aTA2gMZNK6emC`</summary>

```text
&lt;persisted-output>
Output too large (52.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/bh7z8xr2r.txt

Preview (first 2KB):
{"exp_id": "eval-pi05-vla-only-object-s44", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.81, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "server": null, "tags": null}
{"exp_id": "eval-pi05-vla-only-object-s43", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.815, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "server": null, "tags": null}
{"exp_id": "eval-pi05-vla-only-goal-s43", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.97, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}, "server": null, "tags": null}
{"exp_id": "eval-pi05-vla-only-goal-s42", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.955, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "vla_only", "model": "pi0.5"}, "server": null, "tags": null}
{"exp_id": "eval-pi05-vla-only-object-s42", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.965, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "object", "mode": "vla_only", "model": "pi0.5"}, "server": null, "tags": null}
{"exp_id": "eval-supp-crm-norm005-goal-s48", "status": "DONE", "conclusion": "success", "metrics": {"overall_success_rate": 0.8, "n_rollouts": 20, "n_tasks": 10, "total_rollouts": 200, "benchmark": "goal", "mode": "crm_obs_only", "max_correction_norm": 0.05, "K": 10}, "server": null, "tags": null}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d71caa32-0369-4878-93ec-c3484175b994",
  "tool_use_result": {
    "stdout": "{\"exp_id\": \"eval-pi05-vla-only-object-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-vla-only-goal-s49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-vla-only-goal-s48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed43-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-obj-vla-only-s50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s49\", \"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s48\", \"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-crm-obj-s47-reeval\", \"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-k2mean-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29241, \"crm_applied_steps\": 2594, \"n_rollouts\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s47-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"precompute-pi05-object-2048-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"train-crm-pi05-goal-k1\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"crm-train-openvla-k1-multiscale-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-perdof-object-norm003-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-k2mean-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.855}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-ablation-tau015-goal-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"trigger_rate\": 0.339, \"tau\": 0.15, \"crm_applied_steps\": 9590, \"total_steps\": 28273}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-k2mean-object-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.75, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.8, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.55, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.85, \"successes\": 170, \"total\": 200, \"per_task\": {\"open_middle_drawer\": 0.85, \"put_bowl_stove\": 0.95, \"wine_bottle_cabinet\": 0.85, \"open_top_drawer_bowl\": 0.7, \"bowl_on_cabinet\": 0.9, \"push_plate_stove\": 0.9, \"cream_cheese_bowl\": 0.65, \"turn_on_stove\": 1, \"bowl_on_plate\": 0.95, \"wine_bottle_rack\": 0.75}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-crm-norm005-goal-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"total_rollouts\": 200, \"total_successes\": 167, \"three_seed_summary\": {\"seeds\": [42, 43, 44], \"srs\": [0.855, 0.82, 0.835], \"mean\": 0.8367, \"std\": 0.0176}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-k2mean-object-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"total_successes\": 156, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0.85, \"cream_cheese\": 0.85, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.85, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.9}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-k2mean-goal-s42-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.855, \"n_tasks\": 10, \"n_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 1, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.65, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.865, \"trigger_rate\": 0.0677, \"crm_applied_steps\": 1870, \"total_steps\": 27642}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.845, \"trigger_rate\": 0.088, \"crm_applied_steps\": 2509, \"total_steps\": 28500}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-k2mean-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"total_rollouts\": 200, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.9, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.55, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.45, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.95, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-k2mean-object-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79.5, \"total_successes\": 159, \"total_rollouts\": 200, \"mode\": \"vla_only\", \"K\": 2, \"baseline_mode\": \"mean\", \"per_task\": {\"alphabet_soup\": 75, \"cream_cheese\": 70, \"salad_dressing\": 85, \"bbq_sauce\": 90, \"ketchup\": 95, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 70, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 84, \"total_rollouts\": 200, \"total_successes\": 168, \"trigger_rate\": 8.3, \"mean_unc\": 0.1448, \"per_task\": {\"open_middle_drawer_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"put_bowl_on_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_wine_bottle_on_cabinet\": {\"sr\": 80, \"success\": 16, \"total\": 20}, \"open_top_drawer_put_bowl\": {\"sr\": 70, \"success\": 14, \"total\": 20}, \"put_bowl_on_top_cabinet\": {\"sr\": 85, \"success\": 17, \"total\": 20}, \"push_plate_to_stove\": {\"sr\": 95, \"success\": 19, \"total\": 20}, \"put_cream_cheese_in_bowl\": {\"sr\": 60, \"success\": 12, \"total\": 20}, \"turn_on_stove\": {\"sr\": 100, \"success\": 20, \"total\": 20}, \"put_bowl_on_plate\": {\"sr\": 90, \"success\": 18, \"total\": 20}, \"put_wine_bottle_on_rack\": {\"sr\": 80, \"success\": 16, \"total\": 20}}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-supp-goal-crm005-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 85.5, \"total_successes\": 171, \"total_episodes\": 200, \"per_task\": {\"middle_drawer\": 85, \"bowl_stove\": 100, \"wine_bottle_cabinet\": 95, \"top_drawer_bowl\": 70, \"bowl_cabinet\": 95, \"plate_stove\": 95, \"cream_cheese_bowl\": 50, \"stove\": 95, \"bowl_plate\": 95, \"wine_bottle_rack\": 75}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-goal-vla-only-wrapper-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-object-vla-only-wrapper-s44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 77.5, \"total_successes\": 155, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 90, \"ketchup\": 90, \"tomato_sauce\": 80, \"butter\": 75, \"milk\": 65, \"chocolate_pudding\": 65, \"orange_juice\": 95}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-object-vla-only-wrapper-s43-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 77, \"total_successes\": 154, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 70, \"cream_cheese\": 70, \"salad_dressing\": 75, \"bbq_sauce\": 85, \"ketchup\": 80, \"tomato_sauce\": 85, \"butter\": 60, \"milk\": 75, \"chocolate_pudding\": 75, \"orange_juice\": 95}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-object-vla-only-wrapper-s42-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"total_successes\": 158, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 85, \"cream_cheese\": 75, \"salad_dressing\": 85, \"bbq_sauce\": 85, \"ketchup\": 90, \"tomato_sauce\": 75, \"butter\": 65, \"milk\": 65, \"chocolate_pudding\": 70, \"orange_juice\": 95}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-goal-seed44-v3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 78, \"n_episodes\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-goal-seed43-v3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 82, \"n_episodes\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-object-seed44-v2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-object-seed43-v2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed42-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed44-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.975, \"successes\": 195, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed43-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed44-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99.5, \"total_successes\": 199, \"total_episodes\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-official-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed42-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 100, \"total_success\": 200, \"total_rollouts\": 200, \"n_action_steps\": 10, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 100, \"bbq_sauce\": 100, \"ketchup\": 100, \"tomato_sauce\": 100, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 100, \"orange_juice\": 100}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"precompute-smolvla-goal-bjb1-18228\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 61728, \"obs_dim\": 960, \"K\": 10, \"action_dim\": 6, \"h_eff\": 5}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"crm-train-pi05-object-full\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"val_loss\": 0.004018, \"best_epoch\": 50, \"total_epochs\": 50}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed44-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"n_tasks\": 10, \"total_rollouts\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed43-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.815, \"n_tasks\": 10, \"total_rollouts\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-pi05-vla-only-object-seed42-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"n_tasks\": 10, \"total_rollouts\": 200}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed66\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.115, \"total_successes\": 23, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.03_seed66.json\"}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed66\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.135, \"total_successes\": 27, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.1_seed66.json\"}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed66\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_successes\": 22, \"total_rollouts\": 200, \"n_rollouts_per_task\": 20, \"n_tasks\": 10, \"output_json\": \"/root/logs/eval_object_crm_obs_only_norm0.05_seed66.json\"}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}, \"server\": \"bjb2-28827\", \"tags\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-crm-object-k20-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-crm-object-k20-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed53\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed51\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed48-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed43-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed67\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"server\": \"bjb1-32546\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed67\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}, \"server\": \"bjb1-18228\", \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1}, \"server\": \"bjb2-40593\", \"tags\": null}\n{\"exp_id\": \"eval-plan-a-object-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-vla-only-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-plan-a-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-plan-a-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-random-selection-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-random-selection-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed60\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed54\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed53\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed52\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed45-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.17}, \"server\": \"bjb2-28827\", \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed55\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed43-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed47-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\": null, \"tags\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}, \"server\":",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/bh7z8xr2r.txt",
    "persistedOutputSize": 53382
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_019NbFU9tn9q28tAM7ovvCZj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/bh7z8xr2r.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "73474fc5-d992-4aed-aa5f-0c4e3cc44f70",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016bMs1bMCP8e7WPPYCZT4nR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 36408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1565
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 17 · 2026-05-25T02:15:29.737Z_

<details><summary>↩ Tool result · reported error · `toolu_019NbFU9tn9q28tAM7ovvCZj`</summary>

```text
File content (27197 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "24a5be7e-8458-4bcd-a2d2-318bd74242a9",
  "tool_use_result": "Error: File content (27197 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01NAA1xqzQepjPFTSQseDLNf`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt | python3 << 'PYEOF'\nimport json, sys, re\n\ndata = json.loads(sys.stdin.read())\nexps = data['data']['experiments']\n\n# Group goal/object experiments by (benchmark, mode)\ngroups = {}\nfor exp_id, exp in exps.items():\n    name = exp_id.lower()\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        continue\n    benchmark = metrics.get('benchmark', '').lower()\n    mode = metrics.get('mode', '')\n    \n    # Skip non-goal/object\n    if benchmark not in ('goal', 'object'):\n        # Try to infer from name\n        if 'goal' in name:\n            benchmark = 'goal'\n        elif 'object' in name:\n            benchmark = 'object'\n        else:\n            continue\n    \n    # Try to infer mode if missing\n    if not mode:\n        if 'vla-only' in name or 'vla_only' in name:\n            mode = 'vla_only'\n        elif 'crm' in name:\n            mode = 'crm'\n        elif 'adaptive' in name:\n            mode = 'adaptive'\n        elif 'spatial' in name and benchmark in ('goal', 'object'):\n            pass\n        elif 'k' in name and ('tau' in name or 'eta' in name):\n            mode = 'adaptive_or_crm'\n    \n    # Extract seed\n    m = re.search(r's(\\d+)$', name)\n    seed = int(m.group(1)) if m else None\n    \n    key = (benchmark, mode)\n    groups.setdefault(key, []).append({\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'SR': metrics.get('overall_success_rate', metrics.get('SR')),\n        'n_rollouts': metrics.get('n_rollouts'),\n        'seed': seed,\n        'K': metrics.get('K'),\n        'tau': metrics.get('tau'),\n        'eta': metrics.get('eta'),\n        'max_correction_norm': metrics.get('max_correction_norm'),\n        'model': metrics.get('model'),\n    })\n\n# Print grouped\nfor key in sorted(groups.keys()):\n    bench, mode = key\n    print(f\"\\n===== {bench} / {mode} ({len(groups[key])}) =====\")\n    for e in sorted(groups[key], key=lambda x: (x.get('seed') or 0, x['exp_id'])):\n        print(json.dumps(e, ensure_ascii=False))\nPYEOF\n",
  "description": "Group and dump Goal/Object DONE experiments by mode"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b42daeea-632a-454f-9adc-80c49f5de3bb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RY63XmAHMGRouVpUcRSqg4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 37973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 19 · 2026-05-25T02:15:43.962Z_

<details><summary>↩ Tool result · reported error · `toolu_01NAA1xqzQepjPFTSQseDLNf`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b8c7e120-dae9-402f-82b1-9675a3cc0417",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_016SSYUaqWsKDubqUU7RKxon`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\ngroups = {}\nfor exp_id, exp in exps.items():\n    name = exp_id.lower()\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        continue\n    benchmark = metrics.get('benchmark', '').lower()\n    mode = metrics.get('mode', '')\n    \n    if benchmark not in ('goal', 'object'):\n        if 'goal' in name:\n            benchmark = 'goal'\n        elif 'object' in name:\n            benchmark = 'object'\n        else:\n            continue\n    \n    if not mode:\n        if 'vla-only' in name or 'vla_only' in name:\n            mode = 'vla_only?'\n        elif 'crm' in name:\n            mode = 'crm?'\n        elif 'adaptive' in name:\n            mode = 'adaptive?'\n    \n    m = re.search(r's(\\d+)$', name)\n    seed = int(m.group(1)) if m else None\n    \n    key = (benchmark, mode)\n    groups.setdefault(key, []).append({\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'SR': metrics.get('overall_success_rate', metrics.get('SR')),\n        'n_rollouts': metrics.get('n_rollouts'),\n        'seed': seed,\n        'K': metrics.get('K'),\n        'tau': metrics.get('tau'),\n        'eta': metrics.get('eta'),\n        'max_correction_norm': metrics.get('max_correction_norm'),\n        'model': metrics.get('model'),\n    })\n\nfor key in sorted(groups.keys()):\n    bench, mode = key\n    print(f\"\\n===== {bench} / {mode} ({len(groups[key])}) =====\")\n    for e in sorted(groups[key], key=lambda x: (x.get('seed') or 0, x['exp_id'])):\n        print(json.dumps(e, ensure_ascii=False))\nPYEOF\n",
  "description": "Group Goal/Object DONE experiments by mode"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "ef6460bb-abdf-4199-a04f-47caad54bf3d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016Q5stJSfFXEESwwUt6Saa6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 38228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1429
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 21 · 2026-05-25T02:15:58.461Z_

<details><summary>↩ Tool result · `toolu_016SSYUaqWsKDubqUU7RKxon`</summary>

```text
&lt;persisted-output>
Output too large (58.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/bbvlph0hi.txt

Preview (first 2KB):
===== goal /  (20) =====
{"exp_id": "eval-obs-only-goal-norm02-seed51", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-obs-only-goal-norm02-seed52", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-smolvla-lerobot-goal-seed43-v3", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-smolvla-lerobot-goal-seed44-v3", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-supp-k2mean-goal-s42-r2", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": 200, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "precompute-pi05-goal-2048-r2", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "precompute-smolvla-goal-bjb1-18228", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": null, "K": 10, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-ablation-tau015-goal-s42", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": 42, "K": null, "tau": 0.15, "eta": null, "max_correction_norm": null, "model": null}
{"exp_id": "eval-supp-goal-adapt-tau025-s42", "status": "DONE", "conclusion": "success", "SR": null, "n_rollouts": null, "seed": 42, "K": null, "tau": null, "eta": null, "max_correction_norm": null, "model": null}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "302459ca-78b5-4979-8f6f-6dc9cd29e573",
  "tool_use_result": {
    "stdout": "===== goal /  (20) =====\n{\"exp_id\": \"eval-obs-only-goal-norm02-seed51\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-goal-norm02-seed52\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-goal-seed43-v3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-smolvla-lerobot-goal-seed44-v3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-k2mean-goal-s42-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 200, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"precompute-smolvla-goal-bjb1-18228\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": 10, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-ablation-tau015-goal-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 42, \"K\": null, \"tau\": 0.15, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 42, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 43, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-k2mean-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.815, \"n_rollouts\": null, \"seed\": 43, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 44, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 45, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.855, \"n_rollouts\": null, \"seed\": 45, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 46, \"K\": null, \"tau\": 0.25, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-k2mean-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 46, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 46, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-reconvla-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.835, \"n_rollouts\": null, \"seed\": 47, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s48\", \"status\": \"PREPARING\", \"conclusion\": \"success\", \"SR\": 0.845, \"n_rollouts\": null, \"seed\": 48, \"K\": null, \"tau\": 0.25, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-adapt-tau025-goal-s49\", \"status\": \"PREPARING\", \"conclusion\": \"success\", \"SR\": 0.815, \"n_rollouts\": null, \"seed\": 49, \"K\": null, \"tau\": 0.25, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n\n===== goal / adaptive_conformal_crm (1) =====\n{\"exp_id\": \"eval-supp-goal-adapt-tau025-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.82, \"n_rollouts\": 20, \"seed\": 47, \"K\": null, \"tau\": 0.25, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n\n===== goal / crm? (10) =====\n{\"exp_id\": \"eval-crm-goal-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.67, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-crm-goal-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.72, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-crm-goal-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-crm-goal-seed45-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-crm-goal-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.72, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"train-crm-pi05-goal-k1\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-crm005-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 42, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-crm-norm005-goal-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 44, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 45, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 46, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n\n===== goal / crm_obs_only (2) =====\n{\"exp_id\": \"eval-supp-goal-crm-norm005-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.82, \"n_rollouts\": 20, \"seed\": 47, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.8, \"n_rollouts\": 20, \"seed\": 48, \"K\": 10, \"tau\": null, \"eta\": null, \"max_correction_norm\": 0.05, \"model\": null}\n\n===== goal / vla_only (4) =====\n{\"exp_id\": \"eval-vla-only-goal-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.955, \"n_rollouts\": 20, \"seed\": 42, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": \"pi0.5\"}\n{\"exp_id\": \"eval-pi05-vla-only-goal-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.97, \"n_rollouts\": 20, \"seed\": 43, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": \"pi0.5\"}\n{\"exp_id\": \"eval-supp-goal-k2mean-s47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.825, \"n_rollouts\": 20, \"seed\": 47, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n\n===== goal / vla_only? (18) =====\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed42-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed43-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-pi05-vla-only-goal-seed44-r4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s47-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.825, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.85, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.71, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.69, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.63, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.71, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-vla-only-goal-seed51\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-goal-vla-only-wrapper-s42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 42, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 43, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 44, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.835, \"n_rollouts\": null, \"seed\": 45, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-goal-vla-only-s46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 46, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-vla-only-goal-s48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 48, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-supp-vla-only-goal-s49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": 49, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n\n===== object /  (167) =====\n{\"exp_id\": \"eval-acr-object-obs-only-default\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-acr-object-obs-only-norm02\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-acr-object-v4-default-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-k5-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-k5-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-k5-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.17, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-argmin-object-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-direct-correction-object-seed42-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed42\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.2, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.18, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.18, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.19, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k5-obs-only-object-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-obsonly-norm003-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-perdof-norm003-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-perdof-norm005-object\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-mag-perdof-norm03-object-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-object-v8-full\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.12, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed45-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-default-seed48-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed43-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed44-bjb2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed44-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed46\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed47-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed56\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed59\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed64\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.17, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed65\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.17, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed66\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.115, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm003-seed73\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.16, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed43\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed43-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.12, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed45\", \"status\": \"DEPLOYED\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed55\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed58\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.16, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed61\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed64\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed65\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed66\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.11, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed67\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.1, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed72\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.11, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm005-seed75\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed42\", \"status\": \"DEPLOYED\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed44\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.16, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed45-r2\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.17, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed46-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.17, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed48\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.13, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed49\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.16, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed50\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.14, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed51\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": null, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed51-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.11, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed52\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed52-r3\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed53\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.19, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed54\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed57\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.19, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed60\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": 10, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"max_correction_norm\": null, \"model\": null}\n{\"exp_id\": \"eval-obs-only-object-norm01-seed64\", \"status\": \"DONE\", \"conclusion\": \"success\", \"SR\": 0.15, \"n_rollouts\": null, \"seed\": null, \"K\": null, \"tau\": null, \"eta\": null, \"ma",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/bbvlph0hi.txt",
    "persistedOutputSize": 59999
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "c0a340e4-f157-4397-84f2-f9814820332d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UX8ycfpjbiYML77P1PZUci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2048,
      "cache_read_input_tokens": 39657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2048
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01VCZb2bTk2Lnui8srKaoNFo`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Look at all pi05 / standard goal/object eval experiments\nfor exp_id, exp in exps.items():\n    metrics = exp.get('metrics', {})\n    if not isinstance(metrics, dict):\n        continue\n    bench = metrics.get('benchmark', '').lower()\n    mode = metrics.get('mode', '')\n    if bench not in ('goal', 'object'):\n        continue\n    if exp.get('status') != 'DONE':\n        continue\n    if exp.get('conclusion') != 'success':\n        continue\n    \n    m = re.search(r's(?:eed)?(\\d+)', exp_id.lower())\n    seed = int(m.group(1)) if m else None\n    \n    print(f\"{exp_id} | bench={bench} | mode={mode} | SR={metrics.get('overall_success_rate')} | n_roll={metrics.get('n_rollouts')} | seed={seed} | K={metrics.get('K')} | tau={metrics.get('tau')} | eta={metrics.get('eta')} | norm={metrics.get('max_correction_norm')} | model={metrics.get('model')}\")\nPYEOF\n",
  "description": "Filter Goal/Object DONE-success experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "1455844b-c95f-40ba-a481-4be75bba4348",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UX8ycfpjbiYML77P1PZUci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2048,
      "cache_read_input_tokens": 39657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2048
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

_source line 24 · 2026-05-25T02:16:14.658Z_

<details><summary>↩ Tool result · `toolu_01VCZb2bTk2Lnui8srKaoNFo`</summary>

```text
eval-pi05-vla-only-object-s44 | bench=object | mode=vla_only | SR=0.81 | n_roll=20 | seed=44 | K=None | tau=None | eta=None | norm=None | model=pi0.5
eval-pi05-vla-only-object-s43 | bench=object | mode=vla_only | SR=0.815 | n_roll=20 | seed=43 | K=None | tau=None | eta=None | norm=None | model=pi0.5
eval-pi05-vla-only-goal-s43 | bench=goal | mode=vla_only | SR=0.97 | n_roll=20 | seed=43 | K=None | tau=None | eta=None | norm=None | model=pi0.5
eval-pi05-vla-only-goal-s42 | bench=goal | mode=vla_only | SR=0.955 | n_roll=20 | seed=42 | K=None | tau=None | eta=None | norm=None | model=pi0.5
eval-pi05-vla-only-object-s42 | bench=object | mode=vla_only | SR=0.965 | n_roll=20 | seed=42 | K=None | tau=None | eta=None | norm=None | model=pi0.5
eval-supp-crm-norm005-goal-s48 | bench=goal | mode=crm_obs_only | SR=0.8 | n_roll=20 | seed=48 | K=10 | tau=None | eta=None | norm=0.05 | model=None
eval-supp-obj-vla-only-s50 | bench=object | mode=vla_only | SR=0.74 | n_roll=20 | seed=50 | K=None | tau=None | eta=None | norm=None | model=pi05
eval-supp-goal-k2mean-s47 | bench=goal | mode=vla_only | SR=0.825 | n_roll=20 | seed=47 | K=None | tau=None | eta=None | norm=None | model=None
eval-supp-goal-adapt-tau025-s47 | bench=goal | mode=adaptive_conformal_crm | SR=0.82 | n_roll=20 | seed=47 | K=None | tau=0.25 | eta=None | norm=None | model=None
eval-supp-goal-crm-norm005-s47 | bench=goal | mode=crm_obs_only | SR=0.82 | n_roll=20 | seed=47 | K=None | tau=None | eta=None | norm=None | model=None
eval-perdof-object-norm02-seed49 | bench=object | mode=crm_perdof | SR=0.12 | n_roll=None | seed=49 | K=10 | tau=None | eta=None | norm=0.2 | model=None
eval-argmin-object-seed50 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=50 | K=10 | tau=None | eta=None | norm=None | model=None
eval-perdof-object-norm02-seed48 | bench=object | mode=crm_perdof | SR=None | n_roll=None | seed=48 | K=None | tau=None | eta=None | norm=None | model=None
eval-argmin-object-k5-seed44-r2 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=44 | K=None | tau=None | eta=None | norm=None | model=None
eval-vla-only-goal-seed44-r2 | bench=goal | mode=vla_only | SR=None | n_roll=None | seed=44 | K=None | tau=None | eta=None | norm=None | model=None
eval-argmin-object-seed47 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=47 | K=10 | tau=None | eta=None | norm=None | model=None
eval-perdof-object-norm01-seed45 | bench=object | mode=crm_perdof | SR=None | n_roll=None | seed=45 | K=None | tau=None | eta=None | norm=0.1 | model=None
eval-argmin-object-seed46 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=46 | K=10 | tau=None | eta=None | norm=None | model=None
eval-obs-only-object-norm03-seed45-r2 | bench=object | mode=crm_obs_only | SR=14 | n_roll=None | seed=45 | K=None | tau=None | eta=None | norm=0.3 | model=None
eval-vla-mean-object | bench=object | mode=vla_only | SR=None | n_roll=10 | seed=None | K=10 | tau=None | eta=None | norm=None | model=None
eval-acr-object-v4-obs-only | bench=object | mode=obs_only | SR=None | n_roll=None | seed=None | K=10 | tau=None | eta=None | norm=0.1 | model=None
eval-acr-object-v4-perdof | bench=object | mode=perdof | SR=None | n_roll=None | seed=None | K=10 | tau=None | eta=None | norm=0.1 | model=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "2c7fcafb-0f4a-4d0a-87ba-7c1bf03b6841",
  "tool_use_result": {
    "stdout": "eval-pi05-vla-only-object-s44 | bench=object | mode=vla_only | SR=0.81 | n_roll=20 | seed=44 | K=None | tau=None | eta=None | norm=None | model=pi0.5\neval-pi05-vla-only-object-s43 | bench=object | mode=vla_only | SR=0.815 | n_roll=20 | seed=43 | K=None | tau=None | eta=None | norm=None | model=pi0.5\neval-pi05-vla-only-goal-s43 | bench=goal | mode=vla_only | SR=0.97 | n_roll=20 | seed=43 | K=None | tau=None | eta=None | norm=None | model=pi0.5\neval-pi05-vla-only-goal-s42 | bench=goal | mode=vla_only | SR=0.955 | n_roll=20 | seed=42 | K=None | tau=None | eta=None | norm=None | model=pi0.5\neval-pi05-vla-only-object-s42 | bench=object | mode=vla_only | SR=0.965 | n_roll=20 | seed=42 | K=None | tau=None | eta=None | norm=None | model=pi0.5\neval-supp-crm-norm005-goal-s48 | bench=goal | mode=crm_obs_only | SR=0.8 | n_roll=20 | seed=48 | K=10 | tau=None | eta=None | norm=0.05 | model=None\neval-supp-obj-vla-only-s50 | bench=object | mode=vla_only | SR=0.74 | n_roll=20 | seed=50 | K=None | tau=None | eta=None | norm=None | model=pi05\neval-supp-goal-k2mean-s47 | bench=goal | mode=vla_only | SR=0.825 | n_roll=20 | seed=47 | K=None | tau=None | eta=None | norm=None | model=None\neval-supp-goal-adapt-tau025-s47 | bench=goal | mode=adaptive_conformal_crm | SR=0.82 | n_roll=20 | seed=47 | K=None | tau=0.25 | eta=None | norm=None | model=None\neval-supp-goal-crm-norm005-s47 | bench=goal | mode=crm_obs_only | SR=0.82 | n_roll=20 | seed=47 | K=None | tau=None | eta=None | norm=None | model=None\neval-perdof-object-norm02-seed49 | bench=object | mode=crm_perdof | SR=0.12 | n_roll=None | seed=49 | K=10 | tau=None | eta=None | norm=0.2 | model=None\neval-argmin-object-seed50 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=50 | K=10 | tau=None | eta=None | norm=None | model=None\neval-perdof-object-norm02-seed48 | bench=object | mode=crm_perdof | SR=None | n_roll=None | seed=48 | K=None | tau=None | eta=None | norm=None | model=None\neval-argmin-object-k5-seed44-r2 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=44 | K=None | tau=None | eta=None | norm=None | model=None\neval-vla-only-goal-seed44-r2 | bench=goal | mode=vla_only | SR=None | n_roll=None | seed=44 | K=None | tau=None | eta=None | norm=None | model=None\neval-argmin-object-seed47 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=47 | K=10 | tau=None | eta=None | norm=None | model=None\neval-perdof-object-norm01-seed45 | bench=object | mode=crm_perdof | SR=None | n_roll=None | seed=45 | K=None | tau=None | eta=None | norm=0.1 | model=None\neval-argmin-object-seed46 | bench=object | mode=reconvla | SR=None | n_roll=None | seed=46 | K=10 | tau=None | eta=None | norm=None | model=None\neval-obs-only-object-norm03-seed45-r2 | bench=object | mode=crm_obs_only | SR=14 | n_roll=None | seed=45 | K=None | tau=None | eta=None | norm=0.3 | model=None\neval-vla-mean-object | bench=object | mode=vla_only | SR=None | n_roll=10 | seed=None | K=10 | tau=None | eta=None | norm=None | model=None\neval-acr-object-v4-obs-only | bench=object | mode=obs_only | SR=None | n_roll=None | seed=None | K=10 | tau=None | eta=None | norm=0.1 | model=None\neval-acr-object-v4-perdof | bench=object | mode=perdof | SR=None | n_roll=None | seed=None | K=10 | tau=None | eta=None | norm=0.1 | model=None",
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

_source line 25_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "2d45d53d-4d7a-4add-8694-f303299b0fe5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RU6ZDxuEcAaNepErUxxGK2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2610,
      "cache_read_input_tokens": 41705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2610
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01VYq6TGfmi1na3WpozWUNcK`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "f4795507-a560-4deb-aaf9-70ce7eac5f7c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RU6ZDxuEcAaNepErUxxGK2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2610,
      "cache_read_input_tokens": 41705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2610
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

_source line 27 · 2026-05-25T02:16:25.072Z_

<details><summary>↩ Tool result · `toolu_01VYq6TGfmi1na3WpozWUNcK`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
openvla_oft_wrapper.py
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
patch_modeling.py
registry.lock
registry.yaml
report.md
scripts
src
study_status.lock
task_context
worker_output.md
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "297a8718-e0c3-4ee5-bac3-5bafb923e121",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\n_last_visual_review.json\nartifacts\ncheckpoints\ndecisions.lock\ndecisions.yaml\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.lock\nexperiment_plan.yaml\nfigures\nliterature_map.yaml\nlogs\nmemory.md\nmistakes.lock\nmistakes.yaml\nopenvla_oft_wrapper.py\npaper\npaper_framing.md\npaper_provenance.lock\npaper_provenance.yaml\npatch_modeling.py\nregistry.lock\nregistry.yaml\nreport.md\nscripts\nsrc\nstudy_status.lock\ntask_context\nworker_output.md\nwriting_plan.yaml",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01GdMg7QPLxKzxTfPrDLXmBo`</summary>

```json
{
  "command": "grep -n -A 5 \"Goal\\|Object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_provenance.yaml 2>/dev/null | head -200",
  "description": "Search for Goal/Object provenance entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "fcf0ba9d-f414-4fa7-a8bd-1cd332dd0caf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P8AqBtL6syg2Lac4S27JTv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 44315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
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

_source line 29 · 2026-05-25T02:16:28.333Z_

<details><summary>↩ Tool result · `toolu_01GdMg7QPLxKzxTfPrDLXmBo`</summary>

```text
18:    consistent positive improvement ($+$1.0\,pp Spatial, $+$2.0\,pp Object, $+$1.5\,pp
19:    Goal), using $5{$ fewer VLA forward pass
20-  type: quantitative
21-  location:
22-    section: abstract
23-    context: result_statement
24-  id: C002
--
108:    $+$2.0\,pp on Object (seed 42), and $+$'
109-  type: quantitative
110-  location:
111-    section: experiments
112-    context: result_statement
113-  id: C011
--
158:    on Goal ($-$2.5\,pp). Multi-sample selec'
159-  type: quantitative
160-  location:
161-    section: experiments
162-    context: result_statement
163-  id: C016
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "3ba4678e-b6bf-41ab-86b8-634f66cc5ac2",
  "tool_use_result": {
    "stdout": "18:    consistent positive improvement ($+$1.0\\,pp Spatial, $+$2.0\\,pp Object, $+$1.5\\,pp\n19:    Goal), using $5{$ fewer VLA forward pass\n20-  type: quantitative\n21-  location:\n22-    section: abstract\n23-    context: result_statement\n24-  id: C002\n--\n108:    $+$2.0\\,pp on Object (seed 42), and $+$'\n109-  type: quantitative\n110-  location:\n111-    section: experiments\n112-    context: result_statement\n113-  id: C011\n--\n158:    on Goal ($-$2.5\\,pp). Multi-sample selec'\n159-  type: quantitative\n160-  location:\n161-    section: experiments\n162-    context: result_statement\n163-  id: C016",
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

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ehm2EbwKWBszZrjYxM6CL4`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "output_mode": "files_with_matches",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e0e31534-9094-451b-8e9d-06a12e087998",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012c6ouELHmx4tNU8o2emmox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 45375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 31 · 2026-05-25T02:16:31.788Z_

<details><summary>↩ Tool result · `toolu_01Ehm2EbwKWBszZrjYxM6CL4`</summary>

```text
Found 20 files limit: 20
logs/workers/worker_audit_table1-long-provenance_20260525T021005_retry1.log
logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log
logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl
logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl
logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl
logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry2.log
logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_result.json
logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry2.log
logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log
logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log
logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry1.log
registry.yaml
logs/chats/cron_hook_eval-k2-tau020-spatial-s42.jsonl
logs/workers/worker_fix_bjb2-40593-k2-tau-overlap_20260525T004500.log
logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_result.json
logs/chats/worker_harvest_14-stale-completed-experiments_20260525T004657.jsonl
logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_retry1.log
logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_retry1.log
logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_result.json
logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry2.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "22c0ef28-76aa-48a8-b8b9-1cd77aeddd4a",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_audit_table1-long-provenance_20260525T021005_retry1.log",
      "logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
      "logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl",
      "logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl",
      "logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl",
      "logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry2.log",
      "logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_result.json",
      "logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry2.log",
      "logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log",
      "logs/workers/worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log",
      "logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_retry1.log",
      "registry.yaml",
      "logs/chats/cron_hook_eval-k2-tau020-spatial-s42.jsonl",
      "logs/workers/worker_fix_bjb2-40593-k2-tau-overlap_20260525T004500.log",
      "logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_result.json",
      "logs/chats/worker_harvest_14-stale-completed-experiments_20260525T004657.jsonl",
      "logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_retry1.log",
      "logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_retry1.log",
      "logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_result.json",
      "logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_retry2.log"
    ],
    "numFiles": 20,
    "appliedLimit": 20
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01YSHBe6pyxe2eigYTKGo9No`</summary>

```json
{
  "command": "grep -n -A 30 \"Table 1\\|table1\\|## Goal\\|## Object\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md 2>/dev/null | head -200",
  "description": "Read Table 1 section in report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "10717069-6dbd-492e-8a4f-fef743db21aa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GLxaNMCLDTmiXYBuNL9EvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 972,
      "cache_read_input_tokens": 45833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 972
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 33 · 2026-05-25T02:16:34.624Z_

<details><summary>↩ Tool result · `toolu_01YSHBe6pyxe2eigYTKGo9No`</summary>

```text
12:- eval-k2-tau035-spatial-s42: K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）
13-- …另有 130 项
14-
15-## 近期结论
16:- **eval-k2-tau020-spatial-s42** (success): K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).
17-
18-## 趋势
19-成功 517 / 负向 75 / 失败 94 / 共 850
20-
21-## 下一步
22-（无活跃 idea，请通过 ideas.md 添加）
23-
24-## 资源状态
25-bjb1-18228: 无 GPU 信息
26-bjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
27-bjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
28-bjb2-40593: 无 GPU 信息
29-cqa1-32758: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
30-
31-## 告警
32-- plan_001-crm-smolvla: 训练失败 — unknown
33-- plan_014-reconvla-baseline: 训练失败 — unknown
34-- eval-smolvla-libero-spatial: 训练失败 — unknown
35-- eval-spatial-reeval-v2: 已被终止 — unknown
36-- precompute-v2-shard0: 已被终止 — unknown
37-- precompute-v2-shard1: 已被终止 — unknown
38-- precompute-v2-shard2: 已被终止 — unknown
39-- eval-spatial-v3-full: 已被终止 — unknown
40-- precompute-v3-shard0: 已被终止 — unknown
41-- precompute-v3-shard1: 已被终止 — unknown
42-- precompute-v3-shard2: 已被终止 — unknown
43-- eval-spatial-v4-full: 已被终止 — unknown
44-- eval-object-v4-full: 已被终止 — unknown
45-- eval-spatial-v5-full: 已被终止 — unknown
46-- crm-train-v1: 已被终止 — unknown
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "410a5028-62f1-432e-b7ba-84ee97255e2d",
  "tool_use_result": {
    "stdout": "12:- eval-k2-tau035-spatial-s42: K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）\n13-- …另有 130 项\n14-\n15-## 近期结论\n16:- **eval-k2-tau020-spatial-s42** (success): K=2 τ-sweep: τ=0.20 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting. Key comparison point — τ=0.20 was peak SR under K=10 (81.0%).\n17-\n18-## 趋势\n19-成功 517 / 负向 75 / 失败 94 / 共 850\n20-\n21-## 下一步\n22-（无活跃 idea，请通过 ideas.md 添加）\n23-\n24-## 资源状态\n25-bjb1-18228: 无 GPU 信息\n26-bjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\n27-bjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\n28-bjb2-40593: 无 GPU 信息\n29-cqa1-32758: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\n30-\n31-## 告警\n32-- plan_001-crm-smolvla: 训练失败 — unknown\n33-- plan_014-reconvla-baseline: 训练失败 — unknown\n34-- eval-smolvla-libero-spatial: 训练失败 — unknown\n35-- eval-spatial-reeval-v2: 已被终止 — unknown\n36-- precompute-v2-shard0: 已被终止 — unknown\n37-- precompute-v2-shard1: 已被终止 — unknown\n38-- precompute-v2-shard2: 已被终止 — unknown\n39-- eval-spatial-v3-full: 已被终止 — unknown\n40-- precompute-v3-shard0: 已被终止 — unknown\n41-- precompute-v3-shard1: 已被终止 — unknown\n42-- precompute-v3-shard2: 已被终止 — unknown\n43-- eval-spatial-v4-full: 已被终止 — unknown\n44-- eval-object-v4-full: 已被终止 — unknown\n45-- eval-spatial-v5-full: 已被终止 — unknown\n46-- crm-train-v1: 已被终止 — unknown",
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_0161sMZ45Hq3fTCopPtrxXG5`</summary>

```json
{
  "command": "grep -n \"83\\.7\\|85\\.0\\|77\\.7\\|76\\.5\\|77\\.8\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/*.tex 2>/dev/null | head -40",
  "description": "Find Table 1 numbers in paper .tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "937056a7-7d6f-4679-aa63-e9f13836e77f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017H1jhxykk3Yt3Z5BJ4ZVDG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 46805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1080
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

_source line 35 · 2026-05-25T02:16:38.049Z_

<details><summary>↩ Tool result · `toolu_0161sMZ45Hq3fTCopPtrxXG5`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "da27dd27-c87f-47e0-b200-c4bed4fc6c94",
  "tool_use_result": {
    "stdout": "",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_0135oq8ghPEzNZgzgY1sXEMb`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/ 2>/dev/null\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/tables 2>/dev/null\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/data 2>/dev/null",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "1bcf777d-93d4-4a90-bf3a-c5c834fb3560",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BfJ2Sh7QpZnbYKWSWcysDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 47885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
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

_source line 37 · 2026-05-25T02:16:44.135Z_

<details><summary>↩ Tool result · reported error · `toolu_0135oq8ghPEzNZgzgY1sXEMb`</summary>

```text
Exit code 2
figure_plan.md
outline.md
sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "612a7e54-5cb3-4240-9c33-c6940aa4f5a1",
  "tool_use_result": "Error: Exit code 2\nfigure_plan.md\noutline.md\nsections"
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_012S9REaSwxUvNdMyPVyfFXn`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper",
  "output_mode": "content",
  "-n": true,
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "ffd53136-a428-46b1-9b1a-ab4c7c798838",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Xz8cbubPJRdcAJg5UP8kxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 48104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 312
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

_source line 39 · 2026-05-25T02:16:47.369Z_

<details><summary>↩ Tool result · `toolu_012S9REaSwxUvNdMyPVyfFXn`</summary>

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "34aac024-6603-47f6-921d-fb00aaf4eb30",
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_013AfXyDETRt53V2cNPj6pf7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6d00f01b-5f4c-4c67-b4b3-159a2be74e3b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SASM6QafMeWWJLbce8jSy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 48416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 242
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

_source line 41 · 2026-05-25T02:16:51.490Z_

<details><summary>↩ Tool result · reported error · `toolu_013AfXyDETRt53V2cNPj6pf7`</summary>

```text
File content (1111274 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "437e4e2c-791a-4348-935c-b42cd8013582",
  "tool_use_result": "Error: File content (1111274 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_01S16wmvXchXMG5mmDrXmnVG`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
  "output_mode": "content",
  "-n": true,
  "head_limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d3e0de64-800d-42d7-b475-923b76c9e2c0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XrvRCPzENsDaQ1SnadekxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 48658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
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

_source line 43 · 2026-05-25T02:16:55.446Z_

<details><summary>↩ Tool result · `toolu_01S16wmvXchXMG5mmDrXmnVG`</summary>

```text
8:[Omitted long matching line]
26:[Omitted long matching line]
62:[Omitted long matching line]
71:[Omitted long matching line]
73:[Omitted long matching line]
74:[Omitted long matching line]
77:[Omitted long matching line]
78:[Omitted long matching line]
83:[Omitted long matching line]
85:[Omitted long matching line]
92:[Omitted long matching line]
106:[Omitted long matching line]
120:[Omitted long matching line]
123:[Omitted long matching line]
125:[Omitted long matching line]
126:[Omitted long matching line]
129:[Omitted long matching line]
132:[Omitted long matching line]
134:[Omitted long matching line]
135:[Omitted long matching line]
136:[Omitted long matching line]
139:[Omitted long matching line]
141:[Omitted long matching line]
142:[Omitted long matching line]
143:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "959403c8-bd7e-44e8-8f63-bac01b9ac536",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "8:[Omitted long matching line]\n26:[Omitted long matching line]\n62:[Omitted long matching line]\n71:[Omitted long matching line]\n73:[Omitted long matching line]\n74:[Omitted long matching line]\n77:[Omitted long matching line]\n78:[Omitted long matching line]\n83:[Omitted long matching line]\n85:[Omitted long matching line]\n92:[Omitted long matching line]\n106:[Omitted long matching line]\n120:[Omitted long matching line]\n123:[Omitted long matching line]\n125:[Omitted long matching line]\n126:[Omitted long matching line]\n129:[Omitted long matching line]\n132:[Omitted long matching line]\n134:[Omitted long matching line]\n135:[Omitted long matching line]\n136:[Omitted long matching line]\n139:[Omitted long matching line]\n141:[Omitted long matching line]\n142:[Omitted long matching line]\n143:[Omitted long matching line]",
    "numLines": 25
  }
}
```

</details>

---

### Assistant

_source line 44_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "ecbb8410-b70f-497e-878d-1ce6ec1151c0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0184HNaB3rYMC2wsRs278YSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 48909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 596
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01UgZF27sskNYRkSVQMH6FLr`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/ | grep -i \"table1\\|goal-object\" | head -20",
  "description": "List Table 1 audit worker logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "4bfa87ae-9af7-487b-ba51-b3be0e4e78a6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0184HNaB3rYMC2wsRs278YSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 48909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 596
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 46 · 2026-05-25T02:16:59.240Z_

<details><summary>↩ Tool result · `toolu_01UgZF27sskNYRkSVQMH6FLr`</summary>

```text
worker_audit_table1-K-values_20260524T213618.log
worker_audit_table1-K-values_20260524T213618_result.json
worker_audit_table1-K-values_20260524T213618_retry1.log
worker_audit_table1-goal-object-provenance-r2_20260525T021436.log
worker_audit_table1-goal-object-provenance-r2_20260525T021436_result.json
worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log
worker_audit_table1-goal-object-provenance_20260525T015038.log
worker_audit_table1-goal-object-provenance_20260525T015038_result.json
worker_audit_table1-goal-object-provenance_20260525T015038_retry1.log
worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log
worker_audit_table1-long-gating-consistency_20260525T015057.log
worker_audit_table1-long-gating-consistency_20260525T015057_result.json
worker_audit_table1-long-gating-consistency_20260525T015057_retry1.log
worker_audit_table1-long-gating-consistency_20260525T015057_retry2.log
worker_audit_table1-long-provenance_20260525T021005.log
worker_audit_table1-long-provenance_20260525T021005_result.json
worker_audit_table1-long-provenance_20260525T021005_retry1.log
worker_audit_table1-spatial-provenance_20260525T015026.log
worker_audit_table1-spatial-provenance_20260525T015026_result.json
worker_audit_table1-spatial-provenance_20260525T015026_retry1.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b11c1915-d847-4fdb-b5b1-197fc912e747",
  "tool_use_result": {
    "stdout": "worker_audit_table1-K-values_20260524T213618.log\nworker_audit_table1-K-values_20260524T213618_result.json\nworker_audit_table1-K-values_20260524T213618_retry1.log\nworker_audit_table1-goal-object-provenance-r2_20260525T021436.log\nworker_audit_table1-goal-object-provenance-r2_20260525T021436_result.json\nworker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log\nworker_audit_table1-goal-object-provenance_20260525T015038.log\nworker_audit_table1-goal-object-provenance_20260525T015038_result.json\nworker_audit_table1-goal-object-provenance_20260525T015038_retry1.log\nworker_audit_table1-goal-object-provenance_20260525T015038_retry2.log\nworker_audit_table1-long-gating-consistency_20260525T015057.log\nworker_audit_table1-long-gating-consistency_20260525T015057_result.json\nworker_audit_table1-long-gating-consistency_20260525T015057_retry1.log\nworker_audit_table1-long-gating-consistency_20260525T015057_retry2.log\nworker_audit_table1-long-provenance_20260525T021005.log\nworker_audit_table1-long-provenance_20260525T021005_result.json\nworker_audit_table1-long-provenance_20260525T021005_retry1.log\nworker_audit_table1-spatial-provenance_20260525T015026.log\nworker_audit_table1-spatial-provenance_20260525T015026_result.json\nworker_audit_table1-spatial-provenance_20260525T015026_retry1.log",
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01Mt7sXN2YJ1kaoeETj92KU5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "c4fc0cdc-1e03-4955-8158-a4dcc8d23379",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01F9o74rrAZbHcbizThLQKCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 49505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
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

_source line 48 · 2026-05-25T02:17:01.769Z_

<details><summary>↩ Tool result · `toolu_01Mt7sXN2YJ1kaoeETj92KU5`</summary>

```text
1	{
2	  "raw": "Not logged in · Please run /login"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "03795a7a-ba1a-4c54-963c-63a15148ee42",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_result.json",
      "content": "{\n  \"raw\": \"Not logged in · Please run /login\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01JCjVnqmkCWAH49uvHkUxAv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "f7e28709-a31a-4a1c-b3c1-e22c0e9d5cba",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01B6TMxcCb7PJk8SghqzwLMv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 50295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 50 · 2026-05-25T02:17:04.453Z_

<details><summary>↩ Tool result · `toolu_01JCjVnqmkCWAH49uvHkUxAv`</summary>

```text
1	{
2	  "raw": "Not logged in · Please run /login"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "4a1b1f5f-da8d-4a13-8e63-5a93037ffd22",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_result.json",
      "content": "{\n  \"raw\": \"Not logged in · Please run /login\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_019XKW3kFwgZCngTqrPoF84j`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log\nwc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
  "description": "Check log line counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "94a04b47-c405-4bba-92a7-8ef529e45e10",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016t53gspSv949DwNmfiKau6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 183,
      "cache_read_input_tokens": 50636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 183
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

_source line 52 · 2026-05-25T02:17:09.620Z_

<details><summary>↩ Tool result · `toolu_019XKW3kFwgZCngTqrPoF84j`</summary>

```text
51 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log
143 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "32ed2405-aef1-48f6-9d0a-591b452b6882",
  "tool_use_result": {
    "stdout": "51 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log\n143 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_retry2.log",
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_011GK8D8gbXHwdMWc3S7WFBc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "038367fa-c08d-480e-830a-bd241ea91f92",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PEtBARDpjxi7TDbJzHMPr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 50819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 54 · 2026-05-25T02:17:12.483Z_

<details><summary>↩ Tool result · reported error · `toolu_011GK8D8gbXHwdMWc3S7WFBc`</summary>

```text
File content (306.5KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "94464ac4-2521-4272-af63-29e72be2e082",
  "tool_use_result": "Error: File content (306.5KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01NqVMuFKk24CYnwspQ97K47`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "add56c9c-f8d7-445c-a8dc-815aacbc2632",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TPTsERMXFmVVHXPaP8YZC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 51267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 56 · 2026-05-25T02:17:15.879Z_

<details><summary>↩ Tool result · reported error · `toolu_01NqVMuFKk24CYnwspQ97K47`</summary>

```text
File content (175233 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "370e2075-4468-426d-9f7a-d39601b80b7a",
  "tool_use_result": "Error: File content (175233 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01XAMRpjtnfcL3t9H6x9BDCr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6a0214ba-1039-4d9d-9d02-884212b664cc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019USiS8p6rBzTQhL2AM8gm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 51496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 58 · 2026-05-25T02:17:18.964Z_

<details><summary>↩ Tool result · reported error · `toolu_01XAMRpjtnfcL3t9H6x9BDCr`</summary>

```text
File content (172856 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "100c3262-8589-4cac-8c75-838195b4068d",
  "tool_use_result": "Error: File content (172856 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01FpBw77vQpmYdQmVsd6Zz8E`</summary>

```json
{
  "command": "head -c 30000 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_audit_table1-goal-object-provenance-r2_20260525T021436_retry1.log",
  "description": "Show retry1 head"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "5c25c54d-8caa-4753-bf54-d0ebea52a1d4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XGX4CosLBYWUAzRaZy7oxq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 51749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 60 · 2026-05-25T02:17:21.991Z_

<details><summary>↩ Tool result · `toolu_01FpBw77vQpmYdQmVsd6Zz8E`</summary>

```text
{"type":"system","subtype":"init","cwd":"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement","session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","tools":["Task","AskUserQuestion","Bash","CronCreate","CronDelete","CronList","Edit","EnterPlanMode","EnterWorktree","ExitPlanMode","ExitWorktree","Glob","Grep","ListMcpResourcesTool","Monitor","NotebookEdit","PushNotification","Read","ReadMcpResourceTool","RemoteTrigger","ScheduleWakeup","Skill","TaskOutput","TaskStop","TodoWrite","ToolSearch","WebFetch","WebSearch","Write","mcp__agent-ml-research__detect_image","mcp__agent-ml-research__kill_job","mcp__agent-ml-research__read_registry","mcp__agent-ml-research__register_artifact","mcp__agent-ml-research__ssh_execute","mcp__agent-ml-research__ssh_read_only","mcp__agent-ml-research__update_registry"],"mcp_servers":[{"name":"agent-ml-research","status":"connected"}],"model":"claude-opus-4-7[1m]","permissionMode":"bypassPermissions","slash_commands":["update-config","debug","simplify","batch","fewer-permission-prompts","loop","schedule","claude-api","clear","compact","context","heapdump","init","review","security-review","extra-usage","usage","insights","team-onboarding"],"apiKeySource":"none","claude_code_version":"2.1.126","output_style":"default","agents":["claude","Explore","general-purpose","Plan","statusline-setup"],"skills":["update-config","debug","simplify","batch","fewer-permission-prompts","loop","schedule","claude-api"],"plugins":[],"analytics_disabled":false,"uuid":"fa9eed34-8fe0-4459-a163-23b00dc8bf2b","memory_paths":{"auto":"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"},"fast_mode_state":"off"}
{"type":"rate_limit_event","rate_limit_info":{"status":"allowed","resetsAt":1779682200,"rateLimitType":"five_hour","overageStatus":"rejected","overageDisabledReason":"org_level_disabled","isUsingOverage":false},"uuid":"ad2103dd-d3c3-4df1-a926-9242a12a8a78","session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c"}
{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_011VUb1RPJG6QWKQz9zs3D2K","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"","signature":"Ev0CCmMIDhgCKkAUEx9JYSyhsBe1/qEw6uxp9qLaTorZRMPXafMKFs48ZcurVL6VZUw5HITbj2LXGP+REOvrviBTqgXfLkjYQRABMg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDBhIxTbh8lkROmAOuRoMCXwSdUbov5Lq9t0jIjAVgaApGkyKCg4dZW6PMbS0jGdLQAcMgU3XlrKDPLe6LanjJV1H8Ep7h/vnSPdltikqxwGCsSmcHMpOGlB6Z+IKfeXLdh9IYm+cjtB4vsf7qojPEyxhspSOg1ipTNAfCrPHgsaOQbLtwj/VDOXkLJDNPNzppeHwZJR3y6RlXGTwVclaIJ+Op69x6uZDE5wuoHhtAQUki+t1Em8CI5qfhyJfD5oaHe1XfE8SyzLEjUlzaNKNX3VWQ9Kp+idXH++LHCMU01s/0VWYGK4gOA7uS5RkxAyg2D3cDT9aD0HKdy9pjfHnIJepwMWqbag4ywfTH+LE/qx+xxZ9ohv6GAE="}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":6,"cache_creation_input_tokens":15227,"cache_read_input_tokens":16241,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":15227},"output_tokens":8,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":null,"context_management":null},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"3ea9a7f5-113e-4365-a6ab-782d0c02e6ca"}
{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_011VUb1RPJG6QWKQz9zs3D2K","type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_01UwHoEkACgupTHECMxrPQy7","name":"ToolSearch","input":{"query":"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image","max_results":10},"caller":{"type":"direct"}}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":6,"cache_creation_input_tokens":15227,"cache_read_input_tokens":16241,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":15227},"output_tokens":8,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":null,"context_management":null},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"e2f5ecf5-983f-4b63-9c06-e7de37561acc"}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"toolu_01UwHoEkACgupTHECMxrPQy7","content":[{"type":"tool_reference","tool_name":"mcp__agent-ml-research__read_registry"},{"type":"tool_reference","tool_name":"mcp__agent-ml-research__ssh_read_only"},{"type":"tool_reference","tool_name":"mcp__agent-ml-research__ssh_execute"},{"type":"tool_reference","tool_name":"mcp__agent-ml-research__detect_image"}]}]},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"efcc400d-6e3b-4793-8fe3-6d23d065ceae","timestamp":"2026-05-25T02:14:52.217Z","tool_use_result":{"matches":["mcp__agent-ml-research__read_registry","mcp__agent-ml-research__ssh_read_only","mcp__agent-ml-research__ssh_execute","mcp__agent-ml-research__detect_image"],"query":"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image","total_deferred_tools":26}}
{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_018eXxqPNkSqxiMDRVkJn7ts","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"","signature":"Eo4CCmMIDhgCKkB9LHmfS5mHerUis5PYez+YujBoMU8WN5zVghXvOnc+Fj4zcM/qOoblC/iaPUVvILFj5OWyEK5mpk3UktQUNfuXMg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDHzxKBsi65aEvS7XLBoMlJjlCdk1Al8whRECIjAvTdC+nj0n5qYHU51t2/goLurO9cvDtLg+EII55FmjBK2+uhhcdQppuRAy79vT/UIqWfhwvyt5EN6QAfWIV6oZH55ArGrquhKoXUyG4BXCWiyNkwJoOFmpcNhgWf9O/4VzkS6cdSrcb5SBjgWi48jRZdZxM34QmIKOXRn/PigD1CA12r/jca0e/CURGAE="}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":6,"cache_creation_input_tokens":16908,"cache_read_input_tokens":16334,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":16908},"output_tokens":0,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":{"cache_miss_reason":{"type":"tools_changed","cache_missed_input_tokens":28922}},"context_management":null},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"b274f549-9a28-48df-8add-18f65674b1b5"}
{"type":"assistant","message":{"model":"claude-opus-4-7","id":"msg_018eXxqPNkSqxiMDRVkJn7ts","type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_019fJDXX2ioneWU2zfxFs2C5","name":"mcp__agent-ml-research__read_registry","input":{"project":"acr-vla-conformal-refinement","filters":{"conclusion":"success"},"fields":["exp_id","name","server","status","conclusion","metrics","tags","config"],"limit":0},"caller":{"type":"direct"}}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":6,"cache_creation_input_tokens":16908,"cache_read_input_tokens":16334,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":16908},"output_tokens":0,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":{"cache_miss_reason":{"type":"tools_changed","cache_missed_input_tokens":28922}},"context_management":null},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"1d5802bf-9b9f-4abc-954e-4781282115ab"}
{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_019fJDXX2ioneWU2zfxFs2C5","type":"tool_result","content":"Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n"}]},"parent_tool_use_id":null,"session_id":"cac457c2-38ab-40ed-86ec-14422a05cb5c","uuid":"40864965-5dd6-4b5e-a437-78eb4acb10be","timestamp":"2026-05-25T02:15:04.037Z","tool_use_result":{"content":"Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n","structuredContent":{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau020-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.805, \"trigger_rate\": 0.262, \"mean_unc\": 0.1862}}, \"eval-k2-tau030-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.8, \"success\": 160, \"total\": 200, \"mean_unc\": 0.1924, \"trigger_rate\": 0.169}}, \"eval-pi05-vla-only-spatial-s45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.85, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.81, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.97, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.96, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.98, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.785, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-crm-norm005-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.78, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10}}, \"eval-supp-vla-only-spatial-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.785, \"per_task_sr\": {\"between\": 0.9, \"next_ramekin\": 0.95, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.7, \"on_ramekin\": 0, \"next_cookie\": 0.9, \"stove\": 0.8, \"next_plate\": 0.75, \"cabinet\": 0.95}}}, \"eval-supp-vla-only-spatial-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.795, \"per_task_sr\": {\"between\": 1, \"next_ramekin\": 0.9, \"center\": 0.95, \"cookie_box\": 0.95, \"drawer\": 0.8, \"on_ramekin\": 0, \"next_cookie\": 0.95, \"stove\": 0.75, \"next_plate\": 0.85, \"cabinet\": 0.8}}}, \"eval-supp-vla-only-obj-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.755, \"per_task_sr\": {\"soup\": 0.55, \"cream_cheese\": 0.7, \"salad\": 0.8, \"bbq\": 0.95, \"ketchup\": 0.8, \"tomato\": 0.8, \"butter\": 0.6, \"milk\": 0.65, \"pudding\": 0.8, \"oj\": 0.9}}}, \"eval-supp-vla-only-obj-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.79, \"per_task_sr\": {\"soup\": 0.65, \"cream_cheese\": 0.8, \"salad\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.85, \"tomato\": 0.8, \"butter\": 0.65, \"milk\": 0.8, \"pudding\": 0.75, \"oj\": 0.95}}}, \"eval-supp-vla-only-goal-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.82, \"per_task_sr\": {\"middle_drawer\": 0.75, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.65, \"bowl_cabinet\": 0.95, \"push_plate\": 0.85, \"cream_cheese\": 0.55, \"stove_on\": 1, \"bowl_plate\": 0.85, \"wine_rack\": 0.8}}}, \"eval-supp-vla-only-goal-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.85, \"per_task_sr\": {\"middle_drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.9, \"drawer_bowl\": 0.55, \"bowl_cabinet\": 1, \"push_plate\": 0.9, \"cream_cheese\": 0.6, \"stove_on\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}, \"eval-adaptive-spatial-k1-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-spatial-s42-sweep\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 79, \"K\": 5, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.835}}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.565}, \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"spatial\", \"seed\": 42, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.5, \"total_successes\": 197, \"total_episodes\": 200}}, \"eval-supp-obj-vla-only-s50\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.74, \"successes\": 148, \"total\": 200, \"n_rollouts\": 20, \"benchmark\": \"object\", \"seed\": 50, \"mode\": \"vla_only\", \"model\": \"pi05\"}, \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.74, \"trigger_rate\": 0.0417, \"mean_uncertainty\": 0.1131, \"per_task_sr\": {\"soup\": 0.7, \"cream_cheese\": 0.65, \"salad\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.75, \"tomato\": 0.75, \"butter\": 0.6, \"milk\": 0.6, \"pudding\": 0.8, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-obj-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.76, \"trigger_rate\": 0.0389, \"mean_uncertainty\": 0.1117, \"per_task_sr\": {\"soup\": 0.75, \"cream_cheese\": 0.75, \"salad\": 0.7, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.6, \"milk\": 0.8, \"pudding\": 0.7, \"oj\": 0.95}}}, \"eval-supp-adapt-tau025-goal-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 49}}, \"eval-supp-adapt-tau025-goal-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.845, \"trigger_rate\": 0.089, \"tau\": 0.25, \"benchmark\": \"goal\", \"seed\": 48}}, \"eval-supp-adapt-tau025-spatial-s49\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"trigger_rate\": 0.195, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 49}}, \"eval-supp-adapt-tau025-spatial-s48\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.198, \"tau\": 0.25, \"benchmark\": \"spatial\", \"seed\": 48}}, \"eval-adaptive-k1-spatial-tau025-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.795, \"trigger_rate\": 0.197, \"tau\": 0.25, \"K\": 1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-crm-obj-s47-reeval\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\", \"seed\": 47}}, \"eval-tau-sweep-spatial-tau030-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.805, \"trigger_rate\": 0.167, \"tau\": 0.3, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau020-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"trigger_rate\": 0.266, \"tau\": 0.2, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-tau-sweep-spatial-tau010-s42\": {\"status\": \"PREPARING\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.79, \"trigger_rate\": 0.752, \"tau\": 0.1, \"benchmark\": \"spatial\", \"seed\": 42}}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.545, \"successes\": 109, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"note\": \"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\"}}, \"eval-supp-spatial-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.78, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"total_rollouts\": 200, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.7}}}, \"eval-supp-long-vla-only-s47-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.595, \"total_successes\": 119, \"total_trials\": 200}}, \"eval-supp-obj-adapt-tau025-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"trigger_rate\": 0.0403, \"crm_applied_steps\": 1458}}, \"eval-supp-obj-crm-norm005-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825}}, \"eval-supp-obj-vla-only-s47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"note\": \"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\"}}, \"eval-supp-spatial-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"total_successes\": 162, \"total_trials\": 200, \"per_task_range\": \"0.0-1.0\", \"worst_task\": \"pick_up_black_bowl_on_ramekin (0/20)\", \"best_tasks\": \"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"successes\": 163, \"total\": 200, \"trigger_rate\": 0.2046, \"mean_uncertainty\": 0.1873, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-spatial-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}}, \"eval-supp-obj-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.765, \"total_successes\": 153, \"total_trials\": 200, \"per_task\": {\"alphabet_soup\": 0.75, \"cream_cheese\": 0.95, \"salad_dressing\": 0.7, \"bbq_sauce\": 0.95, \"ketchup\": 0.75, \"tomato_sauce\": 0.65, \"butter\": 0.5, \"milk\": 0.7, \"chocolate_pudding\": 0.75, \"orange_juice\": 0.95}}}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"tau\": 0.25, \"trigger_rate\": 0.0887, \"mean_uncertainty\": 0.1476, \"total_steps\": 29241, \"crm_applied_steps\": 2594, \"n_rollouts\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"n_rollouts\": 20}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.565, \"successes\": 113, \"total\": 200, \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\", \"note\": \"False failure - completed but harvest missed result\"}}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-k2mean-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-crm-norm005-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-adapt-tau025-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-obj-vla-only-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.755, \"successes\": 151, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-supp-goal-vla-only-s47-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.825, \"successes\": 165, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_goal_vla_only_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20, \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\"}, \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 72507, \"K\": 10, \"obs_dim\": 2048, \"action_dim\": 6, \"h_eff\": 5}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"mean_uncertainty\": 0.1885, \"trigger_rate\": 0.2013, \"tau\": 0.25, \"total_steps\": 28599, \"crm_applied_steps\": 5758}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}, \"train-crm-pi05-spatial-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.002887, \"best_epoch\": 50, \"final_train_loss\": 0.018836}}, \"train-crm-pi05-goal-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.003319, \"best_epoch\": 48, \"final_train_loss\": 0.018992}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"conclusion\": \"success\"}, \"eval-supp-obj-vla-only-s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d3d92786-a40b-4362-b2bc-569d76e76f3b",
  "tool_use_result": {
    "stdout": "{\"type\":\"system\",\"subtype\":\"init\",\"cwd\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement\",\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"tools\":[\"Task\",\"AskUserQuestion\",\"Bash\",\"CronCreate\",\"CronDelete\",\"CronList\",\"Edit\",\"EnterPlanMode\",\"EnterWorktree\",\"ExitPlanMode\",\"ExitWorktree\",\"Glob\",\"Grep\",\"ListMcpResourcesTool\",\"Monitor\",\"NotebookEdit\",\"PushNotification\",\"Read\",\"ReadMcpResourceTool\",\"RemoteTrigger\",\"ScheduleWakeup\",\"Skill\",\"TaskOutput\",\"TaskStop\",\"TodoWrite\",\"ToolSearch\",\"WebFetch\",\"WebSearch\",\"Write\",\"mcp__agent-ml-research__detect_image\",\"mcp__agent-ml-research__kill_job\",\"mcp__agent-ml-research__read_registry\",\"mcp__agent-ml-research__register_artifact\",\"mcp__agent-ml-research__ssh_execute\",\"mcp__agent-ml-research__ssh_read_only\",\"mcp__agent-ml-research__update_registry\"],\"mcp_servers\":[{\"name\":\"agent-ml-research\",\"status\":\"connected\"}],\"model\":\"claude-opus-4-7[1m]\",\"permissionMode\":\"bypassPermissions\",\"slash_commands\":[\"update-config\",\"debug\",\"simplify\",\"batch\",\"fewer-permission-prompts\",\"loop\",\"schedule\",\"claude-api\",\"clear\",\"compact\",\"context\",\"heapdump\",\"init\",\"review\",\"security-review\",\"extra-usage\",\"usage\",\"insights\",\"team-onboarding\"],\"apiKeySource\":\"none\",\"claude_code_version\":\"2.1.126\",\"output_style\":\"default\",\"agents\":[\"claude\",\"Explore\",\"general-purpose\",\"Plan\",\"statusline-setup\"],\"skills\":[\"update-config\",\"debug\",\"simplify\",\"batch\",\"fewer-permission-prompts\",\"loop\",\"schedule\",\"claude-api\"],\"plugins\":[],\"analytics_disabled\":false,\"uuid\":\"fa9eed34-8fe0-4459-a163-23b00dc8bf2b\",\"memory_paths\":{\"auto\":\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/\"},\"fast_mode_state\":\"off\"}\n{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1779682200,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"ad2103dd-d3c3-4df1-a926-9242a12a8a78\",\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_011VUb1RPJG6QWKQz9zs3D2K\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"thinking\",\"thinking\":\"\",\"signature\":\"Ev0CCmMIDhgCKkAUEx9JYSyhsBe1/qEw6uxp9qLaTorZRMPXafMKFs48ZcurVL6VZUw5HITbj2LXGP+REOvrviBTqgXfLkjYQRABMg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDBhIxTbh8lkROmAOuRoMCXwSdUbov5Lq9t0jIjAVgaApGkyKCg4dZW6PMbS0jGdLQAcMgU3XlrKDPLe6LanjJV1H8Ep7h/vnSPdltikqxwGCsSmcHMpOGlB6Z+IKfeXLdh9IYm+cjtB4vsf7qojPEyxhspSOg1ipTNAfCrPHgsaOQbLtwj/VDOXkLJDNPNzppeHwZJR3y6RlXGTwVclaIJ+Op69x6uZDE5wuoHhtAQUki+t1Em8CI5qfhyJfD5oaHe1XfE8SyzLEjUlzaNKNX3VWQ9Kp+idXH++LHCMU01s/0VWYGK4gOA7uS5RkxAyg2D3cDT9aD0HKdy9pjfHnIJepwMWqbag4ywfTH+LE/qx+xxZ9ohv6GAE=\"}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":15227,\"cache_read_input_tokens\":16241,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":15227},\"output_tokens\":8,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"3ea9a7f5-113e-4365-a6ab-782d0c02e6ca\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_011VUb1RPJG6QWKQz9zs3D2K\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_01UwHoEkACgupTHECMxrPQy7\",\"name\":\"ToolSearch\",\"input\":{\"query\":\"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image\",\"max_results\":10},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":15227,\"cache_read_input_tokens\":16241,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":15227},\"output_tokens\":8,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":null,\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"e2f5ecf5-983f-4b63-9c06-e7de37561acc\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"type\":\"tool_result\",\"tool_use_id\":\"toolu_01UwHoEkACgupTHECMxrPQy7\",\"content\":[{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__read_registry\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__ssh_read_only\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__ssh_execute\"},{\"type\":\"tool_reference\",\"tool_name\":\"mcp__agent-ml-research__detect_image\"}]}]},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"efcc400d-6e3b-4793-8fe3-6d23d065ceae\",\"timestamp\":\"2026-05-25T02:14:52.217Z\",\"tool_use_result\":{\"matches\":[\"mcp__agent-ml-research__read_registry\",\"mcp__agent-ml-research__ssh_read_only\",\"mcp__agent-ml-research__ssh_execute\",\"mcp__agent-ml-research__detect_image\"],\"query\":\"select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image\",\"total_deferred_tools\":26}}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_018eXxqPNkSqxiMDRVkJn7ts\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"thinking\",\"thinking\":\"\",\"signature\":\"Eo4CCmMIDhgCKkB9LHmfS5mHerUis5PYez+YujBoMU8WN5zVghXvOnc+Fj4zcM/qOoblC/iaPUVvILFj5OWyEK5mpk3UktQUNfuXMg9jbGF1ZGUtb3B1cy00LTc4AEIIdGhpbmtpbmcSDHzxKBsi65aEvS7XLBoMlJjlCdk1Al8whRECIjAvTdC+nj0n5qYHU51t2/goLurO9cvDtLg+EII55FmjBK2+uhhcdQppuRAy79vT/UIqWfhwvyt5EN6QAfWIV6oZH55ArGrquhKoXUyG4BXCWiyNkwJoOFmpcNhgWf9O/4VzkS6cdSrcb5SBjgWi48jRZdZxM34QmIKOXRn/PigD1CA12r/jca0e/CURGAE=\"}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":16908,\"cache_read_input_tokens\":16334,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":16908},\"output_tokens\":0,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":{\"cache_miss_reason\":{\"type\":\"tools_changed\",\"cache_missed_input_tokens\":28922}},\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"b274f549-9a28-48df-8add-18f65674b1b5\"}\n{\"type\":\"assistant\",\"message\":{\"model\":\"claude-opus-4-7\",\"id\":\"msg_018eXxqPNkSqxiMDRVkJn7ts\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[{\"type\":\"tool_use\",\"id\":\"toolu_019fJDXX2ioneWU2zfxFs2C5\",\"name\":\"mcp__agent-ml-research__read_registry\",\"input\":{\"project\":\"acr-vla-conformal-refinement\",\"filters\":{\"conclusion\":\"success\"},\"fields\":[\"exp_id\",\"name\",\"server\",\"status\",\"conclusion\",\"metrics\",\"tags\",\"config\"],\"limit\":0},\"caller\":{\"type\":\"direct\"}}],\"stop_reason\":null,\"stop_sequence\":null,\"stop_details\":null,\"usage\":{\"input_tokens\":6,\"cache_creation_input_tokens\":16908,\"cache_read_input_tokens\":16334,\"cache_creation\":{\"ephemeral_5m_input_tokens\":0,\"ephemeral_1h_input_tokens\":16908},\"output_tokens\":0,\"service_tier\":\"standard\",\"inference_geo\":\"not_available\"},\"diagnostics\":{\"cache_miss_reason\":{\"type\":\"tools_changed\",\"cache_missed_input_tokens\":28922}},\"context_management\":null},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"1d5802bf-9b9f-4abc-954e-4781282115ab\"}\n{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_019fJDXX2ioneWU2zfxFs2C5\",\"type\":\"tool_result\",\"content\":\"Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.\\nFormat: JSON with schema: {result: string}\\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.\\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\\n\"}]},\"parent_tool_use_id\":null,\"session_id\":\"cac457c2-38ab-40ed-86ec-14422a05cb5c\",\"uuid\":\"40864965-5dd6-4b5e-a437-78eb4acb10be\",\"timestamp\":\"2026-05-25T02:15:04.037Z\",\"tool_use_result\":{\"content\":\"Error: result (159,126 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt.\\nFormat: JSON with schema: {result: string}\\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/cac457c2-38ab-40ed-86ec-14422a05cb5c/tool-results/mcp-agent-ml-research-read_registry-1779675304007.txt in sequential chunks until 100% of the content has been read.\\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\\n\",\"structuredContent\":{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-k2-tau020-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.805, \\\"trigger_rate\\\": 0.262, \\\"mean_unc\\\": 0.1862}}, \\\"eval-k2-tau030-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.8, \\\"success\\\": 160, \\\"total\\\": 200, \\\"mean_unc\\\": 0.1924, \\\"trigger_rate\\\": 0.169}}, \\\"eval-pi05-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.85, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.815, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.97, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.955, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.965, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.96, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.98, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi0.5\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-crm-norm005-goal-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.8, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10}}, \\\"eval-supp-crm-norm005-spatial-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.785, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10}}, \\\"eval-supp-crm-norm005-spatial-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.78, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10}}, \\\"eval-supp-vla-only-spatial-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.785, \\\"per_task_sr\\\": {\\\"between\\\": 0.9, \\\"next_ramekin\\\": 0.95, \\\"center\\\": 0.95, \\\"cookie_box\\\": 0.95, \\\"drawer\\\": 0.7, \\\"on_ramekin\\\": 0, \\\"next_cookie\\\": 0.9, \\\"stove\\\": 0.8, \\\"next_plate\\\": 0.75, \\\"cabinet\\\": 0.95}}}, \\\"eval-supp-vla-only-spatial-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.795, \\\"per_task_sr\\\": {\\\"between\\\": 1, \\\"next_ramekin\\\": 0.9, \\\"center\\\": 0.95, \\\"cookie_box\\\": 0.95, \\\"drawer\\\": 0.8, \\\"on_ramekin\\\": 0, \\\"next_cookie\\\": 0.95, \\\"stove\\\": 0.75, \\\"next_plate\\\": 0.85, \\\"cabinet\\\": 0.8}}}, \\\"eval-supp-vla-only-obj-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.755, \\\"per_task_sr\\\": {\\\"soup\\\": 0.55, \\\"cream_cheese\\\": 0.7, \\\"salad\\\": 0.8, \\\"bbq\\\": 0.95, \\\"ketchup\\\": 0.8, \\\"tomato\\\": 0.8, \\\"butter\\\": 0.6, \\\"milk\\\": 0.65, \\\"pudding\\\": 0.8, \\\"oj\\\": 0.9}}}, \\\"eval-supp-vla-only-obj-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.79, \\\"per_task_sr\\\": {\\\"soup\\\": 0.65, \\\"cream_cheese\\\": 0.8, \\\"salad\\\": 0.75, \\\"bbq\\\": 0.9, \\\"ketchup\\\": 0.85, \\\"tomato\\\": 0.8, \\\"butter\\\": 0.65, \\\"milk\\\": 0.8, \\\"pudding\\\": 0.75, \\\"oj\\\": 0.95}}}, \\\"eval-supp-vla-only-goal-s49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.82, \\\"per_task_sr\\\": {\\\"middle_drawer\\\": 0.75, \\\"bowl_stove\\\": 0.95, \\\"wine_cabinet\\\": 0.85, \\\"drawer_bowl\\\": 0.65, \\\"bowl_cabinet\\\": 0.95, \\\"push_plate\\\": 0.85, \\\"cream_cheese\\\": 0.55, \\\"stove_on\\\": 1, \\\"bowl_plate\\\": 0.85, \\\"wine_rack\\\": 0.8}}}, \\\"eval-supp-vla-only-goal-s48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.85, \\\"per_task_sr\\\": {\\\"middle_drawer\\\": 0.9, \\\"bowl_stove\\\": 0.95, \\\"wine_cabinet\\\": 0.9, \\\"drawer_bowl\\\": 0.55, \\\"bowl_cabinet\\\": 1, \\\"push_plate\\\": 0.9, \\\"cream_cheese\\\": 0.6, \\\"stove_on\\\": 1, \\\"bowl_plate\\\": 0.9, \\\"wine_rack\\\": 0.8}}}, \\\"eval-adaptive-spatial-k1-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-k5-spatial-s42-sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 79, \\\"K\\\": 5, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42}}, \\\"eval-supp-goal-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.835}}, \\\"eval-supp-long-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"SR\\\": 0.575, \\\"successes\\\": 115, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"n_rollouts\\\": 20, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42, \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi05\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-pi05-vla-only-object-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 98.5, \\\"total_successes\\\": 197, \\\"total_episodes\\\": 200}}, \\\"eval-supp-obj-vla-only-s50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.74, \\\"successes\\\": 148, \\\"total\\\": 200, \\\"n_rollouts\\\": 20, \\\"benchmark\\\": \\\"object\\\", \\\"seed\\\": 50, \\\"mode\\\": \\\"vla_only\\\", \\\"model\\\": \\\"pi05\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-adapt-tau025-obj-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.74, \\\"trigger_rate\\\": 0.0417, \\\"mean_uncertainty\\\": 0.1131, \\\"per_task_sr\\\": {\\\"soup\\\": 0.7, \\\"cream_cheese\\\": 0.65, \\\"salad\\\": 0.8, \\\"bbq\\\": 0.8, \\\"ketchup\\\": 0.75, \\\"tomato\\\": 0.75, \\\"butter\\\": 0.6, \\\"milk\\\": 0.6, \\\"pudding\\\": 0.8, \\\"oj\\\": 0.95}}}, \\\"eval-supp-adapt-tau025-obj-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.76, \\\"trigger_rate\\\": 0.0389, \\\"mean_uncertainty\\\": 0.1117, \\\"per_task_sr\\\": {\\\"soup\\\": 0.75, \\\"cream_cheese\\\": 0.75, \\\"salad\\\": 0.7, \\\"bbq\\\": 0.9, \\\"ketchup\\\": 0.8, \\\"tomato\\\": 0.65, \\\"butter\\\": 0.6, \\\"milk\\\": 0.8, \\\"pudding\\\": 0.7, \\\"oj\\\": 0.95}}}, \\\"eval-supp-adapt-tau025-goal-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.815, \\\"trigger_rate\\\": 0.089, \\\"tau\\\": 0.25, \\\"benchmark\\\": \\\"goal\\\", \\\"seed\\\": 49}}, \\\"eval-supp-adapt-tau025-goal-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.845, \\\"trigger_rate\\\": 0.089, \\\"tau\\\": 0.25, \\\"benchmark\\\": \\\"goal\\\", \\\"seed\\\": 48}}, \\\"eval-supp-adapt-tau025-spatial-s49\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.82, \\\"trigger_rate\\\": 0.195, \\\"tau\\\": 0.25, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 49}}, \\\"eval-supp-adapt-tau025-spatial-s48\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"trigger_rate\\\": 0.198, \\\"tau\\\": 0.25, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 48}}, \\\"eval-adaptive-k1-spatial-tau025-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.795, \\\"trigger_rate\\\": 0.197, \\\"tau\\\": 0.25, \\\"K\\\": 1, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42}}, \\\"eval-crm-obj-s47-reeval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.825, \\\"mode\\\": \\\"crm_obs_only\\\", \\\"benchmark\\\": \\\"object\\\", \\\"seed\\\": 47}}, \\\"eval-tau-sweep-spatial-tau030-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.805, \\\"trigger_rate\\\": 0.167, \\\"tau\\\": 0.3, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42}}, \\\"eval-tau-sweep-spatial-tau020-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"trigger_rate\\\": 0.266, \\\"tau\\\": 0.2, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42}}, \\\"eval-tau-sweep-spatial-tau010-s42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.79, \\\"trigger_rate\\\": 0.752, \\\"tau\\\": 0.1, \\\"benchmark\\\": \\\"spatial\\\", \\\"seed\\\": 42}}, \\\"eval-supp-long-k2mean-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.545, \\\"successes\\\": 109, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"note\\\": \\\"output saved as eval_long_vla_only_seed47.json (pre-M083 naming)\\\"}}, \\\"eval-supp-spatial-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.78, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"total_rollouts\\\": 200, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.9, \\\"next_to_ramekin\\\": 0.9, \\\"table_center\\\": 0.95, \\\"on_cookie_box\\\": 1, \\\"top_drawer_cabinet\\\": 0.65, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 1, \\\"on_stove\\\": 0.9, \\\"next_to_plate\\\": 0.8, \\\"on_wooden_cabinet\\\": 0.7}}}, \\\"eval-supp-long-vla-only-s47-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.595, \\\"total_successes\\\": 119, \\\"total_trials\\\": 200}}, \\\"eval-supp-obj-adapt-tau025-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.77, \\\"trigger_rate\\\": 0.0403, \\\"crm_applied_steps\\\": 1458}}, \\\"eval-supp-obj-crm-norm005-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.825}}, \\\"eval-supp-obj-vla-only-s47-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.755}}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"successes\\\": 162, \\\"total\\\": 200, \\\"note\\\": \\\"Completed at 18:07 with SR=81.0% per log; JSON overwritten by vla-only K=1 run which wrote to same output_file (eval_spatial_vla_only_seed47.json). Per-task data recoverable from eval-supp-k2mean-spatial-s47.log on cqa1-32758. Recommend explicit --output_file for future k2mean runs.\\\"}}, \\\"eval-supp-spatial-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.81, \\\"total_successes\\\": 162, \\\"total_trials\\\": 200, \\\"per_task_range\\\": \\\"0.0-1.0\\\", \\\"worst_task\\\": \\\"pick_up_black_bowl_on_ramekin (0/20)\\\", \\\"best_tasks\\\": \\\"from_table_center, on_cookie_box, next_to_cookie_box (20/20)\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.815, \\\"successes\\\": 163, \\\"total\\\": 200, \\\"trigger_rate\\\": 0.2046, \\\"mean_uncertainty\\\": 0.1873, \\\"json_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\\", \\\"note\\\": \\\"False failure - completed but harvest missed result\\\"}}, \\\"eval-supp-spatial-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"total_successes\\\": 164, \\\"total_trials\\\": 200, \\\"note\\\": \\\"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\\\"}}, \\\"eval-supp-obj-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.765, \\\"total_successes\\\": 153, \\\"total_trials\\\": 200, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0.75, \\\"cream_cheese\\\": 0.95, \\\"salad_dressing\\\": 0.7, \\\"bbq_sauce\\\": 0.95, \\\"ketchup\\\": 0.75, \\\"tomato_sauce\\\": 0.65, \\\"butter\\\": 0.5, \\\"milk\\\": 0.7, \\\"chocolate_pudding\\\": 0.75, \\\"orange_juice\\\": 0.95}}}, \\\"eval-supp-goal-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.825, \\\"successes\\\": 165, \\\"total\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"baseline_mode\\\": \\\"mean\\\", \\\"n_rollouts\\\": 20}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.82, \\\"successes\\\": 164, \\\"total\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"tau\\\": 0.25, \\\"trigger_rate\\\": 0.0887, \\\"mean_uncertainty\\\": 0.1476, \\\"total_steps\\\": 29241, \\\"crm_applied_steps\\\": 2594, \\\"n_rollouts\\\": 20}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-goal-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.82, \\\"successes\\\": 164, \\\"total\\\": 200, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"n_rollouts\\\": 20}}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.81, \\\"successes\\\": 162, \\\"total\\\": 200, \\\"json_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed47.json\\\", \\\"note\\\": \\\"False failure - completed but harvest missed result\\\"}}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"json_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\\", \\\"note\\\": \\\"False failure - completed but harvest missed result\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.55, \\\"successes\\\": 110, \\\"total\\\": 200, \\\"json_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed47.json\\\", \\\"note\\\": \\\"False failure - completed but harvest missed result\\\"}}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.565, \\\"successes\\\": 113, \\\"total\\\": 200, \\\"json_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed47.json\\\", \\\"note\\\": \\\"False failure - completed but harvest missed result\\\"}}, \\\"eval-supp-goal-reconvla-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.835, \\\"successes\\\": 167, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}}, \\\"eval-supp-obj-k2mean-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.775, \\\"successes\\\": 155, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}}, \\\"eval-supp-obj-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.825, \\\"successes\\\": 165, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}}, \\\"eval-supp-obj-adapt-tau025-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.77, \\\"successes\\\": 154, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}}, \\\"eval-supp-obj-vla-only-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.755, \\\"successes\\\": 151, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20}}, \\\"eval-supp-goal-vla-only-s47-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.825, \\\"successes\\\": 165, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"output_file\\\": \\\"logs/eval_goal_vla_only_seed47.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 20, \\\"output_file\\\": \\\"logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.54, \\\"successes\\\": 108, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_samples\\\": 72507, \\\"K\\\": 10, \\\"obs_dim\\\": 2048, \\\"action_dim\\\": 6, \\\"h_eff\\\": 5}}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200}}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200, \\\"mean_uncertainty\\\": 0.1885, \\\"trigger_rate\\\": 0.2013, \\\"tau\\\": 0.25, \\\"total_steps\\\": 28599, \\\"crm_applied_steps\\\": 5758}}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.805, \\\"successes\\\": 161, \\\"total\\\": 200}}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.8, \\\"successes\\\": 160, \\\"total\\\": 200}}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.785, \\\"successes\\\": 157, \\\"total\\\": 200}}, \\\"train-crm-pi05-spatial-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.002887, \\\"best_epoch\\\": 50, \\\"final_train_loss\\\": 0.018836}}, \\\"train-crm-pi05-goal-k1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.003319, \\\"best_epoch\\\": 48, \\\"final_train_loss\\\": 0.018992}}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.56, \\\"successes\\\": 112, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.55, \\\"successes\\\": 110, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.585, \\\"successes\\\": 117, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"long\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 46, \\\"K\\\": 2, \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25}}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.077477, \\\"total_epochs\\\": 50, \\\"train_samples\\\": 74507, \\\"obs_dim\\\": 4096, \\\"params\\\": 908106, \\\"architecture\\\": \\\"MultiScaleCRM-K1\\\"}}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.765, \\\"successes\\\": 153, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb2-40593\\\", \\\"json_file\\\": \\\"eval_object_crm_obs_only_norm0.05_seed45.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-supp-obj-vla-only-s",
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

_source line 61_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e48caa97-41a5-4dd7-91b1-0a4b61dda19d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UZU3fz1q3VZ2iyvQJPDdr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16520,
      "cache_read_input_tokens": 52002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16520
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

_source line 62_

Let me check the scripts that build Table 1 to find which seeds were actually used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "3415f5ea-4081-47b2-91b2-f2016623a51a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UZU3fz1q3VZ2iyvQJPDdr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16520,
      "cache_read_input_tokens": 52002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16520
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01RVcCpjjZ954tnv3XMsm5mP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/scripts/ 2>/dev/null",
  "description": "List scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "487788c9-6250-4f20-ba14-6871fa997e4b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UZU3fz1q3VZ2iyvQJPDdr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16520,
      "cache_read_input_tokens": 52002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16520
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

_source line 64 · 2026-05-25T02:17:51.614Z_

<details><summary>↩ Tool result · `toolu_01RVcCpjjZ954tnv3XMsm5mP`</summary>

```text
parse_log_to_json.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "aa617445-5991-43ad-8714-911e7e70fe9d",
  "tool_use_result": {
    "stdout": "parse_log_to_json.py",
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

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_018Scbn9SsojcBsCdwXiJJSC`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8|Goal.*VLA|Object.*VLA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "output_mode": "files_with_matches",
  "glob": "*.tex",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "89070e7e-f8c2-4f46-acf3-4403e52c0faf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Kpyag1J5nEUqML29vA2mbd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 68522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2171
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

_source line 66 · 2026-05-25T02:17:55.506Z_

<details><summary>↩ Tool result · `toolu_018Scbn9SsojcBsCdwXiJJSC`</summary>

```text
Found 12 files
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/sections/discussion.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/dream_reports/dream_20260513T023849/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "08cbe83a-ad85-410b-8bb6-01711ceeb421",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "docs/paper/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/sections/introduction.tex",
      "artifacts/_project/paper/introduction_scenarioC.tex",
      "artifacts/_project/paper/introduction_scenarioC_607d8d.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/sections/discussion.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/dream_reports/dream_20260513T023849/median/paper.tex"
    ],
    "numFiles": 12
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Grep · `toolu_011CdKu4AEiMSbFtbX8Yq6FG`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": true,
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "567487a4-2467-4a5d-83d4-552bed236150",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019roFG5yWE2TpCVGsmZVTiA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 70693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 507
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

_source line 68 · 2026-05-25T02:17:58.626Z_

<details><summary>↩ Tool result · `toolu_011CdKu4AEiMSbFtbX8Yq6FG`</summary>

```text
41-\toprule
42-Method & $K$ & Spatial (\%) & Object (\%) & Goal (\%) & Long (\%) \\
43-\midrule
44:VLA-only & 1 & $78.7 \pm 0.3^{(3)}$ & $77.7 \pm 1.3^{(5)}$ & $83.7 \pm 1.3^{(3)}$ & $58.0 \pm 1.5^{(3)}$ \\
45:CRM always-on & 10 & $79.8 \pm 1.3^{(3)}$ & $76.5 \pm 2.3^{(3)}$ & $83.7 \pm 1.8^{(3)}$ & $55.8 \pm 1.2^{(3)}$ \\
46-$K{=}10$ argmin & 10 & $80.3 \pm 1.0^{(3)}$ & $77.3 \pm 1.5^{(3)}$ & $80.8 \pm 0.3^{(3)}$ & $56.5^{(1)}$ \\
47-$K{=}2$ mean & 2 & --- & $77.5 \pm 2.3^{(3)}$ & $83.0 \pm 2.2^{(3)}$ & $57.0^{(1)}$ \\
48-\midrule
49:ACR-VLA & 2 & $80.8 \pm 1.1^{(3)}$ & $77.8 \pm 2.1^{(5)}$ & $85.0 \pm 1.3^{(3)}$ & $57.7 \pm 1.5^{(3)}$ \\
50-\midrule
51-$\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\
52-$\Delta_{\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\
--
63-
64-[Omitted long context line]
65-
66:[Omitted long matching line]
67-
68-\paragraph{Statistical note.}
69-\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\Delta_{\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\,pp), confirming that gating prevents the degradation caused by unconditional correction.
--
80-
81-[Omitted long context line]
82-
83:[Omitted long matching line]
84-
85-\begin{figure}[t]
86-  \centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d7669391-7f52-43e7-8321-32cc0f13bbb1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "41-\\toprule\n42-Method & $K$ & Spatial (\\%) & Object (\\%) & Goal (\\%) & Long (\\%) \\\\\n43-\\midrule\n44:VLA-only & 1 & $78.7 \\pm 0.3^{(3)}$ & $77.7 \\pm 1.3^{(5)}$ & $83.7 \\pm 1.3^{(3)}$ & $58.0 \\pm 1.5^{(3)}$ \\\\\n45:CRM always-on & 10 & $79.8 \\pm 1.3^{(3)}$ & $76.5 \\pm 2.3^{(3)}$ & $83.7 \\pm 1.8^{(3)}$ & $55.8 \\pm 1.2^{(3)}$ \\\\\n46-$K{=}10$ argmin & 10 & $80.3 \\pm 1.0^{(3)}$ & $77.3 \\pm 1.5^{(3)}$ & $80.8 \\pm 0.3^{(3)}$ & $56.5^{(1)}$ \\\\\n47-$K{=}2$ mean & 2 & --- & $77.5 \\pm 2.3^{(3)}$ & $83.0 \\pm 2.2^{(3)}$ & $57.0^{(1)}$ \\\\\n48-\\midrule\n49:ACR-VLA & 2 & $80.8 \\pm 1.1^{(3)}$ & $77.8 \\pm 2.1^{(5)}$ & $85.0 \\pm 1.3^{(3)}$ & $57.7 \\pm 1.5^{(3)}$ \\\\\n50-\\midrule\n51-$\\Delta$ vs VLA-only & & $+2.1$ & $+0.1$ & $+1.3$ & $-0.3$ \\\\\n52-$\\Delta_{\\mathrm{CRM}}$ vs CRM & & $+1.0$ & $+1.3$ & $+1.3$ & $+1.9$ \\\\\n--\n63-\n64-[Omitted long context line]\n65-\n66:[Omitted long matching line]\n67-\n68-\\paragraph{Statistical note.}\n69-\\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\\Delta_{\\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\\,pp), confirming that gating prevents the degradation caused by unconditional correction.\n--\n80-\n81-[Omitted long context line]\n82-\n83:[Omitted long matching line]\n84-\n85-\\begin{figure}[t]\n86-  \\centering",
    "numLines": 28
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_019RuX4VGtwrTs8BJjYBGmrf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "offset": 60,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6926de80-8a80-4551-8786-1076671ca010",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YEb4ZmF1dUXcphJpGR1vAX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 71200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1356
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 70 · 2026-05-25T02:18:04.186Z_

<details><summary>↩ Tool result · `toolu_019RuX4VGtwrTs8BJjYBGmrf`</summary>

```text
60	  \caption{Success rates across five methods and four LIBERO suites. ACR-VLA (orange) matches or exceeds all baselines on every suite. CRM always-on (pink) degrades on Object and Long; $K{=}10$ argmin (blue) degrades on Goal. Error bars: $\pm$1 std over available seeds.}
61	  \label{fig:method_bar}
62	\end{figure}
63	
64	\looseness=-1 Table~\ref{tab:main} and Figure~\ref{fig:method_bar} report task success rates across all methods and suites. ACR-VLA's adaptive gate correctly modulates intervention intensity: on suites where the VLA shows high uncertainty (trigger rate ${>}$7\%), the gate fires and the CRM applies corrections ($+$2.1\,pp on Spatial, $+$1.3\,pp on Goal, 3 seeds each). On suites where the VLA is already confident (trigger rate ${<}$5\%), the gate rarely fires and the output matches baseline: Object ($\Delta{=}{+}0.1$\,pp, 5 seeds) and Long ($\Delta{=}{-}0.3$\,pp, 3 seeds). This avoids the degradation caused by unconditional correction ($-$1.2\,pp Object, $-$2.2\,pp Long).
65	
66	\looseness=-2 Unconditional correction is unstable across suites. \emph{CRM always-on} ($\varepsilon{=}0.05$) applies correction at every step: $-$2.2\,pp on Long ($55.8 \pm 1.2$\%, 3 seeds), $-$1.2\,pp on Object ($76.5 \pm 2.3$\%, 3 seeds), $\Delta{\approx}0$ on Goal ($83.7 \pm 1.8$\%, 3 seeds), and $+$1.1\,pp on Spatial. Without gating, the CRM hurts on two suites while providing inconsistent benefit elsewhere. \emph{$K{=}10$ argmin} invests $10{\times}$ the VLA forward passes but hurts on Goal ($-$2.9\,pp, $80.8 \pm 0.3$\%, 3 seeds). Selection without correction is insufficient. \emph{$K{=}2$ mean} offers no learned correction mechanism ($-$0.7\,pp Goal, $-$1.0\,pp Long; Long is single-seed preliminary), isolating that multi-sampling alone is not sufficient.
67	
68	\paragraph{Statistical note.}
69	\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\Delta_{\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\,pp), confirming that gating prevents the degradation caused by unconditional correction.
70	
71	\subsection{Why Gating Is Necessary}
72	\label{sec:failure_modes}
73	
74	\begin{figure}[t]
75	  \centering
76	  \includegraphics[width=0.85\linewidth]{fig_trigger_scatter.pdf}
77	  \caption{Trigger rate vs.\ improvement over VLA-only. Suites where the gate fires on ${>}$7\% of steps (Spatial, Goal) see improvement; suites where the VLA is already confident (Object, Long, trigger ${<}$5\%) preserve baseline. The gate correctly partitions correction budget by per-step uncertainty.}
78	  \label{fig:trigger_scatter}
79	\end{figure}
80	
81	\looseness=-1 The main results reveal a core finding: \emph{unconditional correction is unstable across suites}. CRM always-on applies the same learned residual to every step, including the ${\sim}$80--90\% where the VLA is already confident. This produces inconsistent effects: $+$1.1\,pp on Spatial, $\Delta{\approx}0$ on Goal, $-$1.2\,pp on Object (3 seeds), and $-$2.2\,pp on Long (3 seeds). The Object and Long degradation shows that corrections on already-confident steps are harmful noise (Figure~\ref{fig:trigger_scatter}).
82	
83	\looseness=-1 ACR-VLA's adaptive gate resolves this instability. On Object, where the VLA is already confident, the gate triggers on only 3.5\% of steps; the CRM barely fires, and the output matches baseline ($77.8$\%, $\Delta{=}{+}0.1$\,pp, 5 seeds). This is the correct behavior: the gate identifies that Object needs no correction and avoids the $-$1.2\,pp harm of unconditional correction. On Spatial and Goal, where higher uncertainty triggers correction on 7--20\% of steps, the CRM provides targeted improvement ($+$2.1\,pp and $+$1.3\,pp respectively). On Long, the gate triggers on ${\sim}$4\% of steps; ACR-VLA preserves baseline ($57.7 \pm 1.5$\%, $\Delta{=}{-}0.3$\,pp, 3 seeds) while CRM always-on degrades by $-$2.2\,pp.
84	
85	\begin{figure}[t]
86	  \centering
87	  \includegraphics[width=\linewidth]{fig_tau_sweep.pdf}
88	  \caption{Threshold $\tau$ controls trigger rate, which controls improvement: inverted-U on both Goal and Spatial (seed 42, $\varepsilon{=}0.2$). Low $\tau$ overcorrects (${>}$70\% trigger); high $\tau$ disables correction. The optimal region $\tau \in [0.20, 0.25]$ is consistent across suites. Labels show trigger rate at each $\tau$. See Appendix~\ref{sec:tau_sweep} for details.}
89	  \label{fig:tau_sweep}
90	\end{figure}
91	
92	The $K{=}10$ argmin baseline provides a complementary negative result: spending $10{\times}$ the inference budget on selection-only hurts on Goal ($-$2.9\,pp, 3 seeds) and Long ($-$1.5\,pp, 1 seed available). Multi-sample selection refines the action but cannot fix systematic errors in the VLA's output distribution. Learned correction is necessary, but only when gated.
93	
94	\paragraph{$K{=}1$ ablation.}
95	To isolate the contribution of multi-sample centering, we evaluate $K{=}1$ adaptive CRM (single sample, same gating and correction) on Spatial: SR${=}79.5$\% vs.\ $K{=}2$ adaptive SR${=}80.8$\% ($\Delta{=}{+}1.3$\,pp). The gap quantifies the benefit of argmin-to-centroid selection before correction.
96	
97	\subsection{Efficiency}
98	\label{sec:magnitude_results}
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "220717d5-690d-476f-8b0e-e89baca79985",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
      "content": "  \\caption{Success rates across five methods and four LIBERO suites. ACR-VLA (orange) matches or exceeds all baselines on every suite. CRM always-on (pink) degrades on Object and Long; $K{=}10$ argmin (blue) degrades on Goal. Error bars: $\\pm$1 std over available seeds.}\n  \\label{fig:method_bar}\n\\end{figure}\n\n\\looseness=-1 Table~\\ref{tab:main} and Figure~\\ref{fig:method_bar} report task success rates across all methods and suites. ACR-VLA's adaptive gate correctly modulates intervention intensity: on suites where the VLA shows high uncertainty (trigger rate ${>}$7\\%), the gate fires and the CRM applies corrections ($+$2.1\\,pp on Spatial, $+$1.3\\,pp on Goal, 3 seeds each). On suites where the VLA is already confident (trigger rate ${<}$5\\%), the gate rarely fires and the output matches baseline: Object ($\\Delta{=}{+}0.1$\\,pp, 5 seeds) and Long ($\\Delta{=}{-}0.3$\\,pp, 3 seeds). This avoids the degradation caused by unconditional correction ($-$1.2\\,pp Object, $-$2.2\\,pp Long).\n\n\\looseness=-2 Unconditional correction is unstable across suites. \\emph{CRM always-on} ($\\varepsilon{=}0.05$) applies correction at every step: $-$2.2\\,pp on Long ($55.8 \\pm 1.2$\\%, 3 seeds), $-$1.2\\,pp on Object ($76.5 \\pm 2.3$\\%, 3 seeds), $\\Delta{\\approx}0$ on Goal ($83.7 \\pm 1.8$\\%, 3 seeds), and $+$1.1\\,pp on Spatial. Without gating, the CRM hurts on two suites while providing inconsistent benefit elsewhere. \\emph{$K{=}10$ argmin} invests $10{\\times}$ the VLA forward passes but hurts on Goal ($-$2.9\\,pp, $80.8 \\pm 0.3$\\%, 3 seeds). Selection without correction is insufficient. \\emph{$K{=}2$ mean} offers no learned correction mechanism ($-$0.7\\,pp Goal, $-$1.0\\,pp Long; Long is single-seed preliminary), isolating that multi-sampling alone is not sufficient.\n\n\\paragraph{Statistical note.}\n\\looseness=-1 Paired differences (Adaptive$-$VLA) are directionally consistent (positive on 3 of 4 suites) but do not reach $p < 0.05$ with $n{=}$5--6 matched seeds. The stronger claim is Adaptive vs.\\ CRM always-on: ACR-VLA exceeds unconditional correction on all four suites ($\\Delta_{\\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\\,pp), confirming that gating prevents the degradation caused by unconditional correction.\n\n\\subsection{Why Gating Is Necessary}\n\\label{sec:failure_modes}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=0.85\\linewidth]{fig_trigger_scatter.pdf}\n  \\caption{Trigger rate vs.\\ improvement over VLA-only. Suites where the gate fires on ${>}$7\\% of steps (Spatial, Goal) see improvement; suites where the VLA is already confident (Object, Long, trigger ${<}$5\\%) preserve baseline. The gate correctly partitions correction budget by per-step uncertainty.}\n  \\label{fig:trigger_scatter}\n\\end{figure}\n\n\\looseness=-1 The main results reveal a core finding: \\emph{unconditional correction is unstable across suites}. CRM always-on applies the same learned residual to every step, including the ${\\sim}$80--90\\% where the VLA is already confident. This produces inconsistent effects: $+$1.1\\,pp on Spatial, $\\Delta{\\approx}0$ on Goal, $-$1.2\\,pp on Object (3 seeds), and $-$2.2\\,pp on Long (3 seeds). The Object and Long degradation shows that corrections on already-confident steps are harmful noise (Figure~\\ref{fig:trigger_scatter}).\n\n\\looseness=-1 ACR-VLA's adaptive gate resolves this instability. On Object, where the VLA is already confident, the gate triggers on only 3.5\\% of steps; the CRM barely fires, and the output matches baseline ($77.8$\\%, $\\Delta{=}{+}0.1$\\,pp, 5 seeds). This is the correct behavior: the gate identifies that Object needs no correction and avoids the $-$1.2\\,pp harm of unconditional correction. On Spatial and Goal, where higher uncertainty triggers correction on 7--20\\% of steps, the CRM provides targeted improvement ($+$2.1\\,pp and $+$1.3\\,pp respectively). On Long, the gate triggers on ${\\sim}$4\\% of steps; ACR-VLA preserves baseline ($57.7 \\pm 1.5$\\%, $\\Delta{=}{-}0.3$\\,pp, 3 seeds) while CRM always-on degrades by $-$2.2\\,pp.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\linewidth]{fig_tau_sweep.pdf}\n  \\caption{Threshold $\\tau$ controls trigger rate, which controls improvement: inverted-U on both Goal and Spatial (seed 42, $\\varepsilon{=}0.2$). Low $\\tau$ overcorrects (${>}$70\\% trigger); high $\\tau$ disables correction. The optimal region $\\tau \\in [0.20, 0.25]$ is consistent across suites. Labels show trigger rate at each $\\tau$. See Appendix~\\ref{sec:tau_sweep} for details.}\n  \\label{fig:tau_sweep}\n\\end{figure}\n\nThe $K{=}10$ argmin baseline provides a complementary negative result: spending $10{\\times}$ the inference budget on selection-only hurts on Goal ($-$2.9\\,pp, 3 seeds) and Long ($-$1.5\\,pp, 1 seed available). Multi-sample selection refines the action but cannot fix systematic errors in the VLA's output distribution. Learned correction is necessary, but only when gated.\n\n\\paragraph{$K{=}1$ ablation.}\nTo isolate the contribution of multi-sample centering, we evaluate $K{=}1$ adaptive CRM (single sample, same gating and correction) on Spatial: SR${=}79.5$\\% vs.\\ $K{=}2$ adaptive SR${=}80.8$\\% ($\\Delta{=}{+}1.3$\\,pp). The gap quantifies the benefit of argmin-to-centroid selection before correction.\n\n\\subsection{Efficiency}\n\\label{sec:magnitude_results}\n",
      "numLines": 40,
      "startLine": 60,
      "totalLines": 126
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "7ea4619e-0289-421f-abf8-6e2aacc86022",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014JLAziFiMgdCts1oW4tQzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 72556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2681
      },
      "output_tokens": 84,
      "service_tier": "standard",
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

_source line 72_

<details open><summary>🔧 Tool call — Grep · `toolu_01TZuMVonQ2pjkLG8RLJ5B8N`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8|seed.*goal|seed.*object|GOAL_SEEDS|OBJECT_SEEDS",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "output_mode": "files_with_matches",
  "glob": "*.py",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e9c4cc49-ac85-4b3e-bcee-dfcbd3199856",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014JLAziFiMgdCts1oW4tQzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 72556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2681
      },
      "output_tokens": 84,
      "service_tier": "standard",
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

_source line 73 · 2026-05-25T02:18:23.414Z_

<details><summary>↩ Tool result · `toolu_01TZuMVonQ2pjkLG8RLJ5B8N`</summary>

```text
Found 3 files
artifacts/_project/intermediate/magnitude_curve.py
artifacts/figures/magnitude_curve.py
artifacts/analysis/seed43_fisher_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "04ed352e-517f-437c-81fd-e4a87934b9a0",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/intermediate/magnitude_curve.py",
      "artifacts/figures/magnitude_curve.py",
      "artifacts/analysis/seed43_fisher_analysis.py"
    ],
    "numFiles": 3
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01ATXxnXJcTkitKaTt2FySWi`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null | head -50",
  "description": "List artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "dc0d12c2-bc25-4653-8577-7b92fede48cb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P4JLXXtjqZ71fuHMF67RJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 75237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 557
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

_source line 75 · 2026-05-25T02:18:27.515Z_

<details><summary>↩ Tool result · `toolu_01ATXxnXJcTkitKaTt2FySWi`</summary>

```text
3dir_spatial_s42_results.md
__pycache__
_project
ablation_eval_commands.md
adaptive_k_design.md
adaptive_k_eval_prep.md
analysis
analysis-train-crm-unified-4suite-r6.md
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_rank_deficient
analysis_rank_deficient.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
batched_inference_feasibility_report.md
benchmark_data_audit.md
benchmark_survey.md
citation_attribution_audit.md
citation_audit_report.md
competitive_analysis_20260515.md
competitor_analysis.md
conclusion_draft.md
contribution_list.md
corl_paper_outline.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
crm_eval_partial_results.md
crm_eval_results_harvest.md
crm_k1_model.py
d139_status_scan.md
deploy_3dir_spatial_seed42.md
deploy_adaptive_k_eval.sh
deploy_pi05_crm_eval.sh
deploy_smolvla_crm_eval.sh
diag-eval-supp-goal-reconvla-s45.md
diag-eval-v6-batch-failure.md
diag_bjb1_18228.md
diag_bjb2_28827.md
diag_cqa1_32758_failures_20260524.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_bjb1_18228_failure.md
diagnose_bjb1_32546_batch_failure.md
diagnose_bjb2_failures_20260523.md
diagnose_crm_long_seed45.md
diagnose_crm_spatial_timeout.md
diagnose_default_seed46.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "35b1a01b-460d-46dc-9a5d-c811a6a99ee1",
  "tool_use_result": {
    "stdout": "3dir_spatial_s42_results.md\n__pycache__\n_project\nablation_eval_commands.md\nadaptive_k_design.md\nadaptive_k_eval_prep.md\nanalysis\nanalysis-train-crm-unified-4suite-r6.md\nanalysis_magnitude_sweep.py\nanalysis_object_benchmark.py\nanalysis_rank_deficient\nanalysis_rank_deficient.py\nanalysis_spatial_final.py\nargmin_seed44_r2_results.json\nbatched_inference_feasibility_report.md\nbenchmark_data_audit.md\nbenchmark_survey.md\ncitation_attribution_audit.md\ncitation_audit_report.md\ncompetitive_analysis_20260515.md\ncompetitor_analysis.md\nconclusion_draft.md\ncontribution_list.md\ncorl_paper_outline.md\ncorrection_degradation_literature.md\ncrm-train-v2-k5\ncrm_bug_audit.md\ncrm_eval_partial_results.md\ncrm_eval_results_harvest.md\ncrm_k1_model.py\nd139_status_scan.md\ndeploy_3dir_spatial_seed42.md\ndeploy_adaptive_k_eval.sh\ndeploy_pi05_crm_eval.sh\ndeploy_smolvla_crm_eval.sh\ndiag-eval-supp-goal-reconvla-s45.md\ndiag-eval-v6-batch-failure.md\ndiag_bjb1_18228.md\ndiag_bjb2_28827.md\ndiag_cqa1_32758_failures_20260524.md\ndiag_plan_a_spatial_seed42_43.md\ndiagnose-eval-adaptive-k-spatial-p50-seed44.md\ndiagnose-norm02-seed44-r2.md\ndiagnose-random-selection-seed46-r2.md\ndiagnose_bjb1_18228_failure.md\ndiagnose_bjb1_32546_batch_failure.md\ndiagnose_bjb2_failures_20260523.md\ndiagnose_crm_long_seed45.md\ndiagnose_crm_spatial_timeout.md\ndiagnose_default_seed46.md",
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

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gn2Pu4i7opVDyihHdyqCMg`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -iE \"table|main_result|aggregate\" | head -20",
  "description": "Find table-building scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "0e53ba8c-765c-432d-8241-495de63a6b61",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VcXrd8JWuVXHcSuBsejvS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 75794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 868
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

_source line 77 · 2026-05-25T02:18:31.239Z_

<details><summary>↩ Tool result · `toolu_01Gn2Pu4i7opVDyihHdyqCMg`</summary>

```text
results_tables.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b3cdf960-0f1e-4a35-bb37-72095cc25231",
  "tool_use_result": {
    "stdout": "results_tables.md",
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

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_013Hz5G333oMzSK69F6wJQGW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/results_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "cb86c9f6-6355-43b8-9771-e641650b9a38",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019JiwbEnq4AcL2u3PEzeW3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 76662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 184
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 79 · 2026-05-25T02:18:33.765Z_

<details><summary>↩ Tool result · `toolu_013Hz5G333oMzSK69F6wJQGW`</summary>

```text
1	# ACR-VLA Experiment Results Tables
2	
3	> Generated: 2026-05-15 | All numbers from registry. Percentages = success rate (%).
4	
5	---
6	
7	## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
8	
9	| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
10	|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
11	| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |
12	| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |
13	| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |
14	| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |
15	| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |
16	| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |
17	
18	**Key findings:**
19	- obs_only leads by +7pp over all baselines
20	- All methods cluster on chocolate_pudding and bbq_sauce (easiest tasks)
21	- alphabet_soup is universally 0% across all methods
22	
23	---
24	
25	## Table 2: Spatial Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)
26	
27	Task abbreviations: T0=between_plate_and_ramekin, T1=next_to_ramekin, T2=from_table_center, T3=on_cookie_box, T4=in_top_drawer, T5=on_ramekin, T6=next_to_cookie_box, T7=on_stove, T8=next_to_plate, T9=on_wooden_cabinet
28	
29	| Method | Exp ID | **Overall SR** | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
30	|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
31	| **obs_only (norm=0.1)** | `eval-acr-spatial-v4-obs-only-r3` | **35%** | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |
32	| **perdof (norm=0.1)** | `eval-acr-spatial-v4-small-r2` | **35%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |
33	| argmin (K=10) | `eval-argmin-only-spatial-r2` | **34%** | 60 | 100 | 0 | 30 | 10 | 10 | 90 | 0 | 30 | 10 |
34	| scalar (norm=0.1) | `eval-acr-spatial-v4-scalar-r2` | **32%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 0 | 10 | 10 |
35	| VLA-mean (K=10) | `eval-vla-mean-spatial` | **32%** | 70 | 100 | 0 | 30 | 0 | 0 | 80 | 0 | 30 | 10 |
36	| VLA-only (K=1) | `eval-spatial-v7-full` | **30%** | 60 | 100 | 0 | 20 | 0 | 0 | 90 | 0 | 30 | 0 |
37	
38	**Key findings:**
39	- CRM methods (obs_only, perdof) lead by +1pp over argmin, +5pp over VLA-only
40	- T1 (next_to_ramekin) is saturated at 100% for all methods
41	- T2 (from_table_center), T5 (on_ramekin), T7 (on_stove), T9 (on_wooden_cabinet) are near-zero for all methods
42	
43	---
44	
45	## Table 3: Magnitude Sweep — Spatial Benchmark (perdof vs obs_only, seed=42)
46	
47	| norm | perdof SR | perdof exp_id | obs_only SR | obs_only exp_id | gap (obs−perdof) |
48	|:----:|:---------:|---------------|:-----------:|-----------------|:----------------:|
49	| 0.03 | 30% | `eval-mag-perdof-norm003` | **7/10 partial** ¹ | `eval-mag-obsonly-norm003-b2` | — |
50	| 0.05 | 31% | `eval-mag-perdof-norm005` | 35% | `eval-mag-obsonly-norm005` | +4pp |
51	| 0.1 | 35% | `eval-acr-spatial-v4-small-r2` | 35% | `eval-acr-spatial-v4-obs-only-r3` | 0pp |
52	| 0.2 | **6/10 partial** ² | `eval-mag-perdof-norm02` | 35% | `eval-mag-obsonly-norm02` | — |
53	| 0.3 | 26% | `eval-mag-perdof-norm03` | 36% | `eval-mag-obsonly-norm03-r2` | +10pp |
54	
55	¹ obs_only norm=0.03 (`eval-mag-obsonly-norm003-b2`): RUNNING, 7/10 tasks done. Partial per-task:
56	  T0=90, T1=100, T2=0, T3=30, T4=10, T5=0, T6=80. Running avg (7-task) ≈ 44%.
57	
58	² perdof norm=0.2 (`eval-mag-perdof-norm02`): killed (SIGTERM), 6/10 tasks partial:
59	  T0=60, T1=90, T2=0, T3=20, T4=0, T5=0. Running avg (6-task) ≈ 28%.
60	
61	### Per-task breakdown — Completed magnitude experiments
62	
63	**perdof per-task (spatial):**
64	
65	| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
66	|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
67	| 0.03 | 60 | 100 | 0 | 30 | 10 | 0 | 80 | 0 | 20 | 0 |
68	| 0.05 | 50 | 100 | 0 | 30 | 0 | 0 | 100 | 0 | 30 | 0 |
69	| 0.1 | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |
70	| 0.3 | 70 | 50 | 10 | 10 | 0 | 0 | 90 | 10 | 20 | 0 |
71	
72	**obs_only per-task (spatial):**
73	
74	| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
75	|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
76	| 0.05 | 80 | 90 | 0 | 40 | 10 | 0 | 80 | 0 | 50 | 0 |
77	| 0.1 | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |
78	| 0.2 | 90 | 100 | 0 | 30 | 10 | 0 | 90 | 0 | 30 | 0 |
79	| 0.3 | 90 | 100 | 0 | 30 | 10 | 0 | 100 | 0 | 30 | 0 |
80	
81	---
82	
83	## Table 4: Object Benchmark — Magnitude Results (mixed status)
84	
85	### FINAL (seed=42, 10/10 tasks)
86	
87	| Method | norm | Overall SR | Exp ID |
88	|--------|:----:|:---------:|--------|
89	| obs_only | 0.1 | **19%** | `eval-acr-object-v4-obs-only` |
90	| obs_only | 0.2 | **22%** | `eval-acr-object-obs-only-norm02` |
91	
92	obs_only norm=0.2 per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30, bbq_sauce=40, ketchup=20, tomato_sauce=10, butter=10, milk=20, chocolate_pudding=60, orange_juice=30
93	
94	### IN PROGRESS (seed=42, RUNNING)
95	
96	| Method | norm | Exp ID | Tasks Done | Partial per-task |
97	|--------|:----:|--------|:----------:|------------------|
98	| obs_only | 0.03 | `eval-mag-obsonly-norm003-object` | 2/10 | alphabet_soup=0, cream_cheese=20 |
99	| obs_only | 0.05 | `eval-mag-obsonly-norm005-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |
100	| obs_only | 0.3 | `eval-mag-obsonly-norm03-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |
101	| perdof | 0.03 | `eval-mag-perdof-norm003-object` | 1/10 | alphabet_soup=0 |
102	| perdof | 0.05 | `eval-mag-perdof-norm005-object` | 1/10 | alphabet_soup=0 |
103	| perdof | 0.2 | `eval-mag-perdof-norm02-object` | 2/10 | alphabet_soup=0, cream_cheese=10 |
104	| perdof | 0.3 | `eval-mag-perdof-norm03-object-r3` | 0/10 | — |
105	
106	---
107	
108	## Table 5: Seed=43 Object Benchmark — Progress Tracker
109	
110	| Method | Exp ID | Status | Tasks Done | Partial Per-task SR |
111	|--------|--------|:------:|:----------:|---------------------|
112	| VLA-only (K=1) | `eval-vla-only-object-seed43` | **DONE** | 10/10 | **Overall: 12%** — alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0, butter=0, milk=10, chocolate_pudding=40, orange_juice=20 |
113	| obs_only (norm=0.1) | `eval-obs-only-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0 |
114	| argmin (K=10) | `eval-argmin-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=20, ketchup=10, tomato_sauce=10 |
115	| perdof (norm=0.1) | `eval-perdof-object-seed43` | RUNNING | 4/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=30 |
116	| VLA-mean (K=10) | `eval-vla-mean-object-seed43` | RUNNING | 3/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20 |
117	| scalar (norm=0.1) | `eval-scalar-object-seed43` | RUNNING | 2/10 | alphabet_soup=0, cream_cheese=0 |
118	
119	**Notes:**
120	- VLA-only seed=43 (12%) matches seed=42 (12%) exactly — baseline is consistent across seeds
121	- All running experiments last confirmed alive at 2026-05-16T03:55:00
122	
123	---
124	
125	## Cross-reference: Registry ID → Method Mapping
126	
127	| Exp ID | Method | Benchmark | Seed | Norm | Status |
128	|--------|--------|-----------|:----:|:----:|:------:|
129	| `eval-acr-object-v4-obs-only` | obs_only | object | 42 | 0.1 | DONE |
130	| `eval-reconvla-object` | argmin (ReconVLA) | object | 42 | — | DONE |
131	| `eval-vla-only-object` | VLA-only K=1 | object | 42 | — | DONE |
132	| `eval-vla-mean-object` | VLA-mean K=10 | object | 42 | — | DONE |
133	| `eval-acr-object-v4-perdof` | perdof | object | 42 | 0.1 | DONE |
134	| `eval-acr-object-v4-scalar` | scalar | object | 42 | 0.1 | DONE |
135	| `eval-acr-object-obs-only-norm02` | obs_only | object | 42 | 0.2 | DONE |
136	| `eval-acr-spatial-v4-obs-only-r3` | obs_only | spatial | 42 | 0.1 | DONE |
137	| `eval-acr-spatial-v4-small-r2` | perdof | spatial | 42 | 0.1 | DONE |
138	| `eval-argmin-only-spatial-r2` | argmin (ReconVLA) | spatial | 42 | — | DONE |
139	| `eval-acr-spatial-v4-scalar-r2` | scalar | spatial | 42 | 0.1 | DONE |
140	| `eval-vla-mean-spatial` | VLA-mean K=10 | spatial | 42 | — | DONE |
141	| `eval-spatial-v7-full` | VLA-only K=1 | spatial | 42 | — | DONE |
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e8f98aab-6b36-43e0-8aff-cceb0b558f9c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/results_tables.md",
      "content": "# ACR-VLA Experiment Results Tables\n\n> Generated: 2026-05-15 | All numbers from registry. Percentages = success rate (%).\n\n---\n\n## Table 1: Object Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)\n\n| Method | Exp ID | **Overall SR** | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |\n|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n| **obs_only (norm=0.1)** | `eval-acr-object-v4-obs-only` | **19%** | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 |\n| argmin (K=10) | `eval-reconvla-object` | **12%** | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 |\n| VLA-only (K=1) | `eval-vla-only-object` | **12%** | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 |\n| VLA-mean (K=10) | `eval-vla-mean-object` | **12%** | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 |\n| perdof (norm=0.1) | `eval-acr-object-v4-perdof` | **11%** | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 |\n| scalar (norm=0.1) | `eval-acr-object-v4-scalar` | **9%** | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 |\n\n**Key findings:**\n- obs_only leads by +7pp over all baselines\n- All methods cluster on chocolate_pudding and bbq_sauce (easiest tasks)\n- alphabet_soup is universally 0% across all methods\n\n---\n\n## Table 2: Spatial Benchmark 6-way Comparison (seed=42, all FINAL 10/10 tasks)\n\nTask abbreviations: T0=between_plate_and_ramekin, T1=next_to_ramekin, T2=from_table_center, T3=on_cookie_box, T4=in_top_drawer, T5=on_ramekin, T6=next_to_cookie_box, T7=on_stove, T8=next_to_plate, T9=on_wooden_cabinet\n\n| Method | Exp ID | **Overall SR** | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |\n|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n| **obs_only (norm=0.1)** | `eval-acr-spatial-v4-obs-only-r3` | **35%** | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |\n| **perdof (norm=0.1)** | `eval-acr-spatial-v4-small-r2` | **35%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |\n| argmin (K=10) | `eval-argmin-only-spatial-r2` | **34%** | 60 | 100 | 0 | 30 | 10 | 10 | 90 | 0 | 30 | 10 |\n| scalar (norm=0.1) | `eval-acr-spatial-v4-scalar-r2` | **32%** | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 0 | 10 | 10 |\n| VLA-mean (K=10) | `eval-vla-mean-spatial` | **32%** | 70 | 100 | 0 | 30 | 0 | 0 | 80 | 0 | 30 | 10 |\n| VLA-only (K=1) | `eval-spatial-v7-full` | **30%** | 60 | 100 | 0 | 20 | 0 | 0 | 90 | 0 | 30 | 0 |\n\n**Key findings:**\n- CRM methods (obs_only, perdof) lead by +1pp over argmin, +5pp over VLA-only\n- T1 (next_to_ramekin) is saturated at 100% for all methods\n- T2 (from_table_center), T5 (on_ramekin), T7 (on_stove), T9 (on_wooden_cabinet) are near-zero for all methods\n\n---\n\n## Table 3: Magnitude Sweep — Spatial Benchmark (perdof vs obs_only, seed=42)\n\n| norm | perdof SR | perdof exp_id | obs_only SR | obs_only exp_id | gap (obs−perdof) |\n|:----:|:---------:|---------------|:-----------:|-----------------|:----------------:|\n| 0.03 | 30% | `eval-mag-perdof-norm003` | **7/10 partial** ¹ | `eval-mag-obsonly-norm003-b2` | — |\n| 0.05 | 31% | `eval-mag-perdof-norm005` | 35% | `eval-mag-obsonly-norm005` | +4pp |\n| 0.1 | 35% | `eval-acr-spatial-v4-small-r2` | 35% | `eval-acr-spatial-v4-obs-only-r3` | 0pp |\n| 0.2 | **6/10 partial** ² | `eval-mag-perdof-norm02` | 35% | `eval-mag-obsonly-norm02` | — |\n| 0.3 | 26% | `eval-mag-perdof-norm03` | 36% | `eval-mag-obsonly-norm03-r2` | +10pp |\n\n¹ obs_only norm=0.03 (`eval-mag-obsonly-norm003-b2`): RUNNING, 7/10 tasks done. Partial per-task:\n  T0=90, T1=100, T2=0, T3=30, T4=10, T5=0, T6=80. Running avg (7-task) ≈ 44%.\n\n² perdof norm=0.2 (`eval-mag-perdof-norm02`): killed (SIGTERM), 6/10 tasks partial:\n  T0=60, T1=90, T2=0, T3=20, T4=0, T5=0. Running avg (6-task) ≈ 28%.\n\n### Per-task breakdown — Completed magnitude experiments\n\n**perdof per-task (spatial):**\n\n| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |\n|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n| 0.03 | 60 | 100 | 0 | 30 | 10 | 0 | 80 | 0 | 20 | 0 |\n| 0.05 | 50 | 100 | 0 | 30 | 0 | 0 | 100 | 0 | 30 | 0 |\n| 0.1 | 60 | 100 | 10 | 40 | 0 | 0 | 90 | 10 | 40 | 0 |\n| 0.3 | 70 | 50 | 10 | 10 | 0 | 0 | 90 | 10 | 20 | 0 |\n\n**obs_only per-task (spatial):**\n\n| norm | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |\n|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n| 0.05 | 80 | 90 | 0 | 40 | 10 | 0 | 80 | 0 | 50 | 0 |\n| 0.1 | 90 | 100 | 0 | 40 | 10 | 0 | 90 | 0 | 20 | 0 |\n| 0.2 | 90 | 100 | 0 | 30 | 10 | 0 | 90 | 0 | 30 | 0 |\n| 0.3 | 90 | 100 | 0 | 30 | 10 | 0 | 100 | 0 | 30 | 0 |\n\n---\n\n## Table 4: Object Benchmark — Magnitude Results (mixed status)\n\n### FINAL (seed=42, 10/10 tasks)\n\n| Method | norm | Overall SR | Exp ID |\n|--------|:----:|:---------:|--------|\n| obs_only | 0.1 | **19%** | `eval-acr-object-v4-obs-only` |\n| obs_only | 0.2 | **22%** | `eval-acr-object-obs-only-norm02` |\n\nobs_only norm=0.2 per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30, bbq_sauce=40, ketchup=20, tomato_sauce=10, butter=10, milk=20, chocolate_pudding=60, orange_juice=30\n\n### IN PROGRESS (seed=42, RUNNING)\n\n| Method | norm | Exp ID | Tasks Done | Partial per-task |\n|--------|:----:|--------|:----------:|------------------|\n| obs_only | 0.03 | `eval-mag-obsonly-norm003-object` | 2/10 | alphabet_soup=0, cream_cheese=20 |\n| obs_only | 0.05 | `eval-mag-obsonly-norm005-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |\n| obs_only | 0.3 | `eval-mag-obsonly-norm03-object` | 2/10 | alphabet_soup=0, cream_cheese=0 |\n| perdof | 0.03 | `eval-mag-perdof-norm003-object` | 1/10 | alphabet_soup=0 |\n| perdof | 0.05 | `eval-mag-perdof-norm005-object` | 1/10 | alphabet_soup=0 |\n| perdof | 0.2 | `eval-mag-perdof-norm02-object` | 2/10 | alphabet_soup=0, cream_cheese=10 |\n| perdof | 0.3 | `eval-mag-perdof-norm03-object-r3` | 0/10 | — |\n\n---\n\n## Table 5: Seed=43 Object Benchmark — Progress Tracker\n\n| Method | Exp ID | Status | Tasks Done | Partial Per-task SR |\n|--------|--------|:------:|:----------:|---------------------|\n| VLA-only (K=1) | `eval-vla-only-object-seed43` | **DONE** | 10/10 | **Overall: 12%** — alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0, butter=0, milk=10, chocolate_pudding=40, orange_juice=20 |\n| obs_only (norm=0.1) | `eval-obs-only-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=10, salad_dressing=10, bbq_sauce=30, ketchup=0, tomato_sauce=0 |\n| argmin (K=10) | `eval-argmin-object-seed43` | RUNNING | 6/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=20, ketchup=10, tomato_sauce=10 |\n| perdof (norm=0.1) | `eval-perdof-object-seed43` | RUNNING | 4/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20, bbq_sauce=30 |\n| VLA-mean (K=10) | `eval-vla-mean-object-seed43` | RUNNING | 3/10 | alphabet_soup=0, cream_cheese=0, salad_dressing=20 |\n| scalar (norm=0.1) | `eval-scalar-object-seed43` | RUNNING | 2/10 | alphabet_soup=0, cream_cheese=0 |\n\n**Notes:**\n- VLA-only seed=43 (12%) matches seed=42 (12%) exactly — baseline is consistent across seeds\n- All running experiments last confirmed alive at 2026-05-16T03:55:00\n\n---\n\n## Cross-reference: Registry ID → Method Mapping\n\n| Exp ID | Method | Benchmark | Seed | Norm | Status |\n|--------|--------|-----------|:----:|:----:|:------:|\n| `eval-acr-object-v4-obs-only` | obs_only | object | 42 | 0.1 | DONE |\n| `eval-reconvla-object` | argmin (ReconVLA) | object | 42 | — | DONE |\n| `eval-vla-only-object` | VLA-only K=1 | object | 42 | — | DONE |\n| `eval-vla-mean-object` | VLA-mean K=10 | object | 42 | — | DONE |\n| `eval-acr-object-v4-perdof` | perdof | object | 42 | 0.1 | DONE |\n| `eval-acr-object-v4-scalar` | scalar | object | 42 | 0.1 | DONE |\n| `eval-acr-object-obs-only-norm02` | obs_only | object | 42 | 0.2 | DONE |\n| `eval-acr-spatial-v4-obs-only-r3` | obs_only | spatial | 42 | 0.1 | DONE |\n| `eval-acr-spatial-v4-small-r2` | perdof | spatial | 42 | 0.1 | DONE |\n| `eval-argmin-only-spatial-r2` | argmin (ReconVLA) | spatial | 42 | — | DONE |\n| `eval-acr-spatial-v4-scalar-r2` | scalar | spatial | 42 | 0.1 | DONE |\n| `eval-vla-mean-spatial` | VLA-mean K=10 | spatial | 42 | — | DONE |\n| `eval-spatial-v7-full` | VLA-only K=1 | spatial | 42 | — | DONE |\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "bd4b6a45-9312-4eb5-a2c0-550bf505d14d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FDrsSHWK9ss785ji8X72A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 76846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5334
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01991A9gUtu5H7C76C4XxTrL`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -iE \"main_table|aggregate|seed|table1|table_1\" | head -20",
  "description": "Find main table references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "40e50964-5754-4b05-bcbb-feb1df847afc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FDrsSHWK9ss785ji8X72A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 76846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5334
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 82 · 2026-05-25T02:18:40.431Z_

<details><summary>↩ Tool result · `toolu_01991A9gUtu5H7C76C4XxTrL`</summary>

```text
argmin_seed44_r2_results.json
deploy_3dir_spatial_seed42.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_crm_long_seed45.md
diagnose_default_seed46.md
diagnose_spatial_k5_seed44_r2.md
diagnosis-eval-obs-only-object-norm003-seed43.md
diagnosis_random_k5_seed44_r2.md
eval-argmin-object-seed44-r2
eval-obs-only-goal-norm02-seed52.json
eval-obs-only-object-default-seed45
eval-obs-only-object-norm01-seed45-r2
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm03-seed44
eval-openvla-object-vla-only-seed42
eval-openvla-object-vla-only-seed42-v2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "ff873735-ced5-4641-98b8-c1bcb600529d",
  "tool_use_result": {
    "stdout": "argmin_seed44_r2_results.json\ndeploy_3dir_spatial_seed42.md\ndiag_plan_a_spatial_seed42_43.md\ndiagnose-eval-adaptive-k-spatial-p50-seed44.md\ndiagnose-norm02-seed44-r2.md\ndiagnose-random-selection-seed46-r2.md\ndiagnose_crm_long_seed45.md\ndiagnose_default_seed46.md\ndiagnose_spatial_k5_seed44_r2.md\ndiagnosis-eval-obs-only-object-norm003-seed43.md\ndiagnosis_random_k5_seed44_r2.md\neval-argmin-object-seed44-r2\neval-obs-only-goal-norm02-seed52.json\neval-obs-only-object-default-seed45\neval-obs-only-object-norm01-seed45-r2\neval-obs-only-object-norm02-seed44-r2\neval-obs-only-object-norm02-seed46\neval-obs-only-object-norm03-seed44\neval-openvla-object-vla-only-seed42\neval-openvla-object-vla-only-seed42-v2",
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01EeciTm85un8djTn6zpiTF5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ | grep -iE \"provenance|main_results|seed_aggreg|seed.list|aggregat\" | head -20",
  "description": "Find aggregation/provenance docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "f419d515-0309-44d9-864f-0c2b7bbd02cc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WMz3JKeK5LJpnPnki8StL3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 82180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 84 · 2026-05-25T02:18:44.983Z_

<details><summary>↩ Tool result · `toolu_01EeciTm85un8djTn6zpiTF5`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "9b0cae76-ead9-4aab-a029-936870bd7cad",
  "tool_use_result": {
    "stdout": "",
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

_source line 85_

<details open><summary>🔧 Tool call — Grep · `toolu_0146sEHP9iGXphNbAZgq47fS`</summary>

```json
{
  "pattern": "83\\.7|85\\.0|77\\.7|76\\.5|77\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts",
  "output_mode": "files_with_matches",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6c698814-5003-45a7-9f52-899f18663d4c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Me1LSQHF9BEW4oJvsZXX3m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 82832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 86 · 2026-05-25T02:18:49.420Z_

<details><summary>↩ Tool result · `toolu_0146sEHP9iGXphNbAZgq47fS`</summary>

```text
Found 20 files limit: 20
artifacts/spatial_per_task_breakdown.md
artifacts/_project/report/table1_8seed_v2.md
artifacts/_project/data/table1_8seed_final.md
artifacts/_project/report/gpu_scan_r7_9dfa78.md
artifacts/_project/report/gpu_scan_r7.md
artifacts/gpu_scan_r7.md
artifacts/_project/report/a1_vla_survey_and_crm_analysis.md
artifacts/diag-eval-supp-goal-reconvla-s45.md
artifacts/eval-supp-goal-reconvla-s45/report/diag-eval-supp-goal-reconvla-s45.md
artifacts/_project/data/trigger_rate_scatter_data.csv
artifacts/figures/trigger_rate_scatter_data.csv
artifacts/eval-supp-k2mean-spatial-s42/report/eval-supp-k2mean-spatial-s42-analysis.md
artifacts/_project/report/experiment_status_20260523_session25.md
artifacts/experiment_status_20260523_session25.md
artifacts/_project/data/crm_eval_partial_results.md
artifacts/crm_eval_partial_results.md
artifacts/_project/report/crm_eval_results_harvest.md
artifacts/crm_eval_results_harvest.md
artifacts/_project/report/paper_audit_20260521_b7ea89.md
artifacts/paper_audit_20260521.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "566ae10b-57dc-4fac-ba5c-49d16483cd1f",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/spatial_per_task_breakdown.md",
      "artifacts/_project/report/table1_8seed_v2.md",
      "artifacts/_project/data/table1_8seed_final.md",
      "artifacts/_project/report/gpu_scan_r7_9dfa78.md",
      "artifacts/_project/report/gpu_scan_r7.md",
      "artifacts/gpu_scan_r7.md",
      "artifacts/_project/report/a1_vla_survey_and_crm_analysis.md",
      "artifacts/diag-eval-supp-goal-reconvla-s45.md",
      "artifacts/eval-supp-goal-reconvla-s45/report/diag-eval-supp-goal-reconvla-s45.md",
      "artifacts/_project/data/trigger_rate_scatter_data.csv",
      "artifacts/figures/trigger_rate_scatter_data.csv",
      "artifacts/eval-supp-k2mean-spatial-s42/report/eval-supp-k2mean-spatial-s42-analysis.md",
      "artifacts/_project/report/experiment_status_20260523_session25.md",
      "artifacts/experiment_status_20260523_session25.md",
      "artifacts/_project/data/crm_eval_partial_results.md",
      "artifacts/crm_eval_partial_results.md",
      "artifacts/_project/report/crm_eval_results_harvest.md",
      "artifacts/crm_eval_results_harvest.md",
      "artifacts/_project/report/paper_audit_20260521_b7ea89.md",
      "artifacts/paper_audit_20260521.md"
    ],
    "numFiles": 20,
    "appliedLimit": 20
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Read · `toolu_01KmqCDpAmxBBgi3A9bfEnAk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d139fc83-15b3-482f-bcb9-9b9fddcfedc4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AbH9YVWheDr1C6m3yiEq1C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 83039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 740
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 88 · 2026-05-25T02:18:55.937Z_

<details><summary>↩ Tool result · `toolu_01KmqCDpAmxBBgi3A9bfEnAk`</summary>

```text
1	# Table 1 — Multi-seed Results (Clean supp-era data)
2	
3	Generated: 2026-05-24 20:10 UTC
4	
5	## Main Table
6	
7	| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
8	|-------|---------|-------------|-------------------|--------|--------|
9	| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
10	| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
11	| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
12	| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |
13	
14	## Paired t-test: Δ(A-V) = Adaptive - VLA-only
15	
16	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
17	|-------|---------|--------|---------|-----------|-------|
18	| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
19	| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
20	| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
21	| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |
22	
23	## Paired t-test: Δ(A-C) = Adaptive - CRM always-on
24	
25	| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
26	|-------|---------|--------|---------|-----------|-------|
27	| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
28	| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
29	| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
30	| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |
31	
32	## Trigger Rate ↔ Effect Size (D140 key evidence)
33	
34	| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
35	|-------|------------------|--------|-------------|
36	| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
37	| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
38	| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
39	| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |
40	
41	## Per-seed Raw Data
42	
43	### Spatial (8 matched seeds)
44	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
45	|------|---------|----------|-----|--------|
46	| s42 | 80.0% | 82.0% | — | +2.0pp |
47	| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |
48	| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |
49	| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |
50	| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |
51	| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |
52	| s48 | 79.5% | 81.0% | — | +1.5pp |
53	| s49 | 78.5% | 82.0% | — | +3.5pp |
54	
55	### Goal (7 matched seeds for A-V)
56	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
57	|------|---------|----------|-----|--------|
58	| s42 | — | 84.0% | 85.5% | — |
59	| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |
60	| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |
61	| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |
62	| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |
63	| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |
64	| s48 | 85.0% | 84.5% | — | -0.5pp |
65	| s49 | 82.0% | 81.5% | — | -0.5pp |
66	
67	### Object (5 matched seeds for A-V)
68	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
69	|------|---------|----------|-----|--------|
70	| s42 | — | 81.0% | 77.0% | — |
71	| s43 | — | 77.5% | 78.5% | — |
72	| s44 | — | 75.0% | 74.0% | — |
73	| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
74	| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
75	| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
76	| s48 | 79.0% | 76.0% | — | -3.0pp |
77	| s49 | 75.5% | 74.0% | — | -1.5pp |
78	
79	### Long (5 matched seeds for A-V)
80	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
81	|------|---------|----------|-----|--------|
82	| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
83	| s43 | — | 58.0% | 54.5% | — |
84	| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
85	| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
86	| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
87	| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |
88	
89	## Data Gaps
90	- Goal VLA-only s42: missing
91	- Object VLA-only s42/s43/s44: missing
92	- Spatial CRM s42/s48/s49: missing
93	- Goal/Object CRM s48/s49: missing
94	- Long VLA-only s43/s48/s49: missing
95	- Long Adaptive s48/s49: missing
96	
97	## Note on Spatial VLA-only s42
98	eval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "2c8734fa-20a1-4631-b479-9bea8734ac4b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md",
      "content": "# Table 1 — Multi-seed Results (Clean supp-era data)\n\nGenerated: 2026-05-24 20:10 UTC\n\n## Main Table\n\n| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |\n|-------|---------|-------------|-------------------|--------|--------|\n| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |\n| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |\n| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |\n| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |\n\n## Paired t-test: Δ(A-V) = Adaptive - VLA-only\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |\n| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |\n| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |\n| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |\n\n## Paired t-test: Δ(A-C) = Adaptive - CRM always-on\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |\n| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |\n| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |\n| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |\n\n## Trigger Rate ↔ Effect Size (D140 key evidence)\n\n| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |\n|-------|------------------|--------|-------------|\n| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |\n| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |\n| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |\n| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |\n\n## Per-seed Raw Data\n\n### Spatial (8 matched seeds)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 80.0% | 82.0% | — | +2.0pp |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |\n| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |\n| s48 | 79.5% | 81.0% | — | +1.5pp |\n| s49 | 78.5% | 82.0% | — | +3.5pp |\n\n### Goal (7 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 84.0% | 85.5% | — |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |\n| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |\n| s48 | 85.0% | 84.5% | — | -0.5pp |\n| s49 | 82.0% | 81.5% | — | -0.5pp |\n\n### Object (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 81.0% | 77.0% | — |\n| s43 | — | 77.5% | 78.5% | — |\n| s44 | — | 75.0% | 74.0% | — |\n| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n| s48 | 79.0% | 76.0% | — | -3.0pp |\n| s49 | 75.5% | 74.0% | — | -1.5pp |\n\n### Long (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n| s43 | — | 58.0% | 54.5% | — |\n| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |\n\n## Data Gaps\n- Goal VLA-only s42: missing\n- Object VLA-only s42/s43/s44: missing\n- Spatial CRM s42/s48/s49: missing\n- Goal/Object CRM s48/s49: missing\n- Long VLA-only s43/s48/s49: missing\n- Long Adaptive s48/s49: missing\n\n## Note on Spatial VLA-only s42\neval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---

### Assistant

_source line 89_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "3a09df29-7600-4481-ac98-9813009e76a7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012NcxeZ1p4ee8ZZNQ3aJ2er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 83779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 90_

<details open><summary>🔧 Tool call — Read · `toolu_01WKbmiAaXFjz1kJvK9KB221`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "f48ae29a-f028-4424-8b95-686913135129",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012NcxeZ1p4ee8ZZNQ3aJ2er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 83779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 91 · 2026-05-25T02:19:02.131Z_

<details><summary>↩ Tool result · `toolu_01WKbmiAaXFjz1kJvK9KB221`</summary>

```text
1	# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)
2	
3	## Per-Seed Detail
4	
5	### SPATIAL (8/8 VLA-only, 8/8 Adaptive)
6	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
7	|------|----------|----------|-----|--------|-----------|
8	| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |
9	| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |
10	| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |
11	| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |
12	| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |
13	| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |
14	| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |
15	| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |
16	
17	**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*
18	
19	### OBJECT (3/8 VLA-only, 6/8 Adaptive)
20	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
21	|------|----------|----------|-----|--------|-----------|
22	| s42 | --- | 81.0% | 77.0% | | 3.5% |
23	| s43 | --- | 77.5% | 78.5% | | 3.7% |
24	| s44 | --- | 75.0% | 74.0% | | 3.6% |
25	| s45 | --- | --- | 76.5% | | |
26	| s46 | --- | --- | 79.5% | | |
27	| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |
28	| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |
29	| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |
30	
31	**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns
32	**Note:** s42/43/44 VLA-only currently running on bjb1-32546
33	
34	### GOAL (6/8 VLA-only, 8/8 Adaptive)
35	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
36	|------|----------|----------|-----|--------|-----------|
37	| s42 | --- | 84.0% | 85.5% | | 8.3% |
38	| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |
39	| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |
40	| s45 | --- | 81.0% | 81.0% | | 9.4% |
41	| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |
42	| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |
43	| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |
44	| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |
45	
46	**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns
47	
48	### LONG (3/8 each)
49	| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |
50	|------|----------|----------|-----|--------|-----------|
51	| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |
52	| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |
53	| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |
54	
55	**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns
56	
57	## Summary Table
58	
59	| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |
60	|-------|----------|----------|-----|--------|--------|---|
61	| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |
62	| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |
63	| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |
64	| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |
65	
66	## Trigger Rate ↔ Effect Size (D140 方案C evidence)
67	
68	| Suite | trigger_rate | Δ(A-V) | Direction |
69	|-------|-------------|--------|-----------|
70	| Spatial | 19.8% | +1.4%* | Positive (significant) |
71	| Goal | 8.6% | +0.9% | Positive (trend) |
72	| Object | 3.8% | -1.0% | Negligible |
73	| Long | 3.8% | -1.8% | Negligible |
74	
75	Perfect monotonic: higher trigger → larger positive effect.
76	
77	## Data Gaps (being filled)
78	- Object VLA-only s42/43/44: running on bjb1-32546
79	- Goal VLA-only s42/s45: s42 running on bjb1-32546
80	- Spatial CRM s48/s49: running on bjb2-28827
81	- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "b902f83f-0e00-47ea-9bd1-727ffd6d3d9a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/table1_8seed_v2.md",
      "content": "# Table 1: 8-Seed Comprehensive Data (τ=0.25, ε=0.05)\n\n## Per-Seed Detail\n\n### SPATIAL (8/8 VLA-only, 8/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | 80.0% | 82.0% | --- | +2.0% | 19.4% |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0% | 19.4% |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0% | 20.0% |\n| s45 | 80.0% | 80.0% | 80.5% | +0.0% | 20.0% |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5% | 19.9% |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5% | 20.5% |\n| s48 | 79.5% | 81.0% | --- | +1.5% | 19.8% |\n| s49 | 78.5% | 82.0% | --- | +3.5% | 19.5% |\n\n**Stats (8-seed paired):** VLA 79.5%±0.8% → Adaptive 80.9%±0.9%, Δ=+1.4%, p=0.0168*\n\n### OBJECT (3/8 VLA-only, 6/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | --- | 81.0% | 77.0% | | 3.5% |\n| s43 | --- | 77.5% | 78.5% | | 3.7% |\n| s44 | --- | 75.0% | 74.0% | | 3.6% |\n| s45 | --- | --- | 76.5% | | |\n| s46 | --- | --- | 79.5% | | |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5% | 4.0% |\n| s48 | 79.0% | 76.0% | --- | -3.0% | 3.9% |\n| s49 | 75.5% | 74.0% | --- | -1.5% | 4.2% |\n\n**Stats (3-seed paired):** VLA 76.7%±2.0% → Adaptive 75.7%±1.5%, Δ=-1.0%, p=0.53 ns\n**Note:** s42/43/44 VLA-only currently running on bjb1-32546\n\n### GOAL (6/8 VLA-only, 8/8 Adaptive)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | --- | 84.0% | 85.5% | | 8.3% |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0% | 8.8% |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5% | 6.8% |\n| s45 | --- | 81.0% | 81.0% | | 9.4% |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5% | 9.1% |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5% | 8.9% |\n| s48 | 85.0% | 84.5% | --- | -0.5% | 8.9% |\n| s49 | 82.0% | 81.5% | --- | -0.5% | 8.9% |\n\n**Stats (6-seed paired):** VLA 82.8%±1.1% → Adaptive 83.8%±1.8%, Δ=+0.9%, p=0.31 ns\n\n### LONG (3/8 each)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) | trig_rate |\n|------|----------|----------|-----|--------|-----------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0% | 3.9% |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0% | |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5% | 3.7% |\n\n**Stats (3-seed paired):** VLA 59.3%±1.3% → Adaptive 57.5%±2.2%, Δ=-1.8%, p=0.37 ns\n\n## Summary Table\n\n| Suite | VLA-only | Adaptive | CRM | Δ(A-V) | p(A-V) | n |\n|-------|----------|----------|-----|--------|--------|---|\n| Spatial | 79.5%±0.8% | 80.9%±0.9% | 80.3%±1.0% | +1.4% | 0.0168* | 8 |\n| Object | 76.7%±2.0% | 75.7%±1.5% | 78.0% (6s) | -1.0% | 0.53 | 3 |\n| Goal | 82.8%±1.1% | 83.8%±1.8% | 82.4%±0.8% | +0.9% | 0.31 | 6 |\n| Long | 59.3%±1.3% | 57.5%±2.2% | 55.7%±1.4% | -1.8% | 0.37 | 3 |\n\n## Trigger Rate ↔ Effect Size (D140 方案C evidence)\n\n| Suite | trigger_rate | Δ(A-V) | Direction |\n|-------|-------------|--------|-----------|\n| Spatial | 19.8% | +1.4%* | Positive (significant) |\n| Goal | 8.6% | +0.9% | Positive (trend) |\n| Object | 3.8% | -1.0% | Negligible |\n| Long | 3.8% | -1.8% | Negligible |\n\nPerfect monotonic: higher trigger → larger positive effect.\n\n## Data Gaps (being filled)\n- Object VLA-only s42/43/44: running on bjb1-32546\n- Goal VLA-only s42/s45: s42 running on bjb1-32546\n- Spatial CRM s48/s49: running on bjb2-28827\n- Goal CRM s48/s49: running on bjb2-28827 + bjb1-18228\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---

### Assistant

_source line 92_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "651cb0eb-795c-4f07-9439-b09d70b4d2c1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wm8bkNpyDTEoJ4XbzmERv2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2686,
      "cache_read_input_tokens": 86573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2686
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

_source line 93_

Now let me check the actual JSON files on the servers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "545563b0-889d-4bbe-969c-28a2b00ee00f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wm8bkNpyDTEoJ4XbzmERv2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2686,
      "cache_read_input_tokens": 86573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2686
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

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Sj1e5WZT1nDA7gofi8xBgX`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -maxdepth 2 -name \"eval_goal_*.json\" -o -name \"eval_object_*.json\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "e39c6a95-6344-4769-93c6-3b4007393c0e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Wm8bkNpyDTEoJ4XbzmERv2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2686,
      "cache_read_input_tokens": 86573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2686
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

_source line 95 · 2026-05-25T02:19:32.343Z_

<details><summary>↩ Tool result · `toolu_01Sj1e5WZT1nDA7gofi8xBgX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "034896b7-effd-4841-8060-1ca59a8646a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.92}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_acr_vla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_a1_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "ee67ada4-5549-4e68-ac45-df8aa5647b61",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SBZtsJHaxYqQNQ8tm4GrNr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6324,
      "cache_read_input_tokens": 89259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6324
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

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UMUKmehq66yEb6Xdp1EKwP`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', d.get('config', {}).get('mode', '?')) if isinstance(d, dict) else '?'\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        seed = d.get('seed', d.get('config', {}).get('seed', '?')) if isinstance(d, dict) else '?'\n        K = d.get('K', d.get('config', {}).get('K', '?')) if isinstance(d, dict) else '?'\n        ts = d.get('timestamp', '?')\n        print(f'{os.path.basename(f)} | SR={sr} | mode={mode} | n_roll={nr} | seed={seed} | K={K}')\n    except Exception as e:\n        print(f'{os.path.basename(f)} | ERROR: {e}')\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "475a7127-4970-4b03-9a42-d30441be70f0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SBZtsJHaxYqQNQ8tm4GrNr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6324,
      "cache_read_input_tokens": 89259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6324
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

_source line 98 · 2026-05-25T02:19:58.331Z_

<details><summary>↩ Tool result · `toolu_01UMUKmehq66yEb6Xdp1EKwP`</summary>

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "252fb8e7-6fd7-45a4-a28c-7ccfd39209dd",
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

_source line 99_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Jaj7CxQHeETjFvbsmxhtab`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        seed = d.get('seed', '?')\n        K = d.get('K', '?')\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr) + ' || seed=' + str(seed) + ' || K=' + str(K))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "f237cbd5-b49c-40be-8c2b-5150cf6dd5a9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0172xWXTLkkknepp6Gkkt75C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 95583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 100 · 2026-05-25T02:20:04.787Z_

<details><summary>↩ Tool result · `toolu_01Jaj7CxQHeETjFvbsmxhtab`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.865 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_crm_obs_only_norm0.05_seed43.json || SR=0.82 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_goal_obs_only_norm02_seed44.json || SR=0.64 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_goal_obs_only_norm02_seed45.json || SR=0.65 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_goal_vla_only_pi05_seed42.json || SR=0.955 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_pi05_seed43.json || SR=0.97 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed43.json || SR=0.825 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed43_r4.json || SR=0.98 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed44_r4.json || SR=0.975 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed46.json || SR=0.71 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_goal_vla_only_seed52.json || SR=0.68 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_a1_vla_only_seed42.json || SR=0.565 || mode=vla_only || n_roll=20 || seed=42 || K=?\\neval_object_acr_vla_seed42.json || SR=0.09 || mode=acr_vla || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.75 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json || SR=0.77 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json || SR=0.745 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_argmin_k5_seed42.json || SR=0.15 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_argmin_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_argmin_k5_seed45.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed42.json || SR=0.77 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed43.json || SR=0.785 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed44.json || SR=0.74 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed46.json || SR=0.795 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed47.json || SR=0.825 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_norm.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed47.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003_seed43_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003_seed47.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only\\n\\n... [截断: 输出过长，省略 1318 字符] ...\\n\\n_object_obs_only_norm03_seed46.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_perdof.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_default_seed45.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_default_seed46.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm003_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm003_seed48.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed44.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed46.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed45.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed46.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed47_r2.json || SR=0.14 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm02.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm02_seed43_bjb1-32546.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm03_seed45_r2.json || SR=0.06 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm03_seed46.json || SR=0.04 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed42.json || SR=0.14 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed44.json || SR=0.1 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed45.json || SR=0.07 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_reconvla.json || SR=0.12 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_reconvla_seed45.json || SR=0.78 || mode=reconvla || n_roll=20 || seed=? || K=?\\neval_object_reconvla_seed46.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_reconvla_seed47.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed43.json || SR=0.1 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed44_r2.json || SR=0.06 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed46.json || SR=0.09 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_vla_mean.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_mean_seed43.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_mean_seed44.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only_pi05_seed42.json || SR=0.965 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_pi05_seed43.json || SR=0.815 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_pi05_seed44.json || SR=0.81 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed42.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed46.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed47.json || SR=0.755 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only_seed51.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "5cec5eae-2c83-4b5f-8ab6-27ee56baf946",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.865 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_goal_crm_obs_only_norm0.05_seed43.json || SR=0.82 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_goal_obs_only_norm02_seed44.json || SR=0.64 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_goal_obs_only_norm02_seed45.json || SR=0.65 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_goal_vla_only_pi05_seed42.json || SR=0.955 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_pi05_seed43.json || SR=0.97 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed43.json || SR=0.825 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed43_r4.json || SR=0.98 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed44_r4.json || SR=0.975 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_goal_vla_only_seed46.json || SR=0.71 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_goal_vla_only_seed52.json || SR=0.68 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_a1_vla_only_seed42.json || SR=0.565 || mode=vla_only || n_roll=20 || seed=42 || K=?\\\\neval_object_acr_vla_seed42.json || SR=0.09 || mode=acr_vla || n_roll=20 || seed=? || K=?\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.75 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json || SR=0.77 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json || SR=0.745 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\\\neval_object_argmin_k5_seed42.json || SR=0.15 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_argmin_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_argmin_k5_seed45.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_crm_obs_only_norm0.05_seed42.json || SR=0.77 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_object_crm_obs_only_norm0.05_seed43.json || SR=0.785 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_object_crm_obs_only_norm0.05_seed44.json || SR=0.74 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_object_crm_obs_only_norm0.05_seed46.json || SR=0.795 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_object_crm_obs_only_norm0.05_seed47.json || SR=0.825 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_default_norm.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_default_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_default_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_default_seed47.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_norm003.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_norm003_seed43_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only_norm003_seed47.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_obs_only\\\\n\\\\n... [截断: 输出过长，省略 1318 字符] ...\\\\n\\\\n_object_obs_only_norm03_seed46.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\\\neval_object_perdof.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_default_seed45.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_default_seed46.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm003_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm003_seed48.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm005_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm005_seed44.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm005_seed46.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm01_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm01_seed45.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm01_seed46.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm01_seed47_r2.json || SR=0.14 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm02.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm02_seed43_bjb1-32546.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm03_seed45_r2.json || SR=0.06 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_perdof_norm03_seed46.json || SR=0.04 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\\\neval_object_random_selection_k5_seed42.json || SR=0.14 || mode=random_selection || n_roll=10 || seed=? || K=?\\\\neval_object_random_selection_k5_seed44.json || SR=0.1 || mode=random_selection || n_roll=10 || seed=? || K=?\\\\neval_object_random_selection_k5_seed45.json || SR=0.07 || mode=random_selection || n_roll=10 || seed=? || K=?\\\\neval_object_reconvla.json || SR=0.12 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_reconvla_seed45.json || SR=0.78 || mode=reconvla || n_roll=20 || seed=? || K=?\\\\neval_object_reconvla_seed46.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_reconvla_seed47.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\\\neval_object_scalar_seed43.json || SR=0.1 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\\\neval_object_scalar_seed44_r2.json || SR=0.06 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\\\neval_object_scalar_seed46.json || SR=0.09 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\\\neval_object_vla_mean.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_vla_mean_seed43.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_vla_mean_seed44.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_vla_only.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_vla_only_pi05_seed42.json || SR=0.965 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_pi05_seed43.json || SR=0.815 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_pi05_seed44.json || SR=0.81 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed42.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed46.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed47.json || SR=0.755 || mode=vla_only || n_roll=20 || seed=? || K=?\\\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\neval_object_vla_only_seed51.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.865 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_goal_crm_obs_only_norm0.05_seed43.json || SR=0.82 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_goal_obs_only_norm02_seed44.json || SR=0.64 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_goal_obs_only_norm02_seed45.json || SR=0.65 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_goal_vla_only_pi05_seed42.json || SR=0.955 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_pi05_seed43.json || SR=0.97 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed43.json || SR=0.825 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed43_r4.json || SR=0.98 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed44_r4.json || SR=0.975 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_goal_vla_only_seed46.json || SR=0.71 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_goal_vla_only_seed52.json || SR=0.68 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_a1_vla_only_seed42.json || SR=0.565 || mode=vla_only || n_roll=20 || seed=42 || K=?\\neval_object_acr_vla_seed42.json || SR=0.09 || mode=acr_vla || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json || SR=0.75 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json || SR=0.77 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed50.json || SR=0.745 || mode=adaptive_conformal_crm || n_roll=20 || seed=? || K=?\\neval_object_argmin_k5_seed42.json || SR=0.15 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_argmin_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_argmin_k5_seed45.json || SR=0.13 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed42.json || SR=0.77 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed43.json || SR=0.785 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed44.json || SR=0.74 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed46.json || SR=0.795 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_crm_obs_only_norm0.05_seed47.json || SR=0.825 || mode=crm_obs_only || n_roll=20 || seed=? || K=?\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_norm.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed47.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003.json || SR=0.16 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003_seed43_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only_norm003_seed47.json || SR=0.15 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_obs_only\\n\\n... [截断: 输出过长，省略 1318 字符] ...\\n\\n_object_obs_only_norm03_seed46.json || SR=0.17 || mode=crm_obs_only || n_roll=10 || seed=? || K=?\\neval_object_perdof.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_default_seed45.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_default_seed46.json || SR=0.0 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm003_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm003_seed48.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed43.json || SR=0.13 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed44.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm005_seed46.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed45.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed46.json || SR=0.1 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm01_seed47_r2.json || SR=0.14 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm02.json || SR=0.11 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm02_seed43_bjb1-32546.json || SR=0.09 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm03_seed45_r2.json || SR=0.06 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_perdof_norm03_seed46.json || SR=0.04 || mode=crm_perdof || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed42.json || SR=0.14 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed44.json || SR=0.1 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_random_selection_k5_seed45.json || SR=0.07 || mode=random_selection || n_roll=10 || seed=? || K=?\\neval_object_reconvla.json || SR=0.12 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_reconvla_seed45.json || SR=0.78 || mode=reconvla || n_roll=20 || seed=? || K=?\\neval_object_reconvla_seed46.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_reconvla_seed47.json || SR=0.1 || mode=reconvla || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed43.json || SR=0.1 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed44_r2.json || SR=0.06 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_scalar_seed46.json || SR=0.09 || mode=crm_scalar || n_roll=10 || seed=? || K=?\\neval_object_vla_mean.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_mean_seed43.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_mean_seed44.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only.json || SR=0.12 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only_pi05_seed42.json || SR=0.965 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_pi05_seed43.json || SR=0.815 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_pi05_seed44.json || SR=0.81 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed42.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed46.json || SR=0.79 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed47.json || SR=0.755 || mode=vla_only || n_roll=20 || seed=? || K=?\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10 || seed=? || K=?\\neval_object_vla_only_seed51.json || SR=0.15 || mode=vla_only || n_roll=10 || seed=? || K=?\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 101_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6dbddf0b-39ed-47fa-9cb0-a2f415a703d1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TkyyzXsq4sADCBbDgWGHez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5102,
      "cache_read_input_tokens": 97401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5102
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 102_

Let me check the other servers for the missing seed files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "090e7c41-99c0-4e15-a427-7a6aa0252144",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TkyyzXsq4sADCBbDgWGHez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5102,
      "cache_read_input_tokens": 97401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5102
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JxgKpiJ6cMJhUaqvfLUwaM`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "fc64e39a-e9e9-4041-93c4-8bafc8715dc4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TkyyzXsq4sADCBbDgWGHez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5102,
      "cache_read_input_tokens": 97401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5102
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 104 · 2026-05-25T02:20:39.377Z_

<details><summary>↩ Tool result · `toolu_01JxgKpiJ6cMJhUaqvfLUwaM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json || SR=0.85 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.84 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.815 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json || SR=0.82 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed42.json || SR=0.855 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed44.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed45.json || SR=0.81 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed46.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed47.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed48.json || SR=0.8 || mode=crm_obs_only || n_roll=20\\neval_goal_k2mean_seed46.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_obs_only_norm02_seed47.json || SR=0.69 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed48.json || SR=0.68 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed49.json || SR=0.62 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed50.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\neval_goal_reconvla_seed42.json || SR=0.81 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed44.json || SR=0.805 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed45.json || SR=0.855 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed46.json || SR=0.79 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed47.json || SR=0.835 || mode=reconvla || n_roll=20\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed44_r2.json || SR=0.73 || mode=vla_only || n_roll=10\\neval_goal_vla_only_seed45.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed46.json || SR=0.83 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed50.json || SR=0.65 || mode=vla_only || n_roll=10\\neval_goal_vla_only_seed51.json || SR=0.69 || mode=vla_only || n_roll=10\\neval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.78 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.76 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.74 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_argmin_k5_seed44_r2.json || SR=0.11 || mode=reconvla || n_roll=10\\neval_object_argmin_seed45.json || SR=0.12 || mode=reconvla || n_roll=10\\neval_object_crm_obs_only_seed42.json || SR=0.505 || mode=crm_obs_only || n_roll=20\\neval_object_crm_obs_only_seed43.json || SR=0.535 || mode=crm_obs_only || n_roll=20\\neval_object_crm_obs_only_seed44.json || SR=0.515 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_default_seed45.json || SR=0.12 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_default_seed45_r2.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed44.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed43.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed47.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed42.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed45_r2.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_K20_seed44.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed43.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed44.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed45.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03_seed45_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_perdof_default_seed47.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003.json || SR=0.14 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005.json || SR=0.14 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm01_seed42.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed43_r3.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed44.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed45.json || SR=0.09 || mode=crm_perdof || n_roll=20\\neval_object_perdof_norm02_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed47.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed48.json || SR=0.07 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_r3.json || SR=0.04 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_seed47.json || SR=0.05 || mode=crm_perdof || n_roll=10\\neval_object_random_selection_k5_seed43.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed43.json || SR=0.09 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed44.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed45.json || SR=0.1 || mode=random_selection || n_roll=10\\neval_object_reconvla_k5_seed42.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed42.json || SR=0.79 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed43.json || SR=0.77 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed47.json || SR=0.765 || mode=reconvla || n_roll=20\\neval_object_scalar_seed45.json || SR=0.09 || mode=crm_scalar || n_roll=20\\neval_object_vla_mean_seed45.json || SR=0.13 || mode=vla_only || n_roll=10\\neval_object_vla_only_pi05_seed43.json || SR=0.865 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed42.json || SR=0.795 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45.json || SR=0.76 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed47.json || SR=0.1 || mode=vla_only || n_roll=10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d687f080-9688-4c7e-958e-ba56c13ee8d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json || SR=0.85 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.84 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.815 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json || SR=0.82 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed42.json || SR=0.855 || mode=crm_obs_only || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed44.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed45.json || SR=0.81 || mode=crm_obs_only || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed46.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed47.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\\\neval_goal_crm_obs_only_norm0.05_seed48.json || SR=0.8 || mode=crm_obs_only || n_roll=20\\\\neval_goal_k2mean_seed46.json || SR=0.825 || mode=vla_only || n_roll=20\\\\neval_goal_obs_only_norm02_seed47.json || SR=0.69 || mode=crm_obs_only || n_roll=10\\\\neval_goal_obs_only_norm02_seed48.json || SR=0.68 || mode=crm_obs_only || n_roll=10\\\\neval_goal_obs_only_norm02_seed49.json || SR=0.62 || mode=crm_obs_only || n_roll=10\\\\neval_goal_obs_only_norm02_seed50.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\\\neval_goal_reconvla_seed42.json || SR=0.81 || mode=reconvla || n_roll=20\\\\neval_goal_reconvla_seed44.json || SR=0.805 || mode=reconvla || n_roll=20\\\\neval_goal_reconvla_seed45.json || SR=0.855 || mode=reconvla || n_roll=20\\\\neval_goal_reconvla_seed46.json || SR=0.79 || mode=reconvla || n_roll=20\\\\neval_goal_reconvla_seed47.json || SR=0.835 || mode=reconvla || n_roll=20\\\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed44_r2.json || SR=0.73 || mode=vla_only || n_roll=10\\\\neval_goal_vla_only_seed45.json || SR=0.835 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed46.json || SR=0.83 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed50.json || SR=0.65 || mode=vla_only || n_roll=10\\\\neval_goal_vla_only_seed51.json || SR=0.69 || mode=vla_only || n_roll=10\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.78 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.76 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.74 || mode=adaptive_conformal_crm || n_roll=20\\\\neval_object_argmin_k5_seed44_r2.json || SR=0.11 || mode=reconvla || n_roll=10\\\\neval_object_argmin_seed45.json || SR=0.12 || mode=reconvla || n_roll=10\\\\neval_object_crm_obs_only_seed42.json || SR=0.505 || mode=crm_obs_only || n_roll=20\\\\neval_object_crm_obs_only_seed43.json || SR=0.535 || mode=crm_obs_only || n_roll=20\\\\neval_object_crm_obs_only_seed44.json || SR=0.515 || mode=crm_obs_only || n_roll=20\\\\neval_object_obs_only_default_seed45.json || SR=0.12 || mode=crm_obs_only || n_roll=20\\\\neval_object_obs_only_default_seed45_r2.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm003_seed44.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm005.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm005_seed43.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm005_seed47.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm01_seed42.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm01_seed45_r2.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_K20_seed44.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed43.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed44.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed45.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm03.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm03_seed45_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\\\neval_object_perdof_default_seed47.json || SR=0.0 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm003.json || SR=0.14 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm003_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm005.json || SR=0.14 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm01_seed42.json || SR=0.11 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed43_r3.json || SR=0.09 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed44.json || SR=0.1 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed45.json || SR=0.09 || mode=crm_perdof || n_roll=20\\\\neval_object_perdof_norm02_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed47.json || SR=0.11 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed48.json || SR=0.07 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm03_r3.json || SR=0.04 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm03_seed47.json || SR=0.05 || mode=crm_perdof || n_roll=10\\\\neval_object_random_selection_k5_seed43.json || SR=0.11 || mode=random_selection || n_roll=10\\\\neval_object_random_selection_seed42.json || SR=0.11 || mode=random_selection || n_roll=10\\\\neval_object_random_selection_seed43.json || SR=0.09 || mode=random_selection || n_roll=10\\\\neval_object_random_selection_seed44.json || SR=0.11 || mode=random_selection || n_roll=10\\\\neval_object_random_selection_seed45.json || SR=0.1 || mode=random_selection || n_roll=10\\\\neval_object_reconvla_k5_seed42.json || SR=0.13 || mode=reconvla || n_roll=10\\\\neval_object_reconvla_seed42.json || SR=0.79 || mode=reconvla || n_roll=20\\\\neval_object_reconvla_seed43.json || SR=0.77 || mode=reconvla || n_roll=20\\\\neval_object_reconvla_seed47.json || SR=0.765 || mode=reconvla || n_roll=20\\\\neval_object_scalar_seed45.json || SR=0.09 || mode=crm_scalar || n_roll=20\\\\neval_object_vla_mean_seed45.json || SR=0.13 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_pi05_seed43.json || SR=0.865 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed42.json || SR=0.795 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed45.json || SR=0.76 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed47.json || SR=0.1 || mode=vla_only || n_roll=10\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json || SR=0.85 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.84 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.845 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.815 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json || SR=0.835 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_adaptive_conformal_crm_tau0.25_seed47.json || SR=0.82 || mode=adaptive_conformal_crm || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed42.json || SR=0.855 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed44.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed45.json || SR=0.81 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed46.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed47.json || SR=0.82 || mode=crm_obs_only || n_roll=20\\neval_goal_crm_obs_only_norm0.05_seed48.json || SR=0.8 || mode=crm_obs_only || n_roll=20\\neval_goal_k2mean_seed46.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_obs_only_norm02_seed47.json || SR=0.69 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed48.json || SR=0.68 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed49.json || SR=0.62 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed50.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\neval_goal_reconvla_seed42.json || SR=0.81 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed44.json || SR=0.805 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed45.json || SR=0.855 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed46.json || SR=0.79 || mode=reconvla || n_roll=20\\neval_goal_reconvla_seed47.json || SR=0.835 || mode=reconvla || n_roll=20\\neval_goal_vla_only_seed42.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed44_r2.json || SR=0.73 || mode=vla_only || n_roll=10\\neval_goal_vla_only_seed45.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed46.json || SR=0.83 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed50.json || SR=0.65 || mode=vla_only || n_roll=10\\neval_goal_vla_only_seed51.json || SR=0.69 || mode=vla_only || n_roll=10\\neval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json || SR=0.81 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json || SR=0.78 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json || SR=0.775 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json || SR=0.76 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json || SR=0.74 || mode=adaptive_conformal_crm || n_roll=20\\neval_object_argmin_k5_seed44_r2.json || SR=0.11 || mode=reconvla || n_roll=10\\neval_object_argmin_seed45.json || SR=0.12 || mode=reconvla || n_roll=10\\neval_object_crm_obs_only_seed42.json || SR=0.505 || mode=crm_obs_only || n_roll=20\\neval_object_crm_obs_only_seed43.json || SR=0.535 || mode=crm_obs_only || n_roll=20\\neval_object_crm_obs_only_seed44.json || SR=0.515 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_default_seed45.json || SR=0.12 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_default_seed45_r2.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_default_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed44.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed43.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed47.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed42.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed45_r2.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_K20_seed44.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed43.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed44.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed45.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03_seed45_r2.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_perdof_default_seed47.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003.json || SR=0.14 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005.json || SR=0.14 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005_seed45.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm01_seed42.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed43_r3.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed44.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed45.json || SR=0.09 || mode=crm_perdof || n_roll=20\\neval_object_perdof_norm02_seed46.json || SR=0.09 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed47.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed48.json || SR=0.07 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_r3.json || SR=0.04 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_seed47.json || SR=0.05 || mode=crm_perdof || n_roll=10\\neval_object_random_selection_k5_seed43.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed43.json || SR=0.09 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed44.json || SR=0.11 || mode=random_selection || n_roll=10\\neval_object_random_selection_seed45.json || SR=0.1 || mode=random_selection || n_roll=10\\neval_object_reconvla_k5_seed42.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed42.json || SR=0.79 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed43.json || SR=0.77 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed47.json || SR=0.765 || mode=reconvla || n_roll=20\\neval_object_scalar_seed45.json || SR=0.09 || mode=crm_scalar || n_roll=20\\neval_object_vla_mean_seed45.json || SR=0.13 || mode=vla_only || n_roll=10\\neval_object_vla_only_pi05_seed43.json || SR=0.865 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed42.json || SR=0.795 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed43.json || SR=0.77 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed44.json || SR=0.775 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45.json || SR=0.76 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed47.json || SR=0.1 || mode=vla_only || n_roll=10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 105_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "94f74d0d-876e-47b4-ad22-e2411f0da3bf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PR8q8XV3CkTWSD3URmHcBL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7070,
      "cache_read_input_tokens": 102503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7070
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 106_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KwEVs9wo8afn8UDrV2Qdgj`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "63987574-7eff-4184-8355-7685ee193fea",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PR8q8XV3CkTWSD3URmHcBL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7070,
      "cache_read_input_tokens": 102503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7070
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 107 · 2026-05-25T02:20:47.753Z_

<details><summary>↩ Tool result · `toolu_01KwEVs9wo8afn8UDrV2Qdgj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\"\\\\nimport json, os, glob\\\\nfiles = sorted(glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\') + glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        d = json.load(open(f))\\\\n        sr = d.get(\\\\'overall_success_rate\\\\', d.get(\\\\'overall_sr\\\\', d.get(\\\\'success_rate\\\\', \\\\'?\\\\')))\\\\n        mode = d.get(\\\\'mode\\\\', \\\\'?\\\\')\\\\n        nr = d.get(\\\\'n_rollouts\\\\', d.get(\\\\'n_rollouts_per_task\\\\', \\\\'?\\\\'))\\\\n        print(os.path.basename(f) + \\\\' || SR=\\\\' + str(sr) + \\\\' || mode=\\\\' + str(mode) + \\\\' || n_roll=\\\\' + str(nr))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f) + \\\\' || ERROR: \\\\' + str(e))\\\\n\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.92}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "a6b7a0f1-4376-47fc-8421-d4df9bd4fdd5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\\\\\"\\\\\\\\nimport json, os, glob\\\\\\\\nfiles = sorted(glob.glob(\\\\\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\\\\\') + glob.glob(\\\\\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\\\\\'))\\\\\\\\nfor f in files:\\\\\\\\n    try:\\\\\\\\n        d = json.load(open(f))\\\\\\\\n        sr = d.get(\\\\\\\\'overall_success_rate\\\\\\\\', d.get(\\\\\\\\'overall_sr\\\\\\\\', d.get(\\\\\\\\'success_rate\\\\\\\\', \\\\\\\\'?\\\\\\\\')))\\\\\\\\n        mode = d.get(\\\\\\\\'mode\\\\\\\\', \\\\\\\\'?\\\\\\\\')\\\\\\\\n        nr = d.get(\\\\\\\\'n_rollouts\\\\\\\\', d.get(\\\\\\\\'n_rollouts_per_task\\\\\\\\', \\\\\\\\'?\\\\\\\\'))\\\\\\\\n        print(os.path.basename(f) + \\\\\\\\' || SR=\\\\\\\\' + str(sr) + \\\\\\\\' || mode=\\\\\\\\' + str(mode) + \\\\\\\\' || n_roll=\\\\\\\\' + str(nr))\\\\\\\\n    except Exception as e:\\\\\\\\n        print(os.path.basename(f) + \\\\\\\\' || ERROR: \\\\\\\\' + str(e))\\\\\\\\n\\\\\\\"'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.92}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\"\\\\nimport json, os, glob\\\\nfiles = sorted(glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\') + glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        d = json.load(open(f))\\\\n        sr = d.get(\\\\'overall_success_rate\\\\', d.get(\\\\'overall_sr\\\\', d.get(\\\\'success_rate\\\\', \\\\'?\\\\')))\\\\n        mode = d.get(\\\\'mode\\\\', \\\\'?\\\\')\\\\n        nr = d.get(\\\\'n_rollouts\\\\', d.get(\\\\'n_rollouts_per_task\\\\', \\\\'?\\\\'))\\\\n        print(os.path.basename(f) + \\\\' || SR=\\\\' + str(sr) + \\\\' || mode=\\\\' + str(mode) + \\\\' || n_roll=\\\\' + str(nr))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f) + \\\\' || ERROR: \\\\' + str(e))\\\\n\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.92}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 108_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Qp9jP3P969yWL2jhK2T8bd`</summary>

```json
{
  "server": "cqa1-32758",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "6564fbf0-0337-451c-9f71-e1150f141cf1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TWMzcWZ7PevJ8hYGjTizFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 109573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
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

_source line 109 · 2026-05-25T02:20:55.574Z_

<details><summary>↩ Tool result · `toolu_01Qp9jP3P969yWL2jhK2T8bd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_k2mean_seed45.json || SR=0.81 || mode=vla_only || n_roll=20\\neval_goal_reconvla_seed43.json || SR=0.81 || mode=reconvla || n_roll=20\\neval_goal_vla_only_seed42.json || SR=0.82 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed43.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed48.json || SR=0.85 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed49.json || SR=0.82 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed50.json || SR=0.8 || mode=vla_only || n_roll=20\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\neval_object_reconvla_seed44.json || SR=0.76 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed45.json || SR=0.74 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed46.json || SR=0.8 || mode=reconvla || n_roll=20\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\neval_object_vla_only_seed44.json || SR=0.75 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45.json || SR=0.775 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed46.json || SR=0.765 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed48.json || SR=0.79 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed49.json || SR=0.755 || mode=vla_only || n_roll=20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "5681b574-37a9-4033-99c8-9778c780d794",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_k2mean_seed45.json || SR=0.81 || mode=vla_only || n_roll=20\\\\neval_goal_reconvla_seed43.json || SR=0.81 || mode=reconvla || n_roll=20\\\\neval_goal_vla_only_seed42.json || SR=0.82 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed43.json || SR=0.835 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed48.json || SR=0.85 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed49.json || SR=0.82 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed50.json || SR=0.8 || mode=vla_only || n_roll=20\\\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\\\neval_object_reconvla_seed44.json || SR=0.76 || mode=reconvla || n_roll=20\\\\neval_object_reconvla_seed45.json || SR=0.74 || mode=reconvla || n_roll=20\\\\neval_object_reconvla_seed46.json || SR=0.8 || mode=reconvla || n_roll=20\\\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\\\neval_object_vla_only_seed44.json || SR=0.75 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed45.json || SR=0.775 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed46.json || SR=0.765 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed48.json || SR=0.79 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed49.json || SR=0.755 || mode=vla_only || n_roll=20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.05}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_k2mean_seed45.json || SR=0.81 || mode=vla_only || n_roll=20\\neval_goal_reconvla_seed43.json || SR=0.81 || mode=reconvla || n_roll=20\\neval_goal_vla_only_seed42.json || SR=0.82 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed43.json || SR=0.835 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed44.json || SR=0.85 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed48.json || SR=0.85 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed49.json || SR=0.82 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed50.json || SR=0.8 || mode=vla_only || n_roll=20\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\neval_object_reconvla_seed44.json || SR=0.76 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed45.json || SR=0.74 || mode=reconvla || n_roll=20\\neval_object_reconvla_seed46.json || SR=0.8 || mode=reconvla || n_roll=20\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\neval_object_vla_only_seed44.json || SR=0.75 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45.json || SR=0.775 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed46.json || SR=0.765 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed48.json || SR=0.79 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed49.json || SR=0.755 || mode=vla_only || n_roll=20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013hJYxEFqrnkuSqay2jmu5g`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "d3a63e3a-0fe1-4492-a8dd-d2ee884e6abe",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011QABtZqvJYoJQBMbNwYsCD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1437,
      "cache_read_input_tokens": 110732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1437
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

_source line 111 · 2026-05-25T02:21:03.076Z_

<details><summary>↩ Tool result · `toolu_013hJYxEFqrnkuSqay2jmu5g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_crm_obs_only_norm0.05_seed49.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\neval_goal_obs_only_norm02_seed42.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed43.json || SR=0.72 || mode=crm_obs_only || n_roll=10\\neval_goal_vla_only_seed42_r4.json || SR=0.98 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed49.json || SR=0.65 || mode=vla_only || n_roll=10\\neval_object_acr_vla_seed42.json || SR=0.04 || mode=acr_vla || n_roll=20\\neval_object_crm_obs_only_norm0.05_seed48.json || SR=0.735 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_norm003_seed48.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed76.json || SR=0.08 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed77.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed45.json || SR=0.14 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_norm01_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_K20_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed42.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed46.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed47.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed55.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03_seed48.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_seed43.json || SR=0.12 || mode=crm_obs_only || n_roll=10\\neval_object_perdof_default_norm_r2.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_default_seed43.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed44.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed47.json || SR=0.15 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005_seed47.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm01_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed45_r3.json || SR=0.12 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_seed44.json || SR=0.04 || mode=crm_perdof || n_roll=10\\neval_object_perdof_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10\\neval_object_perdof_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\neval_object_reconvla_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed43.json || SR=0.17 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed44.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed43.json || SR=0.985 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed44.json || SR=0.995 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45_r2.json || SR=0.11 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed46.json || SR=0.13 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed48.json || SR=0.11 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed50.json || SR=0.74 || mode=vla_only || n_roll=20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "04421f44-4960-48e9-a27c-7c719d30886c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_crm_obs_only_norm0.05_seed49.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\\\neval_goal_obs_only_norm02_seed42.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\\\neval_goal_obs_only_norm02_seed43.json || SR=0.72 || mode=crm_obs_only || n_roll=10\\\\neval_goal_vla_only_seed42_r4.json || SR=0.98 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\\\neval_goal_vla_only_seed49.json || SR=0.65 || mode=vla_only || n_roll=10\\\\neval_object_acr_vla_seed42.json || SR=0.04 || mode=acr_vla || n_roll=20\\\\neval_object_crm_obs_only_norm0.05_seed48.json || SR=0.735 || mode=crm_obs_only || n_roll=20\\\\neval_object_obs_only_norm003_seed48.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm003_seed76.json || SR=0.08 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm003_seed77.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm005_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm01_seed45.json || SR=0.14 || mode=crm_obs_only || n_roll=20\\\\neval_object_obs_only_norm01_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_K20_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed42.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed46.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_k5_seed47.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm02_seed55.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_norm03_seed48.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\\\neval_object_obs_only_seed43.json || SR=0.12 || mode=crm_obs_only || n_roll=10\\\\neval_object_perdof_default_norm_r2.json || SR=0.0 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_default_seed43.json || SR=0.0 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm003_seed44.json || SR=0.11 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm003_seed47.json || SR=0.15 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm005_seed47.json || SR=0.1 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm01_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm02_seed45_r3.json || SR=0.12 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_norm03_seed44.json || SR=0.04 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10\\\\neval_object_perdof_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\\\neval_object_reconvla_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10\\\\neval_object_reconvla_seed43.json || SR=0.17 || mode=reconvla || n_roll=10\\\\neval_object_reconvla_seed44.json || SR=0.13 || mode=reconvla || n_roll=10\\\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_pi05_seed43.json || SR=0.985 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_pi05_seed44.json || SR=0.995 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_seed45_r2.json || SR=0.11 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_seed46.json || SR=0.13 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_seed48.json || SR=0.11 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_seed50.json || SR=0.74 || mode=vla_only || n_roll=20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.97}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_crm_obs_only_norm0.05_seed49.json || SR=0.835 || mode=crm_obs_only || n_roll=20\\neval_goal_obs_only_norm02_seed42.json || SR=0.67 || mode=crm_obs_only || n_roll=10\\neval_goal_obs_only_norm02_seed43.json || SR=0.72 || mode=crm_obs_only || n_roll=10\\neval_goal_vla_only_seed42_r4.json || SR=0.98 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed47.json || SR=0.825 || mode=vla_only || n_roll=20\\neval_goal_vla_only_seed49.json || SR=0.65 || mode=vla_only || n_roll=10\\neval_object_acr_vla_seed42.json || SR=0.04 || mode=acr_vla || n_roll=20\\neval_object_crm_obs_only_norm0.05_seed48.json || SR=0.735 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_norm003_seed48.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed76.json || SR=0.08 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm003_seed77.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm005_seed48.json || SR=0.17 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm01_seed45.json || SR=0.14 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only_norm01_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_K20_seed42.json || SR=0.2 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed42.json || SR=0.14 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed46.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_k5_seed47.json || SR=0.13 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed44.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed46.json || SR=0.15 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed48.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm02_seed55.json || SR=0.18 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_norm03_seed48.json || SR=0.16 || mode=crm_obs_only || n_roll=10\\neval_object_obs_only_seed43.json || SR=0.12 || mode=crm_obs_only || n_roll=10\\neval_object_perdof_default_norm_r2.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_default_seed43.json || SR=0.0 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed44.json || SR=0.11 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm003_seed47.json || SR=0.15 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm005_seed47.json || SR=0.1 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm01_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm02_seed45_r3.json || SR=0.12 || mode=crm_perdof || n_roll=10\\neval_object_perdof_norm03_seed44.json || SR=0.04 || mode=crm_perdof || n_roll=10\\neval_object_perdof_seed43.json || SR=0.12 || mode=crm_perdof || n_roll=10\\neval_object_perdof_seed44.json || SR=0.08 || mode=crm_perdof || n_roll=10\\neval_object_reconvla_k5_seed43.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed43.json || SR=0.17 || mode=reconvla || n_roll=10\\neval_object_reconvla_seed44.json || SR=0.13 || mode=reconvla || n_roll=10\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed43.json || SR=0.985 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed44.json || SR=0.995 || mode=vla_only || n_roll=20\\neval_object_vla_only_seed45_r2.json || SR=0.11 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed46.json || SR=0.13 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed48.json || SR=0.11 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed49.json || SR=0.1 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed50.json || SR=0.74 || mode=vla_only || n_roll=20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 112_

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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "919e9bc6-46b2-4819-bef1-e478a77bc379",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UzPCNcmUBDd6LbZQHKhzqe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2577,
      "cache_read_input_tokens": 112169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2577
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0123tBtxYVooT5K3RRfd6nuK`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "58b10abf-934f-4017-b6e8-5b2ee355b8ec",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UzPCNcmUBDd6LbZQHKhzqe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2577,
      "cache_read_input_tokens": 112169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2577
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 114 · 2026-05-25T02:21:11.419Z_

<details><summary>↩ Tool result · `toolu_0123tBtxYVooT5K3RRfd6nuK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\"\\\\nimport json, os, glob\\\\nfiles = sorted(glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\') + glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        d = json.load(open(f))\\\\n        sr = d.get(\\\\'overall_success_rate\\\\', d.get(\\\\'overall_sr\\\\', d.get(\\\\'success_rate\\\\', \\\\'?\\\\')))\\\\n        mode = d.get(\\\\'mode\\\\', \\\\'?\\\\')\\\\n        nr = d.get(\\\\'n_rollouts\\\\', d.get(\\\\'n_rollouts_per_task\\\\', \\\\'?\\\\'))\\\\n        print(os.path.basename(f) + \\\\' || SR=\\\\' + str(sr) + \\\\' || mode=\\\\' + str(mode) + \\\\' || n_roll=\\\\' + str(nr))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f) + \\\\' || ERROR: \\\\' + str(e))\\\\n\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "1718639e-b7d7-4c5e-bce6-59f849e0934c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\\\\\"\\\\\\\\nimport json, os, glob\\\\\\\\nfiles = sorted(glob.glob(\\\\\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\\\\\') + glob.glob(\\\\\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\\\\\'))\\\\\\\\nfor f in files:\\\\\\\\n    try:\\\\\\\\n        d = json.load(open(f))\\\\\\\\n        sr = d.get(\\\\\\\\'overall_success_rate\\\\\\\\', d.get(\\\\\\\\'overall_sr\\\\\\\\', d.get(\\\\\\\\'success_rate\\\\\\\\', \\\\\\\\'?\\\\\\\\')))\\\\\\\\n        mode = d.get(\\\\\\\\'mode\\\\\\\\', \\\\\\\\'?\\\\\\\\')\\\\\\\\n        nr = d.get(\\\\\\\\'n_rollouts\\\\\\\\', d.get(\\\\\\\\'n_rollouts_per_task\\\\\\\\', \\\\\\\\'?\\\\\\\\'))\\\\\\\\n        print(os.path.basename(f) + \\\\\\\\' || SR=\\\\\\\\' + str(sr) + \\\\\\\\' || mode=\\\\\\\\' + str(mode) + \\\\\\\\' || n_roll=\\\\\\\\' + str(nr))\\\\\\\\n    except Exception as e:\\\\\\\\n        print(os.path.basename(f) + \\\\\\\\' || ERROR: \\\\\\\\' + str(e))\\\\\\\\n\\\\\\\"'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\"\\\\nimport json, os, glob\\\\nfiles = sorted(glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_goal_*.json\\\\') + glob.glob(\\\\'/root/acr-vla-conformal-refinement/logs/eval_object_*.json\\\\'))\\\\nfor f in files:\\\\n    try:\\\\n        d = json.load(open(f))\\\\n        sr = d.get(\\\\'overall_success_rate\\\\', d.get(\\\\'overall_sr\\\\', d.get(\\\\'success_rate\\\\', \\\\'?\\\\')))\\\\n        mode = d.get(\\\\'mode\\\\', \\\\'?\\\\')\\\\n        nr = d.get(\\\\'n_rollouts\\\\', d.get(\\\\'n_rollouts_per_task\\\\', \\\\'?\\\\'))\\\\n        print(os.path.basename(f) + \\\\' || SR=\\\\' + str(sr) + \\\\' || mode=\\\\' + str(mode) + \\\\' || n_roll=\\\\' + str(nr))\\\\n    except Exception as e:\\\\n        print(os.path.basename(f) + \\\\' || ERROR: \\\\' + str(e))\\\\n\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0186NXDtbW9tf3oqFcjqBJ5P`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -c \"\nimport json, os, glob\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_goal_*.json') + glob.glob('/root/acr-vla-conformal-refinement/logs/eval_object_*.json'))\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('overall_sr', d.get('success_rate', '?')))\n        mode = d.get('mode', '?')\n        nr = d.get('n_rollouts', d.get('n_rollouts_per_task', '?'))\n        print(os.path.basename(f) + ' || SR=' + str(sr) + ' || mode=' + str(mode) + ' || n_roll=' + str(nr))\n    except Exception as e:\n        print(os.path.basename(f) + ' || ERROR: ' + str(e))\n\"",
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
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "dd670473-d232-456f-8127-e2d73571364d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01V6ZWFaeomMnzzwG3vBDGPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 114746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 116 · 2026-05-25T02:21:18.628Z_

<details><summary>↩ Tool result · `toolu_0186NXDtbW9tf3oqFcjqBJ5P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_goal_vla_only_seed42.json || SR=0.855 || mode=vla_only || n_roll=20\\neval_object_crm_obs_only_norm0.05_seed45.json || SR=0.765 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\neval_object_vla_only_seed44.json || SR=0.1 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed48.json || SR=0.1 || mode=vla_only || n_roll=10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cac457c2-38ab-40ed-86ec-14422a05cb5c",
  "uuid": "550a8f1f-e099-4de3-8615-9edc9701ca6d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_goal_vla_only_seed42.json || SR=0.855 || mode=vla_only || n_roll=20\\\\neval_object_crm_obs_only_norm0.05_seed45.json || SR=0.765 || mode=crm_obs_only || n_roll=20\\\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\\\neval_object_vla_only_seed44.json || SR=0.1 || mode=vla_only || n_roll=10\\\\neval_object_vla_only_seed48.json || SR=0.1 || mode=vla_only || n_roll=10\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.04}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_goal_vla_only_seed42.json || SR=0.855 || mode=vla_only || n_roll=20\\neval_object_crm_obs_only_norm0.05_seed45.json || SR=0.765 || mode=crm_obs_only || n_roll=20\\neval_object_obs_only.json || SR=0.19 || mode=crm_obs_only || n_roll=10\\neval_object_random_selection_seed42.json || SR=0.13 || mode=random_selection || n_roll=10\\neval_object_scalar_seed45_r2.json || SR=0.07 || mode=crm_scalar || n_roll=10\\neval_object_vla_only_openvla_oft_seed42.json || SR=0.0 || mode=vla_only || n_roll=20\\neval_object_vla_only_pi05_seed42.json || SR=1.0 || mode=vla_only || n_roll=3\\neval_object_vla_only_seed44.json || SR=0.1 || mode=vla_only || n_roll=10\\neval_object_vla_only_seed48.json || SR=0.1 || mode=vla_only || n_roll=10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"
    }
  }
}
```

</details>

---

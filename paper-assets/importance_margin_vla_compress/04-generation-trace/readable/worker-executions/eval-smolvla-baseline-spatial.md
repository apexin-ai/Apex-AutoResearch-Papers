# eval smolvla baseline spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_eval_smolvla_baseline_spatial_20260519T111128.log`
- **Structured JSON:** [`9141958041e2141f249d.json`](../../sessions/91/9141958041e2141f249d.json)

## Before a recorded user message

79 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
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
  "uuid": "ca10fcd7-a7c5-4341-8778-1095436f5bcf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779190200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fb9f921e-d798-4c99-96e1-2de8e2e52497",
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task: I need to launch a SmolVLA baseline eval (no Smart Compress) on LIBERO-Spatial suite on server cqa1-33015. Let me first check the registry for any existing eval specs, then SSH to the server to find the eval script and set things up.

Let me load the necessary tools first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "19d4b88a-39b3-4d93-a809-f3b1826f4c02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4QN47sMWMquF3Uy8gjXfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12798,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12798
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jm1t9vJnwscdmK5TWPT8AN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c20bb70e-4526-46e5-823b-76f32f8a3806",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4QN47sMWMquF3Uy8gjXfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12798,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12798
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 6 · 2026-05-19T11:11:40.257Z_

<details><summary>↩ Tool result · `toolu_01Jm1t9vJnwscdmK5TWPT8AN`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "a1e78d77-f60d-42ef-a506-8d347b69fd99",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

先查 registry 中已有的 baseline eval 记录，同时探查服务器上的 eval 脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "2a9f6956-1797-41d2-ade9-c265bcf7a12a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8rNDaRkg3qnA8AWB9mRhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1891,
      "cache_read_input_tokens": 24639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1891
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019wEg8822eNadPbhkvBhuow`</summary>

```json
{
  "filters": {
    "exp_id": "eval_smolvla_base_libero"
  },
  "project": "importance_margin_vla_compress",
  "fields": [
    "*"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "cdb7b4bb-1b29-4e58-a36c-b67d19a6035f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8rNDaRkg3qnA8AWB9mRhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1891,
      "cache_read_input_tokens": 24639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1891
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

_source line 9 · 2026-05-19T11:11:45.019Z_

<details><summary>↩ Tool result · `toolu_019wEg8822eNadPbhkvBhuow`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4059}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "78f906cd-a6da-418b-bd9b-a74733f302ce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4059}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4059}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011Citwsk2cMWiNvijn4NP49`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls eval_*libero*.py 2>/dev/null; echo \"---\"; ls eval_*.py 2>/dev/null; echo \"---\"; ls *.py | head -30",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "8798bae2-9d09-418e-9d2f-a4fddd9b8cb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8rNDaRkg3qnA8AWB9mRhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1891,
      "cache_read_input_tokens": 24639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1891
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

_source line 11 · 2026-05-19T11:11:47.762Z_

<details><summary>↩ Tool result · `toolu_011Citwsk2cMWiNvijn4NP49`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_smart_compress_libero.py\\neval_success_rate_libero.py\\n---\\neval_geometric_prior.py\\neval_geometric_prior_k05.py\\neval_geometric_prior_k07.py\\neval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_random_prune_smolvla.py\\neval_sim.py\\neval_smart_compress.py\\neval_smart_compress_libero.py\\neval_success_rate.py\\neval_success_rate_libero.py\\n---\\n_lerobot_compat.py\\nanalyze_gate.py\\ndiag_ep42.py\\ndryrun_pi05.py\\ndryrun_pi05_v2.py\\ndryrun_pi05_v3.py\\neval_geometric_prior.py\\neval_geometric_prior_k05.py\\neval_geometric_prior_k07.py\\neval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_random_prune_smolvla.py\\neval_sim.py\\neval_smart_compress.py\\neval_smart_compress_libero.py\\neval_success_rate.py\\neval_success_rate_libero.py\\nevaluate.py\\ngeometric_prior_pruning.py\\nmeasure_inference_latency.py\\nmeasure_smolvla_entropy_perlayer.py\\nmeasure_smolvla_entropy_perlayer_fixed.py\\nscan_collapse.py\\nsmart_compress_module.py\\ntest_fullft.py\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.07}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "9b9952c2-9b03-491f-8187-f024d8420cae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_libero_100k_sr.py\\\\neval_libero_10k_diversity.py\\\\neval_libero_10k_sim.py\\\\neval_libero_fullft_100k.py\\\\neval_pi05_libero.py\\\\neval_smart_compress_libero.py\\\\neval_success_rate_libero.py\\\\n---\\\\neval_geometric_prior.py\\\\neval_geometric_prior_k05.py\\\\neval_geometric_prior_k07.py\\\\neval_libero_100k_sr.py\\\\neval_libero_10k_diversity.py\\\\neval_libero_10k_sim.py\\\\neval_libero_fullft_100k.py\\\\neval_pi05_libero.py\\\\neval_random_prune_smolvla.py\\\\neval_sim.py\\\\neval_smart_compress.py\\\\neval_smart_compress_libero.py\\\\neval_success_rate.py\\\\neval_success_rate_libero.py\\\\n---\\\\n_lerobot_compat.py\\\\nanalyze_gate.py\\\\ndiag_ep42.py\\\\ndryrun_pi05.py\\\\ndryrun_pi05_v2.py\\\\ndryrun_pi05_v3.py\\\\neval_geometric_prior.py\\\\neval_geometric_prior_k05.py\\\\neval_geometric_prior_k07.py\\\\neval_libero_100k_sr.py\\\\neval_libero_10k_diversity.py\\\\neval_libero_10k_sim.py\\\\neval_libero_fullft_100k.py\\\\neval_pi05_libero.py\\\\neval_random_prune_smolvla.py\\\\neval_sim.py\\\\neval_smart_compress.py\\\\neval_smart_compress_libero.py\\\\neval_success_rate.py\\\\neval_success_rate_libero.py\\\\nevaluate.py\\\\ngeometric_prior_pruning.py\\\\nmeasure_inference_latency.py\\\\nmeasure_smolvla_entropy_perlayer.py\\\\nmeasure_smolvla_entropy_perlayer_fixed.py\\\\nscan_collapse.py\\\\nsmart_compress_module.py\\\\ntest_fullft.py\\\\ntest_inference_fixes.py\\\\ntest_mode_collapse.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.07}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_smart_compress_libero.py\\neval_success_rate_libero.py\\n---\\neval_geometric_prior.py\\neval_geometric_prior_k05.py\\neval_geometric_prior_k07.py\\neval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_random_prune_smolvla.py\\neval_sim.py\\neval_smart_compress.py\\neval_smart_compress_libero.py\\neval_success_rate.py\\neval_success_rate_libero.py\\n---\\n_lerobot_compat.py\\nanalyze_gate.py\\ndiag_ep42.py\\ndryrun_pi05.py\\ndryrun_pi05_v2.py\\ndryrun_pi05_v3.py\\neval_geometric_prior.py\\neval_geometric_prior_k05.py\\neval_geometric_prior_k07.py\\neval_libero_100k_sr.py\\neval_libero_10k_diversity.py\\neval_libero_10k_sim.py\\neval_libero_fullft_100k.py\\neval_pi05_libero.py\\neval_random_prune_smolvla.py\\neval_sim.py\\neval_smart_compress.py\\neval_smart_compress_libero.py\\neval_success_rate.py\\neval_success_rate_libero.py\\nevaluate.py\\ngeometric_prior_pruning.py\\nmeasure_inference_latency.py\\nmeasure_smolvla_entropy_perlayer.py\\nmeasure_smolvla_entropy_perlayer_fixed.py\\nscan_collapse.py\\nsmart_compress_module.py\\ntest_fullft.py\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.07}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Let me check the registry for any existing baseline eval with a broader search, and also look at the eval scripts that might be the baseline (no smart compress). `eval_success_rate_libero.py` seems like a good candidate. Let me also check if there's a previous LIBERO-Object baseline eval in the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "7c1fedf4-8fbf-48cc-aaa1-ce26a771467e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2azLr3fvXZqBwWptEkZnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 26530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

找到了多个 eval 脚本。`eval_success_rate_libero.py` 最可能是 baseline eval 脚本。让我查看它的内容，同时搜索 registry 中已有的 baseline eval 记录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "26a952f4-3765-4b24-a69f-4287d2773d61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2azLr3fvXZqBwWptEkZnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 26530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015dnkkpCM64msx4DCu9UsNE`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && cat eval_success_rate_libero.py",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "415b9d30-2997-4f42-af6b-59c2d36089ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2azLr3fvXZqBwWptEkZnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 26530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 15 · 2026-05-19T11:11:54.878Z_

<details><summary>↩ Tool result · `toolu_015dnkkpCM64msx4DCu9UsNE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50,\\n                   help=\\\"Episodes per task\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--action_horizon\\\", type=int, default=50,\\n                   help=\\\"Actions to execute per chunk before re-planning\\\")\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None,\\n                   help=\\\"Override max steps per episode (default: per-suite)\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"random_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None,\\n                   help=\\\"Comma-separated task IDs to evaluate (default: all)\\\")\\n    p.add_argument(\\\"--pruning-method\\\", type=str, default=\\\"zero_mask\\\",\\n                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n    p.add_argument(\\\"--merge_alpha\\\", type=float, default=1.0,\\n                   help=\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=None,\\n                   help=\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\")\\n    return p.parse_args()\\n\\n\\n# --- Config -------------------------------------------------------------------\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    c\\n\\n... [截断: 输出过长，省略 11793 字符] ...\\n\\n= args.action_horizon:\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                    if args.mode == \\\"acis_prune\\\":\\n                        mask = compute_acis_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    elif args.mode == \\\"random_prune\\\":\\n                        mask = compute_random_mask(wrapper, batch, device, policy=policy, k_ratio=args.k_ratio)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    else:\\n                        action_chunk = predict_actions(policy, batch)\\n\\n                    action_idx = 0\\n\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\n                action = np.clip(action, -1.0, 1.0)\\n                action_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(action)\\n\\n                if info.get(\\\"is_success\\\", False):\\n                    success = True\\n                    break\\n\\n                if terminated or truncated:\\n                    break\\n\\n            ep_steps = step + 1\\n            task_successes.append(success)\\n            task_lengths.append(ep_steps)\\n\\n            log.info(\\n                \\\"  Ep %d/%d | %s | steps=%d\\\",\\n                ep + 1, args.num_episodes,\\n                \\\"SUCCESS\\\" if success else \\\"FAIL\\\", ep_steps,\\n            )\\n\\n        env.close()\\n\\n        n_succ = sum(task_successes)\\n        n_total = len(task_successes)\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\n\\n        all_task_results[task_id] = {\\n            \\\"task_id\\\": task_id,\\n            \\\"task_description\\\": task_desc,\\n            \\\"success_count\\\": n_succ,\\n            \\\"total_episodes\\\": n_total,\\n            \\\"success_rate\\\": round(sr, 4),\\n            \\\"mean_steps\\\": round(float(np.mean(task_lengths)), 1),\\n        }\\n        total_successes += n_succ\\n        total_episodes += n_total\\n\\n        log.info(\\\"  Task %d SR: %d/%d (%.1f%%)\\\", task_id, n_succ, n_total, sr * 100)\\n\\n    # Overall\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\n\\n    log.info(\\\"=\\\" * 60)\\n    log.info(\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\", args.suite, args.mode, args.pruning_method)\\n    log.info(\\\"Overall SR: %d/%d (%.1f%%)\\\", total_successes, total_episodes, overall_sr * 100)\\n    log.info(\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\", ci_lo * 100, ci_hi * 100)\\n\\n    for tid, tr in sorted(all_task_results.items()):\\n        log.info(\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\",\\n                 tid, tr[\\\"success_rate\\\"] * 100, tr[\\\"success_count\\\"],\\n                 tr[\\\"total_episodes\\\"], tr[\\\"task_description\\\"])\\n    log.info(\\\"=\\\" * 60)\\n\\n    summary = {\\n        \\\"suite\\\": args.suite,\\n        \\\"mode\\\": args.mode,\\n        \\\"pruning_method\\\": args.pruning_method,\\n        \\\"checkpoint\\\": args.checkpoint,\\n        \\\"config\\\": args.config,\\n        \\\"total_episodes\\\": total_episodes,\\n        \\\"total_successes\\\": total_successes,\\n        \\\"overall_success_rate\\\": round(overall_sr, 4),\\n        \\\"wilson_ci_95\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\n        \\\"num_episodes_per_task\\\": args.num_episodes,\\n        \\\"max_steps\\\": max_steps,\\n        \\\"action_horizon\\\": args.action_horizon,\\n        \\\"seed\\\": args.seed,\\n        \\\"merge_alpha\\\": args.merge_alpha,\\n        \\\"per_task\\\": all_task_results,\\n    }\\n\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(summary, f, indent=2)\\n    log.info(\\\"Results saved to %s\\\", output_path)\\n\\n    return summary\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_evaluation(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "863407cc-1596-49b4-984b-375a8f96dc3f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\\\n\\\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\\\n\\\\nUsage:\\\\n    python eval_success_rate_libero.py \\\\\\\\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\\\\\\\n        --config configs/libero_baseline.yaml \\\\\\\\\\\\n        --suite libero_object \\\\\\\\\\\\n        --num_episodes 50 \\\\\\\\\\\\n        --gpu 0\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSUITE_MAX_STEPS = {\\\\n    \\\\\\\"libero_spatial\\\\\\\": 280,\\\\n    \\\\\\\"libero_object\\\\\\\": 280,\\\\n    \\\\\\\"libero_goal\\\\\\\": 300,\\\\n    \\\\\\\"libero_10\\\\\\\": 520,\\\\n    \\\\\\\"libero_90\\\\\\\": 400,\\\\n}\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"LIBERO success rate evaluation\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--checkpoint\\\\\\\", type=str, required=True,\\\\n                   help=\\\\\\\"Path to checkpoint.pt\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--config\\\\\\\", type=str, default=\\\\\\\"configs/libero_baseline.yaml\\\\\\\",\\\\n                   help=\\\\\\\"Path to YAML config\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", type=str, default=\\\\\\\"libero_object\\\\\\\",\\\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\\\n                   help=\\\\\\\"LIBERO suite name\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=50,\\\\n                   help=\\\\\\\"Episodes per task\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--action_horizon\\\\\\\", type=int, default=50,\\\\n                   help=\\\\\\\"Actions to execute per chunk before re-planning\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--max_steps\\\\\\\", type=int, default=None,\\\\n                   help=\\\\\\\"Override max steps per episode (default: per-suite)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--output\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", choices=[\\\\\\\"baseline\\\\\\\", \\\\\\\"acis_prune\\\\\\\", \\\\\\\"random_prune\\\\\\\"], default=\\\\\\\"baseline\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Comma-separated task IDs to evaluate (default: all)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--pruning-method\\\\\\\", type=str, default=\\\\\\\"zero_mask\\\\\\\",\\\\n                   choices=[\\\\\\\"zero_mask\\\\\\\", \\\\\\\"true_removal\\\\\\\", \\\\\\\"merge\\\\\\\"],\\\\n                   help=\\\\\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--merge_alpha\\\\\\\", type=float, default=1.0,\\\\n                   help=\\\\\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--k_ratio\\\\\\\", type=float, default=None,\\\\n                   help=\\\\\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\n# --- Config -------------------------------------------------------------------\\\\n\\\\ndef load_config(config_path: str) -> dict:\\\\n    import copy\\\\n    import yaml\\\\n    config_path = Path(config_path)\\\\n    with open(config_path) as f:\\\\n        config = yaml.safe_load(f)\\\\n    if \\\\\\\"_base_\\\\\\\" in config:\\\\n        base_path = config_path.parent / config.pop(\\\\\\\"_base_\\\\\\\")\\\\n        base_config = load_config(str(base_path))\\\\n        for k, v in config.items():\\\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\\\n                base_config[k].update(v)\\\\n            else:\\\\n                base_config[k] = v\\\\n        return base_config\\\\n    return config\\\\n\\\\n\\\\n# --- Model loading ------------------------------------------------------------\\\\n\\\\ndef load_model(args, device: torch.device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Returns (policy, wrapper_or_None, config).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from train import load_smolvla_policy, wrap_with_imm\\\\n\\\\n    c\\\\n\\\\n... [截断: 输出过长，省略 11793 字符] ...\\\\n\\\\n= args.action_horizon:\\\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\\\n\\\\n                    if args.mode == \\\\\\\"acis_prune\\\\\\\":\\\\n                        mask = compute_acis_mask(wrapper, batch, device)\\\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n                        hook_handle.remove()\\\\n                    elif args.mode == \\\\\\\"random_prune\\\\\\\":\\\\n                        mask = compute_random_mask(wrapper, batch, device, policy=policy, k_ratio=args.k_ratio)\\\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n                        hook_handle.remove()\\\\n                    else:\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n\\\\n                    action_idx = 0\\\\n\\\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\\\n                action = np.clip(action, -1.0, 1.0)\\\\n                action_idx += 1\\\\n\\\\n                obs, reward, terminated, truncated, info = env.step(action)\\\\n\\\\n                if info.get(\\\\\\\"is_success\\\\\\\", False):\\\\n                    success = True\\\\n                    break\\\\n\\\\n                if terminated or truncated:\\\\n                    break\\\\n\\\\n            ep_steps = step + 1\\\\n            task_successes.append(success)\\\\n            task_lengths.append(ep_steps)\\\\n\\\\n            log.info(\\\\n                \\\\\\\"  Ep %d/%d | %s | steps=%d\\\\\\\",\\\\n                ep + 1, args.num_episodes,\\\\n                \\\\\\\"SUCCESS\\\\\\\" if success else \\\\\\\"FAIL\\\\\\\", ep_steps,\\\\n            )\\\\n\\\\n        env.close()\\\\n\\\\n        n_succ = sum(task_successes)\\\\n        n_total = len(task_successes)\\\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\\\n\\\\n        all_task_results[task_id] = {\\\\n            \\\\\\\"task_id\\\\\\\": task_id,\\\\n            \\\\\\\"task_description\\\\\\\": task_desc,\\\\n            \\\\\\\"success_count\\\\\\\": n_succ,\\\\n            \\\\\\\"total_episodes\\\\\\\": n_total,\\\\n            \\\\\\\"success_rate\\\\\\\": round(sr, 4),\\\\n            \\\\\\\"mean_steps\\\\\\\": round(float(np.mean(task_lengths)), 1),\\\\n        }\\\\n        total_successes += n_succ\\\\n        total_episodes += n_total\\\\n\\\\n        log.info(\\\\\\\"  Task %d SR: %d/%d (%.1f%%)\\\\\\\", task_id, n_succ, n_total, sr * 100)\\\\n\\\\n    # Overall\\\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\\\n\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    log.info(\\\\\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\\\\\", args.suite, args.mode, args.pruning_method)\\\\n    log.info(\\\\\\\"Overall SR: %d/%d (%.1f%%)\\\\\\\", total_successes, total_episodes, overall_sr * 100)\\\\n    log.info(\\\\\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\\\\\", ci_lo * 100, ci_hi * 100)\\\\n\\\\n    for tid, tr in sorted(all_task_results.items()):\\\\n        log.info(\\\\\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\\\\\",\\\\n                 tid, tr[\\\\\\\"success_rate\\\\\\\"] * 100, tr[\\\\\\\"success_count\\\\\\\"],\\\\n                 tr[\\\\\\\"total_episodes\\\\\\\"], tr[\\\\\\\"task_description\\\\\\\"])\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n\\\\n    summary = {\\\\n        \\\\\\\"suite\\\\\\\": args.suite,\\\\n        \\\\\\\"mode\\\\\\\": args.mode,\\\\n        \\\\\\\"pruning_method\\\\\\\": args.pruning_method,\\\\n        \\\\\\\"checkpoint\\\\\\\": args.checkpoint,\\\\n        \\\\\\\"config\\\\\\\": args.config,\\\\n        \\\\\\\"total_episodes\\\\\\\": total_episodes,\\\\n        \\\\\\\"total_successes\\\\\\\": total_successes,\\\\n        \\\\\\\"overall_success_rate\\\\\\\": round(overall_sr, 4),\\\\n        \\\\\\\"wilson_ci_95\\\\\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\\\n        \\\\\\\"num_episodes_per_task\\\\\\\": args.num_episodes,\\\\n        \\\\\\\"max_steps\\\\\\\": max_steps,\\\\n        \\\\\\\"action_horizon\\\\\\\": args.action_horizon,\\\\n        \\\\\\\"seed\\\\\\\": args.seed,\\\\n        \\\\\\\"merge_alpha\\\\\\\": args.merge_alpha,\\\\n        \\\\\\\"per_task\\\\\\\": all_task_results,\\\\n    }\\\\n\\\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(summary, f, indent=2)\\\\n    log.info(\\\\\\\"Results saved to %s\\\\\\\", output_path)\\\\n\\\\n    return summary\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    args = parse_args()\\\\n    run_evaluation(args)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.73}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50,\\n                   help=\\\"Episodes per task\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--action_horizon\\\", type=int, default=50,\\n                   help=\\\"Actions to execute per chunk before re-planning\\\")\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None,\\n                   help=\\\"Override max steps per episode (default: per-suite)\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"random_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None,\\n                   help=\\\"Comma-separated task IDs to evaluate (default: all)\\\")\\n    p.add_argument(\\\"--pruning-method\\\", type=str, default=\\\"zero_mask\\\",\\n                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n    p.add_argument(\\\"--merge_alpha\\\", type=float, default=1.0,\\n                   help=\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=None,\\n                   help=\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\")\\n    return p.parse_args()\\n\\n\\n# --- Config -------------------------------------------------------------------\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    c\\n\\n... [截断: 输出过长，省略 11793 字符] ...\\n\\n= args.action_horizon:\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                    if args.mode == \\\"acis_prune\\\":\\n                        mask = compute_acis_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    elif args.mode == \\\"random_prune\\\":\\n                        mask = compute_random_mask(wrapper, batch, device, policy=policy, k_ratio=args.k_ratio)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    else:\\n                        action_chunk = predict_actions(policy, batch)\\n\\n                    action_idx = 0\\n\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\n                action = np.clip(action, -1.0, 1.0)\\n                action_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(action)\\n\\n                if info.get(\\\"is_success\\\", False):\\n                    success = True\\n                    break\\n\\n                if terminated or truncated:\\n                    break\\n\\n            ep_steps = step + 1\\n            task_successes.append(success)\\n            task_lengths.append(ep_steps)\\n\\n            log.info(\\n                \\\"  Ep %d/%d | %s | steps=%d\\\",\\n                ep + 1, args.num_episodes,\\n                \\\"SUCCESS\\\" if success else \\\"FAIL\\\", ep_steps,\\n            )\\n\\n        env.close()\\n\\n        n_succ = sum(task_successes)\\n        n_total = len(task_successes)\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\n\\n        all_task_results[task_id] = {\\n            \\\"task_id\\\": task_id,\\n            \\\"task_description\\\": task_desc,\\n            \\\"success_count\\\": n_succ,\\n            \\\"total_episodes\\\": n_total,\\n            \\\"success_rate\\\": round(sr, 4),\\n            \\\"mean_steps\\\": round(float(np.mean(task_lengths)), 1),\\n        }\\n        total_successes += n_succ\\n        total_episodes += n_total\\n\\n        log.info(\\\"  Task %d SR: %d/%d (%.1f%%)\\\", task_id, n_succ, n_total, sr * 100)\\n\\n    # Overall\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\n\\n    log.info(\\\"=\\\" * 60)\\n    log.info(\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\", args.suite, args.mode, args.pruning_method)\\n    log.info(\\\"Overall SR: %d/%d (%.1f%%)\\\", total_successes, total_episodes, overall_sr * 100)\\n    log.info(\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\", ci_lo * 100, ci_hi * 100)\\n\\n    for tid, tr in sorted(all_task_results.items()):\\n        log.info(\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\",\\n                 tid, tr[\\\"success_rate\\\"] * 100, tr[\\\"success_count\\\"],\\n                 tr[\\\"total_episodes\\\"], tr[\\\"task_description\\\"])\\n    log.info(\\\"=\\\" * 60)\\n\\n    summary = {\\n        \\\"suite\\\": args.suite,\\n        \\\"mode\\\": args.mode,\\n        \\\"pruning_method\\\": args.pruning_method,\\n        \\\"checkpoint\\\": args.checkpoint,\\n        \\\"config\\\": args.config,\\n        \\\"total_episodes\\\": total_episodes,\\n        \\\"total_successes\\\": total_successes,\\n        \\\"overall_success_rate\\\": round(overall_sr, 4),\\n        \\\"wilson_ci_95\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\n        \\\"num_episodes_per_task\\\": args.num_episodes,\\n        \\\"max_steps\\\": max_steps,\\n        \\\"action_horizon\\\": args.action_horizon,\\n        \\\"seed\\\": args.seed,\\n        \\\"merge_alpha\\\": args.merge_alpha,\\n        \\\"per_task\\\": all_task_results,\\n    }\\n\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(summary, f, indent=2)\\n    log.info(\\\"Results saved to %s\\\", output_path)\\n\\n    return summary\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_evaluation(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0176HsetBn435J83A7NB4QB6`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "project": "importance_margin_vla_compress",
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics",
    "spec"
  ],
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "2bc9ce78-d506-4fdf-a262-2c6c90dc9568",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2azLr3fvXZqBwWptEkZnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 26530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 17 · 2026-05-19T11:11:55.215Z_

<details><summary>↩ Tool result · `toolu_0176HsetBn435J83A7NB4QB6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_official + VisionTokenCompressor(M=32)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160116, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\", \"gpu_ids\": [\"cuda:3\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.534, \"wilson_ci_95\": [0.4902, 0.5773], \"total_episodes\": 500, \"total_successes\": 267, \"per_task_sr\": {\"task0_alphabet_soup\": 0.64, \"task1_cream_cheese\": 0.48, \"task2_salad_dressing\": 0.56, \"task3_bbq_sauce\": 0.46, \"task4_ketchup\": 0.46, \"task5_tomato_sauce\": 0.28, \"task6_butter\": 0.78, \"task7_milk\": 0.42, \"task8_chocolate_pudding\": 0.66, \"task9_orange_juice\": 0.6}}}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 164042, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160877, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\", \"server\": \"westd-27271\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 480299, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\", \"tmux_session\": \"eval_m128_s44\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128_seed44\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.602, \"total_successes\": 301, \"total_episodes\": 500, \"wilson_ci_95\": [0.5585, 0.644], \"per_task_sr\": {\"alphabet_soup\": 0.54, \"cream_cheese\": 0.3, \"salad_dressing\": 0.62, \"bbq_sauce\": 0.5, \"ketchup\": 0.86, \"tomato_sauce\": 0.4, \"butter\": 0.66, \"milk\": 0.72, \"chocolate_pudding\": 0.88, \"orange_juice\": 0.54}}}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 162254, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": \"full LIBERO dataset\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 764777, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 763351, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 762596, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"data_count\": 0, \"model_name\": \"SmolVLA+VisionTokenCompressor_M128\", \"seed\": 44, \"gpu_ids\": [\"cuda:1\"], \"tmux_session\": \"train_m128_s44\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 355272, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\", \"tmux_session\": \"eval_openvla_k095\", \"pruning_method\": \"random + true_removal\", \"k_ratio\": 0.95, \"vision_tokens\": \"256 -> 243 (remove 13)\"}, \"metrics\": {\"success_rate\": 69.4, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 7, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"pid\": 354653, \"pruning\": \"random, true_removal, k=0.9\", \"vision_tokens\": \"256 -> 230\"}, \"metrics\": {\"success_rate\": 62, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 470232, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\", \"submitted_at\": \"2026-05-18T23:23:07.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m32_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_seed43\", \"wall_clock_seconds\": 5572.6, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 59.2, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 424163, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\", \"submitted_at\": \"2026-05-18T23:01:14.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_spatial\", \"wall_clock_seconds\": 6884.4, \"gpu_hours\": 1.91}, \"metrics\": {\"success_rate\": 53.2, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"num_episodes\": 500, \"suite\": \"libero_spatial\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 560607, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\", \"submitted_at\": \"2026-05-18T23:58:31.377Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m64_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m64_seed43\", \"wall_clock_seconds\": 3446.5, \"gpu_hours\": 0.96}, \"metrics\": {\"success_rate\": 60, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 571598, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"submitted_at\": \"2026-05-19T00:01:35.221Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\", \"wall_clock_seconds\": 3261.2, \"gpu_hours\": 0.91}, \"metrics\": {\"success_rate\": 56.4, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"num_episodes\": 500, \"suite\": \"libero_goal\"}, \"conclusion\": \"success\"}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 394430, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\", \"submitted_at\": \"2026-05-18T22:26:42.237Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_baseline_control_prune_k05\", \"pruning_method\": \"random + zero_mask\", \"k_ratio\": 0.5, \"wall_clock_seconds\": 5583.9, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": null, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 43, \"checkpoint_source\": null, \"eval_data\": null, \"config\": \"configs/smart_compress_m64_seed43.yaml\", \"log_path\": \"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\", \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"pid\": 202271, \"total_steps\": 100000}, \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"200291\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 322232, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\", \"submitted_at\": \"2026-05-18T21:31:55.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m96_seed43_v2\", \"wall_clock_seconds\": 5335.1, \"gpu_hours\": 1.48}, \"metrics\": {\"success_rate\": 58.2, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"num_episodes\": 500, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}, \"conclusion\": \"success\"}}, \"count\": 20, \"total\": 110, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3108}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "3e7660a4-09f9-4442-885b-672511616a25",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_official + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 160116, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\\\", \\\"gpu_ids\\\": [\\\"cuda:3\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_official/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.534, \\\"wilson_ci_95\\\": [0.4902, 0.5773], \\\"total_episodes\\\": 500, \\\"total_successes\\\": 267, \\\"per_task_sr\\\": {\\\"task0_alphabet_soup\\\": 0.64, \\\"task1_cream_cheese\\\": 0.48, \\\"task2_salad_dressing\\\": 0.56, \\\"task3_bbq_sauce\\\": 0.46, \\\"task4_ketchup\\\": 0.46, \\\"task5_tomato_sauce\\\": 0.28, \\\"task6_butter\\\": 0.78, \\\"task7_milk\\\": 0.42, \\\"task8_chocolate_pudding\\\": 0.66, \\\"task9_orange_juice\\\": 0.6}}}, \\\"eval_smart_compress_m96_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 164042, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.528, \\\"total_successes\\\": 264, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.4842, 0.5714]}}, \\\"eval_smart_compress_m32_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 160877, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.596, \\\"total_successes\\\": 298, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.5524, 0.6381]}}, \\\"eval_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 480299, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\\\", \\\"tmux_session\\\": \\\"eval_m128_s44\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m128_seed44\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m128_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.602, \\\"total_successes\\\": 301, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.5585, 0.644], \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0.54, \\\"cream_cheese\\\": 0.3, \\\"salad_dressing\\\": 0.62, \\\"bbq_sauce\\\": 0.5, \\\"ketchup\\\": 0.86, \\\"tomato_sauce\\\": 0.4, \\\"butter\\\": 0.66, \\\"milk\\\": 0.72, \\\"chocolate_pudding\\\": 0.88, \\\"orange_juice\\\": 0.54}}}, \\\"eval_smart_compress_m64_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 162254, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.644, \\\"total_successes\\\": 322, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.6011, 0.6847]}}, \\\"train_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress\\\", \\\"data_count\\\": \\\"full LIBERO dataset\\\", \\\"model_name\\\": \\\"smart_compress_m32\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\\\", \\\"checkpoint_source\\\": \\\"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 764777, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_smart_compress_m64_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 763351, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_smart_compress_m32_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 762596, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/data\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"SmolVLA+VisionTokenCompressor_M128\\\", \\\"seed\\\": 44, \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"train_m128_s44\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 355272, \\\"data_path\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"OpenVLA-7B-libero-object\\\", \\\"seed\\\": 7, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\\\", \\\"tmux_session\\\": \\\"eval_openvla_k095\\\", \\\"pruning_method\\\": \\\"random + true_removal\\\", \\\"k_ratio\\\": 0.95, \\\"vision_tokens\\\": \\\"256 -> 243 (remove 13)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 69.4, \\\"per_task_sr\\\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_openvla_prune_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-object\\\", \\\"seed\\\": 7, \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object (10 tasks x 50 episodes)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"pid\\\": 354653, \\\"pruning\\\": \\\"random, true_removal, k=0.9\\\", \\\"vision_tokens\\\": \\\"256 -> 230\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 62, \\\"per_task_sr\\\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 470232, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:23:07.575Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_seed43\\\", \\\"wall_clock_seconds\\\": 5572.6, \\\"gpu_hours\\\": 1.55}, \\\"metrics\\\": {\\\"success_rate\\\": 59.2, \\\"per_task_sr\\\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_libero_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 424163, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:01:14.874Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32 (seed=42)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_libero_spatial\\\", \\\"wall_clock_seconds\\\": 6884.4, \\\"gpu_hours\\\": 1.91}, \\\"metrics\\\": {\\\"success_rate\\\": 53.2, \\\"per_task_sr\\\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_spatial\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 560607, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:58:31.377Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m64_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m64_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m64_seed43\\\", \\\"wall_clock_seconds\\\": 3446.5, \\\"gpu_hours\\\": 0.96}, \\\"metrics\\\": {\\\"success_rate\\\": 60, \\\"per_task_sr\\\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m32_libero_goal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 571598, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T00:01:35.221Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32 (seed=42)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_libero_goal\\\", \\\"wall_clock_seconds\\\": 3261.2, \\\"gpu_hours\\\": 0.91}, \\\"metrics\\\": {\\\"success_rate\\\": 56.4, \\\"per_task_sr\\\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_goal\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_baseline_control_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 394430, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T22:26:42.237Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"baseline_control_100k_v2\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/baseline_control/latest/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_baseline_control_prune_k05\\\", \\\"pruning_method\\\": \\\"random + zero_mask\\\", \\\"k_ratio\\\": 0.5, \\\"wall_clock_seconds\\\": 5583.9, \\\"gpu_hours\\\": 1.55}, \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": null, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": null, \\\"eval_data\\\": null, \\\"config\\\": \\\"configs/smart_compress_m64_seed43.yaml\\\", \\\"log_path\\\": \\\"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed43/checkpoint.pt\\\", \\\"pid\\\": 202271, \\\"total_steps\\\": 100000}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"200291\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\\\", \\\"submitted_via\\\": \\\"tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"eval_data\\\": \\\"HuggingFaceVLA/libero\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed43/checkpoint.pt\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_smart_compress_m96_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 322232, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\\\", \\\"submitted_at\\\": \\\"2026-05-18T21:31:55.572Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m96_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m96_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m96_seed43_v2\\\", \\\"wall_clock_seconds\\\": 5335.1, \\\"gpu_hours\\\": 1.48}, \\\"metrics\\\": {\\\"success_rate\\\": 58.2, \\\"per_task_sr\\\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\", \\\"wilson_ci_95\\\": [53.8, 62.4]}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 20, \\\"total\\\": 110, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3108}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_official + VisionTokenCompressor(M=32)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160116, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\", \"gpu_ids\": [\"cuda:3\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.534, \"wilson_ci_95\": [0.4902, 0.5773], \"total_episodes\": 500, \"total_successes\": 267, \"per_task_sr\": {\"task0_alphabet_soup\": 0.64, \"task1_cream_cheese\": 0.48, \"task2_salad_dressing\": 0.56, \"task3_bbq_sauce\": 0.46, \"task4_ketchup\": 0.46, \"task5_tomato_sauce\": 0.28, \"task6_butter\": 0.78, \"task7_milk\": 0.42, \"task8_chocolate_pudding\": 0.66, \"task9_orange_juice\": 0.6}}}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 164042, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160877, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\", \"server\": \"westd-27271\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 480299, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\", \"tmux_session\": \"eval_m128_s44\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128_seed44\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.602, \"total_successes\": 301, \"total_episodes\": 500, \"wilson_ci_95\": [0.5585, 0.644], \"per_task_sr\": {\"alphabet_soup\": 0.54, \"cream_cheese\": 0.3, \"salad_dressing\": 0.62, \"bbq_sauce\": 0.5, \"ketchup\": 0.86, \"tomato_sauce\": 0.4, \"butter\": 0.66, \"milk\": 0.72, \"chocolate_pudding\": 0.88, \"orange_juice\": 0.54}}}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 162254, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": \"full LIBERO dataset\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 764777, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 763351, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 762596, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"conclusion\": \"killed\"}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"data_count\": 0, \"model_name\": \"SmolVLA+VisionTokenCompressor_M128\", \"seed\": 44, \"gpu_ids\": [\"cuda:1\"], \"tmux_session\": \"train_m128_s44\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 355272, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\", \"tmux_session\": \"eval_openvla_k095\", \"pruning_method\": \"random + true_removal\", \"k_ratio\": 0.95, \"vision_tokens\": \"256 -> 243 (remove 13)\"}, \"metrics\": {\"success_rate\": 69.4, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 7, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"pid\": 354653, \"pruning\": \"random, true_removal, k=0.9\", \"vision_tokens\": \"256 -> 230\"}, \"metrics\": {\"success_rate\": 62, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 470232, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\", \"submitted_at\": \"2026-05-18T23:23:07.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m32_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_seed43\", \"wall_clock_seconds\": 5572.6, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 59.2, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 424163, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\", \"submitted_at\": \"2026-05-18T23:01:14.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_spatial\", \"wall_clock_seconds\": 6884.4, \"gpu_hours\": 1.91}, \"metrics\": {\"success_rate\": 53.2, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"num_episodes\": 500, \"suite\": \"libero_spatial\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 560607, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\", \"submitted_at\": \"2026-05-18T23:58:31.377Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m64_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m64_seed43\", \"wall_clock_seconds\": 3446.5, \"gpu_hours\": 0.96}, \"metrics\": {\"success_rate\": 60, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 571598, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"submitted_at\": \"2026-05-19T00:01:35.221Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\", \"wall_clock_seconds\": 3261.2, \"gpu_hours\": 0.91}, \"metrics\": {\"success_rate\": 56.4, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"num_episodes\": 500, \"suite\": \"libero_goal\"}, \"conclusion\": \"success\"}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 394430, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\", \"submitted_at\": \"2026-05-18T22:26:42.237Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_baseline_control_prune_k05\", \"pruning_method\": \"random + zero_mask\", \"k_ratio\": 0.5, \"wall_clock_seconds\": 5583.9, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\"}, \"conclusion\": \"success\"}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": null, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 43, \"checkpoint_source\": null, \"eval_data\": null, \"config\": \"configs/smart_compress_m64_seed43.yaml\", \"log_path\": \"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\", \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"pid\": 202271, \"total_steps\": 100000}, \"conclusion\": \"success\"}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"200291\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\"}, \"conclusion\": \"success\"}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 322232, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\", \"submitted_at\": \"2026-05-18T21:31:55.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m96_seed43_v2\", \"wall_clock_seconds\": 5335.1, \"gpu_hours\": 1.48}, \"metrics\": {\"success_rate\": 58.2, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"num_episodes\": 500, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}, \"conclusion\": \"success\"}}, \"count\": 20, \"total\": 110, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3108}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
I can see from the registry that there are previous eval experiments. I need to find the baseline eval for LIBERO-Object (the one that gave SR=44.8%). Let me search the registry specifically for baseline-related experiments. Also, I need to understand the `eval_success_rate_libero.py` script better - it has a `--mode baseline` option which means no pruning.

Looking at the script, the key things I need:
1. A checkpoint for the baseline SmolVLA model (no Smart Compress)
2. The config file for baseline
3. The command with `--mode baseline --suite libero_spatial`


I found a baseline control experiment in the registry, but that's not quite right - I need the original SmolVLA baseline eval that achieved 44.8% on LIBERO-Object, not the baseline_control variant. Let me search more carefully through the registry for that specific experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "ea67863f-f4f6-4e5a-96d3-2ee05375b54b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjJvpCuof9hjCACfhZQ5Ck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12173,
      "cache_read_input_tokens": 27619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12173
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

_source line 19_

需要找到之前 LIBERO-Object baseline eval（SR=44.8%）的配置。让我搜索 registry 中的 baseline 记录和服务器上的 checkpoint。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "efc5b862-bdd7-4f8c-b84e-acac39fc7461",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjJvpCuof9hjCACfhZQ5Ck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12173,
      "cache_read_input_tokens": 27619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12173
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HdC5DEBChJDkSUk8FDwN5A`</summary>

```json
{
  "filters": {
    "exp_id": "eval_smolvla_baseline"
  },
  "project": "importance_margin_vla_compress",
  "fields": [
    "*"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "3a947935-2c14-4a51-ac07-1a08bec6119d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjJvpCuof9hjCACfhZQ5Ck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12173,
      "cache_read_input_tokens": 27619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12173
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

_source line 21 · 2026-05-19T11:12:06.842Z_

<details><summary>↩ Tool result · `toolu_01HdC5DEBChJDkSUk8FDwN5A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4404}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c50553ea-3fc2-4e1a-8719-aa490df107ae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4404}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4404}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Lccdytii5d67M5VfUyhf47`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls checkpoints/ | head -30; echo \"===\"; ls configs/*.yaml | head -20",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "36a8c7a5-b905-4d40-b386-10e3b38c88a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjJvpCuof9hjCACfhZQ5Ck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12173,
      "cache_read_input_tokens": 27619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12173
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

_source line 23 · 2026-05-19T11:12:07.688Z_

<details><summary>↩ Tool result · `toolu_01Lccdytii5d67M5VfUyhf47`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"baseline_control\\nlatest\\nlibero_acis_stage1only_k03\\nlibero_acis_stage1only_k07\\nlibero_baseline\\nlibero_baseline_seed0\\nlibero_full_ft\\nlibero_full_ft_seed0\\nlibero_full_ft_seed1\\nlibero_fullft_batch64\\nlibero_imm_twostage_fullft\\nlibero_imm_twostage_fullft_seed0\\nlibero_stage2_recovery\\nsmart_compress_m128\\nsmart_compress_m16\\nsmart_compress_m32\\nsmart_compress_m32_official\\nsmart_compress_m32_seed43\\nsmart_compress_m32_seed44\\nsmart_compress_m64\\nsmart_compress_m64_seed43\\nsmart_compress_m64_seed44\\nsmart_compress_m96\\nsmart_compress_m96_seed43\\nsmart_compress_m96_seed44\\n===\\nconfigs/baseline.yaml\\nconfigs/baseline_control.yaml\\nconfigs/baseline_v6_alpha16.yaml\\nconfigs/imm_anchor.yaml\\nconfigs/imm_anchor_v7_1.yaml\\nconfigs/imm_anchor_v8.yaml\\nconfigs/imm_anchor_v8_1.yaml\\nconfigs/imm_anchor_v8_2.yaml\\nconfigs/imm_anchor_v8b_twostage.yaml\\nconfigs/imm_anchor_v8c_annealing.yaml\\nconfigs/imm_delta01_lambda01.yaml\\nconfigs/imm_delta05_lambda10.yaml\\nconfigs/imm_k75.yaml\\nconfigs/imm_two_stage.yaml\\nconfigs/libero_acis_stage1only_k03.yaml\\nconfigs/libero_acis_stage1only_k07.yaml\\nconfigs/libero_baseline.yaml\\nconfigs/libero_baseline_seed0.yaml\\nconfigs/libero_full_ft.yaml\\nconfigs/libero_full_ft_seed0.yaml\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "59156852-3dd2-45dd-9e5c-063ee8ac3ee9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"baseline_control\\\\nlatest\\\\nlibero_acis_stage1only_k03\\\\nlibero_acis_stage1only_k07\\\\nlibero_baseline\\\\nlibero_baseline_seed0\\\\nlibero_full_ft\\\\nlibero_full_ft_seed0\\\\nlibero_full_ft_seed1\\\\nlibero_fullft_batch64\\\\nlibero_imm_twostage_fullft\\\\nlibero_imm_twostage_fullft_seed0\\\\nlibero_stage2_recovery\\\\nsmart_compress_m128\\\\nsmart_compress_m16\\\\nsmart_compress_m32\\\\nsmart_compress_m32_official\\\\nsmart_compress_m32_seed43\\\\nsmart_compress_m32_seed44\\\\nsmart_compress_m64\\\\nsmart_compress_m64_seed43\\\\nsmart_compress_m64_seed44\\\\nsmart_compress_m96\\\\nsmart_compress_m96_seed43\\\\nsmart_compress_m96_seed44\\\\n===\\\\nconfigs/baseline.yaml\\\\nconfigs/baseline_control.yaml\\\\nconfigs/baseline_v6_alpha16.yaml\\\\nconfigs/imm_anchor.yaml\\\\nconfigs/imm_anchor_v7_1.yaml\\\\nconfigs/imm_anchor_v8.yaml\\\\nconfigs/imm_anchor_v8_1.yaml\\\\nconfigs/imm_anchor_v8_2.yaml\\\\nconfigs/imm_anchor_v8b_twostage.yaml\\\\nconfigs/imm_anchor_v8c_annealing.yaml\\\\nconfigs/imm_delta01_lambda01.yaml\\\\nconfigs/imm_delta05_lambda10.yaml\\\\nconfigs/imm_k75.yaml\\\\nconfigs/imm_two_stage.yaml\\\\nconfigs/libero_acis_stage1only_k03.yaml\\\\nconfigs/libero_acis_stage1only_k07.yaml\\\\nconfigs/libero_baseline.yaml\\\\nconfigs/libero_baseline_seed0.yaml\\\\nconfigs/libero_full_ft.yaml\\\\nconfigs/libero_full_ft_seed0.yaml\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"baseline_control\\nlatest\\nlibero_acis_stage1only_k03\\nlibero_acis_stage1only_k07\\nlibero_baseline\\nlibero_baseline_seed0\\nlibero_full_ft\\nlibero_full_ft_seed0\\nlibero_full_ft_seed1\\nlibero_fullft_batch64\\nlibero_imm_twostage_fullft\\nlibero_imm_twostage_fullft_seed0\\nlibero_stage2_recovery\\nsmart_compress_m128\\nsmart_compress_m16\\nsmart_compress_m32\\nsmart_compress_m32_official\\nsmart_compress_m32_seed43\\nsmart_compress_m32_seed44\\nsmart_compress_m64\\nsmart_compress_m64_seed43\\nsmart_compress_m64_seed44\\nsmart_compress_m96\\nsmart_compress_m96_seed43\\nsmart_compress_m96_seed44\\n===\\nconfigs/baseline.yaml\\nconfigs/baseline_control.yaml\\nconfigs/baseline_v6_alpha16.yaml\\nconfigs/imm_anchor.yaml\\nconfigs/imm_anchor_v7_1.yaml\\nconfigs/imm_anchor_v8.yaml\\nconfigs/imm_anchor_v8_1.yaml\\nconfigs/imm_anchor_v8_2.yaml\\nconfigs/imm_anchor_v8b_twostage.yaml\\nconfigs/imm_anchor_v8c_annealing.yaml\\nconfigs/imm_delta01_lambda01.yaml\\nconfigs/imm_delta05_lambda10.yaml\\nconfigs/imm_k75.yaml\\nconfigs/imm_two_stage.yaml\\nconfigs/libero_acis_stage1only_k03.yaml\\nconfigs/libero_acis_stage1only_k07.yaml\\nconfigs/libero_baseline.yaml\\nconfigs/libero_baseline_seed0.yaml\\nconfigs/libero_full_ft.yaml\\nconfigs/libero_full_ft_seed0.yaml\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
I see `checkpoints/libero_baseline` directory. Let me also search for the previous baseline eval in the registry more broadly, and check the checkpoint and config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "a441c414-47cf-495d-9f67-1a18f2401f35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEE8RVDDPrH638k4sgKrtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 39792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 25_

找到了 `checkpoints/libero_baseline` 和 `configs/libero_baseline.yaml`。让我确认 checkpoint 存在并查看 config，同时查找 registry 中之前的 baseline eval 记录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "2bb73744-c0fc-45fd-8d08-3bb090fa3b50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEE8RVDDPrH638k4sgKrtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 39792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01US1HM25hRmxJv1erpqvhpw`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls -la checkpoints/libero_baseline/; echo \"===\"; cat configs/libero_baseline.yaml",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "0f582517-6bcd-4cfe-8dcb-132f5878f9d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEE8RVDDPrH638k4sgKrtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 39792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 27 · 2026-05-19T11:12:13.769Z_

<details><summary>↩ Tool result · `toolu_01US1HM25hRmxJv1erpqvhpw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x 12 root root 4096 May 17 05:25 .\\ndrwxr-xr-x 27 root root 4096 May 19 17:23 ..\\nlrwxrwxrwx  1 root root   11 May 17 05:25 latest -> step_099999\\ndrwxr-xr-x  2 root root   27 May 16 23:00 step_010000\\ndrwxr-xr-x  2 root root   35 May 16 23:40 step_020000\\ndrwxr-xr-x  2 root root   35 May 17 00:22 step_030000\\ndrwxr-xr-x  2 root root   35 May 17 01:04 step_040000\\ndrwxr-xr-x  2 root root   35 May 17 01:45 step_050000\\ndrwxr-xr-x  2 root root   27 May 17 02:26 step_060000\\ndrwxr-xr-x  2 root root   35 May 17 03:08 step_070000\\ndrwxr-xr-x  2 root root   35 May 17 03:54 step_080000\\ndrwxr-xr-x  2 root root   35 May 17 04:39 step_090000\\ndrwxr-xr-x  2 root root   35 May 17 05:25 step_099999\\n===\\n# LIBERO baseline: SmolVLA + LoRA fine-tuning, no IMM.\\n# Matches SmolVLA paper protocol for LIBERO benchmark.\\n#\\n# Official SmolVLA LIBERO results (paper): 87.3% avg\\n#   Spatial=90%, Object=96%, Goal=92%, Long=71%\\n#\\n# Training: lerobot-train uses policy.type=smolvla with train_expert_only=True\\n# We use LoRA fine-tuning from smolvla_base for IMM compatibility.\\n\\nmodel:\\n  name: smolvla\\n  pretrained: \\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\"\\n  lora:\\n    rank: 32\\n    alpha: 16\\n    dropout: 0.05\\n    target_modules_regex: \\\"(vlm_with_expert\\\\\\\\.lm_expert\\\\\\\\..*\\\\\\\\.(q|v)_proj|(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\\\"\\n\\nimm:\\n  enabled: false\\n\\ndataset:\\n  repo_id: \\\"HuggingFaceVLA/libero\\\"\\n  features:\\n    state_dim: 8       # eef_pos(3) + axis_angle(3) + gripper_qpos(2)\\n    action_dim: 7      # 6D EEF delta + 1D gripper\\n    cameras:\\n      - \\\"observation.images.image\\\"        # agentview\\n      - \\\"observation.images.image2\\\"       # wrist (robot0_eye_in_hand)\\n\\ntraining:\\n  total_steps: 100000\\n  batch_size: 4\\n  eval_batch_size: 1\\n  num_workers: 4\\n  lr: 1.0e-4\\n  betas: [0.9, 0.95]\\n  weight_decay: 1.0e-10\\n  warmup_steps: 1000\\n  decay_lr: 2.5e-6\\n  grad_clip: 10.0\\n  eval_every: 5000\\n  save_every: 10000\\n  log_every: 50\\n  output_dir: \\\"checkpoints/libero_baseline\\\"\\n  seed: 42\\n\\nevaluation:\\n  # Offline eval metrics (perturbation robustness)\\n  perturbations: [0.0, 0.01, 0.02, 0.05]\\n  pruning_ratio: 0.5\\n  max_eval_batches: 50\\n\\n# LIBERO sim eval protocol (for eval_success_rate_libero.py)\\nlibero_eval:\\n  suites:\\n    - libero_spatial\\n    - libero_object\\n    - libero_goal\\n    - libero_10\\n  n_episodes_per_task: 10    # 10 tasks/suite × 10 eps = 100 eps/suite\\n  control_mode: \\\"relative\\\"\\n  cameras: \\\"agentview_image,robot0_eye_in_hand_image\\\"\\n  max_steps:\\n    libero_spatial: 280\\n    libero_object: 280\\n    libero_goal: 300\\n    libero_10: 520\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "20354e02-b27c-4eea-8f76-7c59d7a8c9d3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 8\\\\ndrwxr-xr-x 12 root root 4096 May 17 05:25 .\\\\ndrwxr-xr-x 27 root root 4096 May 19 17:23 ..\\\\nlrwxrwxrwx  1 root root   11 May 17 05:25 latest -> step_099999\\\\ndrwxr-xr-x  2 root root   27 May 16 23:00 step_010000\\\\ndrwxr-xr-x  2 root root   35 May 16 23:40 step_020000\\\\ndrwxr-xr-x  2 root root   35 May 17 00:22 step_030000\\\\ndrwxr-xr-x  2 root root   35 May 17 01:04 step_040000\\\\ndrwxr-xr-x  2 root root   35 May 17 01:45 step_050000\\\\ndrwxr-xr-x  2 root root   27 May 17 02:26 step_060000\\\\ndrwxr-xr-x  2 root root   35 May 17 03:08 step_070000\\\\ndrwxr-xr-x  2 root root   35 May 17 03:54 step_080000\\\\ndrwxr-xr-x  2 root root   35 May 17 04:39 step_090000\\\\ndrwxr-xr-x  2 root root   35 May 17 05:25 step_099999\\\\n===\\\\n# LIBERO baseline: SmolVLA + LoRA fine-tuning, no IMM.\\\\n# Matches SmolVLA paper protocol for LIBERO benchmark.\\\\n#\\\\n# Official SmolVLA LIBERO results (paper): 87.3% avg\\\\n#   Spatial=90%, Object=96%, Goal=92%, Long=71%\\\\n#\\\\n# Training: lerobot-train uses policy.type=smolvla with train_expert_only=True\\\\n# We use LoRA fine-tuning from smolvla_base for IMM compatibility.\\\\n\\\\nmodel:\\\\n  name: smolvla\\\\n  pretrained: \\\\\\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\\\\\"\\\\n  lora:\\\\n    rank: 32\\\\n    alpha: 16\\\\n    dropout: 0.05\\\\n    target_modules_regex: \\\\\\\"(vlm_with_expert\\\\\\\\\\\\\\\\.lm_expert\\\\\\\\\\\\\\\\..*\\\\\\\\\\\\\\\\.(q|v)_proj|(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\\\\\\\"\\\\n\\\\nimm:\\\\n  enabled: false\\\\n\\\\ndataset:\\\\n  repo_id: \\\\\\\"HuggingFaceVLA/libero\\\\\\\"\\\\n  features:\\\\n    state_dim: 8       # eef_pos(3) + axis_angle(3) + gripper_qpos(2)\\\\n    action_dim: 7      # 6D EEF delta + 1D gripper\\\\n    cameras:\\\\n      - \\\\\\\"observation.images.image\\\\\\\"        # agentview\\\\n      - \\\\\\\"observation.images.image2\\\\\\\"       # wrist (robot0_eye_in_hand)\\\\n\\\\ntraining:\\\\n  total_steps: 100000\\\\n  batch_size: 4\\\\n  eval_batch_size: 1\\\\n  num_workers: 4\\\\n  lr: 1.0e-4\\\\n  betas: [0.9, 0.95]\\\\n  weight_decay: 1.0e-10\\\\n  warmup_steps: 1000\\\\n  decay_lr: 2.5e-6\\\\n  grad_clip: 10.0\\\\n  eval_every: 5000\\\\n  save_every: 10000\\\\n  log_every: 50\\\\n  output_dir: \\\\\\\"checkpoints/libero_baseline\\\\\\\"\\\\n  seed: 42\\\\n\\\\nevaluation:\\\\n  # Offline eval metrics (perturbation robustness)\\\\n  perturbations: [0.0, 0.01, 0.02, 0.05]\\\\n  pruning_ratio: 0.5\\\\n  max_eval_batches: 50\\\\n\\\\n# LIBERO sim eval protocol (for eval_success_rate_libero.py)\\\\nlibero_eval:\\\\n  suites:\\\\n    - libero_spatial\\\\n    - libero_object\\\\n    - libero_goal\\\\n    - libero_10\\\\n  n_episodes_per_task: 10    # 10 tasks/suite × 10 eps = 100 eps/suite\\\\n  control_mode: \\\\\\\"relative\\\\\\\"\\\\n  cameras: \\\\\\\"agentview_image,robot0_eye_in_hand_image\\\\\\\"\\\\n  max_steps:\\\\n    libero_spatial: 280\\\\n    libero_object: 280\\\\n    libero_goal: 300\\\\n    libero_10: 520\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x 12 root root 4096 May 17 05:25 .\\ndrwxr-xr-x 27 root root 4096 May 19 17:23 ..\\nlrwxrwxrwx  1 root root   11 May 17 05:25 latest -> step_099999\\ndrwxr-xr-x  2 root root   27 May 16 23:00 step_010000\\ndrwxr-xr-x  2 root root   35 May 16 23:40 step_020000\\ndrwxr-xr-x  2 root root   35 May 17 00:22 step_030000\\ndrwxr-xr-x  2 root root   35 May 17 01:04 step_040000\\ndrwxr-xr-x  2 root root   35 May 17 01:45 step_050000\\ndrwxr-xr-x  2 root root   27 May 17 02:26 step_060000\\ndrwxr-xr-x  2 root root   35 May 17 03:08 step_070000\\ndrwxr-xr-x  2 root root   35 May 17 03:54 step_080000\\ndrwxr-xr-x  2 root root   35 May 17 04:39 step_090000\\ndrwxr-xr-x  2 root root   35 May 17 05:25 step_099999\\n===\\n# LIBERO baseline: SmolVLA + LoRA fine-tuning, no IMM.\\n# Matches SmolVLA paper protocol for LIBERO benchmark.\\n#\\n# Official SmolVLA LIBERO results (paper): 87.3% avg\\n#   Spatial=90%, Object=96%, Goal=92%, Long=71%\\n#\\n# Training: lerobot-train uses policy.type=smolvla with train_expert_only=True\\n# We use LoRA fine-tuning from smolvla_base for IMM compatibility.\\n\\nmodel:\\n  name: smolvla\\n  pretrained: \\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\"\\n  lora:\\n    rank: 32\\n    alpha: 16\\n    dropout: 0.05\\n    target_modules_regex: \\\"(vlm_with_expert\\\\\\\\.lm_expert\\\\\\\\..*\\\\\\\\.(q|v)_proj|(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\\\"\\n\\nimm:\\n  enabled: false\\n\\ndataset:\\n  repo_id: \\\"HuggingFaceVLA/libero\\\"\\n  features:\\n    state_dim: 8       # eef_pos(3) + axis_angle(3) + gripper_qpos(2)\\n    action_dim: 7      # 6D EEF delta + 1D gripper\\n    cameras:\\n      - \\\"observation.images.image\\\"        # agentview\\n      - \\\"observation.images.image2\\\"       # wrist (robot0_eye_in_hand)\\n\\ntraining:\\n  total_steps: 100000\\n  batch_size: 4\\n  eval_batch_size: 1\\n  num_workers: 4\\n  lr: 1.0e-4\\n  betas: [0.9, 0.95]\\n  weight_decay: 1.0e-10\\n  warmup_steps: 1000\\n  decay_lr: 2.5e-6\\n  grad_clip: 10.0\\n  eval_every: 5000\\n  save_every: 10000\\n  log_every: 50\\n  output_dir: \\\"checkpoints/libero_baseline\\\"\\n  seed: 42\\n\\nevaluation:\\n  # Offline eval metrics (perturbation robustness)\\n  perturbations: [0.0, 0.01, 0.02, 0.05]\\n  pruning_ratio: 0.5\\n  max_eval_batches: 50\\n\\n# LIBERO sim eval protocol (for eval_success_rate_libero.py)\\nlibero_eval:\\n  suites:\\n    - libero_spatial\\n    - libero_object\\n    - libero_goal\\n    - libero_10\\n  n_episodes_per_task: 10    # 10 tasks/suite × 10 eps = 100 eps/suite\\n  control_mode: \\\"relative\\\"\\n  cameras: \\\"agentview_image,robot0_eye_in_hand_image\\\"\\n  max_steps:\\n    libero_spatial: 280\\n    libero_object: 280\\n    libero_goal: 300\\n    libero_10: 520\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01V5Pyo3TW58r1x2cvF2ZJkg`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "spec"
  ],
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c1ccbc8b-0874-416d-83d3-6388e4fab0ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEE8RVDDPrH638k4sgKrtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 39792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 29 · 2026-05-19T11:12:14.155Z_

<details><summary>↩ Tool result · `toolu_01V5Pyo3TW58r1x2cvF2ZJkg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_smart_compress_m32_spatial\": {\"status\": \"PREPARING\"}, \"eval_smolvla_baseline_spatial\": {\"status\": \"PREPARING\"}, \"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_official + VisionTokenCompressor(M=32)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160116, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\", \"gpu_ids\": [\"cuda:3\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.534, \"wilson_ci_95\": [0.4902, 0.5773], \"total_episodes\": 500, \"total_successes\": 267, \"per_task_sr\": {\"task0_alphabet_soup\": 0.64, \"task1_cream_cheese\": 0.48, \"task2_salad_dressing\": 0.56, \"task3_bbq_sauce\": 0.46, \"task4_ketchup\": 0.46, \"task5_tomato_sauce\": 0.28, \"task6_butter\": 0.78, \"task7_milk\": 0.42, \"task8_chocolate_pudding\": 0.66, \"task9_orange_juice\": 0.6}}}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 164042, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160877, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\", \"server\": \"westd-27271\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 480299, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\", \"tmux_session\": \"eval_m128_s44\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128_seed44\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.602, \"total_successes\": 301, \"total_episodes\": 500, \"wilson_ci_95\": [0.5585, 0.644], \"per_task_sr\": {\"alphabet_soup\": 0.54, \"cream_cheese\": 0.3, \"salad_dressing\": 0.62, \"bbq_sauce\": 0.5, \"ketchup\": 0.86, \"tomato_sauce\": 0.4, \"butter\": 0.66, \"milk\": 0.72, \"chocolate_pudding\": 0.88, \"orange_juice\": 0.54}}}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 162254, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"eval_openvla_baseline_spatial\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python eval_openvla_libero.py --suite libero_spatial --num_episodes 50 --mode baseline --seed 42 --output eval_results/eval_openvla_baseline_spatial.json\", \"server\": \"westd-27271\", \"data_path\": \"libero_spatial (LIBERO benchmark)\", \"data_count\": 500, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_spatial\"}}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": \"full LIBERO dataset\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\"}}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 764777, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 763351, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 762596, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}}, \"train_smart_compress_m16_seed44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m16_seed44.yaml --wandb_run smart_compress_m16_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": \"all\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"seed\": 44, \"pid\": 462076, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m16_seed44.log\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"checkpoints/smart_compress_m16_seed44/\", \"eval_data\": \"HuggingFaceVLA/libero (training, not eval)\"}}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"data_count\": 0, \"model_name\": \"SmolVLA+VisionTokenCompressor_M128\", \"seed\": 44, \"gpu_ids\": [\"cuda:1\"], \"tmux_session\": \"train_m128_s44\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\"}}, \"train_smart_compress_m64_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m64_seed44.yaml --wandb_run smart_compress_m64_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": \"all\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m64_seed44.log\"}}, \"train_smart_compress_m32_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_seed44.yaml --wandb_run smart_compress_m32_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m32_seed44.log\"}}, \"train_smart_compress_m96_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m96_seed44.yaml --wandb_run smart_compress_m96_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m96_seed44.log\"}}, \"train_mlp_adapter_control\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/mlp_adapter_control.yaml --wandb_run mlp_adapter_control --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + MLPCompressor(3-layer MLP, 22.14M params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"notes\": \"Control experiment: MLP+avg-pool compressor (no cross-attention) with matched params (~22.14M) vs VisionTokenCompressor M=32. 3x MLP blocks (Linear 960->3840 + GELU + Linear 3840->960 + LN). 128 tokens -> avg pool -> 32 tokens. tmux session: mlp_adapter_control\"}}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 355272, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\", \"tmux_session\": \"eval_openvla_k095\", \"pruning_method\": \"random + true_removal\", \"k_ratio\": 0.95, \"vision_tokens\": \"256 -> 243 (remove 13)\"}, \"metrics\": {\"success_rate\": 69.4, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 7, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"pid\": 354653, \"pruning\": \"random, true_removal, k=0.9\", \"vision_tokens\": \"256 -> 230\"}, \"metrics\": {\"success_rate\": 62, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 470232, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\", \"submitted_at\": \"2026-05-18T23:23:07.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m32_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_seed43\", \"wall_clock_seconds\": 5572.6, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 59.2, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 424163, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\", \"submitted_at\": \"2026-05-18T23:01:14.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_spatial\", \"wall_clock_seconds\": 6884.4, \"gpu_hours\": 1.91}, \"metrics\": {\"success_rate\": 53.2, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"num_episodes\": 500, \"suite\": \"libero_spatial\"}}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 560607, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\", \"submitted_at\": \"2026-05-18T23:58:31.377Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m64_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m64_seed43\", \"wall_clock_seconds\": 3446.5, \"gpu_hours\": 0.96}, \"metrics\": {\"success_rate\": 60, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 571598, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"submitted_at\": \"2026-05-19T00:01:35.221Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\", \"wall_clock_seconds\": 3261.2, \"gpu_hours\": 0.91}, \"metrics\": {\"success_rate\": 56.4, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"num_episodes\": 500, \"suite\": \"libero_goal\"}}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 394430, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\", \"submitted_at\": \"2026-05-18T22:26:42.237Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_baseline_control_prune_k05\", \"pruning_method\": \"random + zero_mask\", \"k_ratio\": 0.5, \"wall_clock_seconds\": 5583.9, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": null, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 43, \"checkpoint_source\": null, \"eval_data\": null, \"config\": \"configs/smart_compress_m64_seed43.yaml\", \"log_path\": \"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\", \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"pid\": 202271, \"total_steps\": 100000}}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"200291\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\"}}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 322232, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\", \"submitted_at\": \"2026-05-18T21:31:55.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m96_seed43_v2\", \"wall_clock_seconds\": 5335.1, \"gpu_hours\": 1.48}, \"metrics\": {\"success_rate\": 58.2, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"num_episodes\": 500, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}}, \"eval_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_success_rate_libero.py --checkpoint checkpoints/smart_compress_m96_seed43/checkpoint.pt --config configs/smart_compress_m96_seed43.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smart_compress_m96_seed43.json\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"libero_object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43.json\"}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\", \"note\": \"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\"}}, \"train_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=2 python -u train_smart_compress.py --config configs/smart_compress_m96_seed43.yaml --wandb_run smart_compress_m96_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"111876\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m96_seed43.log\", \"submitted_at\": \"2026-05-18T12:38:32.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"wall_clock_seconds\": 31663.3, \"gpu_hours\": 8.8}}, \"train_baseline_control_100k_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr_v2\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"109885\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k_v2.log\", \"submitted_at\": \"2026-05-18T12:37:08.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"data_count\": \"same as full_ft baseline\", \"model_name\": \"SmolVLA (from step 99999 checkpoint, fresh lr)\", \"seed\": \"default\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"wall_clock_seconds\": 31745.9, \"gpu_hours\": 8.82}}, \"eval_baseline_control_100k_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_baseline_control_100k_v2.json\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"libero_object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_control_100k_v2.json\"}, \"metrics\": {\"success_rate\": 45, \"per_task_sr\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_official_smolvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.95 --output eval_results/official_libero_object_random_prune_k095.json --seed 42\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"data_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"data_count\": \"500 episodes (10 tasks x 50 eps)\", \"model_name\": \"SmolVLA-LIBERO official checkpoint\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"LIBERO-Object (10 tasks, 50 episodes each)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/official_prune_k095.log\"}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\"}}, \"eval_official_smolvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.9 --output eval_results/official_libero_object_random_prune_k09.json --seed 42\", \"server\": \"westd-27271\", \"data_path\": \"libero_object (10 tasks x 50 episodes)\", \"data_count\": 500, \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object\", \"log_path\": \"eval_results/official_libero_object_random_prune_k09.log\", \"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval_k09\", \"pruning_method\": \"true_removal\", \"k_ratio\": 0.9}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\"}}, \"eval_acis_k05_supplement_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --k_ratio 0.5 --num_episodes 50 --gpu 0 --seed 42 --task_ids 6,7,8,9 --output eval_results/eval_acis_k05_supplement_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_acis_k05_supplement_v2.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"SmolVLA IMM twostage fullft (stage1_done)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"eval_data\": \"libero_object tasks 6-9 x 50 episodes\"}, \"metrics\": {\"overall_SR\": \"0.0% (0/200)\", \"wilson_ci_95\": \"[0.0%, 1.9%]\", \"task6_SR\": \"0% (0/50)\", \"task7_SR\": \"0% (0/50)\", \"task8_SR\": \"0% (0/50)\", \"task9_SR\": \"0% (0/50)\", \"note\": \"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\"}}, \"eval_acis_k05_supplement_200eps\": {\"status\": \"DONE\", \"spec\": {\"failure_reason\": \"cqa1 eval_success_rate_libero.py is OLD version with ACIS hook bug: compares single-camera token shape vs full mask shape, always mismatches, hook returns output unchanged = NO pruning executed. 47.5% SR is unpruned baseline, not ACIS pruning result.\"}, \"metrics\": {\"overall_SR\": \"47.5% (95/200)\", \"wilson_ci_95\": \"[40.7%, 54.4%]\", \"task6_SR\": \"48% (24/50)\", \"task7_SR\": \"40% (20/50)\", \"task8_SR\": \"64% (32/50)\", \"task9_SR\": \"38% (19/50)\"}}, \"eval_official_smolvla_prune_k05_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_official_libero.py --mode random_prune --k_ratio 0.5 --num_episodes 50 --suite libero_object --seed 42\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"136801\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log\", \"submitted_at\": \"2026-05-18T13:24:15.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"data_path\": \"libero_object\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"wall_clock_seconds\": 2825.9, \"gpu_hours\": 0.78}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\"}}, \"eval_official_smolvla_baseline\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode baseline --seed 42\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"117439\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_baseline.log\", \"submitted_at\": \"2026-05-18T13:17:58.352Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:0\", \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"SmolVLA official checkpoint (HuggingFace)\", \"seed\": 42, \"checkpoint_source\": \"smolvla_libero_official\", \"eval_data\": \"LIBERO-Object 10 tasks x 50 episodes\", \"wall_clock_seconds\": 2419.5, \"gpu_hours\": 0.67}, \"metrics\": {\"overall_sr\": 59.2, \"wilson_ci_95\": [54.8, 63.4], \"total_episodes\": 500, \"total_successes\": 296, \"per_task_sr\": {\"task_0_alphabet_soup\": 64, \"task_1_cream_cheese\": 40, \"task_2_salad_dressing\": 44, \"task_3_bbq_sauce\": 38, \"task_4_ketchup\": 60, \"task_5_tomato_sauce\": 46, \"task_6_butter\": 78, \"task_7_milk\": 52, \"task_8_chocolate_pudding\": 90, \"task_9_orange_juice\": 80}}}, \"eval_smolvla_random_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_random_prune_smolvla.py --k_ratio 0.95 --episodes_per_task 50 --output_name smolvla_random_prune_k095.json --seed 42\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"92881\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log\", \"submitted_at\": \"2026-05-18T12:17:00Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"SmolVLA full_ft (baseline)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"wall_clock_seconds\": 3798.0, \"gpu_hours\": 1.05}, \"metrics\": {\"overall_SR\": 0, \"wilson_ci_95\": [0, 0.0076], \"total_episodes\": 500, \"total_successes\": 0, \"tokens_kept\": 121, \"tokens_removed\": 7, \"k_ratio\": 0.95, \"per_task_SR\": {\"T0_alphabet_soup\": 0, \"T1_cream_cheese\": 0, \"T2_salad_dressing\": 0, \"T3_bbq_sauce\": 0, \"T4_ketchup\": 0, \"T5_tomato_sauce\": 0, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0, \"T9_orange_juice\": 0}}}, \"eval_official_smolvla_pruning\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --mode baseline/random_prune --k_ratio 0.5\", \"server\": \"westd-27271\", \"data_path\": \"LIBERO libero_object (sim)\", \"data_count\": 500, \"model_name\": \"SmolVLA-500M-official-LIBERO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\"}}, \"debug_obs_official\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python debug_obs.py\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"86969\", \"log_path\": \"~/runs/importance_margin_vla_compress/debug_obs_official.log\", \"submitted_at\": \"2026-05-18T12:54:22.640Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_official_smolvla_prune_k05\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.5 --pruning_method true_removal --output eval_results/official_libero_object_random_prune_k05.json --seed 42\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"79867\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05.log\", \"submitted_at\": \"2026-05-18T12:51:19.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"train_baseline_control_100k\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": \"100236\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k.log\", \"submitted_at\": \"2026-05-18T12:25:14.994Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"data_count\": \"same as full_ft baseline\", \"model_name\": \"SmolVLA (from step 99999 checkpoint)\", \"seed\": \"default\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"N/A (training experiment, not eval)\", \"trainable_params\": \"99.9M (action expert + projections only)\", \"wall_clock_seconds\": 504.9, \"gpu_hours\": 0.14}}, \"eval_smart_compress_m128\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_smart_compress_libero.py --n_queries 128\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"18074\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128.log\", \"submitted_at\": \"2026-05-18T10:08:26.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m128/checkpoint.pt\", \"eval_data\": \"libero_object\", \"wall_clock_seconds\": 4326.7, \"gpu_hours\": 1.2}, \"metrics\": {\"libero_object_sr\": 0.598, \"libero_object_sr_ci95\": [0.554, 0.64], \"total_episodes\": 500, \"total_successes\": 299, \"per_task_sr\": {\"alphabet_soup\": 0.62, \"cream_cheese\": 0.58, \"salad_dressing\": 0.54, \"bbq_sauce\": 0.34, \"ketchup\": 0.62, \"tomato_sauce\": 0.5, \"butter\": 0.82, \"milk\": 0.56, \"chocolate_pudding\": 0.82, \"orange_juice\": 0.58}}}, \"eval_openvla_pruning_k03_restart\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"openvla-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}, \"metrics\": {\"overall_sr\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"wilson_ci_95\": [0.173, 0.244], \"elapsed_minutes\": 288.6, \"per_task_sr\": {\"alphabet_soup\": 0.14, \"cream_cheese\": 0, \"salad_dressing\": 0.64, \"bbq_sauce\": 0.3, \"ketchup\": 0.3, \"tomato_sauce\": 0.08, \"butter\": 0, \"milk\": 0.08, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.42}}}, \"train_smart_compress_m128_resume\": {\"status\": \"ANALYZING\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128/checkpoint.pt\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m128_resume.log\", \"wandb_offline_run\": \"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_132800-x610qzvt\"}, \"metrics\": {\"train_action_loss\": 0.05412, \"eval_action_loss\": 0.05743, \"train_grad_norm\": 0.92663, \"total_steps\": 99999, \"resumed_from_step\": 32001}}, \"smolvla_entropy_perlayer\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python measure_smolvla_entropy_perlayer.py\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero (cached)\", \"data_count\": 256, \"model_name\": \"smolvla_base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"eval_data\": \"LIBERO mixed tasks\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_entropy_perlayer.log\"}, \"metrics\": {\"overall_entropy_ratio\": 0.9521, \"overall_entropy_std\": 0.02, \"n_images\": 260, \"n_tasks\": 10, \"n_layers\": 16, \"entropy_range\": [0.9311, 0.9826], \"entropy_range_width\": 0.05, \"per_layer\": {\"L0\": 0.9826, \"L1\": 0.9561, \"L2\": 0.9597, \"L3\": 0.9434, \"L4\": 0.9408, \"L5\": 0.9406, \"L6\": 0.9474, \"L7\": 0.9628, \"L8\": 0.9614, \"L9\": 0.9572, \"L10\": 0.9455, \"L11\": 0.951, \"L12\": 0.9485, \"L13\": 0.9311, \"L14\": 0.9482, \"L15\": 0.9566}, \"dataset\": \"LIBERO-Object (task 20-29)\", \"note\": \"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\", \"openvla_comparison\": {\"overall\": 0.639, \"range_width\": 0.5}}}, \"inference_latency_comparison\": {\"status\": \"DONE\", \"spec\": {\"command\": \"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 python measure_inference_latency.py\", \"server\": \"cqa1-33015\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"smolvla_base + SmartCompressWrapper\", \"seed\": 42}, \"metrics\": {\"baseline_128_mean_ms\": 164.33, \"m32_mean_ms\": 154.78, \"m64_mean_ms\": 156.16, \"speedup_m32\": 1.0617, \"speedup_m64\": 1.0523, \"baseline_params\": 450046176, \"compressor_m32_params\": 22179840}}, \"eval_openvla_pruning_k03\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 768729, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"OpenVLA (7B)\", \"seed\": 7, \"checkpoint_source\": \"openvla-libero-object\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.log\"}}, \"openvla_entropy_real\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python measure_openvla_entropy_real.py\", \"server\": \"westd-27271\", \"data_path\": \"LIBERO-Object simulation (10 tasks, 250 rendered frames)\", \"data_count\": 250, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42}, \"metrics\": {\"overall_entropy_ratio\": 0.6393, \"overall_entropy_std\": 0.1334, \"overall_vision_attn_frac\": 0.1211, \"n_images\": 250, \"n_tasks\": 10, \"min_entropy_layer\": {\"layer\": 29, \"ratio\": 0.4774}, \"max_entropy_layer\": {\"layer\": 0, \"ratio\": 0.979}, \"shallow_layers_0_1\": [0.979, 0.952], \"deep_layers_27_30\": [0.542, 0.53, 0.477, 0.524], \"previous_random_N20\": 0.617, \"smolvla_reference\": 0.98}}}, \"count\": 50, \"total\": 127, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3173}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "1f68f941-72dd-4ffd-baad-0aa9675c5f2b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_smart_compress_m32_spatial\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_smolvla_baseline_spatial\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_official + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 160116, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\\\", \\\"gpu_ids\\\": [\\\"cuda:3\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_official/checkpoint.pt\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.534, \\\"wilson_ci_95\\\": [0.4902, 0.5773], \\\"total_episodes\\\": 500, \\\"total_successes\\\": 267, \\\"per_task_sr\\\": {\\\"task0_alphabet_soup\\\": 0.64, \\\"task1_cream_cheese\\\": 0.48, \\\"task2_salad_dressing\\\": 0.56, \\\"task3_bbq_sauce\\\": 0.46, \\\"task4_ketchup\\\": 0.46, \\\"task5_tomato_sauce\\\": 0.28, \\\"task6_butter\\\": 0.78, \\\"task7_milk\\\": 0.42, \\\"task8_chocolate_pudding\\\": 0.66, \\\"task9_orange_juice\\\": 0.6}}}, \\\"eval_smart_compress_m96_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 164042, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.528, \\\"total_successes\\\": 264, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.4842, 0.5714]}}, \\\"eval_smart_compress_m32_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 160877, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.596, \\\"total_successes\\\": 298, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.5524, 0.6381]}}, \\\"eval_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 480299, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\\\", \\\"tmux_session\\\": \\\"eval_m128_s44\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m128_seed44\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m128_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.602, \\\"total_successes\\\": 301, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.5585, 0.644], \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0.54, \\\"cream_cheese\\\": 0.3, \\\"salad_dressing\\\": 0.62, \\\"bbq_sauce\\\": 0.5, \\\"ketchup\\\": 0.86, \\\"tomato_sauce\\\": 0.4, \\\"butter\\\": 0.66, \\\"milk\\\": 0.72, \\\"chocolate_pudding\\\": 0.88, \\\"orange_juice\\\": 0.54}}}, \\\"eval_smart_compress_m64_seed44_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (50 episodes/task)\\\", \\\"pid\\\": 162254, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\"}, \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.644, \\\"total_successes\\\": 322, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.6011, 0.6847]}}, \\\"eval_openvla_baseline_spatial\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python eval_openvla_libero.py --suite libero_spatial --num_episodes 50 --mode baseline --seed 42 --output eval_results/eval_openvla_baseline_spatial.json\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"libero_spatial (LIBERO benchmark)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_spatial\\\"}}, \\\"train_smart_compress_m32_official\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress\\\", \\\"data_count\\\": \\\"full LIBERO dataset\\\", \\\"model_name\\\": \\\"smart_compress_m32\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\\\", \\\"checkpoint_source\\\": \\\"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\\\"}}, \\\"eval_smart_compress_m96_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 764777, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:2\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\"}}, \\\"eval_smart_compress_m64_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 763351, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\"}}, \\\"eval_smart_compress_m32_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object (500 episodes)\\\", \\\"pid\\\": 762596, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\\\", \\\"gpu_ids\\\": [\\\"cuda:0\\\"], \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\"}}, \\\"train_smart_compress_m16_seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m16_seed44.yaml --wandb_run smart_compress_m16_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": \\\"all\\\", \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=16)\\\", \\\"seed\\\": 44, \\\"pid\\\": 462076, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m16_seed44.log\\\", \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m16_seed44/\\\", \\\"eval_data\\\": \\\"HuggingFaceVLA/libero (training, not eval)\\\"}}, \\\"train_smart_compress_m128_seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/data\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"SmolVLA+VisionTokenCompressor_M128\\\", \\\"seed\\\": 44, \\\"gpu_ids\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"train_m128_s44\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\\\"}}, \\\"train_smart_compress_m64_seed44\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m64_seed44.yaml --wandb_run smart_compress_m64_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": \\\"all\\\", \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m64_seed44.log\\\"}}, \\\"train_smart_compress_m32_seed44\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_seed44.yaml --wandb_run smart_compress_m32_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": -1, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m32_seed44.log\\\"}}, \\\"train_smart_compress_m96_seed44\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m96_seed44.yaml --wandb_run smart_compress_m96_seed44 --seed 44 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": -1, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m96_seed44.log\\\"}}, \\\"train_mlp_adapter_control\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/mlp_adapter_control.yaml --wandb_run mlp_adapter_control --seed 42 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": -1, \\\"model_name\\\": \\\"smolvla_base + MLPCompressor(3-layer MLP, 22.14M params)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\", \\\"notes\\\": \\\"Control experiment: MLP+avg-pool compressor (no cross-attention) with matched params (~22.14M) vs VisionTokenCompressor M=32. 3x MLP blocks (Linear 960->3840 + GELU + Linear 3840->960 + LN). 128 tokens -> avg pool -> 32 tokens. tmux session: mlp_adapter_control\\\"}}, \\\"eval_openvla_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 355272, \\\"data_path\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"OpenVLA-7B-libero-object\\\", \\\"seed\\\": 7, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\\\", \\\"tmux_session\\\": \\\"eval_openvla_k095\\\", \\\"pruning_method\\\": \\\"random + true_removal\\\", \\\"k_ratio\\\": 0.95, \\\"vision_tokens\\\": \\\"256 -> 243 (remove 13)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 69.4, \\\"per_task_sr\\\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"eval_openvla_prune_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-object\\\", \\\"seed\\\": 7, \\\"data_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object (10 tasks x 50 episodes)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"pid\\\": 354653, \\\"pruning\\\": \\\"random, true_removal, k=0.9\\\", \\\"vision_tokens\\\": \\\"256 -> 230\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 62, \\\"per_task_sr\\\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"eval_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 470232, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:23:07.575Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_seed43\\\", \\\"wall_clock_seconds\\\": 5572.6, \\\"gpu_hours\\\": 1.55}, \\\"metrics\\\": {\\\"success_rate\\\": 59.2, \\\"per_task_sr\\\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"eval_smart_compress_m32_libero_spatial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 424163, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:01:14.874Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32 (seed=42)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_libero_spatial\\\", \\\"wall_clock_seconds\\\": 6884.4, \\\"gpu_hours\\\": 1.91}, \\\"metrics\\\": {\\\"success_rate\\\": 53.2, \\\"per_task_sr\\\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_spatial\\\"}}, \\\"eval_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 560607, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T23:58:31.377Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m64_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m64_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m64_seed43\\\", \\\"wall_clock_seconds\\\": 3446.5, \\\"gpu_hours\\\": 0.96}, \\\"metrics\\\": {\\\"success_rate\\\": 60, \\\"per_task_sr\\\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"eval_smart_compress_m32_libero_goal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 571598, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T00:01:35.221Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m32 (seed=42)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m32/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m32_libero_goal\\\", \\\"wall_clock_seconds\\\": 3261.2, \\\"gpu_hours\\\": 0.91}, \\\"metrics\\\": {\\\"success_rate\\\": 56.4, \\\"per_task_sr\\\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_goal\\\"}}, \\\"eval_baseline_control_prune_k05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 394430, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T22:26:42.237Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"baseline_control_100k_v2\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/baseline_control/latest/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_baseline_control_prune_k05\\\", \\\"pruning_method\\\": \\\"random + zero_mask\\\", \\\"k_ratio\\\": 0.5, \\\"wall_clock_seconds\\\": 5583.9, \\\"gpu_hours\\\": 1.55}, \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"train_smart_compress_m64_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": null, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=64)\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": null, \\\"eval_data\\\": null, \\\"config\\\": \\\"configs/smart_compress_m64_seed43.yaml\\\", \\\"log_path\\\": \\\"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m64_seed43/checkpoint.pt\\\", \\\"pid\\\": 202271, \\\"total_steps\\\": 100000}}, \\\"train_smart_compress_m32_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"200291\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\\\", \\\"submitted_via\\\": \\\"tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=32)\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"eval_data\\\": \\\"HuggingFaceVLA/libero\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m32_seed43/checkpoint.pt\\\"}}, \\\"eval_smart_compress_m96_seed43_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 322232, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\\\", \\\"submitted_at\\\": \\\"2026-05-18T21:31:55.572Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m96_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m96_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smart_compress_m96_seed43_v2\\\", \\\"wall_clock_seconds\\\": 5335.1, \\\"gpu_hours\\\": 1.48}, \\\"metrics\\\": {\\\"success_rate\\\": 58.2, \\\"per_task_sr\\\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\", \\\"wilson_ci_95\\\": [53.8, 62.4]}}, \\\"eval_smart_compress_m96_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python eval_success_rate_libero.py --checkpoint checkpoints/smart_compress_m96_seed43/checkpoint.pt --config configs/smart_compress_m96_seed43.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smart_compress_m96_seed43.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"smart_compress_m96_seed43\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m96_seed43/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43.json\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"per_task_sr\\\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\", \\\"note\\\": \\\"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\\\"}}, \\\"train_smart_compress_m96_seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=2 python -u train_smart_compress.py --config configs/smart_compress_m96_seed43.yaml --wandb_run smart_compress_m96_seed43 --seed 43 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"111876\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_smart_compress_m96_seed43.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:38:32.454Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"seed\\\": 43, \\\"model_name\\\": \\\"smolvla_base + VisionTokenCompressor(M=96)\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero\\\", \\\"data_count\\\": 0, \\\"checkpoint_source\\\": \\\"smolvla_base (from scratch)\\\", \\\"eval_data\\\": \\\"HuggingFaceVLA/libero\\\", \\\"checkpoint_path\\\": \\\"checkpoints/smart_compress_m96_seed43/checkpoint.pt\\\", \\\"wall_clock_seconds\\\": 31663.3, \\\"gpu_hours\\\": 8.8}}, \\\"train_baseline_control_100k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr_v2\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"109885\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_baseline_control_100k_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:37:08.670Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object (same as full_ft baseline)\\\", \\\"data_count\\\": \\\"same as full_ft baseline\\\", \\\"model_name\\\": \\\"SmolVLA (from step 99999 checkpoint, fresh lr)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\", \\\"eval_data\\\": \\\"N/A (training experiment, not eval)\\\", \\\"checkpoint_path\\\": \\\"checkpoints/baseline_control/latest/checkpoint.pt\\\", \\\"wall_clock_seconds\\\": 31745.9, \\\"gpu_hours\\\": 8.82}}, \\\"eval_baseline_control_100k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_baseline_control_100k_v2.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"baseline_control_100k_v2\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/baseline_control/latest/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_control_100k_v2.json\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 45, \\\"per_task_sr\\\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \\\"num_episodes\\\": 500, \\\"suite\\\": \\\"libero_object\\\"}}, \\\"eval_official_smolvla_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.95 --output eval_results/official_libero_object_random_prune_k095.json --seed 42\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"data_count\\\": \\\"500 episodes (10 tasks x 50 eps)\\\", \\\"model_name\\\": \\\"SmolVLA-LIBERO official checkpoint\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks, 50 episodes each)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/official_prune_k095.log\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 0, \\\"per_task_sr\\\": {\\\"all_10_tasks\\\": \\\"0%\\\"}, \\\"note\\\": \\\"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\\\"}}, \\\"eval_official_smolvla_prune_k09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.9 --output eval_results/official_libero_object_random_prune_k09.json --seed 42\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"libero_object (10 tasks x 50 episodes)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"SmolVLA-LIBERO-official\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"log_path\\\": \\\"eval_results/official_libero_object_random_prune_k09.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"tmux_session\\\": \\\"eval_k09\\\", \\\"pruning_method\\\": \\\"true_removal\\\", \\\"k_ratio\\\": 0.9}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 0, \\\"per_task_sr\\\": {\\\"all_10_tasks\\\": \\\"0%\\\"}, \\\"note\\\": \\\"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\\\"}}, \\\"eval_acis_k05_supplement_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --k_ratio 0.5 --num_episodes 50 --gpu 0 --seed 42 --task_ids 6,7,8,9 --output eval_results/eval_acis_k05_supplement_v2.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_acis_k05_supplement_v2.log\\\", \\\"submitted_via\\\": \\\"tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA IMM twostage fullft (stage1_done)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object tasks 6-9 x 50 episodes\\\"}, \\\"metrics\\\": {\\\"overall_SR\\\": \\\"0.0% (0/200)\\\", \\\"wilson_ci_95\\\": \\\"[0.0%, 1.9%]\\\", \\\"task6_SR\\\": \\\"0% (0/50)\\\", \\\"task7_SR\\\": \\\"0% (0/50)\\\", \\\"task8_SR\\\": \\\"0% (0/50)\\\", \\\"task9_SR\\\": \\\"0% (0/50)\\\", \\\"note\\\": \\\"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\\\"}}, \\\"eval_acis_k05_supplement_200eps\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"failure_reason\\\": \\\"cqa1 eval_success_rate_libero.py is OLD version with ACIS hook bug: compares single-camera token shape vs full mask shape, always mismatches, hook returns output unchanged = NO pruning executed. 47.5% SR is unpruned baseline, not ACIS pruning result.\\\"}, \\\"metrics\\\": {\\\"overall_SR\\\": \\\"47.5% (95/200)\\\", \\\"wilson_ci_95\\\": \\\"[40.7%, 54.4%]\\\", \\\"task6_SR\\\": \\\"48% (24/50)\\\", \\\"task7_SR\\\": \\\"40% (20/50)\\\", \\\"task8_SR\\\": \\\"64% (32/50)\\\", \\\"task9_SR\\\": \\\"38% (19/50)\\\"}}, \\\"eval_official_smolvla_prune_k05_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_official_libero.py --mode random_prune --k_ratio 0.5 --num_episodes 50 --suite libero_object --seed 42\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"136801\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T13:24:15.257Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla_libero_official\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"eval_data\\\": \\\"libero_object (10 tasks x 50 episodes)\\\", \\\"wall_clock_seconds\\\": 2825.9, \\\"gpu_hours\\\": 0.78}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 0, \\\"per_task_sr\\\": {\\\"all_tasks\\\": \\\"0%\\\"}, \\\"note\\\": \\\"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\\\"}}, \\\"eval_official_smolvla_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode baseline --seed 42\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"117439\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_official_smolvla_baseline.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T13:17:58.352Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"gpu_id\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"SmolVLA official checkpoint (HuggingFace)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"smolvla_libero_official\\\", \\\"eval_data\\\": \\\"LIBERO-Object 10 tasks x 50 episodes\\\", \\\"wall_clock_seconds\\\": 2419.5, \\\"gpu_hours\\\": 0.67}, \\\"metrics\\\": {\\\"overall_sr\\\": 59.2, \\\"wilson_ci_95\\\": [54.8, 63.4], \\\"total_episodes\\\": 500, \\\"total_successes\\\": 296, \\\"per_task_sr\\\": {\\\"task_0_alphabet_soup\\\": 64, \\\"task_1_cream_cheese\\\": 40, \\\"task_2_salad_dressing\\\": 44, \\\"task_3_bbq_sauce\\\": 38, \\\"task_4_ketchup\\\": 60, \\\"task_5_tomato_sauce\\\": 46, \\\"task_6_butter\\\": 78, \\\"task_7_milk\\\": 52, \\\"task_8_chocolate_pudding\\\": 90, \\\"task_9_orange_juice\\\": 80}}}, \\\"eval_smolvla_random_prune_k095\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u eval_random_prune_smolvla.py --k_ratio 0.95 --episodes_per_task 50 --output_name smolvla_random_prune_k095.json --seed 42\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"92881\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:17:00Z\\\", \\\"submitted_via\\\": \\\"tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"SmolVLA full_ft (baseline)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\", \\\"wall_clock_seconds\\\": 3798.0, \\\"gpu_hours\\\": 1.05}, \\\"metrics\\\": {\\\"overall_SR\\\": 0, \\\"wilson_ci_95\\\": [0, 0.0076], \\\"total_episodes\\\": 500, \\\"total_successes\\\": 0, \\\"tokens_kept\\\": 121, \\\"tokens_removed\\\": 7, \\\"k_ratio\\\": 0.95, \\\"per_task_SR\\\": {\\\"T0_alphabet_soup\\\": 0, \\\"T1_cream_cheese\\\": 0, \\\"T2_salad_dressing\\\": 0, \\\"T3_bbq_sauce\\\": 0, \\\"T4_ketchup\\\": 0, \\\"T5_tomato_sauce\\\": 0, \\\"T6_butter\\\": 0, \\\"T7_milk\\\": 0, \\\"T8_chocolate_pudding\\\": 0, \\\"T9_orange_juice\\\": 0}}}, \\\"eval_official_smolvla_pruning\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --mode baseline/random_prune --k_ratio 0.5\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"LIBERO libero_object (sim)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"SmolVLA-500M-official-LIBERO\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/smolvla_libero_official\\\", \\\"eval_data\\\": \\\"libero_object 10 tasks x 50 episodes\\\"}}, \\\"debug_obs_official\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python debug_obs.py\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"86969\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/debug_obs_official.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:54:22.640Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval_official_smolvla_prune_k05\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.5 --pruning_method true_removal --output eval_results/official_libero_object_random_prune_k05.json --seed 42\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"79867\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:51:19.230Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"train_baseline_control_100k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"100236\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_baseline_control_100k.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T12:25:14.994Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Object (same as full_ft baseline)\\\", \\\"data_count\\\": \\\"same as full_ft baseline\\\", \\\"model_name\\\": \\\"SmolVLA (from step 99999 checkpoint)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\", \\\"eval_data\\\": \\\"N/A (training experiment, not eval)\\\", \\\"trainable_params\\\": \\\"99.9M (action expert + projections only)\\\", \\\"wall_clock_seconds\\\": 504.9, \\\"gpu_hours\\\": 0.14}}, \\\"eval_smart_compress_m128\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_smart_compress_libero.py --n_queries 128\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"18074\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smart_compress_m128.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T10:08:26.674Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smart_compress_m128\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/smart_compress_m128/checkpoint.pt\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"wall_clock_seconds\\\": 4326.7, \\\"gpu_hours\\\": 1.2}, \\\"metrics\\\": {\\\"libero_object_sr\\\": 0.598, \\\"libero_object_sr_ci95\\\": [0.554, 0.64], \\\"total_episodes\\\": 500, \\\"total_successes\\\": 299, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0.62, \\\"cream_cheese\\\": 0.58, \\\"salad_dressing\\\": 0.54, \\\"bbq_sauce\\\": 0.34, \\\"ketchup\\\": 0.62, \\\"tomato_sauce\\\": 0.5, \\\"butter\\\": 0.82, \\\"milk\\\": 0.56, \\\"chocolate_pudding\\\": 0.82, \\\"orange_juice\\\": 0.58}}}, \\\"eval_openvla_pruning_k03_restart\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 7, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 0.206, \\\"total_successes\\\": 103, \\\"total_episodes\\\": 500, \\\"wilson_ci_95\\\": [0.173, 0.244], \\\"elapsed_minutes\\\": 288.6, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0.14, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.64, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0.3, \\\"tomato_sauce\\\": 0.08, \\\"butter\\\": 0, \\\"milk\\\": 0.08, \\\"chocolate_pudding\\\": 0.1, \\\"orange_juice\\\": 0.42}}}, \\\"train_smart_compress_m128_resume\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128/checkpoint.pt\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/train_smart_compress_m128_resume.log\\\", \\\"wandb_offline_run\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_132800-x610qzvt\\\"}, \\\"metrics\\\": {\\\"train_action_loss\\\": 0.05412, \\\"eval_action_loss\\\": 0.05743, \\\"train_grad_norm\\\": 0.92663, \\\"total_steps\\\": 99999, \\\"resumed_from_step\\\": 32001}}, \\\"smolvla_entropy_perlayer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python measure_smolvla_entropy_perlayer.py\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"HuggingFaceVLA/libero (cached)\\\", \\\"data_count\\\": 256, \\\"model_name\\\": \\\"smolvla_base\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\", \\\"eval_data\\\": \\\"LIBERO mixed tasks\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_entropy_perlayer.log\\\"}, \\\"metrics\\\": {\\\"overall_entropy_ratio\\\": 0.9521, \\\"overall_entropy_std\\\": 0.02, \\\"n_images\\\": 260, \\\"n_tasks\\\": 10, \\\"n_layers\\\": 16, \\\"entropy_range\\\": [0.9311, 0.9826], \\\"entropy_range_width\\\": 0.05, \\\"per_layer\\\": {\\\"L0\\\": 0.9826, \\\"L1\\\": 0.9561, \\\"L2\\\": 0.9597, \\\"L3\\\": 0.9434, \\\"L4\\\": 0.9408, \\\"L5\\\": 0.9406, \\\"L6\\\": 0.9474, \\\"L7\\\": 0.9628, \\\"L8\\\": 0.9614, \\\"L9\\\": 0.9572, \\\"L10\\\": 0.9455, \\\"L11\\\": 0.951, \\\"L12\\\": 0.9485, \\\"L13\\\": 0.9311, \\\"L14\\\": 0.9482, \\\"L15\\\": 0.9566}, \\\"dataset\\\": \\\"LIBERO-Object (task 20-29)\\\", \\\"note\\\": \\\"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\\\", \\\"openvla_comparison\\\": {\\\"overall\\\": 0.639, \\\"range_width\\\": 0.5}}}, \\\"inference_latency_comparison\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 python measure_inference_latency.py\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"smolvla_base + SmartCompressWrapper\\\", \\\"seed\\\": 42}, \\\"metrics\\\": {\\\"baseline_128_mean_ms\\\": 164.33, \\\"m32_mean_ms\\\": 154.78, \\\"m64_mean_ms\\\": 156.16, \\\"speedup_m32\\\": 1.0617, \\\"speedup_m64\\\": 1.0523, \\\"baseline_params\\\": 450046176, \\\"compressor_m32_params\\\": 22179840}}, \\\"eval_openvla_pruning_k03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 768729, \\\"data_path\\\": \\\"LIBERO-Object (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"OpenVLA (7B)\\\", \\\"seed\\\": 7, \\\"checkpoint_source\\\": \\\"openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.log\\\"}}, \\\"openvla_entropy_real\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python measure_openvla_entropy_real.py\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"data_path\\\": \\\"LIBERO-Object simulation (10 tasks, 250 rendered frames)\\\", \\\"data_count\\\": 250, \\\"model_name\\\": \\\"OpenVLA-7B-libero-object\\\", \\\"seed\\\": 42}, \\\"metrics\\\": {\\\"overall_entropy_ratio\\\": 0.6393, \\\"overall_entropy_std\\\": 0.1334, \\\"overall_vision_attn_frac\\\": 0.1211, \\\"n_images\\\": 250, \\\"n_tasks\\\": 10, \\\"min_entropy_layer\\\": {\\\"layer\\\": 29, \\\"ratio\\\": 0.4774}, \\\"max_entropy_layer\\\": {\\\"layer\\\": 0, \\\"ratio\\\": 0.979}, \\\"shallow_layers_0_1\\\": [0.979, 0.952], \\\"deep_layers_27_30\\\": [0.542, 0.53, 0.477, 0.524], \\\"previous_random_N20\\\": 0.617, \\\"smolvla_reference\\\": 0.98}}}, \\\"count\\\": 50, \\\"total\\\": 127, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3173}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_smart_compress_m32_spatial\": {\"status\": \"PREPARING\"}, \"eval_smolvla_baseline_spatial\": {\"status\": \"PREPARING\"}, \"eval_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_official + VisionTokenCompressor(M=32)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160116, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\", \"gpu_ids\": [\"cuda:3\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.534, \"wilson_ci_95\": [0.4902, 0.5773], \"total_episodes\": 500, \"total_successes\": 267, \"per_task_sr\": {\"task0_alphabet_soup\": 0.64, \"task1_cream_cheese\": 0.48, \"task2_salad_dressing\": 0.56, \"task3_bbq_sauce\": 0.46, \"task4_ketchup\": 0.46, \"task5_tomato_sauce\": 0.28, \"task6_butter\": 0.78, \"task7_milk\": 0.42, \"task8_chocolate_pudding\": 0.66, \"task9_orange_juice\": 0.6}}}, \"eval_smart_compress_m96_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 164042, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m32_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 160877, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\", \"server\": \"westd-27271\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 480299, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\", \"tmux_session\": \"eval_m128_s44\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128_seed44\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.602, \"total_successes\": 301, \"total_episodes\": 500, \"wilson_ci_95\": [0.5585, 0.644], \"per_task_sr\": {\"alphabet_soup\": 0.54, \"cream_cheese\": 0.3, \"salad_dressing\": 0.62, \"bbq_sauce\": 0.5, \"ketchup\": 0.86, \"tomato_sauce\": 0.4, \"butter\": 0.66, \"milk\": 0.72, \"chocolate_pudding\": 0.88, \"orange_juice\": 0.54}}}, \"eval_smart_compress_m64_seed44_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (50 episodes/task)\", \"pid\": 162254, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}, \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"eval_openvla_baseline_spatial\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python eval_openvla_libero.py --suite libero_spatial --num_episodes 50 --mode baseline --seed 42 --output eval_results/eval_openvla_baseline_spatial.json\", \"server\": \"westd-27271\", \"data_path\": \"libero_spatial (LIBERO benchmark)\", \"data_count\": 500, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_spatial\"}}, \"train_smart_compress_m32_official\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"data_count\": \"full LIBERO dataset\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\"}}, \"eval_smart_compress_m96_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 764777, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"gpu_ids\": [\"cuda:2\"], \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\"}}, \"eval_smart_compress_m64_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 763351, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\"}}, \"eval_smart_compress_m32_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"eval_data\": \"libero_object (500 episodes)\", \"pid\": 762596, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\"}}, \"train_smart_compress_m16_seed44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m16_seed44.yaml --wandb_run smart_compress_m16_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": \"all\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"seed\": 44, \"pid\": 462076, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m16_seed44.log\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"checkpoints/smart_compress_m16_seed44/\", \"eval_data\": \"HuggingFaceVLA/libero (training, not eval)\"}}, \"train_smart_compress_m128_seed44\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"data_count\": 0, \"model_name\": \"SmolVLA+VisionTokenCompressor_M128\", \"seed\": 44, \"gpu_ids\": [\"cuda:1\"], \"tmux_session\": \"train_m128_s44\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\"}}, \"train_smart_compress_m64_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m64_seed44.yaml --wandb_run smart_compress_m64_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": \"all\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m64_seed44.log\"}}, \"train_smart_compress_m32_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_seed44.yaml --wandb_run smart_compress_m32_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m32_seed44.log\"}}, \"train_smart_compress_m96_seed44\": {\"status\": \"ANALYZING\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m96_seed44.yaml --wandb_run smart_compress_m96_seed44 --seed 44 --gpu 0\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m96_seed44.log\"}}, \"train_mlp_adapter_control\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/mlp_adapter_control.yaml --wandb_run mlp_adapter_control --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": -1, \"model_name\": \"smolvla_base + MLPCompressor(3-layer MLP, 22.14M params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"notes\": \"Control experiment: MLP+avg-pool compressor (no cross-attention) with matched params (~22.14M) vs VisionTokenCompressor M=32. 3x MLP blocks (Linear 960->3840 + GELU + Linear 3840->960 + LN). 128 tokens -> avg pool -> 32 tokens. tmux session: mlp_adapter_control\"}}, \"eval_openvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 355272, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\", \"tmux_session\": \"eval_openvla_k095\", \"pruning_method\": \"random + true_removal\", \"k_ratio\": 0.95, \"vision_tokens\": \"256 -> 243 (remove 13)\"}, \"metrics\": {\"success_rate\": 69.4, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_openvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 7, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"pid\": 354653, \"pruning\": \"random, true_removal, k=0.9\", \"vision_tokens\": \"256 -> 230\"}, \"metrics\": {\"success_rate\": 62, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 470232, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\", \"submitted_at\": \"2026-05-18T23:23:07.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m32_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_seed43\", \"wall_clock_seconds\": 5572.6, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 59.2, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_libero_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 424163, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\", \"submitted_at\": \"2026-05-18T23:01:14.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_spatial\", \"wall_clock_seconds\": 6884.4, \"gpu_hours\": 1.91}, \"metrics\": {\"success_rate\": 53.2, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"num_episodes\": 500, \"suite\": \"libero_spatial\"}}, \"eval_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"pid\": 560607, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\", \"submitted_at\": \"2026-05-18T23:58:31.377Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m64_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m64_seed43\", \"wall_clock_seconds\": 3446.5, \"gpu_hours\": 0.96}, \"metrics\": {\"success_rate\": 60, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_smart_compress_m32_libero_goal\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 571598, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"submitted_at\": \"2026-05-19T00:01:35.221Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"smart_compress_m32 (seed=42)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\", \"wall_clock_seconds\": 3261.2, \"gpu_hours\": 0.91}, \"metrics\": {\"success_rate\": 56.4, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"num_episodes\": 500, \"suite\": \"libero_goal\"}}, \"eval_baseline_control_prune_k05\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 394430, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\", \"submitted_at\": \"2026-05-18T22:26:42.237Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_baseline_control_prune_k05\", \"pruning_method\": \"random + zero_mask\", \"k_ratio\": 0.5, \"wall_clock_seconds\": 5583.9, \"gpu_hours\": 1.55}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"train_smart_compress_m64_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:1\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": null, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 43, \"checkpoint_source\": null, \"eval_data\": null, \"config\": \"configs/smart_compress_m64_seed43.yaml\", \"log_path\": \"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\", \"checkpoint_path\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"pid\": 202271, \"total_steps\": 100000}}, \"train_smart_compress_m32_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"200291\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 43, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\"}}, \"eval_smart_compress_m96_seed43_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 322232, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\", \"submitted_at\": \"2026-05-18T21:31:55.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smart_compress_m96_seed43_v2\", \"wall_clock_seconds\": 5335.1, \"gpu_hours\": 1.48}, \"metrics\": {\"success_rate\": 58.2, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"num_episodes\": 500, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}}, \"eval_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_success_rate_libero.py --checkpoint checkpoints/smart_compress_m96_seed43/checkpoint.pt --config configs/smart_compress_m96_seed43.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smart_compress_m96_seed43.json\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"eval_data\": \"libero_object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43.json\"}, \"metrics\": {\"success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"num_episodes\": 500, \"suite\": \"libero_object\", \"note\": \"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\"}}, \"train_smart_compress_m96_seed43\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=2 python -u train_smart_compress.py --config configs/smart_compress_m96_seed43.yaml --wandb_run smart_compress_m96_seed43 --seed 43 --gpu 0\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:2\"], \"pid\": \"111876\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m96_seed43.log\", \"submitted_at\": \"2026-05-18T12:38:32.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"data_path\": \"HuggingFaceVLA/libero\", \"data_count\": 0, \"checkpoint_source\": \"smolvla_base (from scratch)\", \"eval_data\": \"HuggingFaceVLA/libero\", \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"wall_clock_seconds\": 31663.3, \"gpu_hours\": 8.8}}, \"train_baseline_control_100k_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr_v2\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"109885\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k_v2.log\", \"submitted_at\": \"2026-05-18T12:37:08.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"data_count\": \"same as full_ft baseline\", \"model_name\": \"SmolVLA (from step 99999 checkpoint, fresh lr)\", \"seed\": \"default\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"wall_clock_seconds\": 31745.9, \"gpu_hours\": 8.82}}, \"eval_baseline_control_100k_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_baseline_control_100k_v2.json\", \"server\": \"cqa1-33015\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"eval_data\": \"libero_object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_control_100k_v2.json\"}, \"metrics\": {\"success_rate\": 45, \"per_task_sr\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \"num_episodes\": 500, \"suite\": \"libero_object\"}}, \"eval_official_smolvla_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.95 --output eval_results/official_libero_object_random_prune_k095.json --seed 42\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"data_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"data_count\": \"500 episodes (10 tasks x 50 eps)\", \"model_name\": \"SmolVLA-LIBERO official checkpoint\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"LIBERO-Object (10 tasks, 50 episodes each)\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/official_prune_k095.log\"}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\"}}, \"eval_official_smolvla_prune_k09\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.9 --output eval_results/official_libero_object_random_prune_k09.json --seed 42\", \"server\": \"westd-27271\", \"data_path\": \"libero_object (10 tasks x 50 episodes)\", \"data_count\": 500, \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object\", \"log_path\": \"eval_results/official_libero_object_random_prune_k09.log\", \"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval_k09\", \"pruning_method\": \"true_removal\", \"k_ratio\": 0.9}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\"}}, \"eval_acis_k05_supplement_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --k_ratio 0.5 --num_episodes 50 --gpu 0 --seed 42 --task_ids 6,7,8,9 --output eval_results/eval_acis_k05_supplement_v2.json\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_acis_k05_supplement_v2.log\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"SmolVLA IMM twostage fullft (stage1_done)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"eval_data\": \"libero_object tasks 6-9 x 50 episodes\"}, \"metrics\": {\"overall_SR\": \"0.0% (0/200)\", \"wilson_ci_95\": \"[0.0%, 1.9%]\", \"task6_SR\": \"0% (0/50)\", \"task7_SR\": \"0% (0/50)\", \"task8_SR\": \"0% (0/50)\", \"task9_SR\": \"0% (0/50)\", \"note\": \"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\"}}, \"eval_acis_k05_supplement_200eps\": {\"status\": \"DONE\", \"spec\": {\"failure_reason\": \"cqa1 eval_success_rate_libero.py is OLD version with ACIS hook bug: compares single-camera token shape vs full mask shape, always mismatches, hook returns output unchanged = NO pruning executed. 47.5% SR is unpruned baseline, not ACIS pruning result.\"}, \"metrics\": {\"overall_SR\": \"47.5% (95/200)\", \"wilson_ci_95\": \"[40.7%, 54.4%]\", \"task6_SR\": \"48% (24/50)\", \"task7_SR\": \"40% (20/50)\", \"task8_SR\": \"64% (32/50)\", \"task9_SR\": \"38% (19/50)\"}}, \"eval_official_smolvla_prune_k05_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u eval_official_libero.py --mode random_prune --k_ratio 0.5 --num_episodes 50 --suite libero_object --seed 42\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"136801\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log\", \"submitted_at\": \"2026-05-18T13:24:15.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"data_path\": \"libero_object\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"wall_clock_seconds\": 2825.9, \"gpu_hours\": 0.78}, \"metrics\": {\"overall_sr\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"per_task_sr\": {\"all_tasks\": \"0%\"}, \"note\": \"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\"}}, \"eval_official_smolvla_baseline\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode baseline --seed 42\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"117439\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_baseline.log\", \"submitted_at\": \"2026-05-18T13:17:58.352Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:0\", \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"SmolVLA official checkpoint (HuggingFace)\", \"seed\": 42, \"checkpoint_source\": \"smolvla_libero_official\", \"eval_data\": \"LIBERO-Object 10 tasks x 50 episodes\", \"wall_clock_seconds\": 2419.5, \"gpu_hours\": 0.67}, \"metrics\": {\"overall_sr\": 59.2, \"wilson_ci_95\": [54.8, 63.4], \"total_episodes\": 500, \"total_successes\": 296, \"per_task_sr\": {\"task_0_alphabet_soup\": 64, \"task_1_cream_cheese\": 40, \"task_2_salad_dressing\": 44, \"task_3_bbq_sauce\": 38, \"task_4_ketchup\": 60, \"task_5_tomato_sauce\": 46, \"task_6_butter\": 78, \"task_7_milk\": 52, \"task_8_chocolate_pudding\": 90, \"task_9_orange_juice\": 80}}}, \"eval_smolvla_random_prune_k095\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_random_prune_smolvla.py --k_ratio 0.95 --episodes_per_task 50 --output_name smolvla_random_prune_k095.json --seed 42\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:1\"], \"pid\": \"92881\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log\", \"submitted_at\": \"2026-05-18T12:17:00Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"SmolVLA full_ft (baseline)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"wall_clock_seconds\": 3798.0, \"gpu_hours\": 1.05}, \"metrics\": {\"overall_SR\": 0, \"wilson_ci_95\": [0, 0.0076], \"total_episodes\": 500, \"total_successes\": 0, \"tokens_kept\": 121, \"tokens_removed\": 7, \"k_ratio\": 0.95, \"per_task_SR\": {\"T0_alphabet_soup\": 0, \"T1_cream_cheese\": 0, \"T2_salad_dressing\": 0, \"T3_bbq_sauce\": 0, \"T4_ketchup\": 0, \"T5_tomato_sauce\": 0, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0, \"T9_orange_juice\": 0}}}, \"eval_official_smolvla_pruning\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --mode baseline/random_prune --k_ratio 0.5\", \"server\": \"westd-27271\", \"data_path\": \"LIBERO libero_object (sim)\", \"data_count\": 500, \"model_name\": \"SmolVLA-500M-official-LIBERO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\"}}, \"debug_obs_official\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python debug_obs.py\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"86969\", \"log_path\": \"~/runs/importance_margin_vla_compress/debug_obs_official.log\", \"submitted_at\": \"2026-05-18T12:54:22.640Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_official_smolvla_prune_k05\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.5 --pruning_method true_removal --output eval_results/official_libero_object_random_prune_k05.json --seed 42\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"79867\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05.log\", \"submitted_at\": \"2026-05-18T12:51:19.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"train_baseline_control_100k\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": \"100236\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k.log\", \"submitted_at\": \"2026-05-18T12:25:14.994Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"data_count\": \"same as full_ft baseline\", \"model_name\": \"SmolVLA (from step 99999 checkpoint)\", \"seed\": \"default\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"N/A (training experiment, not eval)\", \"trainable_params\": \"99.9M (action expert + projections only)\", \"wall_clock_seconds\": 504.9, \"gpu_hours\": 0.14}}, \"eval_smart_compress_m128\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_smart_compress_libero.py --n_queries 128\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:0\"], \"pid\": \"18074\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128.log\", \"submitted_at\": \"2026-05-18T10:08:26.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smart_compress_m128\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/smart_compress_m128/checkpoint.pt\", \"eval_data\": \"libero_object\", \"wall_clock_seconds\": 4326.7, \"gpu_hours\": 1.2}, \"metrics\": {\"libero_object_sr\": 0.598, \"libero_object_sr_ci95\": [0.554, 0.64], \"total_episodes\": 500, \"total_successes\": 299, \"per_task_sr\": {\"alphabet_soup\": 0.62, \"cream_cheese\": 0.58, \"salad_dressing\": 0.54, \"bbq_sauce\": 0.34, \"ketchup\": 0.62, \"tomato_sauce\": 0.5, \"butter\": 0.82, \"milk\": 0.56, \"chocolate_pudding\": 0.82, \"orange_juice\": 0.58}}}, \"eval_openvla_pruning_k03_restart\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"data_count\": 500, \"model_name\": \"openvla-libero-object\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\"}, \"metrics\": {\"overall_sr\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"wilson_ci_95\": [0.173, 0.244], \"elapsed_minutes\": 288.6, \"per_task_sr\": {\"alphabet_soup\": 0.14, \"cream_cheese\": 0, \"salad_dressing\": 0.64, \"bbq_sauce\": 0.3, \"ketchup\": 0.3, \"tomato_sauce\": 0.08, \"butter\": 0, \"milk\": 0.08, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.42}}}, \"train_smart_compress_m128_resume\": {\"status\": \"ANALYZING\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128/checkpoint.pt\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m128_resume.log\", \"wandb_offline_run\": \"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_132800-x610qzvt\"}, \"metrics\": {\"train_action_loss\": 0.05412, \"eval_action_loss\": 0.05743, \"train_grad_norm\": 0.92663, \"total_steps\": 99999, \"resumed_from_step\": 32001}}, \"smolvla_entropy_perlayer\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python measure_smolvla_entropy_perlayer.py\", \"server\": \"cqa1-33015\", \"data_path\": \"HuggingFaceVLA/libero (cached)\", \"data_count\": 256, \"model_name\": \"smolvla_base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"eval_data\": \"LIBERO mixed tasks\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_entropy_perlayer.log\"}, \"metrics\": {\"overall_entropy_ratio\": 0.9521, \"overall_entropy_std\": 0.02, \"n_images\": 260, \"n_tasks\": 10, \"n_layers\": 16, \"entropy_range\": [0.9311, 0.9826], \"entropy_range_width\": 0.05, \"per_layer\": {\"L0\": 0.9826, \"L1\": 0.9561, \"L2\": 0.9597, \"L3\": 0.9434, \"L4\": 0.9408, \"L5\": 0.9406, \"L6\": 0.9474, \"L7\": 0.9628, \"L8\": 0.9614, \"L9\": 0.9572, \"L10\": 0.9455, \"L11\": 0.951, \"L12\": 0.9485, \"L13\": 0.9311, \"L14\": 0.9482, \"L15\": 0.9566}, \"dataset\": \"LIBERO-Object (task 20-29)\", \"note\": \"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\", \"openvla_comparison\": {\"overall\": 0.639, \"range_width\": 0.5}}}, \"inference_latency_comparison\": {\"status\": \"DONE\", \"spec\": {\"command\": \"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 python measure_inference_latency.py\", \"server\": \"cqa1-33015\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"smolvla_base + SmartCompressWrapper\", \"seed\": 42}, \"metrics\": {\"baseline_128_mean_ms\": 164.33, \"m32_mean_ms\": 154.78, \"m64_mean_ms\": 156.16, \"speedup_m32\": 1.0617, \"speedup_m64\": 1.0523, \"baseline_params\": 450046176, \"compressor_m32_params\": 22179840}}, \"eval_openvla_pruning_k03\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"server\": \"westd-27271\", \"gpu\": \"cuda:1\", \"pid\": 768729, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"OpenVLA (7B)\", \"seed\": 7, \"checkpoint_source\": \"openvla-libero-object\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.log\"}}, \"openvla_entropy_real\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python measure_openvla_entropy_real.py\", \"server\": \"westd-27271\", \"data_path\": \"LIBERO-Object simulation (10 tasks, 250 rendered frames)\", \"data_count\": 250, \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42}, \"metrics\": {\"overall_entropy_ratio\": 0.6393, \"overall_entropy_std\": 0.1334, \"overall_vision_attn_frac\": 0.1211, \"n_images\": 250, \"n_tasks\": 10, \"min_entropy_layer\": {\"layer\": 29, \"ratio\": 0.4774}, \"max_entropy_layer\": {\"layer\": 0, \"ratio\": 0.979}, \"shallow_layers_0_1\": [0.979, 0.952], \"deep_layers_27_30\": [0.542, 0.53, 0.477, 0.524], \"previous_random_N20\": 0.617, \"smolvla_reference\": 0.98}}}, \"count\": 50, \"total\": 127, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3173}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
I found the key information. There's already a `eval_smolvla_baseline_spatial` entry in the registry with status "PREPARING". 

The baseline eval uses `eval_success_rate_libero.py` with `--mode baseline`. Looking at previous successful baseline evals:
- `eval_baseline_control_100k_v2` used the baseline_control checkpoint with `eval_success_rate_libero.py --mode baseline`
- The LIBERO-Object baseline SR=44.8% was likely from `eval_fullft_baseline_libero` or similar

But wait, the task says "SmolVLA base" - this is the LoRA fine-tuned model, not the official SmolVLA. 

I need to find the `libero_baseline` checkpoint (the LoRA fine-tuned SmolVLA without compression) at `checkpoints/libero_baseline/latest/` and verify what's there, then check GPU availability on cqa1-33015.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "dc03c1b4-2b6e-4145-bb98-a4ce613b23ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8HKxhg1JqgayzSjkhUdKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 41187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20585
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

Registry 中已有 `eval_smolvla_baseline_spatial` (PREPARING 状态)。让我确认 checkpoint 文件和 GPU 可用性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "e82776d6-94dc-44f5-9ef5-0becaba1c099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8HKxhg1JqgayzSjkhUdKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 41187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20585
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01ENn7bT1NwRfsFjr7UWbbCj`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && ls -la checkpoints/libero_baseline/latest/; echo \"===\"; nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader; echo \"===\"; tmux ls 2>/dev/null || echo \"no tmux sessions\"",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "99a88b75-7414-45eb-b8fc-c8bf2459ebd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8HKxhg1JqgayzSjkhUdKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 41187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20585
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

_source line 33 · 2026-05-19T11:12:26.562Z_

<details><summary>↩ Tool result · `toolu_01ENn7bT1NwRfsFjr7UWbbCj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 903184\\ndrwxr-xr-x  2 root root        35 May 17 05:25 .\\ndrwxr-xr-x 12 root root      4096 May 17 05:25 ..\\n-rw-r--r--  1 root root 924851886 May 17 05:25 checkpoint.pt\\n===\\n0, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n3, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n===\\nno tmux sessions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "7f2afd38-8bc9-4215-b892-d0d1e9e9b8e3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 903184\\\\ndrwxr-xr-x  2 root root        35 May 17 05:25 .\\\\ndrwxr-xr-x 12 root root      4096 May 17 05:25 ..\\\\n-rw-r--r--  1 root root 924851886 May 17 05:25 checkpoint.pt\\\\n===\\\\n0, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\\\n1, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\\\n2, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\\\n3, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\\\n===\\\\nno tmux sessions\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 903184\\ndrwxr-xr-x  2 root root        35 May 17 05:25 .\\ndrwxr-xr-x 12 root root      4096 May 17 05:25 ..\\n-rw-r--r--  1 root root 924851886 May 17 05:25 checkpoint.pt\\n===\\n0, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n3, NVIDIA GeForce RTX 4090 D, 0 MiB, 24564 MiB, 0 %\\n===\\nno tmux sessions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
All 4 GPUs are free. The checkpoint is at `checkpoints/libero_baseline/latest/checkpoint.pt` (925MB). The config is `configs/libero_baseline.yaml`.

Now I need to construct the eval command. Looking at how `eval_success_rate_libero.py` works:
- `--checkpoint checkpoints/libero_baseline/latest/checkpoint.pt`
- `--config configs/libero_baseline.yaml`


- `--suite libero_spatial`
- `--num_episodes 50`
- `--gpu 0`
- `--seed 42`
- `--mode baseline`
- `--output eval_results/eval_smolvla_baseline_spatial.json`

I don't have access to submit_training_job, so I'll set up a tmux session manually using ssh_execute to run the evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "79030020-3ff4-4712-82d4-fc088636ff3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F5RgpajnLmcDzbxFBPwox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 61772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 862
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

_source line 35_

所有 4 GPU 空闲，checkpoint 就绪。启动 eval。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "79f52fba-a020-477d-8fcd-cdf586882291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F5RgpajnLmcDzbxFBPwox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 61772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 862
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AbeX7CZF7bZDJtJAsTogm4`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\" && sleep 2 && tmux ls",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c9960a64-f615-4be9-aca0-974e013df5d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F5RgpajnLmcDzbxFBPwox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 61772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 862
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

_source line 37 · 2026-05-19T11:12:40.273Z_

<details><summary>↩ Tool result · `toolu_01AbeX7CZF7bZDJtJAsTogm4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial \\\"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\\\" && sleep 2 && tmux ls'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nno server running on /tmp/tmux-0/default\\n\\n\", \"metadata\": {\"elapsed_seconds\": 2.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "04dabb05-a225-42e3-890c-efb7b73a2a13",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial \\\\\\\"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\\\\\\\" && sleep 2 && tmux ls'\\\\n\\\\nExit code: 1\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nno server running on /tmp/tmux-0/default\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial \\\"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\\\" && sleep 2 && tmux ls'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nno server running on /tmp/tmux-0/default\\n\\n\", \"metadata\": {\"elapsed_seconds\": 2.4}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
The tmux session failed because the tmux server isn't running. Let me create the runs directory first and then try again.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "f631b9ba-1e9a-44dc-8630-93840a815371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gqruy7xGfVpwwDU37m1cAa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 62634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1026
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AJU5ZMLMXP3YRapHeoXs6t`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "mkdir -p ~/runs/importance_margin_vla_compress && cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\"",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "ba4e2243-5f12-45d5-add4-5e9f5494668c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gqruy7xGfVpwwDU37m1cAa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 62634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1026
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

_source line 40 · 2026-05-19T11:12:46.805Z_

<details><summary>↩ Tool result · `toolu_01AJU5ZMLMXP3YRapHeoXs6t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "fab1993d-619a-48de-9d0d-6c89855c918b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.89}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SfcN3D2ijZiafLGfojakZ8`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tmux ls && sleep 5 && tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null || echo \"log not yet available\"",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "e18b2ece-0ca3-4de9-a4b7-57cbb67c944f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9i7VYCLX6xH8YUVkc8yH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 63660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 42 · 2026-05-19T11:12:50.892Z_

<details><summary>↩ Tool result · `toolu_01SfcN3D2ijZiafLGfojakZ8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"log not yet available\\n\", \"stderr\": \"no server running on /tmp/tmux-0/default\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "76aa7954-2c28-4051-83e4-07e295871358",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"log not yet available\\\\n\\\", \\\"stderr\\\": \\\"no server running on /tmp/tmux-0/default\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"log not yet available\\n\", \"stderr\": \"no server running on /tmp/tmux-0/default\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Hmm, the tmux session seems to have crashed immediately. Let me check what happened by running the command directly to see if there's an error.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "8996085f-c7b3-460b-bd66-caa62dcb0b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3FdgWUgz7eNTMRSnqYJSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 64096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 44_

tmux session 立即退出。让我排查问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "250339f0-c85e-48df-9464-0f92486730d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3FdgWUgz7eNTMRSnqYJSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 64096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015hfMsbxyCxRi4AXRkDuA3R`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | head -60",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "d3af3834-8fec-45c7-9b78-c941292187fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3FdgWUgz7eNTMRSnqYJSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 64096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 46 · 2026-05-19T11:12:56.710Z_

<details><summary>↩ Tool result · `toolu_015hfMsbxyCxRi4AXRkDuA3R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "90609018-304c-4ca7-b94b-e2dfca8143f7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"bash: line 1: python: command not found\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

需要 activate conda。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "18cf3fb2-d844-4054-87a7-93024d799a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMqW4y7Sno4RZhs8FSEZXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 64340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 535
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01L7NQ29S5Dz7YptKwJY5Kdj`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "which python3 2>/dev/null; source /root/miniconda3/bin/activate 2>/dev/null && which python; conda info --envs 2>/dev/null | head -10",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "4933f400-02f7-45d7-991e-f9b5c977e941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMqW4y7Sno4RZhs8FSEZXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 64340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 535
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T11:13:02.115Z_

<details><summary>↩ Tool result · `toolu_01L7NQ29S5Dz7YptKwJY5Kdj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n# conda environments:\\n#\\nbase                  *  /root/miniconda3\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "15d3f035-b8b0-41af-9df3-e156ac00c7c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/bin/python\\\\n# conda environments:\\\\n#\\\\nbase                  *  /root/miniconda3\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n# conda environments:\\n#\\nbase                  *  /root/miniconda3\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TLnKKyEktnhCYtvV4yaCGt`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && tmux new-session -d -s eval_smolvla_baseline_spatial 'source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json 2>&1 | tee ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log'",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "13c024a6-5dea-4f8c-9314-20396214acd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jnzrmia7uvHD3nNXv46m6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 64340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 799
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T11:13:09.826Z_

<details><summary>↩ Tool result · `toolu_01TLnKKyEktnhCYtvV4yaCGt`</summary>

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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "8e606547-2ac4-433c-8d6f-cc6ce5fbaca3",
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

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Jb7CpUNdSzi4aX1ot4aUbH`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "sleep 10 && tmux ls 2>/dev/null && tail -40 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null || echo \"log not available yet\"",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "a2694c8c-287e-416a-a9f1-3a7eb2eb8550",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4PRjRhYXa9tRtC2hAPr9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 65139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 412
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

_source line 53 · 2026-05-19T11:13:25.259Z_

<details><summary>↩ Tool result · `toolu_01Jb7CpUNdSzi4aX1ot4aUbH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_smolvla_baseline_spatial: 1 windows (created Tue May 19 19:13:09 2026)\\n2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "67d43b31-544b-4cbd-bfbb-afdba9ad4df0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_smolvla_baseline_spatial: 1 windows (created Tue May 19 19:13:09 2026)\\\\n2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\\\nReducing the number of VLM layers to 16 ...\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_smolvla_baseline_spatial: 1 windows (created Tue May 19 19:13:09 2026)\\n2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

模型正在加载。让我等更多日志确认 eval 正常开始。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "5c48f480-5cdd-4dc8-a002-996585a067e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDk3P47Vu2EGbuEHDGWkuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 65551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01GXcom1uAVNw19JCWeEoqUv`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "sleep 30 && tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "eae3decd-9063-455a-82ce-c2de63290f82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDk3P47Vu2EGbuEHDGWkuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 65551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 56 · 2026-05-19T11:13:59.653Z_

<details><summary>↩ Tool result · `toolu_01GXcom1uAVNw19JCWeEoqUv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 30 && tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "5212326d-7e4a-481f-81c2-2ce7579368e4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Command did not complete within 30 seconds!\\\\n\\\\nCommand: 'sleep 30 && tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null'\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 30.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 30 && tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0168yhCAPPPFwF81fQSoyAcT`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -30 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "ab67a6c0-6b33-45f8-a7e7-21bd1536553a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114wUsSUtr4kX9VDJfEAiSi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 66057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 297
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

_source line 58 · 2026-05-19T11:14:03.317Z_

<details><summary>↩ Tool result · `toolu_0168yhCAPPPFwF81fQSoyAcT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n2026-05-19 19:13:26 [INFO] Updated state feature shape: (6,) -> (8,)\\n2026-05-19 19:13:26 [INFO] Updated action feature shape: (6,) -> (7,)\\n2026-05-19 19:13:26 [INFO] Updated cameras: ['observation.images.camera1', 'observation.images.camera2', 'observation.images.camera3'] -> ['observation.images.image', 'observation.images.image2'] (shape=(3, 256, 256))\\n2026-05-19 19:13:26 [INFO] LoRA applied: rank=32, alpha=16, trainable params: 1485312\\n2026-05-19 19:13:27 [INFO] Model loaded in 15.9s\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-19 19:13:27 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-19 19:13:27 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-19 19:13:27 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-19 19:13:27 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 19:13:27 [INFO] Suite 'libero_spatial' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 19:13:27 [INFO] --- Task 0: pick up the black bowl between the plate and the ramekin and place it on the plate ---\\nLocal assets not found. Downloading from HuggingFace Hub...\\nAssets already downloaded at /root/.cache/libero/assets\\n2026-05-19 19:13:41 [INFO]   Ep 1/50 | FAIL | steps=280\\n2026-05-19 19:13:51 [INFO]   Ep 2/50 | FAIL | steps=280\\n2026-05-19 19:14:02 [INFO]   Ep 3/50 | SUCCESS | steps=205\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c76663e0-f1c0-425f-b31a-6516fb0cccbd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\\\nReducing the number of VLM layers to 16 ...\\\\nLoading weights from local directory\\\\n2026-05-19 19:13:26 [INFO] Updated state feature shape: (6,) -> (8,)\\\\n2026-05-19 19:13:26 [INFO] Updated action feature shape: (6,) -> (7,)\\\\n2026-05-19 19:13:26 [INFO] Updated cameras: ['observation.images.camera1', 'observation.images.camera2', 'observation.images.camera3'] -> ['observation.images.image', 'observation.images.image2'] (shape=(3, 256, 256))\\\\n2026-05-19 19:13:26 [INFO] LoRA applied: rank=32, alpha=16, trainable params: 1485312\\\\n2026-05-19 19:13:27 [INFO] Model loaded in 15.9s\\\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\\\n2026-05-19 19:13:27 [WARNING] No private macro file found!\\\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\\\n2026-05-19 19:13:27 [WARNING] It is recommended to use a private macro file\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\\\n2026-05-19 19:13:27 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\\\n2026-05-19 19:13:27 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n2026-05-19 19:13:27 [INFO] Suite 'libero_spatial' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n2026-05-19 19:13:27 [INFO] --- Task 0: pick up the black bowl between the plate and the ramekin and place it on the plate ---\\\\nLocal assets not found. Downloading from HuggingFace Hub...\\\\nAssets already downloaded at /root/.cache/libero/assets\\\\n2026-05-19 19:13:41 [INFO]   Ep 1/50 | FAIL | steps=280\\\\n2026-05-19 19:13:51 [INFO]   Ep 2/50 | FAIL | steps=280\\\\n2026-05-19 19:14:02 [INFO]   Ep 3/50 | SUCCESS | steps=205\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 19:13:11 [INFO] Suite: libero_spatial | Device: cuda:0 | Mode: baseline | Pruning: zero_mask | Episodes/task: 50 | Max steps: 280\\n2026-05-19 19:13:11 [INFO] Loading model from checkpoints/libero_baseline/latest/checkpoint.pt ...\\n2026-05-19 19:13:12 [INFO] JAX version 0.10.0 available.\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\nYou have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n2026-05-19 19:13:26 [INFO] Updated state feature shape: (6,) -> (8,)\\n2026-05-19 19:13:26 [INFO] Updated action feature shape: (6,) -> (7,)\\n2026-05-19 19:13:26 [INFO] Updated cameras: ['observation.images.camera1', 'observation.images.camera2', 'observation.images.camera3'] -> ['observation.images.image', 'observation.images.image2'] (shape=(3, 256, 256))\\n2026-05-19 19:13:26 [INFO] LoRA applied: rank=32, alpha=16, trainable params: 1485312\\n2026-05-19 19:13:27 [INFO] Model loaded in 15.9s\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-19 19:13:27 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-19 19:13:27 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-19 19:13:27 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-19 19:13:27 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 19:13:27 [INFO] Suite 'libero_spatial' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-19 19:13:27 [INFO] --- Task 0: pick up the black bowl between the plate and the ramekin and place it on the plate ---\\nLocal assets not found. Downloading from HuggingFace Hub...\\nAssets already downloaded at /root/.cache/libero/assets\\n2026-05-19 19:13:41 [INFO]   Ep 1/50 | FAIL | steps=280\\n2026-05-19 19:13:51 [INFO]   Ep 2/50 | FAIL | steps=280\\n2026-05-19 19:14:02 [INFO]   Ep 3/50 | SUCCESS | steps=205\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

Eval 正常运行中，已经在 Task 0 跑到 Ep 3。现在注册 registry 和 PID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c05cb699-9928-4091-ac3e-fe00487c0e82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDB4f1nVT5n68Hwcy9YoYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 66354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Ns86eBQ833sYRqDf4wYKjV`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "pgrep -f \"eval_success_rate_libero.py.*libero_spatial\" | head -1",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "58013ba5-3c41-480e-8a9d-a73198cfa8f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDB4f1nVT5n68Hwcy9YoYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 66354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

_source line 61 · 2026-05-19T11:14:07.616Z_

<details><summary>↩ Tool result · `toolu_01Ns86eBQ833sYRqDf4wYKjV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"439389\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "c9d4c78c-2b29-49d7-a02a-65ec8b9ed947",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"439389\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"439389\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EXHMGQbhJqsx37teQux8KK`</summary>

```json
{
  "exp_id": "eval_smolvla_baseline_spatial",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json",
    "server": "cqa1-33015",
    "gpu": "cuda:0",
    "pid": 439389,
    "log_path": "~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log",
    "submitted_at": "2026-05-19T19:13:09Z",
    "submitted_via": "tmux",
    "backend": "tmux",
    "account": "root",
    "data_path": "libero_spatial",
    "data_count": 500,
    "model_name": "smolvla_baseline (LoRA fine-tuned, no compression)",
    "seed": 42,
    "checkpoint_source": "checkpoints/libero_baseline/latest/checkpoint.pt",
    "eval_data": "LIBERO-Spatial (10 tasks x 50 episodes)",
    "checkpoint_path": "N/A (eval only)",
    "tmux_session": "eval_smolvla_baseline_spatial"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "b5fad5e0-3505-4488-abdb-8282dd6d362a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmYPU248BgCRuX733VJ5ys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 67540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 242
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

_source line 63 · 2026-05-19T11:14:16.354Z_

<details><summary>↩ Tool result · `toolu_01EXHMGQbhJqsx37teQux8KK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2951}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "cfc18b20-1d2b-4b12-b355-d0161df42bdc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2951}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2951}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
The registry has a state machine. Let me transition through PENDING first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "18f2c4e6-2024-43b5-8412-2eca58754cdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFHzHUBwyivpp1DHSV9zMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 67782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01XNTXynaE2kvoCxqj6Cz4xc`</summary>

```json
{
  "exp_id": "eval_smolvla_baseline_spatial",
  "field": "status",
  "value": "PENDING",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "1ab562c8-e0f6-45a1-b0f9-2845279eb62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFHzHUBwyivpp1DHSV9zMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 67782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 66 · 2026-05-19T11:14:20.832Z_

<details><summary>↩ Tool result · `toolu_01XNTXynaE2kvoCxqj6Cz4xc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:20.208Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9178}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "f316e831-b31d-442b-b8db-57ba9fb58e10",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_smolvla_baseline_spatial\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T11:11:07.968Z\\\", \\\"updated_at\\\": \\\"2026-05-19T11:14:20.208Z\\\", \\\"hypothesis\\\": \\\"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9178}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:20.208Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9178}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019xpWEQuMb8JzF5sFeXHY2B`</summary>

```json
{
  "exp_id": "eval_smolvla_baseline_spatial",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json",
    "server": "cqa1-33015",
    "gpu": "cuda:0",
    "pid": 439389,
    "log_path": "~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log",
    "submitted_at": "2026-05-19T19:13:09Z",
    "submitted_via": "tmux",
    "backend": "tmux",
    "account": "root",
    "data_path": "libero_spatial",
    "data_count": 500,
    "model_name": "smolvla_baseline (LoRA fine-tuned, no compression)",
    "seed": 42,
    "checkpoint_source": "checkpoints/libero_baseline/latest/checkpoint.pt",
    "eval_data": "LIBERO-Spatial (10 tasks x 50 episodes)",
    "checkpoint_path": "N/A (eval only)",
    "tmux_session": "eval_smolvla_baseline_spatial"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "e24b7b38-8624-407e-ab15-632da81a7710",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zxkPQg6iQQCXQCNE5qp2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 68468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
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

_source line 68 · 2026-05-19T11:14:29.404Z_

<details><summary>↩ Tool result · `toolu_019xpWEQuMb8JzF5sFeXHY2B`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3316}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "a950b3d8-ea4b-4f0f-b2a9-28d4fb785218",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3316}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3316}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DfLZ8PrJERoh6sVSGNE4wn`</summary>

```json
{
  "exp_id": "eval_smolvla_baseline_spatial",
  "field": "status",
  "value": "QUEUED",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "de51ab28-62d8-409d-bec0-85c83243d227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQdJvQ6Poz1V8yotWSWj98",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 68858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 583
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

_source line 70 · 2026-05-19T11:14:33.219Z_

<details><summary>↩ Tool result · `toolu_01DfLZ8PrJERoh6sVSGNE4wn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:32.611Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9833}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "20bdc2a6-2e63-4ad5-943e-29711c749c8b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_smolvla_baseline_spatial\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T11:11:07.968Z\\\", \\\"updated_at\\\": \\\"2026-05-19T11:14:32.611Z\\\", \\\"hypothesis\\\": \\\"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9833}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:32.611Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9833}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01KhjHdJ5ETABrf2P156p8xm`</summary>

```json
{
  "exp_id": "eval_smolvla_baseline_spatial",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json",
    "server": "cqa1-33015",
    "gpu": "cuda:0",
    "pid": 439389,
    "log_path": "~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log",
    "submitted_at": "2026-05-19T19:13:09Z",
    "submitted_via": "tmux",
    "backend": "tmux",
    "account": "root",
    "data_path": "libero_spatial",
    "data_count": 500,
    "model_name": "smolvla_baseline (LoRA fine-tuned, no compression)",
    "seed": 42,
    "checkpoint_source": "checkpoints/libero_baseline/latest/checkpoint.pt",
    "eval_data": "LIBERO-Spatial (10 tasks x 50 episodes)",
    "checkpoint_path": "N/A (eval only)",
    "tmux_session": "eval_smolvla_baseline_spatial"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "63329d5d-926f-4553-a913-64c28b9a0d5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqddaNcf4qRYRu18giHeDn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 69441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 72 · 2026-05-19T11:14:39.958Z_

<details><summary>↩ Tool result · `toolu_01KhjHdJ5ETABrf2P156p8xm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:39.354Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 439389, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\", \"submitted_at\": \"2026-05-19T19:13:09Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smolvla_baseline (LoRA fine-tuned, no compression)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_baseline/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smolvla_baseline_spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9101}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "82b10833-e9df-4442-904a-3ab944c4b735",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_smolvla_baseline_spatial\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T11:11:07.968Z\\\", \\\"updated_at\\\": \\\"2026-05-19T11:14:39.354Z\\\", \\\"hypothesis\\\": \\\"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 439389, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T19:13:09Z\\\", \\\"submitted_via\\\": \\\"tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_spatial\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"smolvla_baseline (LoRA fine-tuned, no compression)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/libero_baseline/latest/checkpoint.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 50 episodes)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"tmux_session\\\": \\\"eval_smolvla_baseline_spatial\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9101}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_smolvla_baseline_spatial\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:11:07.968Z\", \"updated_at\": \"2026-05-19T11:14:39.354Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 439389, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\", \"submitted_at\": \"2026-05-19T19:13:09Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_spatial\", \"data_count\": 500, \"model_name\": \"smolvla_baseline (LoRA fine-tuned, no compression)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/libero_baseline/latest/checkpoint.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"checkpoint_path\": \"N/A (eval only)\", \"tmux_session\": \"eval_smolvla_baseline_spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9101}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 73_

Registry 更新完成。现在设置 cron 监控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "890dea5b-36b3-4531-b345-4cac81a18c56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C78t41uJ4oHqt6K5mLDiGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 69803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1134
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

_source line 74_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P1yqnnXosBbV7kxDA5E7yQ`</summary>

```json
{
  "query": "select:CronCreate",
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "bf980cd9-74af-4b2f-8dee-60db0bb472fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C78t41uJ4oHqt6K5mLDiGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 69803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1134
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

_source line 75 · 2026-05-19T11:14:43.269Z_

<details><summary>↩ Tool result · `toolu_01P1yqnnXosBbV7kxDA5E7yQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "CronCreate"
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
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "52990e65-ecca-4025-a436-1a70572a45eb",
  "tool_use_result": {
    "matches": [
      "CronCreate"
    ],
    "query": "select:CronCreate",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — CronCreate · `toolu_01Po7bxg7LwUprJTdyvhc4M7`</summary>

```json
{
  "cron": "*/12 * * * *",
  "prompt": "Check eval_smolvla_baseline_spatial on cqa1-33015: ssh_execute \"tail -5 ~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log 2>/dev/null; tmux has-session -t eval_smolvla_baseline_spatial 2>/dev/null && echo TMUX_ALIVE || echo TMUX_DEAD\". If TMUX_DEAD or log shows completion, read eval_results/eval_smolvla_baseline_spatial.json and update registry eval_smolvla_baseline_spatial to DONE with metrics. If still running, just report progress.",
  "recurring": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "3fc6b7b5-3f5c-4a05-9631-cca11c736c3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RTPtAp6zAxYoSn1Z8SBSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 70937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

_source line 77 · 2026-05-19T11:14:49.072Z_

<details><summary>↩ Tool result · `toolu_01Po7bxg7LwUprJTdyvhc4M7`</summary>

```text
Scheduled recurring job 01841a32 (Every 12 minutes). Session-only (not written to disk, dies when Claude exits). Auto-expires after 7 days. Use CronDelete to cancel sooner.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "6d52a3ea-a786-458f-9006-7d583c144759",
  "tool_use_result": {
    "id": "01841a32",
    "humanSchedule": "Every 12 minutes",
    "recurring": true,
    "durable": false
  }
}
```

</details>

---

### Assistant

_source line 78_

已完成：

- **Eval 已启动**: `eval_smolvla_baseline_spatial` 在 cqa1-33015 cuda:0 上运行
  - 脚本: `eval_success_rate_libero.py --mode baseline --suite libero_spatial`
  - Checkpoint: `checkpoints/libero_baseline/latest/checkpoint.pt` (SmolVLA LoRA fine-tuned, 无压缩)
  - 参数: 50 episodes/task, seed=42, 10 tasks = 500 total episodes
  - tmux session: `eval_smolvla_baseline_spatial`
- **Registry**: `eval_smolvla_baseline_spatial` → RUNNING
- **Cron 监控**: 每 12 分钟检查一次进度（job 01841a32）
- 日志已确认 eval 正常进行中（Task 0 已开始，Ep 3 成功）

预计运行约 1.5-2 小时（参考之前 spatial eval ~6800s）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "uuid": "31362409-f9c9-4ebc-b35e-a50c70e70009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5vL1s5J5odUrsHp5Rsay1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 72135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 304
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

_source line 79_

已完成：

- **Eval 已启动**: `eval_smolvla_baseline_spatial` 在 cqa1-33015 cuda:0 上运行
  - 脚本: `eval_success_rate_libero.py --mode baseline --suite libero_spatial`
  - Checkpoint: `checkpoints/libero_baseline/latest/checkpoint.pt` (SmolVLA LoRA fine-tuned, 无压缩)
  - 参数: 50 episodes/task, seed=42, 10 tasks = 500 total episodes
  - tmux session: `eval_smolvla_baseline_spatial`
- **Registry**: `eval_smolvla_baseline_spatial` → RUNNING
- **Cron 监控**: 每 12 分钟检查一次进度（job 01841a32）
- 日志已确认 eval 正常进行中（Task 0 已开始，Ep 3 成功）

预计运行约 1.5-2 小时（参考之前 spatial eval ~6800s）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 201067,
  "duration_api_ms": 147138,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "6b32ee66-1020-4b04-b133-e3ea1175caf9",
  "total_cost_usd": 1.25600775,
  "usage": {
    "input_tokens": 30,
    "cache_creation_input_tokens": 61133,
    "cache_read_input_tokens": 1370515,
    "output_tokens": 7483,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61133,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 273,
        "cache_read_input_tokens": 72135,
        "cache_creation_input_tokens": 304,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 304
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1334,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001444,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 30,
      "outputTokens": 7483,
      "cacheReadInputTokens": 1370515,
      "cacheCreationInputTokens": 61133,
      "webSearchRequests": 0,
      "costUSD": 1.25456375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5e7aeafe-abb0-4a2c-937e-a2a8fc11acaa"
}
```

</details>

---

# ssh read exp files

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_ssh_read_exp_files_20260517T083443.log`
- **Structured JSON:** [`766aa1cefd9af3788f74.json`](../../sessions/76/766aa1cefd9af3788f74.json)

## Before a recorded user message

12 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
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
  "uuid": "a875353c-1f8c-423b-b6bb-9d0434733be5",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/memory/"
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
    "resetsAt": 1779021000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c49e1cfe-8974-43d4-8c8a-13c37892ac32",
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to read two files from a remote server. Let me use the MCP tools to do this. First, I need to load the tool schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "9ca4d611-6a1e-4a9c-9fdf-8588db503a40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMin2hZDFcYGTPmexYEfX6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12275,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12275
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014wM55mpjp3nvb1x7Un2Rhp`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "c51bb9ca-51ae-4ab4-b07d-98af849134d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMin2hZDFcYGTPmexYEfX6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12275,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12275
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

_source line 6 · 2026-05-17T08:34:56.697Z_

<details><summary>↩ Tool result · `toolu_014wM55mpjp3nvb1x7Un2Rhp`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "730a5be8-387a-4317-97a1-76b8d5ca1809",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GvAd6XnHzHKDyemAuTMkXj`</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/results.json",
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
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "661d1216-63b8-4e44-8dc9-1ffc4c7a39bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tdMcUFxhJienrfySr1n8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F1WyQ25BZZrGRyAWzL4Bkb`</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/report.md",
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
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "f1604637-c25a-4c41-897c-1880893430c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tdMcUFxhJienrfySr1n8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
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

_source line 9 · 2026-05-17T08:35:05.115Z_

<details><summary>↩ Tool result · `toolu_01GvAd6XnHzHKDyemAuTMkXj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_ot7b_full_pipeline\\\",\\n  \\\"model\\\": \\\"open-thoughts/OpenThinker-7B\\\",\\n  \\\"n_traces\\\": 228,\\n  \\\"split\\\": {\\n    \\\"train\\\": 136,\\n    \\\"val\\\": 45,\\n    \\\"test\\\": 47\\n  },\\n  \\\"phase2_layer_sweep\\\": {\\n    \\\"best_layer\\\": 0,\\n    \\\"best_depth_pct\\\": 0,\\n    \\\"results\\\": [\\n      {\\n        \\\"layer\\\": 0,\\n        \\\"bal_acc\\\": 0.6671,\\n        \\\"crossing_rate\\\": 0.5319,\\n        \\\"lead_mean\\\": 29.8,\\n        \\\"pre_cp_fpr\\\": 0.2186,\\n        \\\"score\\\": 0.3549\\n      },\\n      {\\n        \\\"layer\\\": 4,\\n        \\\"bal_acc\\\": 0.663,\\n        \\\"crossing_rate\\\": 0.4043,\\n        \\\"lead_mean\\\": 25.6,\\n        \\\"pre_cp_fpr\\\": 0.1538,\\n        \\\"score\\\": 0.268\\n      },\\n      {\\n        \\\"layer\\\": 8,\\n        \\\"bal_acc\\\": 0.664,\\n        \\\"crossing_rate\\\": 0.2553,\\n        \\\"lead_mean\\\": 23.4,\\n        \\\"pre_cp_fpr\\\": 0.14,\\n        \\\"score\\\": 0.1695\\n      },\\n      {\\n        \\\"layer\\\": 12,\\n        \\\"bal_acc\\\": 0.6752,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 15.6,\\n        \\\"pre_cp_fpr\\\": 0.1242,\\n        \\\"score\\\": 0.2155\\n      },\\n      {\\n        \\\"layer\\\": 16,\\n        \\\"bal_acc\\\": 0.6816,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 16.1,\\n        \\\"pre_cp_fpr\\\": 0.12,\\n        \\\"score\\\": 0.2175\\n      },\\n      {\\n        \\\"layer\\\": 20,\\n        \\\"bal_acc\\\": 0.6551,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 13.8,\\n        \\\"pre_cp_fpr\\\": 0.1355,\\n        \\\"score\\\": 0.2091\\n      },\\n      {\\n        \\\"layer\\\": 24,\\n        \\\"bal_acc\\\": 0.6686,\\n        \\\"crossing_rate\\\": 0.2979,\\n        \\\"lead_mean\\\": 26.5,\\n        \\\"pre_cp_fpr\\\": 0.1324,\\n        \\\"score\\\": 0.1992\\n      },\\n      {\\n        \\\"layer\\\": 27,\\n        \\\"bal_acc\\\": 0.6299,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 29.5,\\n        \\\"pre_cp_fpr\\\": 0.1524,\\n        \\\"score\\\": 0.201\\n      }\\n    ]\\n  },\\n  \\\"phase3_temporal_probes\\\": {\\n    \\\"best_window\\\": 3,\\n    \\\"best_layer\\\": 0,\\n    \\\"results\\\": [\\n      {\\n        \\\"window\\\": 1,\\n        \\\"bal_acc\\\": 0.6671,\\n        \\\"precision\\\": 0.3369,\\n        \\\"coverage\\\": 0.6809,\\n        \\\"pre_cp_fpr\\\": 0.2186,\\n        \\\"lead_mean\\\": 29.8\\n      },\\n      {\\n        \\\"window\\\": 3,\\n        \\\"bal_acc\\\": 0.6721,\\n        \\\"precision\\\": 0.3571,\\n        \\\"coverage\\\": 0.5957,\\n        \\\"pre_cp_fpr\\\": 0.1877,\\n        \\\"lead_mean\\\": 32.9\\n      },\\n      {\\n        \\\"window\\\": 5,\\n        \\\"bal_acc\\\": 0.6668,\\n        \\\"precision\\\": 0.3598,\\n        \\\"coverage\\\": 0.617,\\n        \\\"pre_cp_fpr\\\": 0.1782,\\n        \\\"lead_mean\\\": 33.7\\n      },\\n      {\\n        \\\"window\\\": 10,\\n        \\\"bal_acc\\\": 0.6636,\\n        \\\"precision\\\": 0.3635,\\n        \\\"coverage\\\": 0.617,\\n        \\\"pre_cp_fpr\\\": 0.1728,\\n        \\\"lead_mean\\\": 32.3\\n      },\\n      {\\n        \\\"window\\\": 15,\\n        \\\"bal_acc\\\": 0.657,\\n        \\\"precision\\\": 0.3556,\\n        \\\"coverage\\\": 0.6383,\\n        \\\"pre_cp_fpr\\\": 0.1789,\\n        \\\"lead_mean\\\": 31.6\\n      },\\n      {\\n        \\\"window\\\": 20,\\n        \\\"bal_acc\\\": 0.6314,\\n        \\\"precision\\\": 0.333,\\n        \\\"coverage\\\": 0.5745,\\n        \\\"pre_cp_fpr\\\": 0.1811,\\n        \\\"lead_mean\\\": 32.9\\n      },\\n      {\\n        \\\"window\\\": 25,\\n        \\\"bal_acc\\\": 0.6305,\\n        \\\"precision\\\": 0.331,\\n        \\\"coverage\\\": 0.5957,\\n        \\\"pre_cp_fpr\\\": 0.1802,\\n        \\\"lead_mean\\\": 31.3\\n      }\\n    ]\\n  },\\n  \\\"phase4_text_probes\\\": [\\n    {\\n      \\\"window\\\": 1,\\n      \\\"bal_acc\\\": 0.5810269175108538,\\n      \\\"precision\\\": 0.24462924462924462,\\n      \\\"coverage\\\": 0.6382978723404256,\\n      \\\"pre_cp_fpr\\\": 0.3448561527812028,\\n      \\\"lead_mean\\\": 37.083333333333336\\n    },\\n    {\\n      \\\"window\\\": 3,\\n      \\\"bal_acc\\\": 0.5788797684515196,\\n      \\\"precision\\\": 0.25365853658536586,\\n      \\\"coverage\\\": 0.7446808510638298,\\n      \\\"pre_cp_fpr\\\": 0.2709037727203341,\\n      \\\"lead_mean\\\": 41.57142857142857\\n    },\\n    {\\n      \\\"window\\\": 5,\\n      \\\"bal_acc\\\": 0.5689643994211289,\\n      \\\"precision\\\": 0.24744897959183673,\\n      \\\"coverage\\\": 0.7021276595744681,\\n      \\\"pre_cp_fpr\\\": 0.254684434724532,\\n      \\\"lead_mean\\\": 50.851851851851855\\n    },\\n    {\\n      \\\"window\\\": 10,\\n      \\\"bal_acc\\\": 0.5826192764109985,\\n      \\\"precision\\\": 0.26996197718631176,\\n      \\\"coverage\\\": 0.7021276595744681,\\n      \\\"pre_cp_fpr\\\": 0.22232284961863977,\\n      \\\"lead_mean\\\": 45.592592592592595\\n    },\\n    {\\n      \\\"window\\\": 15,\\n      \\\"bal_acc\\\": 0.5892485094066571,\\n      \\\"precision\\\": 0.28269617706237427,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.20037626046595514,\\n      \\\"lead_mean\\\": 46.52\\n    },\\n    {\\n      \\\"window\\\": 20,\\n      \\\"bal_acc\\\": 0.6091172214182344,\\n      \\\"precision\\\": 0.3161925601750547,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.1758008391112723,\\n      \\\"lead_mean\\\": 39.375\\n    },\\n    {\\n      \\\"window\\\": 25,\\n      \\\"bal_acc\\\": 0.6140700434153401,\\n      \\\"precision\\\": 0.3291284403669725,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.1605430087993206,\\n      \\\"lead_mean\\\": 45.476190476190474\\n    }\\n  ],\\n  \\\"phase5_bootstrap\\\": {\\n    \\\"bal_acc\\\": {\\n      \\\"hs_mean\\\": 0.7372878502504099,\\n      \\\"text_mean\\\": 0.6557832624037719,\\n      \\\"delta\\\": 0.08150458784663794,\\n      \\\"ci_95\\\": [\\n        0.028372540246562543,\\n        0.13588955303691563\\n      ],\\n      \\\"p_value\\\": 0.001,\\n      \\\"bonferroni_sig\\\": \\\"Yes\\\"\\n    },\\n    \\\"precision\\\": {\\n      \\\"hs_mean\\\": 0.42492856373959575,\\n      \\\"text_mean\\\": 0.3458941700046874,\\n      \\\"delta\\\": 0.07903439373490834,\\n      \\\"ci_95\\\": [\\n        -0.00498217647350165,\\n        0.15817691203377748\\n      ],\\n      \\\"p_value\\\": 0.056,\\n      \\\"bonferroni_sig\\\": \\\"No\\\"\\n    },\\n    \\\"pre_cp_fpr\\\": {\\n      \\\"hs_mean\\\": 0.18767066132639668,\\n      \\\"text_mean\\\": 0.2709037727203341,\\n      \\\"delta\\\": -0.08323311139393744,\\n      \\\"ci_95\\\": [\\n        -0.1398406438408706,\\n        -0.02360816993128593\\n      ],\\n      \\\"p_value\\\": 0.007,\\n      \\\"bonferroni_sig\\\": \\\"Yes\\\"\\n    }\\n  },\\n  \\\"phase6_selectivity\\\": {\\n    \\\"real_acc\\\": 0.6720576555716353,\\n    \\\"random_mean\\\": 0.48699563531114326,\\n    \\\"random_std\\\": 0.014265457001283764,\\n    \\\"selectivity_pp\\\": 18.506202026049206,\\n    \\\"n_perms\\\": 10,\\n    \\\"random_accs\\\": [\\n      0.4764624023154848,\\n      0.47802396526772795,\\n      0.4941962373371925,\\n      0.49634292329956586,\\n      0.4810044573082489,\\n      0.46669013024602024,\\n      0.5106239073806078,\\n      0.4970116353111433,\\n      0.501945470332851,\\n      0.46765522431259043\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "1b3c1ecc-0465-4794-ae15-6a53e0c3dfb5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"experiment\\\\\\\": \\\\\\\"exp_ot7b_full_pipeline\\\\\\\",\\\\n  \\\\\\\"model\\\\\\\": \\\\\\\"open-thoughts/OpenThinker-7B\\\\\\\",\\\\n  \\\\\\\"n_traces\\\\\\\": 228,\\\\n  \\\\\\\"split\\\\\\\": {\\\\n    \\\\\\\"train\\\\\\\": 136,\\\\n    \\\\\\\"val\\\\\\\": 45,\\\\n    \\\\\\\"test\\\\\\\": 47\\\\n  },\\\\n  \\\\\\\"phase2_layer_sweep\\\\\\\": {\\\\n    \\\\\\\"best_layer\\\\\\\": 0,\\\\n    \\\\\\\"best_depth_pct\\\\\\\": 0,\\\\n    \\\\\\\"results\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 0,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6671,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.5319,\\\\n        \\\\\\\"lead_mean\\\\\\\": 29.8,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.2186,\\\\n        \\\\\\\"score\\\\\\\": 0.3549\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 4,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.663,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.4043,\\\\n        \\\\\\\"lead_mean\\\\\\\": 25.6,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1538,\\\\n        \\\\\\\"score\\\\\\\": 0.268\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 8,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.664,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.2553,\\\\n        \\\\\\\"lead_mean\\\\\\\": 23.4,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.14,\\\\n        \\\\\\\"score\\\\\\\": 0.1695\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 12,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6752,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.3191,\\\\n        \\\\\\\"lead_mean\\\\\\\": 15.6,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1242,\\\\n        \\\\\\\"score\\\\\\\": 0.2155\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 16,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6816,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.3191,\\\\n        \\\\\\\"lead_mean\\\\\\\": 16.1,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.12,\\\\n        \\\\\\\"score\\\\\\\": 0.2175\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 20,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6551,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.3191,\\\\n        \\\\\\\"lead_mean\\\\\\\": 13.8,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1355,\\\\n        \\\\\\\"score\\\\\\\": 0.2091\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 24,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6686,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.2979,\\\\n        \\\\\\\"lead_mean\\\\\\\": 26.5,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1324,\\\\n        \\\\\\\"score\\\\\\\": 0.1992\\\\n      },\\\\n      {\\\\n        \\\\\\\"layer\\\\\\\": 27,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6299,\\\\n        \\\\\\\"crossing_rate\\\\\\\": 0.3191,\\\\n        \\\\\\\"lead_mean\\\\\\\": 29.5,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1524,\\\\n        \\\\\\\"score\\\\\\\": 0.201\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"phase3_temporal_probes\\\\\\\": {\\\\n    \\\\\\\"best_window\\\\\\\": 3,\\\\n    \\\\\\\"best_layer\\\\\\\": 0,\\\\n    \\\\\\\"results\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 1,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6671,\\\\n        \\\\\\\"precision\\\\\\\": 0.3369,\\\\n        \\\\\\\"coverage\\\\\\\": 0.6809,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.2186,\\\\n        \\\\\\\"lead_mean\\\\\\\": 29.8\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 3,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6721,\\\\n        \\\\\\\"precision\\\\\\\": 0.3571,\\\\n        \\\\\\\"coverage\\\\\\\": 0.5957,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1877,\\\\n        \\\\\\\"lead_mean\\\\\\\": 32.9\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 5,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6668,\\\\n        \\\\\\\"precision\\\\\\\": 0.3598,\\\\n        \\\\\\\"coverage\\\\\\\": 0.617,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1782,\\\\n        \\\\\\\"lead_mean\\\\\\\": 33.7\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 10,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6636,\\\\n        \\\\\\\"precision\\\\\\\": 0.3635,\\\\n        \\\\\\\"coverage\\\\\\\": 0.617,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1728,\\\\n        \\\\\\\"lead_mean\\\\\\\": 32.3\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 15,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.657,\\\\n        \\\\\\\"precision\\\\\\\": 0.3556,\\\\n        \\\\\\\"coverage\\\\\\\": 0.6383,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1789,\\\\n        \\\\\\\"lead_mean\\\\\\\": 31.6\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 20,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6314,\\\\n        \\\\\\\"precision\\\\\\\": 0.333,\\\\n        \\\\\\\"coverage\\\\\\\": 0.5745,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1811,\\\\n        \\\\\\\"lead_mean\\\\\\\": 32.9\\\\n      },\\\\n      {\\\\n        \\\\\\\"window\\\\\\\": 25,\\\\n        \\\\\\\"bal_acc\\\\\\\": 0.6305,\\\\n        \\\\\\\"precision\\\\\\\": 0.331,\\\\n        \\\\\\\"coverage\\\\\\\": 0.5957,\\\\n        \\\\\\\"pre_cp_fpr\\\\\\\": 0.1802,\\\\n        \\\\\\\"lead_mean\\\\\\\": 31.3\\\\n      }\\\\n    ]\\\\n  },\\\\n  \\\\\\\"phase4_text_probes\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 1,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.5810269175108538,\\\\n      \\\\\\\"precision\\\\\\\": 0.24462924462924462,\\\\n      \\\\\\\"coverage\\\\\\\": 0.6382978723404256,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.3448561527812028,\\\\n      \\\\\\\"lead_mean\\\\\\\": 37.083333333333336\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 3,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.5788797684515196,\\\\n      \\\\\\\"precision\\\\\\\": 0.25365853658536586,\\\\n      \\\\\\\"coverage\\\\\\\": 0.7446808510638298,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.2709037727203341,\\\\n      \\\\\\\"lead_mean\\\\\\\": 41.57142857142857\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 5,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.5689643994211289,\\\\n      \\\\\\\"precision\\\\\\\": 0.24744897959183673,\\\\n      \\\\\\\"coverage\\\\\\\": 0.7021276595744681,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.254684434724532,\\\\n      \\\\\\\"lead_mean\\\\\\\": 50.851851851851855\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 10,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.5826192764109985,\\\\n      \\\\\\\"precision\\\\\\\": 0.26996197718631176,\\\\n      \\\\\\\"coverage\\\\\\\": 0.7021276595744681,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.22232284961863977,\\\\n      \\\\\\\"lead_mean\\\\\\\": 45.592592592592595\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 15,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.5892485094066571,\\\\n      \\\\\\\"precision\\\\\\\": 0.28269617706237427,\\\\n      \\\\\\\"coverage\\\\\\\": 0.6595744680851063,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.20037626046595514,\\\\n      \\\\\\\"lead_mean\\\\\\\": 46.52\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 20,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.6091172214182344,\\\\n      \\\\\\\"precision\\\\\\\": 0.3161925601750547,\\\\n      \\\\\\\"coverage\\\\\\\": 0.6595744680851063,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.1758008391112723,\\\\n      \\\\\\\"lead_mean\\\\\\\": 39.375\\\\n    },\\\\n    {\\\\n      \\\\\\\"window\\\\\\\": 25,\\\\n      \\\\\\\"bal_acc\\\\\\\": 0.6140700434153401,\\\\n      \\\\\\\"precision\\\\\\\": 0.3291284403669725,\\\\n      \\\\\\\"coverage\\\\\\\": 0.6595744680851063,\\\\n      \\\\\\\"pre_cp_fpr\\\\\\\": 0.1605430087993206,\\\\n      \\\\\\\"lead_mean\\\\\\\": 45.476190476190474\\\\n    }\\\\n  ],\\\\n  \\\\\\\"phase5_bootstrap\\\\\\\": {\\\\n    \\\\\\\"bal_acc\\\\\\\": {\\\\n      \\\\\\\"hs_mean\\\\\\\": 0.7372878502504099,\\\\n      \\\\\\\"text_mean\\\\\\\": 0.6557832624037719,\\\\n      \\\\\\\"delta\\\\\\\": 0.08150458784663794,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.028372540246562543,\\\\n        0.13588955303691563\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.001,\\\\n      \\\\\\\"bonferroni_sig\\\\\\\": \\\\\\\"Yes\\\\\\\"\\\\n    },\\\\n    \\\\\\\"precision\\\\\\\": {\\\\n      \\\\\\\"hs_mean\\\\\\\": 0.42492856373959575,\\\\n      \\\\\\\"text_mean\\\\\\\": 0.3458941700046874,\\\\n      \\\\\\\"delta\\\\\\\": 0.07903439373490834,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.00498217647350165,\\\\n        0.15817691203377748\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.056,\\\\n      \\\\\\\"bonferroni_sig\\\\\\\": \\\\\\\"No\\\\\\\"\\\\n    },\\\\n    \\\\\\\"pre_cp_fpr\\\\\\\": {\\\\n      \\\\\\\"hs_mean\\\\\\\": 0.18767066132639668,\\\\n      \\\\\\\"text_mean\\\\\\\": 0.2709037727203341,\\\\n      \\\\\\\"delta\\\\\\\": -0.08323311139393744,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.1398406438408706,\\\\n        -0.02360816993128593\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.007,\\\\n      \\\\\\\"bonferroni_sig\\\\\\\": \\\\\\\"Yes\\\\\\\"\\\\n    }\\\\n  },\\\\n  \\\\\\\"phase6_selectivity\\\\\\\": {\\\\n    \\\\\\\"real_acc\\\\\\\": 0.6720576555716353,\\\\n    \\\\\\\"random_mean\\\\\\\": 0.48699563531114326,\\\\n    \\\\\\\"random_std\\\\\\\": 0.014265457001283764,\\\\n    \\\\\\\"selectivity_pp\\\\\\\": 18.506202026049206,\\\\n    \\\\\\\"n_perms\\\\\\\": 10,\\\\n    \\\\\\\"random_accs\\\\\\\": [\\\\n      0.4764624023154848,\\\\n      0.47802396526772795,\\\\n      0.4941962373371925,\\\\n      0.49634292329956586,\\\\n      0.4810044573082489,\\\\n      0.46669013024602024,\\\\n      0.5106239073806078,\\\\n      0.4970116353111433,\\\\n      0.501945470332851,\\\\n      0.46765522431259043\\\\n    ]\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.07}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_ot7b_full_pipeline\\\",\\n  \\\"model\\\": \\\"open-thoughts/OpenThinker-7B\\\",\\n  \\\"n_traces\\\": 228,\\n  \\\"split\\\": {\\n    \\\"train\\\": 136,\\n    \\\"val\\\": 45,\\n    \\\"test\\\": 47\\n  },\\n  \\\"phase2_layer_sweep\\\": {\\n    \\\"best_layer\\\": 0,\\n    \\\"best_depth_pct\\\": 0,\\n    \\\"results\\\": [\\n      {\\n        \\\"layer\\\": 0,\\n        \\\"bal_acc\\\": 0.6671,\\n        \\\"crossing_rate\\\": 0.5319,\\n        \\\"lead_mean\\\": 29.8,\\n        \\\"pre_cp_fpr\\\": 0.2186,\\n        \\\"score\\\": 0.3549\\n      },\\n      {\\n        \\\"layer\\\": 4,\\n        \\\"bal_acc\\\": 0.663,\\n        \\\"crossing_rate\\\": 0.4043,\\n        \\\"lead_mean\\\": 25.6,\\n        \\\"pre_cp_fpr\\\": 0.1538,\\n        \\\"score\\\": 0.268\\n      },\\n      {\\n        \\\"layer\\\": 8,\\n        \\\"bal_acc\\\": 0.664,\\n        \\\"crossing_rate\\\": 0.2553,\\n        \\\"lead_mean\\\": 23.4,\\n        \\\"pre_cp_fpr\\\": 0.14,\\n        \\\"score\\\": 0.1695\\n      },\\n      {\\n        \\\"layer\\\": 12,\\n        \\\"bal_acc\\\": 0.6752,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 15.6,\\n        \\\"pre_cp_fpr\\\": 0.1242,\\n        \\\"score\\\": 0.2155\\n      },\\n      {\\n        \\\"layer\\\": 16,\\n        \\\"bal_acc\\\": 0.6816,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 16.1,\\n        \\\"pre_cp_fpr\\\": 0.12,\\n        \\\"score\\\": 0.2175\\n      },\\n      {\\n        \\\"layer\\\": 20,\\n        \\\"bal_acc\\\": 0.6551,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 13.8,\\n        \\\"pre_cp_fpr\\\": 0.1355,\\n        \\\"score\\\": 0.2091\\n      },\\n      {\\n        \\\"layer\\\": 24,\\n        \\\"bal_acc\\\": 0.6686,\\n        \\\"crossing_rate\\\": 0.2979,\\n        \\\"lead_mean\\\": 26.5,\\n        \\\"pre_cp_fpr\\\": 0.1324,\\n        \\\"score\\\": 0.1992\\n      },\\n      {\\n        \\\"layer\\\": 27,\\n        \\\"bal_acc\\\": 0.6299,\\n        \\\"crossing_rate\\\": 0.3191,\\n        \\\"lead_mean\\\": 29.5,\\n        \\\"pre_cp_fpr\\\": 0.1524,\\n        \\\"score\\\": 0.201\\n      }\\n    ]\\n  },\\n  \\\"phase3_temporal_probes\\\": {\\n    \\\"best_window\\\": 3,\\n    \\\"best_layer\\\": 0,\\n    \\\"results\\\": [\\n      {\\n        \\\"window\\\": 1,\\n        \\\"bal_acc\\\": 0.6671,\\n        \\\"precision\\\": 0.3369,\\n        \\\"coverage\\\": 0.6809,\\n        \\\"pre_cp_fpr\\\": 0.2186,\\n        \\\"lead_mean\\\": 29.8\\n      },\\n      {\\n        \\\"window\\\": 3,\\n        \\\"bal_acc\\\": 0.6721,\\n        \\\"precision\\\": 0.3571,\\n        \\\"coverage\\\": 0.5957,\\n        \\\"pre_cp_fpr\\\": 0.1877,\\n        \\\"lead_mean\\\": 32.9\\n      },\\n      {\\n        \\\"window\\\": 5,\\n        \\\"bal_acc\\\": 0.6668,\\n        \\\"precision\\\": 0.3598,\\n        \\\"coverage\\\": 0.617,\\n        \\\"pre_cp_fpr\\\": 0.1782,\\n        \\\"lead_mean\\\": 33.7\\n      },\\n      {\\n        \\\"window\\\": 10,\\n        \\\"bal_acc\\\": 0.6636,\\n        \\\"precision\\\": 0.3635,\\n        \\\"coverage\\\": 0.617,\\n        \\\"pre_cp_fpr\\\": 0.1728,\\n        \\\"lead_mean\\\": 32.3\\n      },\\n      {\\n        \\\"window\\\": 15,\\n        \\\"bal_acc\\\": 0.657,\\n        \\\"precision\\\": 0.3556,\\n        \\\"coverage\\\": 0.6383,\\n        \\\"pre_cp_fpr\\\": 0.1789,\\n        \\\"lead_mean\\\": 31.6\\n      },\\n      {\\n        \\\"window\\\": 20,\\n        \\\"bal_acc\\\": 0.6314,\\n        \\\"precision\\\": 0.333,\\n        \\\"coverage\\\": 0.5745,\\n        \\\"pre_cp_fpr\\\": 0.1811,\\n        \\\"lead_mean\\\": 32.9\\n      },\\n      {\\n        \\\"window\\\": 25,\\n        \\\"bal_acc\\\": 0.6305,\\n        \\\"precision\\\": 0.331,\\n        \\\"coverage\\\": 0.5957,\\n        \\\"pre_cp_fpr\\\": 0.1802,\\n        \\\"lead_mean\\\": 31.3\\n      }\\n    ]\\n  },\\n  \\\"phase4_text_probes\\\": [\\n    {\\n      \\\"window\\\": 1,\\n      \\\"bal_acc\\\": 0.5810269175108538,\\n      \\\"precision\\\": 0.24462924462924462,\\n      \\\"coverage\\\": 0.6382978723404256,\\n      \\\"pre_cp_fpr\\\": 0.3448561527812028,\\n      \\\"lead_mean\\\": 37.083333333333336\\n    },\\n    {\\n      \\\"window\\\": 3,\\n      \\\"bal_acc\\\": 0.5788797684515196,\\n      \\\"precision\\\": 0.25365853658536586,\\n      \\\"coverage\\\": 0.7446808510638298,\\n      \\\"pre_cp_fpr\\\": 0.2709037727203341,\\n      \\\"lead_mean\\\": 41.57142857142857\\n    },\\n    {\\n      \\\"window\\\": 5,\\n      \\\"bal_acc\\\": 0.5689643994211289,\\n      \\\"precision\\\": 0.24744897959183673,\\n      \\\"coverage\\\": 0.7021276595744681,\\n      \\\"pre_cp_fpr\\\": 0.254684434724532,\\n      \\\"lead_mean\\\": 50.851851851851855\\n    },\\n    {\\n      \\\"window\\\": 10,\\n      \\\"bal_acc\\\": 0.5826192764109985,\\n      \\\"precision\\\": 0.26996197718631176,\\n      \\\"coverage\\\": 0.7021276595744681,\\n      \\\"pre_cp_fpr\\\": 0.22232284961863977,\\n      \\\"lead_mean\\\": 45.592592592592595\\n    },\\n    {\\n      \\\"window\\\": 15,\\n      \\\"bal_acc\\\": 0.5892485094066571,\\n      \\\"precision\\\": 0.28269617706237427,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.20037626046595514,\\n      \\\"lead_mean\\\": 46.52\\n    },\\n    {\\n      \\\"window\\\": 20,\\n      \\\"bal_acc\\\": 0.6091172214182344,\\n      \\\"precision\\\": 0.3161925601750547,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.1758008391112723,\\n      \\\"lead_mean\\\": 39.375\\n    },\\n    {\\n      \\\"window\\\": 25,\\n      \\\"bal_acc\\\": 0.6140700434153401,\\n      \\\"precision\\\": 0.3291284403669725,\\n      \\\"coverage\\\": 0.6595744680851063,\\n      \\\"pre_cp_fpr\\\": 0.1605430087993206,\\n      \\\"lead_mean\\\": 45.476190476190474\\n    }\\n  ],\\n  \\\"phase5_bootstrap\\\": {\\n    \\\"bal_acc\\\": {\\n      \\\"hs_mean\\\": 0.7372878502504099,\\n      \\\"text_mean\\\": 0.6557832624037719,\\n      \\\"delta\\\": 0.08150458784663794,\\n      \\\"ci_95\\\": [\\n        0.028372540246562543,\\n        0.13588955303691563\\n      ],\\n      \\\"p_value\\\": 0.001,\\n      \\\"bonferroni_sig\\\": \\\"Yes\\\"\\n    },\\n    \\\"precision\\\": {\\n      \\\"hs_mean\\\": 0.42492856373959575,\\n      \\\"text_mean\\\": 0.3458941700046874,\\n      \\\"delta\\\": 0.07903439373490834,\\n      \\\"ci_95\\\": [\\n        -0.00498217647350165,\\n        0.15817691203377748\\n      ],\\n      \\\"p_value\\\": 0.056,\\n      \\\"bonferroni_sig\\\": \\\"No\\\"\\n    },\\n    \\\"pre_cp_fpr\\\": {\\n      \\\"hs_mean\\\": 0.18767066132639668,\\n      \\\"text_mean\\\": 0.2709037727203341,\\n      \\\"delta\\\": -0.08323311139393744,\\n      \\\"ci_95\\\": [\\n        -0.1398406438408706,\\n        -0.02360816993128593\\n      ],\\n      \\\"p_value\\\": 0.007,\\n      \\\"bonferroni_sig\\\": \\\"Yes\\\"\\n    }\\n  },\\n  \\\"phase6_selectivity\\\": {\\n    \\\"real_acc\\\": 0.6720576555716353,\\n    \\\"random_mean\\\": 0.48699563531114326,\\n    \\\"random_std\\\": 0.014265457001283764,\\n    \\\"selectivity_pp\\\": 18.506202026049206,\\n    \\\"n_perms\\\": 10,\\n    \\\"random_accs\\\": [\\n      0.4764624023154848,\\n      0.47802396526772795,\\n      0.4941962373371925,\\n      0.49634292329956586,\\n      0.4810044573082489,\\n      0.46669013024602024,\\n      0.5106239073806078,\\n      0.4970116353111433,\\n      0.501945470332851,\\n      0.46765522431259043\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:35:05.542Z_

<details><summary>↩ Tool result · `toolu_01F1WyQ25BZZrGRyAWzL4Bkb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# OpenThinker-7B Commitment Detection Pipeline Report\\n\\n**Model**: open-thoughts/OpenThinker-7B\\n**Traces**: 228 (train=136, val=45, test=47)\\n**Date**: 2026-05-17 16:29\\n\\n## Phase 2: Layer Sweep\\n\\nBest layer: **0** (depth=0%)\\n\\n| Layer | Bal Acc | Crossing Rate | Lead | Pre-CP FPR | Score |\\n|-------|---------|---------------|------|-----------|-------|\\n|  0 | 0.6671 | 0.5319 | 29.8 | 0.2186 | 0.3549 |\\n|  4 | 0.6630 | 0.4043 | 25.6 | 0.1538 | 0.2680 |\\n|  8 | 0.6640 | 0.2553 | 23.4 | 0.1400 | 0.1695 |\\n| 12 | 0.6752 | 0.3191 | 15.6 | 0.1242 | 0.2155 |\\n| 16 | 0.6816 | 0.3191 | 16.1 | 0.1200 | 0.2175 |\\n| 20 | 0.6551 | 0.3191 | 13.8 | 0.1355 | 0.2091 |\\n| 24 | 0.6686 | 0.2979 | 26.5 | 0.1324 | 0.1992 |\\n| 27 | 0.6299 | 0.3191 | 29.5 | 0.1524 | 0.2010 |\\n\\n## Phase 3: Hidden State Temporal Probes (layer=0)\\n\\nBest window: **W=3**\\n\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|---|---------|-----------|----------|-----------|------|\\n|  1 | 0.6671 | 0.3369 | 0.6809 | 0.2186 | 29.8 |\\n|  3 | 0.6721 | 0.3571 | 0.5957 | 0.1877 | 32.9 |\\n|  5 | 0.6668 | 0.3598 | 0.6170 | 0.1782 | 33.7 |\\n| 10 | 0.6636 | 0.3635 | 0.6170 | 0.1728 | 32.3 |\\n| 15 | 0.6570 | 0.3556 | 0.6383 | 0.1789 | 31.6 |\\n| 20 | 0.6314 | 0.3330 | 0.5745 | 0.1811 | 32.9 |\\n| 25 | 0.6305 | 0.3310 | 0.5957 | 0.1802 | 31.3 |\\n\\n## Phase 4: Text Baseline Probes\\n\\nBest window: **W=25**\\n\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|---|---------|-----------|----------|-----------|------|\\n|  1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |\\n|  3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |\\n|  5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |\\n| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |\\n| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |\\n| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |\\n| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |\\n\\n## Phase 5: Paired Bootstrap (HS vs Text)\\n\\n| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |\\n|--------|-----|------|-------|--------|---------|-----------|\\n| bal_acc | 0.7373 | 0.6558 | 0.0815 | [0.0284, 0.1359] | 0.0010 | Yes |\\n| precision | 0.4249 | 0.3459 | 0.0790 | [-0.0050, 0.1582] | 0.0560 | No |\\n| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.0070 | Yes |\\n\\n## Phase 6: Selectivity Control\\n\\n- Real accuracy: 0.6721\\n- Random mean: 0.4870 +/- 0.0143\\n- **Selectivity: 18.5 pp**\\n- N permutations: 10\\n\\n## Summary\\n\\n- Best layer: 0 (depth 0%)\\n- Best HS probe: W=3, bal_acc=0.6721\\n- Best text probe: W=25, bal_acc=0.6141\\n- Selectivity: 18.5 pp above random\\n- HS vs Text: HS > Text\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "6e568946-5d6f-4f23-adfe-d3d69549bf4c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# OpenThinker-7B Commitment Detection Pipeline Report\\\\n\\\\n**Model**: open-thoughts/OpenThinker-7B\\\\n**Traces**: 228 (train=136, val=45, test=47)\\\\n**Date**: 2026-05-17 16:29\\\\n\\\\n## Phase 2: Layer Sweep\\\\n\\\\nBest layer: **0** (depth=0%)\\\\n\\\\n| Layer | Bal Acc | Crossing Rate | Lead | Pre-CP FPR | Score |\\\\n|-------|---------|---------------|------|-----------|-------|\\\\n|  0 | 0.6671 | 0.5319 | 29.8 | 0.2186 | 0.3549 |\\\\n|  4 | 0.6630 | 0.4043 | 25.6 | 0.1538 | 0.2680 |\\\\n|  8 | 0.6640 | 0.2553 | 23.4 | 0.1400 | 0.1695 |\\\\n| 12 | 0.6752 | 0.3191 | 15.6 | 0.1242 | 0.2155 |\\\\n| 16 | 0.6816 | 0.3191 | 16.1 | 0.1200 | 0.2175 |\\\\n| 20 | 0.6551 | 0.3191 | 13.8 | 0.1355 | 0.2091 |\\\\n| 24 | 0.6686 | 0.2979 | 26.5 | 0.1324 | 0.1992 |\\\\n| 27 | 0.6299 | 0.3191 | 29.5 | 0.1524 | 0.2010 |\\\\n\\\\n## Phase 3: Hidden State Temporal Probes (layer=0)\\\\n\\\\nBest window: **W=3**\\\\n\\\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\\\n|---|---------|-----------|----------|-----------|------|\\\\n|  1 | 0.6671 | 0.3369 | 0.6809 | 0.2186 | 29.8 |\\\\n|  3 | 0.6721 | 0.3571 | 0.5957 | 0.1877 | 32.9 |\\\\n|  5 | 0.6668 | 0.3598 | 0.6170 | 0.1782 | 33.7 |\\\\n| 10 | 0.6636 | 0.3635 | 0.6170 | 0.1728 | 32.3 |\\\\n| 15 | 0.6570 | 0.3556 | 0.6383 | 0.1789 | 31.6 |\\\\n| 20 | 0.6314 | 0.3330 | 0.5745 | 0.1811 | 32.9 |\\\\n| 25 | 0.6305 | 0.3310 | 0.5957 | 0.1802 | 31.3 |\\\\n\\\\n## Phase 4: Text Baseline Probes\\\\n\\\\nBest window: **W=25**\\\\n\\\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\\\n|---|---------|-----------|----------|-----------|------|\\\\n|  1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |\\\\n|  3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |\\\\n|  5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |\\\\n| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |\\\\n| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |\\\\n| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |\\\\n| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |\\\\n\\\\n## Phase 5: Paired Bootstrap (HS vs Text)\\\\n\\\\n| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |\\\\n|--------|-----|------|-------|--------|---------|-----------|\\\\n| bal_acc | 0.7373 | 0.6558 | 0.0815 | [0.0284, 0.1359] | 0.0010 | Yes |\\\\n| precision | 0.4249 | 0.3459 | 0.0790 | [-0.0050, 0.1582] | 0.0560 | No |\\\\n| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.0070 | Yes |\\\\n\\\\n## Phase 6: Selectivity Control\\\\n\\\\n- Real accuracy: 0.6721\\\\n- Random mean: 0.4870 +/- 0.0143\\\\n- **Selectivity: 18.5 pp**\\\\n- N permutations: 10\\\\n\\\\n## Summary\\\\n\\\\n- Best layer: 0 (depth 0%)\\\\n- Best HS probe: W=3, bal_acc=0.6721\\\\n- Best text probe: W=25, bal_acc=0.6141\\\\n- Selectivity: 18.5 pp above random\\\\n- HS vs Text: HS > Text\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# OpenThinker-7B Commitment Detection Pipeline Report\\n\\n**Model**: open-thoughts/OpenThinker-7B\\n**Traces**: 228 (train=136, val=45, test=47)\\n**Date**: 2026-05-17 16:29\\n\\n## Phase 2: Layer Sweep\\n\\nBest layer: **0** (depth=0%)\\n\\n| Layer | Bal Acc | Crossing Rate | Lead | Pre-CP FPR | Score |\\n|-------|---------|---------------|------|-----------|-------|\\n|  0 | 0.6671 | 0.5319 | 29.8 | 0.2186 | 0.3549 |\\n|  4 | 0.6630 | 0.4043 | 25.6 | 0.1538 | 0.2680 |\\n|  8 | 0.6640 | 0.2553 | 23.4 | 0.1400 | 0.1695 |\\n| 12 | 0.6752 | 0.3191 | 15.6 | 0.1242 | 0.2155 |\\n| 16 | 0.6816 | 0.3191 | 16.1 | 0.1200 | 0.2175 |\\n| 20 | 0.6551 | 0.3191 | 13.8 | 0.1355 | 0.2091 |\\n| 24 | 0.6686 | 0.2979 | 26.5 | 0.1324 | 0.1992 |\\n| 27 | 0.6299 | 0.3191 | 29.5 | 0.1524 | 0.2010 |\\n\\n## Phase 3: Hidden State Temporal Probes (layer=0)\\n\\nBest window: **W=3**\\n\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|---|---------|-----------|----------|-----------|------|\\n|  1 | 0.6671 | 0.3369 | 0.6809 | 0.2186 | 29.8 |\\n|  3 | 0.6721 | 0.3571 | 0.5957 | 0.1877 | 32.9 |\\n|  5 | 0.6668 | 0.3598 | 0.6170 | 0.1782 | 33.7 |\\n| 10 | 0.6636 | 0.3635 | 0.6170 | 0.1728 | 32.3 |\\n| 15 | 0.6570 | 0.3556 | 0.6383 | 0.1789 | 31.6 |\\n| 20 | 0.6314 | 0.3330 | 0.5745 | 0.1811 | 32.9 |\\n| 25 | 0.6305 | 0.3310 | 0.5957 | 0.1802 | 31.3 |\\n\\n## Phase 4: Text Baseline Probes\\n\\nBest window: **W=25**\\n\\n| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|---|---------|-----------|----------|-----------|------|\\n|  1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |\\n|  3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |\\n|  5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |\\n| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |\\n| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |\\n| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |\\n| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |\\n\\n## Phase 5: Paired Bootstrap (HS vs Text)\\n\\n| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |\\n|--------|-----|------|-------|--------|---------|-----------|\\n| bal_acc | 0.7373 | 0.6558 | 0.0815 | [0.0284, 0.1359] | 0.0010 | Yes |\\n| precision | 0.4249 | 0.3459 | 0.0790 | [-0.0050, 0.1582] | 0.0560 | No |\\n| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.0070 | Yes |\\n\\n## Phase 6: Selectivity Control\\n\\n- Real accuracy: 0.6721\\n- Random mean: 0.4870 +/- 0.0143\\n- **Selectivity: 18.5 pp**\\n- N permutations: 10\\n\\n## Summary\\n\\n- Best layer: 0 (depth 0%)\\n- Best HS probe: W=3, bal_acc=0.6721\\n- Best text probe: W=25, bal_acc=0.6141\\n- Selectivity: 18.5 pp above random\\n- HS vs Text: HS > Text\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

---

### File 1: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/results.json`

```json
{
  "experiment": "exp_ot7b_full_pipeline",
  "model": "open-thoughts/OpenThinker-7B",
  "n_traces": 228,
  "split": {
    "train": 136,
    "val": 45,
    "test": 47
  },
  "phase2_layer_sweep": {
    "best_layer": 0,
    "best_depth_pct": 0,
    "results": [
      {
        "layer": 0,
        "bal_acc": 0.6671,
        "crossing_rate": 0.5319,
        "lead_mean": 29.8,
        "pre_cp_fpr": 0.2186,
        "score": 0.3549
      },
      {
        "layer": 4,
        "bal_acc": 0.663,
        "crossing_rate": 0.4043,
        "lead_mean": 25.6,
        "pre_cp_fpr": 0.1538,
        "score": 0.268
      },
      {
        "layer": 8,
        "bal_acc": 0.664,
        "crossing_rate": 0.2553,
        "lead_mean": 23.4,
        "pre_cp_fpr": 0.14,
        "score": 0.1695
      },
      {
        "layer": 12,
        "bal_acc": 0.6752,
        "crossing_rate": 0.3191,
        "lead_mean": 15.6,
        "pre_cp_fpr": 0.1242,
        "score": 0.2155
      },
      {
        "layer": 16,
        "bal_acc": 0.6816,
        "crossing_rate": 0.3191,
        "lead_mean": 16.1,
        "pre_cp_fpr": 0.12,
        "score": 0.2175
      },
      {
        "layer": 20,
        "bal_acc": 0.6551,
        "crossing_rate": 0.3191,
        "lead_mean": 13.8,
        "pre_cp_fpr": 0.1355,
        "score": 0.2091
      },
      {
        "layer": 24,
        "bal_acc": 0.6686,
        "crossing_rate": 0.2979,
        "lead_mean": 26.5,
        "pre_cp_fpr": 0.1324,
        "score": 0.1992
      },
      {
        "layer": 27,
        "bal_acc": 0.6299,
        "crossing_rate": 0.3191,
        "lead_mean": 29.5,
        "pre_cp_fpr": 0.1524,
        "score": 0.201
      }
    ]
  },
  "phase3_temporal_probes": {
    "best_window": 3,
    "best_layer": 0,
    "results": [
      {
        "window": 1,
        "bal_acc": 0.6671,
        "precision": 0.3369,
        "coverage": 0.6809,
        "pre_cp_fpr": 0.2186,
        "lead_mean": 29.8
      },
      {
        "window": 3,
        "bal_acc": 0.6721,
        "precision": 0.3571,
        "coverage": 0.5957,
        "pre_cp_fpr": 0.1877,
        "lead_mean": 32.9
      },
      {
        "window": 5,
        "bal_acc": 0.6668,
        "precision": 0.3598,
        "coverage": 0.617,
        "pre_cp_fpr": 0.1782,
        "lead_mean": 33.7
      },
      {
        "window": 10,
        "bal_acc": 0.6636,
        "precision": 0.3635,
        "coverage": 0.617,
        "pre_cp_fpr": 0.1728,
        "lead_mean": 32.3
      },
      {
        "window": 15,
        "bal_acc": 0.657,
        "precision": 0.3556,
        "coverage": 0.6383,
        "pre_cp_fpr": 0.1789,
        "lead_mean": 31.6
      },
      {
        "window": 20,
        "bal_acc": 0.6314,
        "precision": 0.333,
        "coverage": 0.5745,
        "pre_cp_fpr": 0.1811,
        "lead_mean": 32.9
      },
      {
        "window": 25,
        "bal_acc": 0.6305,
        "precision": 0.331,
        "coverage": 0.5957,
        "pre_cp_fpr": 0.1802,
        "lead_mean": 31.3
      }
    ]
  },
  "phase4_text_probes": [
    {
      "window": 1,
      "bal_acc": 0.5810269175108538,
      "precision": 0.24462924462924462,
      "coverage": 0.6382978723404256,
      "pre_cp_fpr": 0.3448561527812028,
      "lead_mean": 37.083333333333336
    },
    {
      "window": 3,
      "bal_acc": 0.5788797684515196,
      "precision": 0.25365853658536586,
      "coverage": 0.7446808510638298,
      "pre_cp_fpr": 0.2709037727203341,
      "lead_mean": 41.57142857142857
    },
    {
      "window": 5,
      "bal_acc": 0.5689643994211289,
      "precision": 0.24744897959183673,
      "coverage": 0.7021276595744681,
      "pre_cp_fpr": 0.254684434724532,
      "lead_mean": 50.851851851851855
    },
    {
      "window": 10,
      "bal_acc": 0.5826192764109985,
      "precision": 0.26996197718631176,
      "coverage": 0.7021276595744681,
      "pre_cp_fpr": 0.22232284961863977,
      "lead_mean": 45.592592592592595
    },
    {
      "window": 15,
      "bal_acc": 0.5892485094066571,
      "precision": 0.28269617706237427,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.20037626046595514,
      "lead_mean": 46.52
    },
    {
      "window": 20,
      "bal_acc": 0.6091172214182344,
      "precision": 0.3161925601750547,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.1758008391112723,
      "lead_mean": 39.375
    },
    {
      "window": 25,
      "bal_acc": 0.6140700434153401,
      "precision": 0.3291284403669725,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.1605430087993206,
      "lead_mean": 45.476190476190474
    }
  ],
  "phase5_bootstrap": {
    "bal_acc": {
      "hs_mean": 0.7372878502504099,
      "text_mean": 0.6557832624037719,
      "delta": 0.08150458784663794,
      "ci_95": [
        0.028372540246562543,
        0.13588955303691563
      ],
      "p_value": 0.001,
      "bonferroni_sig": "Yes"
    },
    "precision": {
      "hs_mean": 0.42492856373959575,
      "text_mean": 0.3458941700046874,
      "delta": 0.07903439373490834,
      "ci_95": [
        -0.00498217647350165,
        0.15817691203377748
      ],
      "p_value": 0.056,
      "bonferroni_sig": "No"
    },
    "pre_cp_fpr": {
      "hs_mean": 0.18767066132639668,
      "text_mean": 0.2709037727203341,
      "delta": -0.08323311139393744,
      "ci_95": [
        -0.1398406438408706,
        -0.02360816993128593
      ],
      "p_value": 0.007,
      "bonferroni_sig": "Yes"
    }
  },
  "phase6_selectivity": {
    "real_acc": 0.6720576555716353,
    "random_mean": 0.48699563531114326,
    "random_std": 0.014265457001283764,
    "selectivity_pp": 18.506202026049206,
    "n_perms": 10,
    "random_accs": [
      0.4764624023154848,
      0.47802396526772795,
      0.4941962373371925,
      0.49634292329956586,
      0.4810044573082489,
      0.46669013024602024,
      0.5106239073806078,
      0.4970116353111433,
      0.501945470332851,
      0.46765522431259043
    ]
  }
}
```

---

### File 2: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/report.md`

```markdown
# OpenThinker-7B Commitment Detection Pipeline Report

**Model**: open-thoughts/OpenThinker-7B
**Traces**: 228 (train=136, val=45, test=47)
**Date**: 2026-05-17 16:29

## Phase 2: Layer Sweep

Best layer: **0** (depth=0%)

| Layer | Bal Acc | Crossing Rate | Lead | Pre-CP FPR | Score |
|-------|---------|---------------|------|-----------|-------|
|  0 | 0.6671 | 0.5319 | 29.8 | 0.2186 | 0.3549 |
|  4 | 0.6630 | 0.4043 | 25.6 | 0.1538 | 0.2680 |
|  8 | 0.6640 | 0.2553 | 23.4 | 0.1400 | 0.1695 |
| 12 | 0.6752 | 0.3191 | 15.6 | 0.1242 | 0.2155 |
| 16 | 0.6816 | 0.3191 | 16.1 | 0.1200 | 0.2175 |
| 20 | 0.6551 | 0.3191 | 13.8 | 0.1355 | 0.2091 |
| 24 | 0.6686 | 0.2979 | 26.5 | 0.1324 | 0.1992 |
| 27 | 0.6299 | 0.3191 | 29.5 | 0.1524 | 0.2010 |

## Phase 3: Hidden State Temporal Probes (layer=0)

Best window: **W=3**

| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|---|---------|-----------|----------|-----------|------|
|  1 | 0.6671 | 0.3369 | 0.6809 | 0.2186 | 29.8 |
|  3 | 0.6721 | 0.3571 | 0.5957 | 0.1877 | 32.9 |
|  5 | 0.6668 | 0.3598 | 0.6170 | 0.1782 | 33.7 |
| 10 | 0.6636 | 0.3635 | 0.6170 | 0.1728 | 32.3 |
| 15 | 0.6570 | 0.3556 | 0.6383 | 0.1789 | 31.6 |
| 20 | 0.6314 | 0.3330 | 0.5745 | 0.1811 | 32.9 |
| 25 | 0.6305 | 0.3310 | 0.5957 | 0.1802 | 31.3 |

## Phase 4: Text Baseline Probes

Best window: **W=25**

| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|---|---------|-----------|----------|-----------|------|
|  1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |
|  3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |
|  5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |
| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |
| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |
| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |
| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |

## Phase 5: Paired Bootstrap (HS vs Text)

| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |
|--------|-----|------|-------|--------|---------|-----------|
| bal_acc | 0.7373 | 0.6558 | 0.0815 | [0.0284, 0.1359] | 0.0010 | Yes |
| precision | 0.4249 | 0.3459 | 0.0790 | [-0.0050, 0.1582] | 0.0560 | No |
| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.0070 | Yes |

## Phase 6: Selectivity Control

- Real accuracy: 0.6721
- Random mean: 0.4870 +/- 0.0143
- **Selectivity: 18.5 pp**
- N permutations: 10

## Summary

- Best layer: 0 (depth 0%)
- Best HS probe: W=3, bal_acc=0.6721
- Best text probe: W=25, bal_acc=0.6141
- Selectivity: 18.5 pp above random
- HS vs Text: HS > Text
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "uuid": "265d601c-1466-4a73-aa2d-40cb258a6e65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJH3TQfQKSwgp6CRdY9Jew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5576,
      "cache_read_input_tokens": 24591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5576
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

_source line 12_

---

### File 1: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/results.json`

```json
{
  "experiment": "exp_ot7b_full_pipeline",
  "model": "open-thoughts/OpenThinker-7B",
  "n_traces": 228,
  "split": {
    "train": 136,
    "val": 45,
    "test": 47
  },
  "phase2_layer_sweep": {
    "best_layer": 0,
    "best_depth_pct": 0,
    "results": [
      {
        "layer": 0,
        "bal_acc": 0.6671,
        "crossing_rate": 0.5319,
        "lead_mean": 29.8,
        "pre_cp_fpr": 0.2186,
        "score": 0.3549
      },
      {
        "layer": 4,
        "bal_acc": 0.663,
        "crossing_rate": 0.4043,
        "lead_mean": 25.6,
        "pre_cp_fpr": 0.1538,
        "score": 0.268
      },
      {
        "layer": 8,
        "bal_acc": 0.664,
        "crossing_rate": 0.2553,
        "lead_mean": 23.4,
        "pre_cp_fpr": 0.14,
        "score": 0.1695
      },
      {
        "layer": 12,
        "bal_acc": 0.6752,
        "crossing_rate": 0.3191,
        "lead_mean": 15.6,
        "pre_cp_fpr": 0.1242,
        "score": 0.2155
      },
      {
        "layer": 16,
        "bal_acc": 0.6816,
        "crossing_rate": 0.3191,
        "lead_mean": 16.1,
        "pre_cp_fpr": 0.12,
        "score": 0.2175
      },
      {
        "layer": 20,
        "bal_acc": 0.6551,
        "crossing_rate": 0.3191,
        "lead_mean": 13.8,
        "pre_cp_fpr": 0.1355,
        "score": 0.2091
      },
      {
        "layer": 24,
        "bal_acc": 0.6686,
        "crossing_rate": 0.2979,
        "lead_mean": 26.5,
        "pre_cp_fpr": 0.1324,
        "score": 0.1992
      },
      {
        "layer": 27,
        "bal_acc": 0.6299,
        "crossing_rate": 0.3191,
        "lead_mean": 29.5,
        "pre_cp_fpr": 0.1524,
        "score": 0.201
      }
    ]
  },
  "phase3_temporal_probes": {
    "best_window": 3,
    "best_layer": 0,
    "results": [
      {
        "window": 1,
        "bal_acc": 0.6671,
        "precision": 0.3369,
        "coverage": 0.6809,
        "pre_cp_fpr": 0.2186,
        "lead_mean": 29.8
      },
      {
        "window": 3,
        "bal_acc": 0.6721,
        "precision": 0.3571,
        "coverage": 0.5957,
        "pre_cp_fpr": 0.1877,
        "lead_mean": 32.9
      },
      {
        "window": 5,
        "bal_acc": 0.6668,
        "precision": 0.3598,
        "coverage": 0.617,
        "pre_cp_fpr": 0.1782,
        "lead_mean": 33.7
      },
      {
        "window": 10,
        "bal_acc": 0.6636,
        "precision": 0.3635,
        "coverage": 0.617,
        "pre_cp_fpr": 0.1728,
        "lead_mean": 32.3
      },
      {
        "window": 15,
        "bal_acc": 0.657,
        "precision": 0.3556,
        "coverage": 0.6383,
        "pre_cp_fpr": 0.1789,
        "lead_mean": 31.6
      },
      {
        "window": 20,
        "bal_acc": 0.6314,
        "precision": 0.333,
        "coverage": 0.5745,
        "pre_cp_fpr": 0.1811,
        "lead_mean": 32.9
      },
      {
        "window": 25,
        "bal_acc": 0.6305,
        "precision": 0.331,
        "coverage": 0.5957,
        "pre_cp_fpr": 0.1802,
        "lead_mean": 31.3
      }
    ]
  },
  "phase4_text_probes": [
    {
      "window": 1,
      "bal_acc": 0.5810269175108538,
      "precision": 0.24462924462924462,
      "coverage": 0.6382978723404256,
      "pre_cp_fpr": 0.3448561527812028,
      "lead_mean": 37.083333333333336
    },
    {
      "window": 3,
      "bal_acc": 0.5788797684515196,
      "precision": 0.25365853658536586,
      "coverage": 0.7446808510638298,
      "pre_cp_fpr": 0.2709037727203341,
      "lead_mean": 41.57142857142857
    },
    {
      "window": 5,
      "bal_acc": 0.5689643994211289,
      "precision": 0.24744897959183673,
      "coverage": 0.7021276595744681,
      "pre_cp_fpr": 0.254684434724532,
      "lead_mean": 50.851851851851855
    },
    {
      "window": 10,
      "bal_acc": 0.5826192764109985,
      "precision": 0.26996197718631176,
      "coverage": 0.7021276595744681,
      "pre_cp_fpr": 0.22232284961863977,
      "lead_mean": 45.592592592592595
    },
    {
      "window": 15,
      "bal_acc": 0.5892485094066571,
      "precision": 0.28269617706237427,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.20037626046595514,
      "lead_mean": 46.52
    },
    {
      "window": 20,
      "bal_acc": 0.6091172214182344,
      "precision": 0.3161925601750547,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.1758008391112723,
      "lead_mean": 39.375
    },
    {
      "window": 25,
      "bal_acc": 0.6140700434153401,
      "precision": 0.3291284403669725,
      "coverage": 0.6595744680851063,
      "pre_cp_fpr": 0.1605430087993206,
      "lead_mean": 45.476190476190474
    }
  ],
  "phase5_bootstrap": {
    "bal_acc": {
      "hs_mean": 0.7372878502504099,
      "text_mean": 0.6557832624037719,
      "delta": 0.08150458784663794,
      "ci_95": [
        0.028372540246562543,
        0.13588955303691563
      ],
      "p_value": 0.001,
      "bonferroni_sig": "Yes"
    },
    "precision": {
      "hs_mean": 0.42492856373959575,
      "text_mean": 0.3458941700046874,
      "delta": 0.07903439373490834,
      "ci_95": [
        -0.00498217647350165,
        0.15817691203377748
      ],
      "p_value": 0.056,
      "bonferroni_sig": "No"
    },
    "pre_cp_fpr": {
      "hs_mean": 0.18767066132639668,
      "text_mean": 0.2709037727203341,
      "delta": -0.08323311139393744,
      "ci_95": [
        -0.1398406438408706,
        -0.02360816993128593
      ],
      "p_value": 0.007,
      "bonferroni_sig": "Yes"
    }
  },
  "phase6_selectivity": {
    "real_acc": 0.6720576555716353,
    "random_mean": 0.48699563531114326,
    "random_std": 0.014265457001283764,
    "selectivity_pp": 18.506202026049206,
    "n_perms": 10,
    "random_accs": [
      0.4764624023154848,
      0.47802396526772795,
      0.4941962373371925,
      0.49634292329956586,
      0.4810044573082489,
      0.46669013024602024,
      0.5106239073806078,
      0.4970116353111433,
      0.501945470332851,
      0.46765522431259043
    ]
  }
}
```

---

### File 2: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_ot7b_full_pipeline/report.md`

```markdown
# OpenThinker-7B Commitment Detection Pipeline Report

**Model**: open-thoughts/OpenThinker-7B
**Traces**: 228 (train=136, val=45, test=47)
**Date**: 2026-05-17 16:29

## Phase 2: Layer Sweep

Best layer: **0** (depth=0%)

| Layer | Bal Acc | Crossing Rate | Lead | Pre-CP FPR | Score |
|-------|---------|---------------|------|-----------|-------|
|  0 | 0.6671 | 0.5319 | 29.8 | 0.2186 | 0.3549 |
|  4 | 0.6630 | 0.4043 | 25.6 | 0.1538 | 0.2680 |
|  8 | 0.6640 | 0.2553 | 23.4 | 0.1400 | 0.1695 |
| 12 | 0.6752 | 0.3191 | 15.6 | 0.1242 | 0.2155 |
| 16 | 0.6816 | 0.3191 | 16.1 | 0.1200 | 0.2175 |
| 20 | 0.6551 | 0.3191 | 13.8 | 0.1355 | 0.2091 |
| 24 | 0.6686 | 0.2979 | 26.5 | 0.1324 | 0.1992 |
| 27 | 0.6299 | 0.3191 | 29.5 | 0.1524 | 0.2010 |

## Phase 3: Hidden State Temporal Probes (layer=0)

Best window: **W=3**

| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|---|---------|-----------|----------|-----------|------|
|  1 | 0.6671 | 0.3369 | 0.6809 | 0.2186 | 29.8 |
|  3 | 0.6721 | 0.3571 | 0.5957 | 0.1877 | 32.9 |
|  5 | 0.6668 | 0.3598 | 0.6170 | 0.1782 | 33.7 |
| 10 | 0.6636 | 0.3635 | 0.6170 | 0.1728 | 32.3 |
| 15 | 0.6570 | 0.3556 | 0.6383 | 0.1789 | 31.6 |
| 20 | 0.6314 | 0.3330 | 0.5745 | 0.1811 | 32.9 |
| 25 | 0.6305 | 0.3310 | 0.5957 | 0.1802 | 31.3 |

## Phase 4: Text Baseline Probes

Best window: **W=25**

| W | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|---|---------|-----------|----------|-----------|------|
|  1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |
|  3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |
|  5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |
| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |
| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |
| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |
| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |

## Phase 5: Paired Bootstrap (HS vs Text)

| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |
|--------|-----|------|-------|--------|---------|-----------|
| bal_acc | 0.7373 | 0.6558 | 0.0815 | [0.0284, 0.1359] | 0.0010 | Yes |
| precision | 0.4249 | 0.3459 | 0.0790 | [-0.0050, 0.1582] | 0.0560 | No |
| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.0070 | Yes |

## Phase 6: Selectivity Control

- Real accuracy: 0.6721
- Random mean: 0.4870 +/- 0.0143
- **Selectivity: 18.5 pp**
- N permutations: 10

## Summary

- Best layer: 0 (depth 0%)
- Best HS probe: W=3, bal_acc=0.6721
- Best text probe: W=25, bal_acc=0.6141
- Selectivity: 18.5 pp above random
- HS vs Text: HS > Text
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 68668,
  "duration_api_ms": 68434,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "3ccbd028-5c42-4b4a-b635-dad5365554aa",
  "total_cost_usd": 0.25913349999999996,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 18326,
    "cache_read_input_tokens": 60548,
    "output_tokens": 4534,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18326,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4141,
        "cache_read_input_tokens": 24591,
        "cache_creation_input_tokens": 5576,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5576
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 867,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.000937,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4534,
      "cacheReadInputTokens": 60548,
      "cacheCreationInputTokens": 18326,
      "webSearchRequests": 0,
      "costUSD": 0.2581965,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3f570a5a-b03c-4ef4-a450-d0e003f5d111"
}
```

</details>

---

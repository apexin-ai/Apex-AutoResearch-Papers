# analysis finalize 3B d005 s123 sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_analysis_finalize-3B-d005-s123-sft_20260515T150831.log`
- **Structured JSON:** [`77087d7f8f91b4bcbc13.json`](../../sessions/77/77087d7f8f91b4bcbc13.json)

## Before a recorded user message

37 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
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
  "uuid": "20dfd331-58d9-4fc4-b8c1-22f914f044bf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778866800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6d8784a0-37c2-4307-954d-362ef235fdaa",
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into steps:
1. SSH to read training logs and check checkpoints
2. Update registry with training metrics
3. Check GPU 2 is free, then submit eval job

Let me start by reading the logs and checking checkpoints, and also checking GPU status (for constraint C001/C002/C003).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "5971d6f1-3372-421c-86cb-f6f6d3aa21cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnW7dcLEokXCwUhfDhNpos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12463
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

先读取训练日志、检查 checkpoint、确认 GPU 2 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "d8b9f203-ac5c-438c-97f6-76f4d0e47297",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnW7dcLEokXCwUhfDhNpos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12463
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J8FDGdhThNVAEQtF4LHoUv`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "e906e95e-8b76-49dd-8880-a4ca8ffe37fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnW7dcLEokXCwUhfDhNpos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12463
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

_source line 7 · 2026-05-15T15:08:43.732Z_

<details><summary>↩ Tool result · `toolu_01J8FDGdhThNVAEQtF4LHoUv`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "03bc3c5f-b426-476e-a40e-6c729cf82fc4",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HkbLLTUPAyKCFMFZH1khHu`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -50 ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "bed70aab-39e7-48e3-878c-aa1ff53b5552",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U5a7VdQ38s2BewEWv8MkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 24304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2352
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Bu4njw4WnAwhLD2W3ZNkt6`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "ba43352a-06ad-449c-b711-d24ef17f6399",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U5a7VdQ38s2BewEWv8MkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 24304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2352
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Dn47v8wVQGhsjbN5vzGVUH`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "ab2e9ea5-1148-45f1-a802-b8e46138daf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U5a7VdQ38s2BewEWv8MkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 24304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2352
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

_source line 11 · 2026-05-15T15:08:49.027Z_

<details><summary>↩ Tool result · `toolu_01HkbLLTUPAyKCFMFZH1khHu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.0535, 'grad_norm': 0.3016066551208496, 'learning_rate': 1.067830117935864e-05, 'entropy': 1.0953976672142745, 'num_tokens': 16920593.0, 'mean_token_accuracy': 0.746736004948616, 'epoch': 0.86}\\n{'loss': 1.1651, 'grad_norm': 0.21130098402500153, 'learning_rate': 1.0215110087810365e-05, 'entropy': 1.141738547757268, 'num_tokens': 16979837.0, 'mean_token_accuracy': 0.7378625921905041, 'epoch': 0.86}\\n{'loss': 1.0913, 'grad_norm': 0.30132246017456055, 'learning_rate': 9.761647826098874e-06, 'entropy': 1.0703248102217913, 'num_tokens': 17043969.0, 'mean_token_accuracy': 0.7539968468248844, 'epoch': 0.87}\\n{'loss': 1.2266, 'grad_norm': 0.2510029375553131, 'learning_rate': 9.317963530077489e-06, 'entropy': 1.1594497542828321, 'num_tokens': 17112258.0, 'mean_token_accuracy': 0.7315925098955631, 'epoch': 0.87}\\n{'loss': 1.1391, 'grad_norm': 0.1511574685573578, 'learning_rate': 8.884105276087584e-06, 'entropy': 1.1314034838229419, 'num_tokens': 17176130.0, 'mean_token_accuracy': 0.7412561275064945, 'epoch': 0.87}\\n{'loss': 1.1419, 'grad_norm': 0.3425018787384033, 'learning_rate': 8.460120075749178e-06, 'entropy': 1.1326146267354489, 'num_tokens': 17236150.0, 'mean_token_accuracy': 0.7379473384469748, 'epoch': 0.88}\\n\\r 88%|████████▊ | 2790/3177 [2:43:53<17:48,  2.76s/it]\\r 88%|████████▊ | 2791/3177 [2:43:57<19:51,  3.09s/it]\\r 88%|████████▊ | 2792/3177 [2:44:00<19:55,  3.11s/it]\\r 88%|████████▊ | 2793/3177 [2:44:02<18:10,  2.84s/it]\\r 88%|████████▊ | 2794/3177 [2:44:06<19:23,  3.04s/it]\\r 88%|████████▊ | 2795/3177 [2:44:08<17:41,  2.78s/it]\\r 88%|████████▊ | 2796/3177 [2:44:11<18:01,  2.84s/it]\\r 88%|████████▊ | 2797/3177 [2:44:13<17:42,  2.80s/it]\\r 88%|████████▊ | 2798/3177 [2:44:17<18:25,  2.92s/it]\\r 88%|████████▊ | 2799/3177 [2:44:19<18:22,  2.92s/it]\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\r                                                     \\r\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\r 88%|████████▊ | 2801/3177 [2:44:25<17:36,  2.81s/it]\\r 88%|████████▊ | 2802/3177 [2:44:29<20:05,  3.21s/it]\\r 88%|████████▊ | 2803/3177 [2:44:31<18:04,  2.90s/it]\\r 88%|████████▊ | 2804/3177 [2:44:34<18:31,  2.98s/it]\\r 88%|████████▊ | 2805/3177 [2:44:38<19:40,  3.17s/it]\\r 88%|████████▊ | 2806/3177 [2:44:40<17:41,  2.86s/it]\\r 88%|████████▊ | 2807/3177 [2:44:43<17:45,  2.88s/it]\\r 88%|████████▊ | 2808/3177 [2:44:45<16:53,  2.75s/it]\\r 88%|████████▊ | 2809/3177 [2:44:49<17:38,  2.88s/it]\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\r                                                     \\r\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\r 88%|████████▊ | 2811/3177 [2:44:55<17:58,  2.95s/it]\\r 89%|████████▊ | 2812/3177 [2:44:59<19:54,  3.27s/it]\\r 89%|████████▊ | 2813/3177 [2:45:02<18:54,  3.12s/it]\\r 89%|████████▊ | 2814/3177 [2:45:05<19:01,  3.14s/it]\\r 89%|████████▊ | 2815/3177 [2:45:07<17:47,  2.95s/it]\\r 89%|████████▊ | 2816/3177 [2:45:10<17:26,  2.90s/it]\\r 89%|████████▊ | 2817/3177 [2:45:13<16:55,  2.82s/it]\\r 89%|████████▊ | 2818/3177 [2:45:15<16:27,  2.75s/it]\\r 89%|████████▊ | 2819/3177 [2:45:19<17:14,  2.89s/it]\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\r                                                     \\r\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\r 89%|████████▉ | 2821/3177 [2:45:26<21:07,  3.56s/it]\\r 89%|████████▉ | 2822/3177 [2:45:29<19:47,  3.35s/it]\\r 89%|████████▉ | 2823/3177 [2:45:32<18:57,  3.21s/it]\\r 89%|████████▉ | 2824/3177 [2:45:36<19:32,  3.32s/it]\\r 89%|████████▉ | 2825/3177 [2:45:38<17:59,  3.07s/it]\\r 89%|████████▉ | 2826/3177 [2:45:42<18:36,  3.18s/it]\\r 89%|████████▉ | 2827/3177 [2:45:45<18:14,  3.13s/it]\\r 89%|████████▉ | 2828/3177 [2:45:48<17:41,  3.04s/it]\\r 89%|████████▉ | 2829/3177 [2:45:50<16:52,  2.91s/it]\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\r                                                     \\r\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\r 89%|████████▉ | 2831/3177 [2:45:56<16:59,  2.95s/it]\\r 89%|████████▉ | 2832/3177 [2:45:59<17:45,  3.09s/it]\\r 89%|█████\\n\\n... [截断: 输出过长，省略 26943 字符] ...\\n\\n808462619781494, 'learning_rate': 1.5252559400982248e-06, 'entropy': 1.1810461785644293, 'num_tokens': 18646848.0, 'mean_token_accuracy': 0.7274677500128746, 'epoch': 0.95}\\n{'loss': 1.0962, 'grad_norm': 0.2264097034931183, 'learning_rate': 1.3494793441252596e-06, 'entropy': 1.1037385869771241, 'num_tokens': 18705692.0, 'mean_token_accuracy': 0.7475869849324226, 'epoch': 0.95}\\n{'loss': 1.0598, 'grad_norm': 0.2986776828765869, 'learning_rate': 1.184392231980913e-06, 'entropy': 1.0663477946072817, 'num_tokens': 18769740.0, 'mean_token_accuracy': 0.7524430483579636, 'epoch': 0.95}\\n{'loss': 1.1347, 'grad_norm': 0.48912671208381653, 'learning_rate': 1.0300124920250898e-06, 'entropy': 1.1496282391250134, 'num_tokens': 18830274.0, 'mean_token_accuracy': 0.7392949819564819, 'epoch': 0.96}\\n{'loss': 1.052, 'grad_norm': 0.24146032333374023, 'learning_rate': 8.863568523978849e-07, 'entropy': 1.0591788075864315, 'num_tokens': 18896650.0, 'mean_token_accuracy': 0.7516838304698468, 'epoch': 0.96}\\n{'loss': 1.1978, 'grad_norm': 0.33905860781669617, 'learning_rate': 7.534408792071124e-07, 'entropy': 1.1518729954957962, 'num_tokens': 18958854.0, 'mean_token_accuracy': 0.7395789340138436, 'epoch': 0.96}\\n{'loss': 1.1323, 'grad_norm': 0.40755578875541687, 'learning_rate': 6.312789748414872e-07, 'entropy': 1.11591779589653, 'num_tokens': 19024127.0, 'mean_token_accuracy': 0.7427128277719021, 'epoch': 0.97}\\n{'loss': 1.0651, 'grad_norm': 0.2427470088005066, 'learning_rate': 5.198843764100402e-07, 'entropy': 1.0564614221453668, 'num_tokens': 19085848.0, 'mean_token_accuracy': 0.756194906681776, 'epoch': 0.97}\\n{'loss': 1.0388, 'grad_norm': 0.19322356581687927, 'learning_rate': 4.192691543078886e-07, 'entropy': 1.0639300301671029, 'num_tokens': 19137650.0, 'mean_token_accuracy': 0.7544002160429955, 'epoch': 0.97}\\n{'loss': 1.1812, 'grad_norm': 0.26979121565818787, 'learning_rate': 3.2944421090816966e-07, 'entropy': 1.1278279833495617, 'num_tokens': 19196394.0, 'mean_token_accuracy': 0.7429495207965374, 'epoch': 0.98}\\n{'loss': 1.1261, 'grad_norm': 0.2794036269187927, 'learning_rate': 2.504192793808202e-07, 'entropy': 1.1463834058493376, 'num_tokens': 19258270.0, 'mean_token_accuracy': 0.7371742427349091, 'epoch': 0.98}\\n{'loss': 1.1025, 'grad_norm': 0.2706645429134369, 'learning_rate': 1.822029226378419e-07, 'entropy': 1.0933510724455118, 'num_tokens': 19315498.0, 'mean_token_accuracy': 0.7484965719282627, 'epoch': 0.98}\\n{'loss': 1.0752, 'grad_norm': 0.19337567687034607, 'learning_rate': 1.248025324054658e-07, 'entropy': 1.0974016677588225, 'num_tokens': 19370475.0, 'mean_token_accuracy': 0.7497679188847541, 'epoch': 0.99}\\n{'loss': 1.0205, 'grad_norm': 0.23332369327545166, 'learning_rate': 7.822432842322647e-08, 'entropy': 1.043929935619235, 'num_tokens': 19430762.0, 'mean_token_accuracy': 0.762982676923275, 'epoch': 0.99}\\n{'loss': 1.2093, 'grad_norm': 0.2347133755683899, 'learning_rate': 4.247335777000094e-08, 'entropy': 1.1957145411521197, 'num_tokens': 19496915.0, 'mean_token_accuracy': 0.7246698684990406, 'epoch': 0.99}\\n{'loss': 1.0528, 'grad_norm': 0.21410523355007172, 'learning_rate': 1.755349431710185e-08, 'entropy': 1.0614502843469382, 'num_tokens': 19560020.0, 'mean_token_accuracy': 0.7566995985805989, 'epoch': 0.99}\\n{'loss': 1.0704, 'grad_norm': 0.2421649843454361, 'learning_rate': 3.4674383085464558e-09, 'entropy': 1.0813588958233595, 'num_tokens': 19616545.0, 'mean_token_accuracy': 0.7478238351643085, 'epoch': 1.0}\\n\\r100%|██████████| 3177/3177 [3:03:02<00:00,  2.74s/it]\\r100%|██████���███| 3177/3177 [3:03:02<00:00,  3.46s/it]\\n2026-05-15 23:02:36,875 [INFO] LoRA adapter saved to /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\n2026-05-15 23:02:36,876 [INFO] Training complete.\\n{'train_runtime': 10982.2409, 'train_samples_per_second': 4.628, 'train_steps_per_second': 0.289, 'train_loss': 1.1349195613026581, 'entropy': 1.2588623031130377, 'num_tokens': 19657865.0, 'mean_token_accuracy': 0.706937847272405, 'epoch': 1.0}\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "4a279901-2d98-4d71-ab23-a78dbd6edd55",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{'loss': 1.0535, 'grad_norm': 0.3016066551208496, 'learning_rate': 1.067830117935864e-05, 'entropy': 1.0953976672142745, 'num_tokens': 16920593.0, 'mean_token_accuracy': 0.746736004948616, 'epoch': 0.86}\\\\n{'loss': 1.1651, 'grad_norm': 0.21130098402500153, 'learning_rate': 1.0215110087810365e-05, 'entropy': 1.141738547757268, 'num_tokens': 16979837.0, 'mean_token_accuracy': 0.7378625921905041, 'epoch': 0.86}\\\\n{'loss': 1.0913, 'grad_norm': 0.30132246017456055, 'learning_rate': 9.761647826098874e-06, 'entropy': 1.0703248102217913, 'num_tokens': 17043969.0, 'mean_token_accuracy': 0.7539968468248844, 'epoch': 0.87}\\\\n{'loss': 1.2266, 'grad_norm': 0.2510029375553131, 'learning_rate': 9.317963530077489e-06, 'entropy': 1.1594497542828321, 'num_tokens': 17112258.0, 'mean_token_accuracy': 0.7315925098955631, 'epoch': 0.87}\\\\n{'loss': 1.1391, 'grad_norm': 0.1511574685573578, 'learning_rate': 8.884105276087584e-06, 'entropy': 1.1314034838229419, 'num_tokens': 17176130.0, 'mean_token_accuracy': 0.7412561275064945, 'epoch': 0.87}\\\\n{'loss': 1.1419, 'grad_norm': 0.3425018787384033, 'learning_rate': 8.460120075749178e-06, 'entropy': 1.1326146267354489, 'num_tokens': 17236150.0, 'mean_token_accuracy': 0.7379473384469748, 'epoch': 0.88}\\\\n\\\\r 88%|████████▊ | 2790/3177 [2:43:53<17:48,  2.76s/it]\\\\r 88%|████████▊ | 2791/3177 [2:43:57<19:51,  3.09s/it]\\\\r 88%|████████▊ | 2792/3177 [2:44:00<19:55,  3.11s/it]\\\\r 88%|████████▊ | 2793/3177 [2:44:02<18:10,  2.84s/it]\\\\r 88%|████████▊ | 2794/3177 [2:44:06<19:23,  3.04s/it]\\\\r 88%|████████▊ | 2795/3177 [2:44:08<17:41,  2.78s/it]\\\\r 88%|████████▊ | 2796/3177 [2:44:11<18:01,  2.84s/it]\\\\r 88%|████████▊ | 2797/3177 [2:44:13<17:42,  2.80s/it]\\\\r 88%|████████▊ | 2798/3177 [2:44:17<18:25,  2.92s/it]\\\\r 88%|████████▊ | 2799/3177 [2:44:19<18:22,  2.92s/it]\\\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\\\r                                                     \\\\r\\\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\\\r 88%|████████▊ | 2801/3177 [2:44:25<17:36,  2.81s/it]\\\\r 88%|████████▊ | 2802/3177 [2:44:29<20:05,  3.21s/it]\\\\r 88%|████████▊ | 2803/3177 [2:44:31<18:04,  2.90s/it]\\\\r 88%|████████▊ | 2804/3177 [2:44:34<18:31,  2.98s/it]\\\\r 88%|████████▊ | 2805/3177 [2:44:38<19:40,  3.17s/it]\\\\r 88%|████████▊ | 2806/3177 [2:44:40<17:41,  2.86s/it]\\\\r 88%|████████▊ | 2807/3177 [2:44:43<17:45,  2.88s/it]\\\\r 88%|████████▊ | 2808/3177 [2:44:45<16:53,  2.75s/it]\\\\r 88%|████████▊ | 2809/3177 [2:44:49<17:38,  2.88s/it]\\\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\\\r                                                     \\\\r\\\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\\\r 88%|████████▊ | 2811/3177 [2:44:55<17:58,  2.95s/it]\\\\r 89%|████████▊ | 2812/3177 [2:44:59<19:54,  3.27s/it]\\\\r 89%|████████▊ | 2813/3177 [2:45:02<18:54,  3.12s/it]\\\\r 89%|████████▊ | 2814/3177 [2:45:05<19:01,  3.14s/it]\\\\r 89%|████████▊ | 2815/3177 [2:45:07<17:47,  2.95s/it]\\\\r 89%|████████▊ | 2816/3177 [2:45:10<17:26,  2.90s/it]\\\\r 89%|████████▊ | 2817/3177 [2:45:13<16:55,  2.82s/it]\\\\r 89%|████████▊ | 2818/3177 [2:45:15<16:27,  2.75s/it]\\\\r 89%|████████▊ | 2819/3177 [2:45:19<17:14,  2.89s/it]\\\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\\\r                                                     \\\\r\\\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\\\r 89%|████████▉ | 2821/3177 [2:45:26<21:07,  3.56s/it]\\\\r 89%|████████▉ | 2822/3177 [2:45:29<19:47,  3.35s/it]\\\\r 89%|████████▉ | 2823/3177 [2:45:32<18:57,  3.21s/it]\\\\r 89%|████████▉ | 2824/3177 [2:45:36<19:32,  3.32s/it]\\\\r 89%|████████▉ | 2825/3177 [2:45:38<17:59,  3.07s/it]\\\\r 89%|████████▉ | 2826/3177 [2:45:42<18:36,  3.18s/it]\\\\r 89%|████████▉ | 2827/3177 [2:45:45<18:14,  3.13s/it]\\\\r 89%|████████▉ | 2828/3177 [2:45:48<17:41,  3.04s/it]\\\\r 89%|████████▉ | 2829/3177 [2:45:50<16:52,  2.91s/it]\\\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\\\r                                                     \\\\r\\\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\\\r 89%|████████▉ | 2831/3177 [2:45:56<16:59,  2.95s/it]\\\\r 89%|████████▉ | 2832/3177 [2:45:59<17:45,  3.09s/it]\\\\r 89%|█████\\\\n\\\\n... [截断: 输出过长，省略 26943 字符] ...\\\\n\\\\n808462619781494, 'learning_rate': 1.5252559400982248e-06, 'entropy': 1.1810461785644293, 'num_tokens': 18646848.0, 'mean_token_accuracy': 0.7274677500128746, 'epoch': 0.95}\\\\n{'loss': 1.0962, 'grad_norm': 0.2264097034931183, 'learning_rate': 1.3494793441252596e-06, 'entropy': 1.1037385869771241, 'num_tokens': 18705692.0, 'mean_token_accuracy': 0.7475869849324226, 'epoch': 0.95}\\\\n{'loss': 1.0598, 'grad_norm': 0.2986776828765869, 'learning_rate': 1.184392231980913e-06, 'entropy': 1.0663477946072817, 'num_tokens': 18769740.0, 'mean_token_accuracy': 0.7524430483579636, 'epoch': 0.95}\\\\n{'loss': 1.1347, 'grad_norm': 0.48912671208381653, 'learning_rate': 1.0300124920250898e-06, 'entropy': 1.1496282391250134, 'num_tokens': 18830274.0, 'mean_token_accuracy': 0.7392949819564819, 'epoch': 0.96}\\\\n{'loss': 1.052, 'grad_norm': 0.24146032333374023, 'learning_rate': 8.863568523978849e-07, 'entropy': 1.0591788075864315, 'num_tokens': 18896650.0, 'mean_token_accuracy': 0.7516838304698468, 'epoch': 0.96}\\\\n{'loss': 1.1978, 'grad_norm': 0.33905860781669617, 'learning_rate': 7.534408792071124e-07, 'entropy': 1.1518729954957962, 'num_tokens': 18958854.0, 'mean_token_accuracy': 0.7395789340138436, 'epoch': 0.96}\\\\n{'loss': 1.1323, 'grad_norm': 0.40755578875541687, 'learning_rate': 6.312789748414872e-07, 'entropy': 1.11591779589653, 'num_tokens': 19024127.0, 'mean_token_accuracy': 0.7427128277719021, 'epoch': 0.97}\\\\n{'loss': 1.0651, 'grad_norm': 0.2427470088005066, 'learning_rate': 5.198843764100402e-07, 'entropy': 1.0564614221453668, 'num_tokens': 19085848.0, 'mean_token_accuracy': 0.756194906681776, 'epoch': 0.97}\\\\n{'loss': 1.0388, 'grad_norm': 0.19322356581687927, 'learning_rate': 4.192691543078886e-07, 'entropy': 1.0639300301671029, 'num_tokens': 19137650.0, 'mean_token_accuracy': 0.7544002160429955, 'epoch': 0.97}\\\\n{'loss': 1.1812, 'grad_norm': 0.26979121565818787, 'learning_rate': 3.2944421090816966e-07, 'entropy': 1.1278279833495617, 'num_tokens': 19196394.0, 'mean_token_accuracy': 0.7429495207965374, 'epoch': 0.98}\\\\n{'loss': 1.1261, 'grad_norm': 0.2794036269187927, 'learning_rate': 2.504192793808202e-07, 'entropy': 1.1463834058493376, 'num_tokens': 19258270.0, 'mean_token_accuracy': 0.7371742427349091, 'epoch': 0.98}\\\\n{'loss': 1.1025, 'grad_norm': 0.2706645429134369, 'learning_rate': 1.822029226378419e-07, 'entropy': 1.0933510724455118, 'num_tokens': 19315498.0, 'mean_token_accuracy': 0.7484965719282627, 'epoch': 0.98}\\\\n{'loss': 1.0752, 'grad_norm': 0.19337567687034607, 'learning_rate': 1.248025324054658e-07, 'entropy': 1.0974016677588225, 'num_tokens': 19370475.0, 'mean_token_accuracy': 0.7497679188847541, 'epoch': 0.99}\\\\n{'loss': 1.0205, 'grad_norm': 0.23332369327545166, 'learning_rate': 7.822432842322647e-08, 'entropy': 1.043929935619235, 'num_tokens': 19430762.0, 'mean_token_accuracy': 0.762982676923275, 'epoch': 0.99}\\\\n{'loss': 1.2093, 'grad_norm': 0.2347133755683899, 'learning_rate': 4.247335777000094e-08, 'entropy': 1.1957145411521197, 'num_tokens': 19496915.0, 'mean_token_accuracy': 0.7246698684990406, 'epoch': 0.99}\\\\n{'loss': 1.0528, 'grad_norm': 0.21410523355007172, 'learning_rate': 1.755349431710185e-08, 'entropy': 1.0614502843469382, 'num_tokens': 19560020.0, 'mean_token_accuracy': 0.7566995985805989, 'epoch': 0.99}\\\\n{'loss': 1.0704, 'grad_norm': 0.2421649843454361, 'learning_rate': 3.4674383085464558e-09, 'entropy': 1.0813588958233595, 'num_tokens': 19616545.0, 'mean_token_accuracy': 0.7478238351643085, 'epoch': 1.0}\\\\n\\\\r100%|██████████| 3177/3177 [3:03:02<00:00,  2.74s/it]\\\\r100%|██████���███| 3177/3177 [3:03:02<00:00,  3.46s/it]\\\\n2026-05-15 23:02:36,875 [INFO] LoRA adapter saved to /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\\\n2026-05-15 23:02:36,876 [INFO] Training complete.\\\\n{'train_runtime': 10982.2409, 'train_samples_per_second': 4.628, 'train_steps_per_second': 0.289, 'train_loss': 1.1349195613026581, 'entropy': 1.2588623031130377, 'num_tokens': 19657865.0, 'mean_token_accuracy': 0.706937847272405, 'epoch': 1.0}\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.0535, 'grad_norm': 0.3016066551208496, 'learning_rate': 1.067830117935864e-05, 'entropy': 1.0953976672142745, 'num_tokens': 16920593.0, 'mean_token_accuracy': 0.746736004948616, 'epoch': 0.86}\\n{'loss': 1.1651, 'grad_norm': 0.21130098402500153, 'learning_rate': 1.0215110087810365e-05, 'entropy': 1.141738547757268, 'num_tokens': 16979837.0, 'mean_token_accuracy': 0.7378625921905041, 'epoch': 0.86}\\n{'loss': 1.0913, 'grad_norm': 0.30132246017456055, 'learning_rate': 9.761647826098874e-06, 'entropy': 1.0703248102217913, 'num_tokens': 17043969.0, 'mean_token_accuracy': 0.7539968468248844, 'epoch': 0.87}\\n{'loss': 1.2266, 'grad_norm': 0.2510029375553131, 'learning_rate': 9.317963530077489e-06, 'entropy': 1.1594497542828321, 'num_tokens': 17112258.0, 'mean_token_accuracy': 0.7315925098955631, 'epoch': 0.87}\\n{'loss': 1.1391, 'grad_norm': 0.1511574685573578, 'learning_rate': 8.884105276087584e-06, 'entropy': 1.1314034838229419, 'num_tokens': 17176130.0, 'mean_token_accuracy': 0.7412561275064945, 'epoch': 0.87}\\n{'loss': 1.1419, 'grad_norm': 0.3425018787384033, 'learning_rate': 8.460120075749178e-06, 'entropy': 1.1326146267354489, 'num_tokens': 17236150.0, 'mean_token_accuracy': 0.7379473384469748, 'epoch': 0.88}\\n\\r 88%|████████▊ | 2790/3177 [2:43:53<17:48,  2.76s/it]\\r 88%|████████▊ | 2791/3177 [2:43:57<19:51,  3.09s/it]\\r 88%|████████▊ | 2792/3177 [2:44:00<19:55,  3.11s/it]\\r 88%|████████▊ | 2793/3177 [2:44:02<18:10,  2.84s/it]\\r 88%|████████▊ | 2794/3177 [2:44:06<19:23,  3.04s/it]\\r 88%|████████▊ | 2795/3177 [2:44:08<17:41,  2.78s/it]\\r 88%|████████▊ | 2796/3177 [2:44:11<18:01,  2.84s/it]\\r 88%|████████▊ | 2797/3177 [2:44:13<17:42,  2.80s/it]\\r 88%|████████▊ | 2798/3177 [2:44:17<18:25,  2.92s/it]\\r 88%|████████▊ | 2799/3177 [2:44:19<18:22,  2.92s/it]\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\r                                                     \\r\\r 88%|████████▊ | 2800/3177 [2:44:22<17:44,  2.82s/it]\\r 88%|████████▊ | 2801/3177 [2:44:25<17:36,  2.81s/it]\\r 88%|████████▊ | 2802/3177 [2:44:29<20:05,  3.21s/it]\\r 88%|████████▊ | 2803/3177 [2:44:31<18:04,  2.90s/it]\\r 88%|████████▊ | 2804/3177 [2:44:34<18:31,  2.98s/it]\\r 88%|████████▊ | 2805/3177 [2:44:38<19:40,  3.17s/it]\\r 88%|████████▊ | 2806/3177 [2:44:40<17:41,  2.86s/it]\\r 88%|████████▊ | 2807/3177 [2:44:43<17:45,  2.88s/it]\\r 88%|████████▊ | 2808/3177 [2:44:45<16:53,  2.75s/it]\\r 88%|████████▊ | 2809/3177 [2:44:49<17:38,  2.88s/it]\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\r                                                     \\r\\r 88%|████████▊ | 2810/3177 [2:44:52<18:46,  3.07s/it]\\r 88%|████████▊ | 2811/3177 [2:44:55<17:58,  2.95s/it]\\r 89%|████████▊ | 2812/3177 [2:44:59<19:54,  3.27s/it]\\r 89%|████████▊ | 2813/3177 [2:45:02<18:54,  3.12s/it]\\r 89%|████████▊ | 2814/3177 [2:45:05<19:01,  3.14s/it]\\r 89%|████████▊ | 2815/3177 [2:45:07<17:47,  2.95s/it]\\r 89%|████████▊ | 2816/3177 [2:45:10<17:26,  2.90s/it]\\r 89%|████████▊ | 2817/3177 [2:45:13<16:55,  2.82s/it]\\r 89%|████████▊ | 2818/3177 [2:45:15<16:27,  2.75s/it]\\r 89%|████████▊ | 2819/3177 [2:45:19<17:14,  2.89s/it]\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\r                                                     \\r\\r 89%|████████▉ | 2820/3177 [2:45:21<16:34,  2.79s/it]\\r 89%|████████▉ | 2821/3177 [2:45:26<21:07,  3.56s/it]\\r 89%|████████▉ | 2822/3177 [2:45:29<19:47,  3.35s/it]\\r 89%|████████▉ | 2823/3177 [2:45:32<18:57,  3.21s/it]\\r 89%|████████▉ | 2824/3177 [2:45:36<19:32,  3.32s/it]\\r 89%|████████▉ | 2825/3177 [2:45:38<17:59,  3.07s/it]\\r 89%|████████▉ | 2826/3177 [2:45:42<18:36,  3.18s/it]\\r 89%|████████▉ | 2827/3177 [2:45:45<18:14,  3.13s/it]\\r 89%|████████▉ | 2828/3177 [2:45:48<17:41,  3.04s/it]\\r 89%|████████▉ | 2829/3177 [2:45:50<16:52,  2.91s/it]\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\r                                                     \\r\\r 89%|████████▉ | 2830/3177 [2:45:53<16:21,  2.83s/it]\\r 89%|████████▉ | 2831/3177 [2:45:56<16:59,  2.95s/it]\\r 89%|████████▉ | 2832/3177 [2:45:59<17:45,  3.09s/it]\\r 89%|█████\\n\\n... [截断: 输出过长，省略 26943 字符] ...\\n\\n808462619781494, 'learning_rate': 1.5252559400982248e-06, 'entropy': 1.1810461785644293, 'num_tokens': 18646848.0, 'mean_token_accuracy': 0.7274677500128746, 'epoch': 0.95}\\n{'loss': 1.0962, 'grad_norm': 0.2264097034931183, 'learning_rate': 1.3494793441252596e-06, 'entropy': 1.1037385869771241, 'num_tokens': 18705692.0, 'mean_token_accuracy': 0.7475869849324226, 'epoch': 0.95}\\n{'loss': 1.0598, 'grad_norm': 0.2986776828765869, 'learning_rate': 1.184392231980913e-06, 'entropy': 1.0663477946072817, 'num_tokens': 18769740.0, 'mean_token_accuracy': 0.7524430483579636, 'epoch': 0.95}\\n{'loss': 1.1347, 'grad_norm': 0.48912671208381653, 'learning_rate': 1.0300124920250898e-06, 'entropy': 1.1496282391250134, 'num_tokens': 18830274.0, 'mean_token_accuracy': 0.7392949819564819, 'epoch': 0.96}\\n{'loss': 1.052, 'grad_norm': 0.24146032333374023, 'learning_rate': 8.863568523978849e-07, 'entropy': 1.0591788075864315, 'num_tokens': 18896650.0, 'mean_token_accuracy': 0.7516838304698468, 'epoch': 0.96}\\n{'loss': 1.1978, 'grad_norm': 0.33905860781669617, 'learning_rate': 7.534408792071124e-07, 'entropy': 1.1518729954957962, 'num_tokens': 18958854.0, 'mean_token_accuracy': 0.7395789340138436, 'epoch': 0.96}\\n{'loss': 1.1323, 'grad_norm': 0.40755578875541687, 'learning_rate': 6.312789748414872e-07, 'entropy': 1.11591779589653, 'num_tokens': 19024127.0, 'mean_token_accuracy': 0.7427128277719021, 'epoch': 0.97}\\n{'loss': 1.0651, 'grad_norm': 0.2427470088005066, 'learning_rate': 5.198843764100402e-07, 'entropy': 1.0564614221453668, 'num_tokens': 19085848.0, 'mean_token_accuracy': 0.756194906681776, 'epoch': 0.97}\\n{'loss': 1.0388, 'grad_norm': 0.19322356581687927, 'learning_rate': 4.192691543078886e-07, 'entropy': 1.0639300301671029, 'num_tokens': 19137650.0, 'mean_token_accuracy': 0.7544002160429955, 'epoch': 0.97}\\n{'loss': 1.1812, 'grad_norm': 0.26979121565818787, 'learning_rate': 3.2944421090816966e-07, 'entropy': 1.1278279833495617, 'num_tokens': 19196394.0, 'mean_token_accuracy': 0.7429495207965374, 'epoch': 0.98}\\n{'loss': 1.1261, 'grad_norm': 0.2794036269187927, 'learning_rate': 2.504192793808202e-07, 'entropy': 1.1463834058493376, 'num_tokens': 19258270.0, 'mean_token_accuracy': 0.7371742427349091, 'epoch': 0.98}\\n{'loss': 1.1025, 'grad_norm': 0.2706645429134369, 'learning_rate': 1.822029226378419e-07, 'entropy': 1.0933510724455118, 'num_tokens': 19315498.0, 'mean_token_accuracy': 0.7484965719282627, 'epoch': 0.98}\\n{'loss': 1.0752, 'grad_norm': 0.19337567687034607, 'learning_rate': 1.248025324054658e-07, 'entropy': 1.0974016677588225, 'num_tokens': 19370475.0, 'mean_token_accuracy': 0.7497679188847541, 'epoch': 0.99}\\n{'loss': 1.0205, 'grad_norm': 0.23332369327545166, 'learning_rate': 7.822432842322647e-08, 'entropy': 1.043929935619235, 'num_tokens': 19430762.0, 'mean_token_accuracy': 0.762982676923275, 'epoch': 0.99}\\n{'loss': 1.2093, 'grad_norm': 0.2347133755683899, 'learning_rate': 4.247335777000094e-08, 'entropy': 1.1957145411521197, 'num_tokens': 19496915.0, 'mean_token_accuracy': 0.7246698684990406, 'epoch': 0.99}\\n{'loss': 1.0528, 'grad_norm': 0.21410523355007172, 'learning_rate': 1.755349431710185e-08, 'entropy': 1.0614502843469382, 'num_tokens': 19560020.0, 'mean_token_accuracy': 0.7566995985805989, 'epoch': 0.99}\\n{'loss': 1.0704, 'grad_norm': 0.2421649843454361, 'learning_rate': 3.4674383085464558e-09, 'entropy': 1.0813588958233595, 'num_tokens': 19616545.0, 'mean_token_accuracy': 0.7478238351643085, 'epoch': 1.0}\\n\\r100%|██████████| 3177/3177 [3:03:02<00:00,  2.74s/it]\\r100%|██████���███| 3177/3177 [3:03:02<00:00,  3.46s/it]\\n2026-05-15 23:02:36,875 [INFO] LoRA adapter saved to /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\n2026-05-15 23:02:36,876 [INFO] Training complete.\\n{'train_runtime': 10982.2409, 'train_samples_per_second': 4.628, 'train_steps_per_second': 0.289, 'train_loss': 1.1349195613026581, 'entropy': 1.2588623031130377, 'num_tokens': 19657865.0, 'mean_token_accuracy': 0.706937847272405, 'epoch': 1.0}\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FgrgLzXhbY6ebLeW9ncJX5`</summary>

```json
{
  "filters": {
    "exp_id": "exp_001_sft_3B_d005_s123"
  },
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "0d35d7eb-2e75-486f-a51e-6e836a98be8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U5a7VdQ38s2BewEWv8MkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 24304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2352
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

_source line 13 · 2026-05-15T15:08:49.640Z_

<details><summary>↩ Tool result · `toolu_01Bu4njw4WnAwhLD2W3ZNkt6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   63 May 15 23:02 .\\ndrwxr-xr-x 28 root root 4096 May 15 19:58 ..\\ndrwxr-xr-x  3 root root 4096 May 15 23:02 lora_adapter\\n-rw-r--r--  1 root root  306 May 15 23:02 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "893b46ae-8fe5-4a12-aeda-2c9ee761cf51",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 12\\\\ndrwxr-xr-x  3 root root   63 May 15 23:02 .\\\\ndrwxr-xr-x 28 root root 4096 May 15 19:58 ..\\\\ndrwxr-xr-x  3 root root 4096 May 15 23:02 lora_adapter\\\\n-rw-r--r--  1 root root  306 May 15 23:02 train_config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   63 May 15 23:02 .\\ndrwxr-xr-x 28 root root 4096 May 15 19:58 ..\\ndrwxr-xr-x  3 root root 4096 May 15 23:02 lora_adapter\\n-rw-r--r--  1 root root  306 May 15 23:02 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T15:08:51.039Z_

<details><summary>↩ Tool result · `toolu_01Dn47v8wVQGhsjbN5vzGVUH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fri May 15 23:08:50 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\n| 32%   54C    P2            333W /  425W |   17400MiB /  24564MiB |    100%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |\\n| 30%   43C    P2            143W /  425W |    5857MiB /  24564MiB |     48%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |\\n| 85%   71C    P2            401W /  425W |    8985MiB /  24564MiB |     91%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\n| 30%   53C    P2            195W /  425W |    8985MiB /  24564MiB |     63%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   4  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |\\n| 36%   56C    P2            180W /  425W |    9017MiB /  24564MiB |     66%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   5  NVIDIA GeForce RTX 4090 D      On  |   00000000:B8:00.0 Off |                  Off |\\n| 30%   53C    P2            200W /  425W |    9017MiB /  24564MiB |     64%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          566224      C   /root/miniconda3/bin/python            5848MiB |\\n|    0   N/A  N/A          576040      C   /root/miniconda3/bin/python           11538MiB |\\n|    1   N/A  N/A          566311      C   /root/miniconda3/bin/python            5848MiB |\\n|    2   N/A  N/A          580698      C   /root/miniconda3/bin/python            8976MiB |\\n|    3   N/A  N/A          576735      C   /root/miniconda3/bin/python            8976MiB |\\n|    4   N/A  N/A          576825      C   /root/miniconda3/bin/python            9008MiB |\\n|    5   N/A  N/A          576978      C   /root/miniconda3/bin/python            9008MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "5c038c3b-b844-4088-9a2a-b46c7fdec2e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Fri May 15 23:08:50 2026       \\\\n+-----------------------------------------------------------------------------------------+\\\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\\\n|                                         |                        |               MIG M. |\\\\n|=========================================+========================+======================|\\\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\\\n| 32%   54C    P2            333W /  425W |   17400MiB /  24564MiB |    100%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |\\\\n| 30%   43C    P2            143W /  425W |    5857MiB /  24564MiB |     48%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |\\\\n| 85%   71C    P2            401W /  425W |    8985MiB /  24564MiB |     91%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\\\n| 30%   53C    P2            195W /  425W |    8985MiB /  24564MiB |     63%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   4  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |\\\\n| 36%   56C    P2            180W /  425W |    9017MiB /  24564MiB |     66%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   5  NVIDIA GeForce RTX 4090 D      On  |   00000000:B8:00.0 Off |                  Off |\\\\n| 30%   53C    P2            200W /  425W |    9017MiB /  24564MiB |     64%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n\\\\n+-----------------------------------------------------------------------------------------+\\\\n| Processes:                                                                              |\\\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\\\n|        ID   ID                                                               Usage      |\\\\n|=========================================================================================|\\\\n|    0   N/A  N/A          566224      C   /root/miniconda3/bin/python            5848MiB |\\\\n|    0   N/A  N/A          576040      C   /root/miniconda3/bin/python           11538MiB |\\\\n|    1   N/A  N/A          566311      C   /root/miniconda3/bin/python            5848MiB |\\\\n|    2   N/A  N/A          580698      C   /root/miniconda3/bin/python            8976MiB |\\\\n|    3   N/A  N/A          576735      C   /root/miniconda3/bin/python            8976MiB |\\\\n|    4   N/A  N/A          576825      C   /root/miniconda3/bin/python            9008MiB |\\\\n|    5   N/A  N/A          576978      C   /root/miniconda3/bin/python            9008MiB |\\\\n+-----------------------------------------------------------------------------------------+\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Fri May 15 23:08:50 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\n| 32%   54C    P2            333W /  425W |   17400MiB /  24564MiB |    100%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |\\n| 30%   43C    P2            143W /  425W |    5857MiB /  24564MiB |     48%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |\\n| 85%   71C    P2            401W /  425W |    8985MiB /  24564MiB |     91%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\n| 30%   53C    P2            195W /  425W |    8985MiB /  24564MiB |     63%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   4  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |\\n| 36%   56C    P2            180W /  425W |    9017MiB /  24564MiB |     66%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   5  NVIDIA GeForce RTX 4090 D      On  |   00000000:B8:00.0 Off |                  Off |\\n| 30%   53C    P2            200W /  425W |    9017MiB /  24564MiB |     64%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          566224      C   /root/miniconda3/bin/python            5848MiB |\\n|    0   N/A  N/A          576040      C   /root/miniconda3/bin/python           11538MiB |\\n|    1   N/A  N/A          566311      C   /root/miniconda3/bin/python            5848MiB |\\n|    2   N/A  N/A          580698      C   /root/miniconda3/bin/python            8976MiB |\\n|    3   N/A  N/A          576735      C   /root/miniconda3/bin/python            8976MiB |\\n|    4   N/A  N/A          576825      C   /root/miniconda3/bin/python            9008MiB |\\n|    5   N/A  N/A          576978      C   /root/miniconda3/bin/python            9008MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T15:08:51.860Z_

<details><summary>↩ Tool result · `toolu_01FgrgLzXhbY6ebLeW9ncJX5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8038}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "83d5d486-9f7b-46e9-85b9-ea2378ca2d53",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8038}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8038}}"
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
Let me analyze what I found:

1. **Training log**: Training completed successfully. Key metrics from the final summary line:
   - `train_loss`: 1.1349195613026581
   - `mean_token_accuracy`: 0.706937847272405 (this is the overall average, but the last step showed 0.7478)
   - `total_steps`: 3177
   - `train_runtime`: 10982.2409 seconds (~3h 3min)
   - `EXIT_CODE=0`
   - Last logged step loss: 1.0704, mean_token_accuracy: 0.7478
   
2. **Checkpoint**: The LoRA adapter has been saved successfully and exists at `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/`

3. **GPU 2**: There's a process occupying GPU 2 (PID 580698) using 8976MiB of memory that I need to investigate further.

Before I can submit the evaluation job, I need to identify what PID 580698 is running and verify the eval registry entry to ensure GPU 2 will actually be free for the job.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "9df979cc-82c9-427a-a465-9a92d0a2f695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVrZLgQTvuweTyL8P4RpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6445,
      "cache_read_input_tokens": 26656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6445
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

GPU 2 被占用（PID 580698）。需要确认该进程是什么，再决定是否可以提交 eval。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "17b1a9b4-4679-46ed-9a5b-6e0926be2d03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVrZLgQTvuweTyL8P4RpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6445,
      "cache_read_input_tokens": 26656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6445
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PZgfYtNVQDp9mMkpBJ5ub1`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 580698 -o pid,start,etime,args"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "93ba2087-f84a-4b25-8f11-91bbede1ceb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVrZLgQTvuweTyL8P4RpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6445,
      "cache_read_input_tokens": 26656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6445
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

_source line 19 · 2026-05-15T15:09:03.719Z_

<details><summary>↩ Tool result · `toolu_01PZgfYtNVQDp9mMkpBJ5ub1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID  STARTED     ELAPSED COMMAND\\n580698 23:06:21       02:42 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "c57e67dd-d989-4b09-b473-909ab2bd894a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"   PID  STARTED     ELAPSED COMMAND\\\\n580698 23:06:21       02:42 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"   PID  STARTED     ELAPSED COMMAND\\n580698 23:06:21       02:42 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BokErgfkoMWWruGjTKd5G8`</summary>

```json
{
  "filters": {
    "exp_id": "exp_001_eval_3B_d005_s123"
  },
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "f40c403b-168b-443e-bc37-a161f824ea5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVrZLgQTvuweTyL8P4RpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6445,
      "cache_read_input_tokens": 26656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6445
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RJDg5TJQMk1wm57JKyaMTW`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "c1c5fa5b-ad13-4dd8-8b54-b694972bd8c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjVrZLgQTvuweTyL8P4RpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6445,
      "cache_read_input_tokens": 26656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6445
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

_source line 22 · 2026-05-15T15:09:05.721Z_

<details><summary>↩ Tool result · `toolu_01BokErgfkoMWWruGjTKd5G8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4941}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "7c075ff2-c7a0-4083-82d0-fb4915e9da0c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4941}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4941}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T15:09:06.561Z_

<details><summary>↩ Tool result · `toolu_01RJDg5TJQMk1wm57JKyaMTW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:06:22.987Z\", \"updated_at\": \"2026-05-15T15:07:26.619Z\", \"spec\": {\"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 580693, \"submitted_at\": \"2026-05-15T15:06:22Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\"}, \"exp_002_signals_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T15:01:04.042Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\"}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T14:52:55.775Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T14:52:51.417Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T14:52:46.200Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\"}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T13:53:17.512Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T13:53:13.050Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}}}, \"count\": 9, \"total\": 9, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.819}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "b872bbb8-1ff4-4878-ac55-4d38160e9569",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_001_eval_3B_d005_s123_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T15:06:22.987Z\\\", \\\"updated_at\\\": \\\"2026-05-15T15:07:26.619Z\\\", \\\"spec\\\": {\\\"parent\\\": \\\"exp_001_sft_3B_d005_s123\\\", \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d005_s123\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\\", \\\"data_count\\\": 4, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 580693, \\\"submitted_at\\\": \\\"2026-05-15T15:06:22Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\\\"}, \\\"exp_002_signals_3B\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:46:52.925Z\\\", \\\"updated_at\\\": \\\"2026-05-15T15:01:04.042Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"576030\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T14:46:52.136Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"data_path\\\": \\\"/root/contamcal-irt-calibration/exp002/\\\", \\\"data_count\\\": \\\"12 tasks (4 dosages x 3 benchmarks)\\\", \\\"seed\\\": \\\"N/A (signal computation)\\\", \\\"signals\\\": [\\\"embedding\\\", \\\"minkpp\\\", \\\"selfcritique\\\"], \\\"benchmarks\\\": [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"], \\\"dosages\\\": [\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d100\\\"], \\\"note\\\": \\\"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\\\"}}, \\\"exp_001_eval_3B_d000_s42_para_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:20.059Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:55.775Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:39.151Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 576973, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/paraphrases\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d000_s42\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d000_s42\\\", \\\"hypothesis\\\": \\\"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\\\"}, \\\"pid\\\": \\\"576973\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\\\"}, \\\"exp_001_eval_3B_d100_s42_para_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:17.570Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:51.417Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:34.257Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 576820, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/paraphrases\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exp_001_sft_d100_3B_v2\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\\\", \\\"parent\\\": \\\"exp_001_sft_d100_3B_v2\\\", \\\"hypothesis\\\": \\\"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\\\"}, \\\"pid\\\": \\\"576820\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\\\"}, \\\"exp_001_eval_3B_d025_s123_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:16.431Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:46.200Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:29.435Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 576730, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d025_s123\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d025_s123\\\", \\\"hypothesis\\\": \\\"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\\\"}, \\\"pid\\\": \\\"576730\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\\\"}, \\\"exp_001_eval_15B_d005_s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:05:33.959Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:55:00.000Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"566224\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:42:01.362Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"notes\\\": \\\"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\\\"}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"566224\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\\\"}, \\\"exp_001_eval_15B_d025_s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:05:35.304Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:55:00.000Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"566311\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:42:05.132Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"notes\\\": \\\"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\\\"}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"566311\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\\\"}, \\\"exp_001_eval_15B_d025_s123_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T13:52:50.883Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:53:17.512Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 566311, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_15B_d025_s123_v2\\\", \\\"hypothesis\\\": \\\"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\\\"}}, \\\"exp_001_eval_15B_d005_s123_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T13:52:49.837Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:53:13.050Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 566224, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_15B_d005_s123_v2\\\", \\\"hypothesis\\\": \\\"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\\\"}}}, \\\"count\\\": 9, \\\"total\\\": 9, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.819}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:06:22.987Z\", \"updated_at\": \"2026-05-15T15:07:26.619Z\", \"spec\": {\"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 580693, \"submitted_at\": \"2026-05-15T15:06:22Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\"}, \"exp_002_signals_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T15:01:04.042Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\"}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T14:52:55.775Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T14:52:51.417Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T14:52:46.200Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\"}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T13:53:17.512Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T13:53:13.050Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}}}, \"count\": 9, \"total\": 9, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.819}}"
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
Key findings:

1. **GPU 2 already has the d005 s123 eval running** - PID 580698, started at 23:06:21, running for ~2:42 minutes. The command is exactly the eval we were asked to submit: `evaluate.py --adapter-path .../Qwen2.5-3B_d005_s123/lora_adapter --output-dir .../Qwen2.5-3B_d005_s123_aligned`

2. **Registry already has `exp_001_eval_3B_d005_s123_aligned`** (note the `_aligned` suffix) in RUNNING state, created at 15:06:22, with PID 580693 on cuda:2. This is the same eval job.
   
The eval is already submitted and running, so I won't resubmit it. Instead, I'll extract the SFT metrics from the training log—final loss of 1.1349 and token accuracy of 0.7069—then update the registry and report the eval status.

Looking at the detailed metrics, the last step shows a loss of 1.0704 with accuracy at 0.7478, and the training completed in about 3 hours on a single GPU across 3,177 steps. I'll use the summary values for the registry since those represent the epoch average, then check the current SFT registry state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "cdb961a2-8667-46d4-b098-0869f9f20a55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPc1FD1crvBWSDyNjESH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7938,
      "cache_read_input_tokens": 33101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7938
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

GPU 2 上已经在跑 `exp_001_eval_3B_d005_s123_aligned`（PID 580698，started 23:06），无需重复提交。

现在更新 SFT registry。训练日志关键指标：
- train_loss: 1.1349, final step loss: 1.0704
- mean_token_accuracy: 0.7069 (avg), final step: 0.7478
- total_steps: 3177, runtime: 10982s (~3.05h)
- checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "3bd17a0a-18c3-424a-bfb7-00301a5e15b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPc1FD1crvBWSDyNjESH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7938,
      "cache_read_input_tokens": 33101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7938
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EZctmTbwLLyyjK7r3fep6E`</summary>

```json
{
  "filters": {
    "exp_id": "exp_001_sft_3B_d005_s123"
  },
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "f756b700-c24b-4915-b55d-e99ac140a16f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPc1FD1crvBWSDyNjESH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7938,
      "cache_read_input_tokens": 33101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7938
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

_source line 27 · 2026-05-15T15:09:27.342Z_

<details><summary>↩ Tool result · `toolu_01EZctmTbwLLyyjK7r3fep6E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3746}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "ed6ab501-8899-42b4-be07-50b9e23c67f7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3746}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3746}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The SFT experiment doesn't exist in the registry with that exact ID. Let me search without the exp_id filter to see all experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "9c78777a-c544-435a-870c-159d2d17201f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkE23AYqb6HnFvNtjiywv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
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

_source line 29_

ID 不匹配，查一下 SFT 相关的所有实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "d243f522-0a36-42de-95b2-2d72677b974a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkE23AYqb6HnFvNtjiywv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01F19w2HMa7VZqqb7Mmicxo1`</summary>

```json
{
  "filters": {
    "status": "ANALYZING"
  },
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "89aa9042-03df-414f-8ce9-25e7b1c335b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgkE23AYqb6HnFvNtjiywv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 943
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

_source line 31 · 2026-05-15T15:09:31.700Z_

<details><summary>↩ Tool result · `toolu_01F19w2HMa7VZqqb7Mmicxo1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4069}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "012e5a05-7a15-4cb6-949a-1dac26985df3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4069}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4069}}"
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
No ANALYZING experiments. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "f770413e-13e9-4d0d-930d-ce8c5c59b3f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBzkiiHDJWsTMW2ZmQcdVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 41982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HMpR74B96EwrZSj61jsn34`</summary>

```json
{
  "fields": [
    "*"
  ],
  "project": "contamcal-irt-calibration",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "434453d4-41ff-402e-9331-d98612527326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBzkiiHDJWsTMW2ZmQcdVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 41982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 34 · 2026-05-15T15:09:35.038Z_

<details><summary>↩ Tool result · `toolu_01HMpR74B96EwrZSj61jsn34`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_sft_3B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:15.842Z\", \"updated_at\": \"2026-05-15T15:08:45.951Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir Qwen2.5-3B_d005_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 555936, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log\", \"submitted_at\": \"2026-05-15T11:58:30.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123\", \"wall_clock_seconds\": 11333.2, \"gpu_hours\": 3.15}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:03:17.430Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:03:27.534050+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"completed_at\": \"2026-05-15T15:07:23.368Z\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:06:22.987Z\", \"updated_at\": \"2026-05-15T15:07:26.619Z\", \"spec\": {\"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 580693, \"submitted_at\": \"2026-05-15T15:06:22Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\"}, \"exp_002_signals_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T15:01:04.042Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\"}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T14:52:55.775Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T14:52:51.417Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T14:52:46.200Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"exp_001_sft_3B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:17.463Z\", \"updated_at\": \"2026-05-15T14:48:17.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 556016, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\", \"submitted_at\": \"2026-05-15T11:58:33.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:4\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\", \"wall_clock_seconds\": 10087.1, \"gpu_hours\": 2.8}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:44:02.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:44:06.449580+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"completed_at\": \"2026-05-15T14:46:40.166Z\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:12.687Z\", \"updated_at\": \"2026-05-15T14:36:58.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 551219, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d000_s123\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d000_s123\", \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\"}, \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:33:26.658Z\", \"metrics\": {\"mmlu\": 0.6332, \"gsm8k\": 0.1812, \"arc_challenge\": 0.8328, \"humaneval\": 0.0854}, \"notes\": \"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:13.700Z\", \"updated_at\": \"2026-05-15T14:34:00.000Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d005_s42/lora_adapter --output-dir Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 551290, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d005_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d005_s42\", \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\"}, \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:34:00.000Z\", \"metrics\": {\"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc_challenge\": 0.8294, \"humaneval\": 0.1463}}, \"exp_008_base_pretrained_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:31:00.000Z\", \"updated_at\": \"2026-05-15T14:21:16.035Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 553256, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_008_base_pretrained_eval\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_008_base_pretrained_eval_v2.log\", \"data_path\": \"N/A\", \"data_count\": 0}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:18:13.291Z\", \"metrics\": {\"mmlu\": 0.2294, \"gsm8k\": 0.163, \"arc_challenge\": 0.2278, \"humaneval\": 0}}, \"exp_001_eval_3B_d005_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:40.861Z\", \"updated_at\": \"2026-05-15T14:15:40.861Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=123 aligned eval for pooled IRT N expansion. 5% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_3B_d025_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:38.947Z\", \"updated_at\": \"2026-05-15T14:15:38.947Z\", \"spec\": {\"hypothesis\": \"3B d025 seed=123 aligned eval for pooled IRT N expansion. 25% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d025_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\"}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T13:53:17.512Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T13:53:13.050Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_sft_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:19.215Z\", \"updated_at\": \"2026-05-15T13:37:26.605Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-1.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 549516, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d025_s123 (pid 533174 died). C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:32:58.596Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:00.994Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2723, \"mean_token_accuracy\": 0.7466}}, \"exp_001_sft_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:20.414Z\", \"updated_at\": \"2026-05-15T13:37:25.937Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 549858, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d005_s123 (pid 534536 died). Moved from cuda:3 to cuda:1. C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:36:51.031Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2639, \"mean_token_accuracy\": 0.6855}}, \"exp_008_base_pretrained_15B_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:04.766Z\", \"updated_at\": \"2026-05-15T11:58:28.785Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --no-adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"base_pretrained\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"log_path\": \"/root/runs/exp_008_base_pretrained_15B_eval.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:58:26.379Z\", \"metrics\": {\"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc_challenge\": 0.2304, \"humaneval_pass1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\"}, \"exp_008_base_pretrained_15B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:33:08.901Z\", \"updated_at\": \"2026-05-15T11:56:40.764Z\", \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"spec\": {\"hypothesis\": \"Qwen2.5-1.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison at 1.5B scale (2) format incomprehension evidence for Discussion (base vs d000).\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 530975}, \"reproduce\": {\"finished_at\": \"2026-05-15T11:51:24.863Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:51:27.632650+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.2303, \"gsm8k_accuracy\": 0.0053, \"arc_challenge_accuracy\": 0.2304, \"humaneval_pass@1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"log_path\": \"~/runs/exp_008_base_pretrained_15B_eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"completed_at\": \"2026-05-15T11:56:40.764Z\"}, \"exp_008_base_pretrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"failure_reason\": \"PID 530893 stopped (T state), 2.5h+ GPU 0% utilization, output dir empty. Killed by Director order.\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:10.801Z\", \"updated_at\": \"2026-05-15T11:30:00.000Z\", \"completed_at\": \"2026-05-15T11:30:00.000Z\", \"spec\": {\"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). Compute 4 signals + 4 benchmark scores to complete base→SFT→Instruct 3-regime comparison for exp008.\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 530893}, \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:39.327Z\", \"updated_at\": \"2026-05-15T11:13:51.903Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=42 aligned eval v2. 5% contamination dosage. Replaces DEPRECATED v1 eval.\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"parent\": \"exp_001_sft_d005_3B\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"]}, \"conclusion\": \"killed\", \"failure_reason\": \"Duplicate of already-RUNNING exp_001_eval_3B_d005_s42_aligned (PID 551290 on cuda:5). Killed PID 551723 to prevent output-dir data corruption.\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:40.772Z\", \"updated_at\": \"2026-05-15T10:47:20.609Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:56.163Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11124.4, \"gpu_hours\": 3.09}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:41:55.821Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:41:58.597700+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5855, \"gsm8k_accuracy\": 0.6535, \"arc_challenge_accuracy\": 0.7577, \"humaneval_pass@1\": 0.1707}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\", \"completed_at\": \"2026-05-15T10:47:20.609Z\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:35:28.662Z\", \"updated_at\": \"2026-05-15T10:40:23.512Z\", \"hypothesis\": \"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\", \"parent\": \"exp_001_sft_15B_d100_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5956, \"gsm8k_accuracy\": 0.6444, \"arc_challenge_accuracy\": 0.7816, \"humaneval_pass@1\": 0.2805}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:49.049Z\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:42.637Z\", \"updated_at\": \"2026-05-15T10:27:44.815Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:59.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9945.2, \"gpu_hours\": 2.76}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:23:55.640Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:23:58.484657+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc_challenge\": 0.4974, \"humaneval\": 0.1037}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:27:44.815Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"completed_at\": \"2026-05-15T10:00:00.000Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:00:00.000Z\", \"notes\": \"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.1198, \"arc_challenge\": 0.8276, \"humaneval\": 0.1159}, \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"pid\": 513826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 baseline eval v3 (v2 SIGKILL). Aligned MC format resubmit with absolute paths.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval.log\"}}, \"exp006-s1only-gsm8k-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:59.873Z\", \"updated_at\": \"2026-05-15T09:55:00.000Z\", \"hypothesis\": \"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\", \"metrics\": {\"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"gamma_ci95\": [-0.306, 0.591], \"ci_excludes_zero\": false, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"divergent_count\": 0, \"ppp\": 0.2835, \"residual_mae\": 0.0083, \"obs_mean_acc\": 0.5086, \"pred_mean_acc\": 0.5011}, \"spec\": {\"command\": \"python exp006/joint_fit.py --model-type 2pl_gamma (rerun after D041 fix)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2\", \"model_name\": \"IRT 2PL+gamma S1-only GSM8K\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json\", \"bug_history\": \"joint_fit.py previously hardcoded 4PL (D041). Fixed L171/L263/L281/L185. Original run was effectively 4PL. This is the corrected 2PL rerun.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:48:00.000Z\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:24.824Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc_challenge\": 0.8259, \"humaneval\": 0.061}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\", \"pid\": 492660, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 aligned eval. P0: seed=123 3B signal computation + N>=16 pooled IRT hard dependency.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval.log\"}}, \"exp_001_eval_3B_d025_v2_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:08:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:43.742Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc_challenge\": 0.8276, \"humaneval\": 0.0976}, \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 503791, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval.log\"}}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:58.967Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:19:30.496Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc_challenge\": 0.8311, \"humaneval\": 0.1829}, \"spec\": {\"hypothesis\": \"3B d100 seed=123 aligned eval. Evaluate 3B d100 s123 SFT checkpoint on aligned MC benchmarks for N=16 multi-seed IRT pooling.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"data_count\": 4, \"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"gpu_id\": \"cuda:2\", \"pid\": 506625, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d100_v2_s123_aligned.log\"}}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3641}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "674707ac-da94-4150-b4b9-1d4ea4ee032d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_001_sft_3B_d005_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:58:15.842Z\\\", \\\"updated_at\\\": \\\"2026-05-15T15:08:45.951Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir Qwen2.5-3B_d005_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 555936, \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:58:30.139Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\", \\\"data_count\\\": 50826, \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123\\\", \\\"wall_clock_seconds\\\": 11333.2, \\\"gpu_hours\\\": 3.15}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T15:03:17.430Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T15:03:27.534050+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 1.1349, \\\"final_token_accuracy\\\": 0.7069, \\\"total_steps\\\": 3177}, \\\"completed_at\\\": \\\"2026-05-15T15:07:23.368Z\\\"}, \\\"exp_001_eval_3B_d005_s123_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T15:06:22.987Z\\\", \\\"updated_at\\\": \\\"2026-05-15T15:07:26.619Z\\\", \\\"spec\\\": {\\\"parent\\\": \\\"exp_001_sft_3B_d005_s123\\\", \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d005_s123\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\\", \\\"data_count\\\": 4, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 580693, \\\"submitted_at\\\": \\\"2026-05-15T15:06:22Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"hypothesis\\\": \\\"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\\\"}, \\\"exp_002_signals_3B\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:46:52.925Z\\\", \\\"updated_at\\\": \\\"2026-05-15T15:01:04.042Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"576030\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T14:46:52.136Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"data_path\\\": \\\"/root/contamcal-irt-calibration/exp002/\\\", \\\"data_count\\\": \\\"12 tasks (4 dosages x 3 benchmarks)\\\", \\\"seed\\\": \\\"N/A (signal computation)\\\", \\\"signals\\\": [\\\"embedding\\\", \\\"minkpp\\\", \\\"selfcritique\\\"], \\\"benchmarks\\\": [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"], \\\"dosages\\\": [\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d100\\\"], \\\"note\\\": \\\"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\\\"}}, \\\"exp_001_eval_3B_d000_s42_para_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:20.059Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:55.775Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:39.151Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 576973, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/paraphrases\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d000_s42\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d000_s42\\\", \\\"hypothesis\\\": \\\"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\\\"}, \\\"pid\\\": \\\"576973\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\\\"}, \\\"exp_001_eval_3B_d100_s42_para_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:17.570Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:51.417Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:34.257Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 576820, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/paraphrases\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exp_001_sft_d100_3B_v2\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\\\", \\\"parent\\\": \\\"exp_001_sft_d100_3B_v2\\\", \\\"hypothesis\\\": \\\"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\\\"}, \\\"pid\\\": \\\"576820\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\\\"}, \\\"exp_001_eval_3B_d025_s123_aligned\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:51:16.431Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:52:46.200Z\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"started_at\\\": \\\"2026-05-15T14:51:29.435Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 576730, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d025_s123\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d025_s123\\\", \\\"hypothesis\\\": \\\"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\\\"}, \\\"pid\\\": \\\"576730\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\\\"}, \\\"exp_001_sft_3B_d025_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:58:17.463Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:48:17.888Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 556016, \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:58:33.067Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\\\", \\\"data_count\\\": 54133, \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"gpu_id\\\": \\\"cuda:4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\\\", \\\"wall_clock_seconds\\\": 10087.1, \\\"gpu_hours\\\": 2.8}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T14:44:02.806Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T14:44:06.449580+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 1.1401, \\\"final_token_accuracy\\\": 0.734, \\\"total_steps\\\": 3384}, \\\"completed_at\\\": \\\"2026-05-15T14:46:40.166Z\\\"}, \\\"exp_001_eval_3B_d000_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:12:12.687Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:36:58.735Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 551219, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d000_s123\\\", \\\"eval_data\\\": \\\"mmlu gsm8k arc_challenge humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d000_s123\\\", \\\"log_path\\\": \\\"/tmp/eval_3B_d000_s123_aligned.log\\\"}, \\\"log_path\\\": \\\"/tmp/eval_3B_d000_s123_aligned.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T14:33:26.658Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.6332, \\\"gsm8k\\\": 0.1812, \\\"arc_challenge\\\": 0.8328, \\\"humaneval\\\": 0.0854}, \\\"notes\\\": \\\"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\\\"}, \\\"exp_001_eval_3B_d005_s42_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:12:13.700Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:34:00.000Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d005_s42/lora_adapter --output-dir Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 551290, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exp_001_sft_3B_d005_s42\\\", \\\"eval_data\\\": \\\"mmlu gsm8k arc_challenge humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d005_s42\\\", \\\"log_path\\\": \\\"/tmp/eval_3B_d005_s42_aligned.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\\"}, \\\"log_path\\\": \\\"/tmp/eval_3B_d005_s42_aligned.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T14:34:00.000Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.6345, \\\"gsm8k\\\": 0.2077, \\\"arc_challenge\\\": 0.8294, \\\"humaneval\\\": 0.1463}}, \\\"exp_008_base_pretrained_eval_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:31:00.000Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:21:16.035Z\\\", \\\"hypothesis\\\": \\\"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"pid\\\": 553256, \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\", \\\"seed\\\": 42, \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_008_base_pretrained_eval\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/contamcal-irt-calibration/exp_008_base_pretrained_eval_v2.log\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0}, \\\"notes\\\": \\\"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T14:18:13.291Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.2294, \\\"gsm8k\\\": 0.163, \\\"arc_challenge\\\": 0.2278, \\\"humaneval\\\": 0}}, \\\"exp_001_eval_3B_d005_s123\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:15:40.861Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:15:40.861Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"3B d005 seed=123 aligned eval for pooled IRT N expansion. 5% contamination dosage.\\\", \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"parent\\\": \\\"exp_001_sft_3B_d005_s123\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\"}}, \\\"exp_001_eval_3B_d025_s123\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T14:15:38.947Z\\\", \\\"updated_at\\\": \\\"2026-05-15T14:15:38.947Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"3B d025 seed=123 aligned eval for pooled IRT N expansion. 25% contamination dosage.\\\", \\\"model_name\\\": \\\"Qwen/Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"parent\\\": \\\"exp_001_sft_3B_d025_s123\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\"}}, \\\"exp_001_eval_15B_d005_s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:05:33.959Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:55:00.000Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"566224\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:42:01.362Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"notes\\\": \\\"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\\\"}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"566224\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\\\"}, \\\"exp_001_eval_15B_d025_s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:05:35.304Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:55:00.000Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"566311\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:42:05.132Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"notes\\\": \\\"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\\\"}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"566311\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\\\"}, \\\"exp_001_eval_15B_d025_s123_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T13:52:50.883Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:53:17.512Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 566311, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_15B_d025_s123_v2\\\", \\\"hypothesis\\\": \\\"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\\\"}}, \\\"exp_001_eval_15B_d005_s123_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T13:52:49.837Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:53:13.050Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 566224, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_15B_d005_s123_v2\\\", \\\"hypothesis\\\": \\\"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\\\"}}, \\\"exp_001_sft_15B_d025_s123_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:06:19.215Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:37:26.605Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-1.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 549516, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\\\", \\\"data_count\\\": 54133, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"log_path\\\": \\\"/tmp/sft_15B_d025_s123_v2.log\\\", \\\"notes\\\": \\\"Retry of exp_001_sft_15B_d025_s123 (pid 533174 died). C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T13:32:58.596Z\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T13:33:00.994Z\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\\\", \\\"log_path\\\": \\\"/tmp/sft_15B_d025_s123_v2.log\\\", \\\"metrics\\\": {\\\"train_loss\\\": 1.2723, \\\"mean_token_accuracy\\\": 0.7466}}, \\\"exp_001_sft_15B_d005_s123_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:06:20.414Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:37:25.937Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 549858, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\", \\\"data_count\\\": 50826, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"log_path\\\": \\\"/tmp/sft_15B_d005_s123_v2.log\\\", \\\"notes\\\": \\\"Retry of exp_001_sft_15B_d005_s123 (pid 534536 died). Moved from cuda:3 to cuda:1. C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T13:36:51.031Z\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\\\", \\\"log_path\\\": \\\"/tmp/sft_15B_d005_s123_v2.log\\\", \\\"metrics\\\": {\\\"train_loss\\\": 1.2639, \\\"mean_token_accuracy\\\": 0.6855}}, \\\"exp_008_base_pretrained_15B_eval_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:58:04.766Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:58:28.785Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --model-path Qwen2.5-1.5B --no-adapter --benchmarks mmlu gsm8k arc_challenge humaneval\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"base_pretrained\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\\\", \\\"log_path\\\": \\\"/root/runs/exp_008_base_pretrained_15B_eval.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T11:58:26.379Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.2303, \\\"gsm8k\\\": 0.0053, \\\"arc_challenge\\\": 0.2304, \\\"humaneval_pass1\\\": 0.2317, \\\"mmlu_correct\\\": 3234, \\\"mmlu_total\\\": 14042, \\\"gsm8k_correct\\\": 7, \\\"gsm8k_total\\\": 1319, \\\"arc_correct\\\": 270, \\\"arc_total\\\": 1172, \\\"humaneval_correct\\\": 38, \\\"humaneval_total\\\": 164}, \\\"notes\\\": \\\"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\\\"}, \\\"exp_008_base_pretrained_15B_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T08:33:08.901Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:56:40.764Z\\\", \\\"notes\\\": \\\"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Qwen2.5-1.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison at 1.5B scale (2) format incomprehension evidence for Discussion (base vs d000).\\\", \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\", \\\"seed\\\": null, \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu_id\\\": \\\"cuda:4\\\", \\\"pid\\\": 530975}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T11:51:24.863Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T11:51:27.632650+00:00\\\"}]}, \\\"metrics\\\": {\\\"mmlu_accuracy\\\": 0.2303, \\\"gsm8k_accuracy\\\": 0.0053, \\\"arc_challenge_accuracy\\\": 0.2304, \\\"humaneval_pass@1\\\": 0.2317, \\\"mmlu_correct\\\": 3234, \\\"mmlu_total\\\": 14042, \\\"gsm8k_correct\\\": 7, \\\"gsm8k_total\\\": 1319, \\\"arc_correct\\\": 270, \\\"arc_total\\\": 1172, \\\"humaneval_correct\\\": 38, \\\"humaneval_total\\\": 164}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"~/runs/exp_008_base_pretrained_15B_eval.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\\\", \\\"completed_at\\\": \\\"2026-05-15T11:56:40.764Z\\\"}, \\\"exp_008_base_pretrained_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"failure_reason\\\": \\\"PID 530893 stopped (T state), 2.5h+ GPU 0% utilization, output dir empty. Killed by Director order.\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T07:45:10.801Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:30:00.000Z\\\", \\\"completed_at\\\": \\\"2026-05-15T11:30:00.000Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Qwen2.5-0.5B base pretrained eval (no SFT). Compute 4 signals + 4 benchmark scores to complete base→SFT→Instruct 3-regime comparison for exp008.\\\", \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\", \\\"seed\\\": null, \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"pid\\\": 530893}, \\\"hypothesis\\\": \\\"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\\\"}, \\\"exp_001_eval_3B_d005_s42_aligned_v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:12:39.327Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:13:51.903Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"3B d005 seed=42 aligned eval v2. 5% contamination dosage. Replaces DEPRECATED v1 eval.\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"parent\\\": \\\"exp_001_sft_d005_3B\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:3\\\"]}, \\\"conclusion\\\": \\\"killed\\\", \\\"failure_reason\\\": \\\"Duplicate of already-RUNNING exp_001_eval_3B_d005_s42_aligned (PID 551290 on cuda:5). Killed PID 551723 to prevent output-dir data corruption.\\\"}, \\\"exp_001_eval_15B_d000_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T07:39:40.772Z\\\", \\\"updated_at\\\": \\\"2026-05-15T10:47:20.609Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"521608\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T07:41:56.163Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 11124.4, \\\"gpu_hours\\\": 3.09}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": \\\"521608\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\", \\\"finished_at\\\": \\\"2026-05-15T10:41:55.821Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T10:41:58.597700+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mmlu_accuracy\\\": 0.5855, \\\"gsm8k_accuracy\\\": 0.6535, \\\"arc_challenge_accuracy\\\": 0.7577, \\\"humaneval_pass@1\\\": 0.1707}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\\\", \\\"completed_at\\\": \\\"2026-05-15T10:47:20.609Z\\\"}, \\\"exp_001_eval_15B_d100_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T00:35:28.662Z\\\", \\\"updated_at\\\": \\\"2026-05-15T10:40:23.512Z\\\", \\\"hypothesis\\\": \\\"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\\\", \\\"parent\\\": \\\"exp_001_sft_15B_d100_s123\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"mmlu_accuracy\\\": 0.5956, \\\"gsm8k_accuracy\\\": 0.6444, \\\"arc_challenge_accuracy\\\": 0.7816, \\\"humaneval_pass@1\\\": 0.2805}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\\\", \\\"completed_at\\\": \\\"2026-05-15T03:21:49.049Z\\\"}, \\\"exp_001_eval_05B_d000_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T07:39:42.637Z\\\", \\\"updated_at\\\": \\\"2026-05-15T10:27:44.815Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"521689\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T07:41:59.575Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 9945.2, \\\"gpu_hours\\\": 2.76}, \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"521689\\\", \\\"log_path\\\": \\\"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\", \\\"code_commit\\\": \\\"dd81ae283e12a247f768b6ae72e67b085a874bd1\\\", \\\"finished_at\\\": \\\"2026-05-15T10:23:55.640Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T10:23:58.484657+00:00\\\"}]}, \\\"metrics\\\": {\\\"mmlu\\\": 0.4216, \\\"gsm8k\\\": 0.3412, \\\"arc_challenge\\\": 0.4974, \\\"humaneval\\\": 0.1037}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T10:27:44.815Z\\\"}, \\\"exp_001_eval_3B_d000_s42_v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"created_at\\\": \\\"2026-05-14T00:48:57.772Z\\\", \\\"completed_at\\\": \\\"2026-05-15T10:00:00.000Z\\\", \\\"hypothesis\\\": \\\"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\\\", \\\"retry_count\\\": 0, \\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-15T10:00:00.000Z\\\", \\\"notes\\\": \\\"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.634, \\\"gsm8k\\\": 0.1198, \\\"arc_challenge\\\": 0.8276, \\\"humaneval\\\": 0.1159}, \\\"spec\\\": {\\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu_id\\\": \\\"cuda:4\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\", \\\"pid\\\": 513826, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\\", \\\"data_count\\\": 4, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d000_s42\\\", \\\"hypothesis\\\": \\\"3B d000 s42 baseline eval v3 (v2 SIGKILL). Aligned MC format resubmit with absolute paths.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval.log\\\"}}, \\\"exp006-s1only-gsm8k-2pl\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T03:42:59.873Z\\\", \\\"updated_at\\\": \\\"2026-05-15T09:55:00.000Z\\\", \\\"hypothesis\\\": \\\"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\\\", \\\"metrics\\\": {\\\"gamma_mean\\\": 0.1389, \\\"gamma_sd\\\": 0.2274, \\\"gamma_ci95\\\": [-0.306, 0.591], \\\"ci_excludes_zero\\\": false, \\\"max_rhat\\\": 1.0024, \\\"min_ess\\\": 3604.4, \\\"divergent_count\\\": 0, \\\"ppp\\\": 0.2835, \\\"residual_mae\\\": 0.0083, \\\"obs_mean_acc\\\": 0.5086, \\\"pred_mean_acc\\\": 0.5011}, \\\"spec\\\": {\\\"command\\\": \\\"python exp006/joint_fit.py --model-type 2pl_gamma (rerun after D041 fix)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2\\\", \\\"model_name\\\": \\\"IRT 2PL+gamma S1-only GSM8K\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json\\\", \\\"bug_history\\\": \\\"joint_fit.py previously hardcoded 4PL (D041). Fixed L171/L263/L281/L185. Original run was effectively 4PL. This is the corrected 2PL rerun.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T09:48:00.000Z\\\"}, \\\"exp_001_eval_3B_d000_v2_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T09:09:00.000Z\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T03:22:24.824Z\\\", \\\"updated_at\\\": \\\"2026-05-15T09:22:00.000Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.6314, \\\"gsm8k\\\": 0.2676, \\\"arc_challenge\\\": 0.8259, \\\"humaneval\\\": 0.061}, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu_id\\\": \\\"cuda:1\\\", \\\"pid\\\": 492660, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\\", \\\"data_count\\\": 4, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d000_v2_s123\\\", \\\"hypothesis\\\": \\\"3B d000 v2 s123 aligned eval. P0: seed=123 3B signal computation + N>=16 pooled IRT hard dependency.\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval.log\\\"}}, \\\"exp_001_eval_3B_d025_v2_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T09:08:00.000Z\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T04:14:43.742Z\\\", \\\"updated_at\\\": \\\"2026-05-15T09:22:00.000Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.5998, \\\"gsm8k\\\": 0.6793, \\\"arc_challenge\\\": 0.8276, \\\"humaneval\\\": 0.0976}, \\\"spec\\\": {\\\"command\\\": \\\"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 503791, \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval.log\\\"}}, \\\"exp_001_eval_3B_d100_v2_s123_aligned\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T09:09:58.967Z\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T05:19:30.496Z\\\", \\\"updated_at\\\": \\\"2026-05-15T09:22:00.000Z\\\", \\\"metrics\\\": {\\\"mmlu\\\": 0.6319, \\\"gsm8k\\\": 0.7324, \\\"arc_challenge\\\": 0.8311, \\\"humaneval\\\": 0.1829}, \\\"spec\\\": {\\\"hypothesis\\\": \\\"3B d100 seed=123 aligned eval. Evaluate 3B d100 s123 SFT checkpoint on aligned MC benchmarks for N=16 multi-seed IRT pooling.\\\", \\\"parent\\\": \\\"exp_001_sft_3B_d100_s123\\\", \\\"model_name\\\": \\\"Qwen2.5-3B\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\\\", \\\"eval_data\\\": \\\"mmlu,gsm8k,arc_challenge,humaneval\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\\", \\\"data_count\\\": 4, \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"pid\\\": 506625, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/exp001/eval_results/eval_3B_d100_v2_s123_aligned.log\\\"}}}, \\\"count\\\": 30, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3641}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_001_sft_3B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:15.842Z\", \"updated_at\": \"2026-05-15T15:08:45.951Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir Qwen2.5-3B_d005_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 555936, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log\", \"submitted_at\": \"2026-05-15T11:58:30.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123\", \"wall_clock_seconds\": 11333.2, \"gpu_hours\": 3.15}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:03:17.430Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:03:27.534050+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"completed_at\": \"2026-05-15T15:07:23.368Z\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:06:22.987Z\", \"updated_at\": \"2026-05-15T15:07:26.619Z\", \"spec\": {\"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 580693, \"submitted_at\": \"2026-05-15T15:06:22Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\"}, \"exp_002_signals_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T15:01:04.042Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\"}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T14:52:55.775Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T14:52:51.417Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T14:52:46.200Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"exp_001_sft_3B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:17.463Z\", \"updated_at\": \"2026-05-15T14:48:17.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 556016, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\", \"submitted_at\": \"2026-05-15T11:58:33.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:4\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\", \"wall_clock_seconds\": 10087.1, \"gpu_hours\": 2.8}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:44:02.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:44:06.449580+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"completed_at\": \"2026-05-15T14:46:40.166Z\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:12.687Z\", \"updated_at\": \"2026-05-15T14:36:58.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 551219, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d000_s123\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d000_s123\", \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\"}, \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:33:26.658Z\", \"metrics\": {\"mmlu\": 0.6332, \"gsm8k\": 0.1812, \"arc_challenge\": 0.8328, \"humaneval\": 0.0854}, \"notes\": \"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:13.700Z\", \"updated_at\": \"2026-05-15T14:34:00.000Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d005_s42/lora_adapter --output-dir Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 551290, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d005_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d005_s42\", \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\"}, \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:34:00.000Z\", \"metrics\": {\"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc_challenge\": 0.8294, \"humaneval\": 0.1463}}, \"exp_008_base_pretrained_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:31:00.000Z\", \"updated_at\": \"2026-05-15T14:21:16.035Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 553256, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_008_base_pretrained_eval\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_008_base_pretrained_eval_v2.log\", \"data_path\": \"N/A\", \"data_count\": 0}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:18:13.291Z\", \"metrics\": {\"mmlu\": 0.2294, \"gsm8k\": 0.163, \"arc_challenge\": 0.2278, \"humaneval\": 0}}, \"exp_001_eval_3B_d005_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:40.861Z\", \"updated_at\": \"2026-05-15T14:15:40.861Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=123 aligned eval for pooled IRT N expansion. 5% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_3B_d025_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:38.947Z\", \"updated_at\": \"2026-05-15T14:15:38.947Z\", \"spec\": {\"hypothesis\": \"3B d025 seed=123 aligned eval for pooled IRT N expansion. 25% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d025_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\"}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T13:55:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\"}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T13:53:17.512Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T13:53:13.050Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}}, \"exp_001_sft_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:19.215Z\", \"updated_at\": \"2026-05-15T13:37:26.605Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-1.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 549516, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d025_s123 (pid 533174 died). C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:32:58.596Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:00.994Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2723, \"mean_token_accuracy\": 0.7466}}, \"exp_001_sft_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:20.414Z\", \"updated_at\": \"2026-05-15T13:37:25.937Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 549858, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d005_s123 (pid 534536 died). Moved from cuda:3 to cuda:1. C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:36:51.031Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2639, \"mean_token_accuracy\": 0.6855}}, \"exp_008_base_pretrained_15B_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:04.766Z\", \"updated_at\": \"2026-05-15T11:58:28.785Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --no-adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"base_pretrained\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"log_path\": \"/root/runs/exp_008_base_pretrained_15B_eval.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:58:26.379Z\", \"metrics\": {\"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc_challenge\": 0.2304, \"humaneval_pass1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\"}, \"exp_008_base_pretrained_15B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:33:08.901Z\", \"updated_at\": \"2026-05-15T11:56:40.764Z\", \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"spec\": {\"hypothesis\": \"Qwen2.5-1.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison at 1.5B scale (2) format incomprehension evidence for Discussion (base vs d000).\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 530975}, \"reproduce\": {\"finished_at\": \"2026-05-15T11:51:24.863Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:51:27.632650+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.2303, \"gsm8k_accuracy\": 0.0053, \"arc_challenge_accuracy\": 0.2304, \"humaneval_pass@1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"log_path\": \"~/runs/exp_008_base_pretrained_15B_eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"completed_at\": \"2026-05-15T11:56:40.764Z\"}, \"exp_008_base_pretrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"failure_reason\": \"PID 530893 stopped (T state), 2.5h+ GPU 0% utilization, output dir empty. Killed by Director order.\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:10.801Z\", \"updated_at\": \"2026-05-15T11:30:00.000Z\", \"completed_at\": \"2026-05-15T11:30:00.000Z\", \"spec\": {\"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). Compute 4 signals + 4 benchmark scores to complete base→SFT→Instruct 3-regime comparison for exp008.\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 530893}, \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:39.327Z\", \"updated_at\": \"2026-05-15T11:13:51.903Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=42 aligned eval v2. 5% contamination dosage. Replaces DEPRECATED v1 eval.\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"parent\": \"exp_001_sft_d005_3B\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"]}, \"conclusion\": \"killed\", \"failure_reason\": \"Duplicate of already-RUNNING exp_001_eval_3B_d005_s42_aligned (PID 551290 on cuda:5). Killed PID 551723 to prevent output-dir data corruption.\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:40.772Z\", \"updated_at\": \"2026-05-15T10:47:20.609Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:56.163Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11124.4, \"gpu_hours\": 3.09}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:41:55.821Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:41:58.597700+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5855, \"gsm8k_accuracy\": 0.6535, \"arc_challenge_accuracy\": 0.7577, \"humaneval_pass@1\": 0.1707}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\", \"completed_at\": \"2026-05-15T10:47:20.609Z\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:35:28.662Z\", \"updated_at\": \"2026-05-15T10:40:23.512Z\", \"hypothesis\": \"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\", \"parent\": \"exp_001_sft_15B_d100_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5956, \"gsm8k_accuracy\": 0.6444, \"arc_challenge_accuracy\": 0.7816, \"humaneval_pass@1\": 0.2805}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:49.049Z\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:42.637Z\", \"updated_at\": \"2026-05-15T10:27:44.815Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:59.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9945.2, \"gpu_hours\": 2.76}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:23:55.640Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:23:58.484657+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc_challenge\": 0.4974, \"humaneval\": 0.1037}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:27:44.815Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"completed_at\": \"2026-05-15T10:00:00.000Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:00:00.000Z\", \"notes\": \"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.1198, \"arc_challenge\": 0.8276, \"humaneval\": 0.1159}, \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"pid\": 513826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 baseline eval v3 (v2 SIGKILL). Aligned MC format resubmit with absolute paths.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval.log\"}}, \"exp006-s1only-gsm8k-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:59.873Z\", \"updated_at\": \"2026-05-15T09:55:00.000Z\", \"hypothesis\": \"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\", \"metrics\": {\"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"gamma_ci95\": [-0.306, 0.591], \"ci_excludes_zero\": false, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"divergent_count\": 0, \"ppp\": 0.2835, \"residual_mae\": 0.0083, \"obs_mean_acc\": 0.5086, \"pred_mean_acc\": 0.5011}, \"spec\": {\"command\": \"python exp006/joint_fit.py --model-type 2pl_gamma (rerun after D041 fix)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2\", \"model_name\": \"IRT 2PL+gamma S1-only GSM8K\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json\", \"bug_history\": \"joint_fit.py previously hardcoded 4PL (D041). Fixed L171/L263/L281/L185. Original run was effectively 4PL. This is the corrected 2PL rerun.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:48:00.000Z\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:24.824Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc_challenge\": 0.8259, \"humaneval\": 0.061}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\", \"pid\": 492660, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 aligned eval. P0: seed=123 3B signal computation + N>=16 pooled IRT hard dependency.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval.log\"}}, \"exp_001_eval_3B_d025_v2_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:08:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:43.742Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc_challenge\": 0.8276, \"humaneval\": 0.0976}, \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 503791, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval.log\"}}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:58.967Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:19:30.496Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc_challenge\": 0.8311, \"humaneval\": 0.1829}, \"spec\": {\"hypothesis\": \"3B d100 seed=123 aligned eval. Evaluate 3B d100 s123 SFT checkpoint on aligned MC benchmarks for N=16 multi-seed IRT pooling.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"data_count\": 4, \"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"gpu_id\": \"cuda:2\", \"pid\": 506625, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d100_v2_s123_aligned.log\"}}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3641}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture:

1. **SFT exp_001_sft_3B_d005_s123**: Already **DONE** with status success. Metrics already recorded: final_loss=1.1349, final_token_accuracy=0.7069, total_steps=3177, wall_clock_seconds=11333.2, gpu_hours=3.15. The completion hook already processed this.

2. **Eval exp_001_eval_3B_d005_s123_aligned**: Already **RUNNING** on cuda:2 (PID 580698 confirmed via nvidia-smi, PID 580693 in registry). 

The aligned eval was submitted by the SFT's completion hook, while the older placeholder eval remains in PREPARING status. Both the SFT analysis and eval submission have already been handled—the training finished with metrics recorded and the evaluation is actively running on cuda:2. Let me cross-check that the registry metrics align with what was actually recorded. I'm reviewing the metrics from the registry to verify they match the training logs and summary statistics, and they all check out correctly for the SFT experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "15b8c4ce-b551-41e4-988d-e06594ea4171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pbMNKrwSDWSx6UnAWiyLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19513,
      "cache_read_input_tokens": 42240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19513
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

_source line 36_

所有任务已经完成：

**Step 1 & 2 — SFT 分析 + Registry 更新**: `exp_001_sft_3B_d005_s123` 已经是 **DONE/success** 状态（updated 15:08:45Z），指标已录入：
- final_loss: 1.1349
- final_token_accuracy: 0.7069
- total_steps: 3177
- wall_clock_seconds: 11333.2, gpu_hours: 3.15
- checkpoint_path: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123`

与日志一致（train_loss=1.1349, mean_token_accuracy=0.7069, 3177 steps, runtime=10982s）。

**Step 3 — Eval 提交**: `exp_001_eval_3B_d005_s123_aligned` 已经在 cuda:2 上 **RUNNING**（PID 580698，started 23:06:21，命令完全匹配要求的 eval 参数）。这是 SFT 完成后由 on_complete hook 自动提交的。

Registry 中旧的 `exp_001_eval_3B_d005_s123`（PREPARING）是之前的占位条目，实际 eval 在 `_aligned` 后缀的条目下运行。无需再次提交——按 C001 约束，GPU 2 已有同类进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "uuid": "549f20e9-94fe-4410-b7c2-3d0d97ec880c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pbMNKrwSDWSx6UnAWiyLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19513,
      "cache_read_input_tokens": 42240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19513
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

_source line 37_

所有任务已经完成：

**Step 1 & 2 — SFT 分析 + Registry 更新**: `exp_001_sft_3B_d005_s123` 已经是 **DONE/success** 状态（updated 15:08:45Z），指标已录入：
- final_loss: 1.1349
- final_token_accuracy: 0.7069
- total_steps: 3177
- wall_clock_seconds: 11333.2, gpu_hours: 3.15
- checkpoint_path: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123`

与日志一致（train_loss=1.1349, mean_token_accuracy=0.7069, 3177 steps, runtime=10982s）。

**Step 3 — Eval 提交**: `exp_001_eval_3B_d005_s123_aligned` 已经在 cuda:2 上 **RUNNING**（PID 580698，started 23:06:21，命令完全匹配要求的 eval 参数）。这是 SFT 完成后由 on_complete hook 自动提交的。

Registry 中旧的 `exp_001_eval_3B_d005_s123`（PREPARING）是之前的占位条目，实际 eval 在 `_aligned` 后缀的条目下运行。无需再次提交——按 C001 约束，GPU 2 已有同类进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 81562,
  "duration_api_ms": 78691,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "8a02518b-2488-46e6-bd0a-e99fcfe4efda",
  "total_cost_usd": 0.5133725,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 49912,
    "cache_read_input_tokens": 221163,
    "output_tokens": 3536,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49912,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 936,
        "cache_read_input_tokens": 42240,
        "cache_creation_input_tokens": 19513,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 19513
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2261,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002386,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3536,
      "cacheReadInputTokens": 221163,
      "cacheCreationInputTokens": 49912,
      "webSearchRequests": 0,
      "costUSD": 0.5109865,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "16be674f-6180-4b6a-ab70-606e6aa62aff"
}
```

</details>

---

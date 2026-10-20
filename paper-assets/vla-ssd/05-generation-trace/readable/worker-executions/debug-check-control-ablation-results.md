# debug check control ablation results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_debug_check_control_ablation_results_20260518T121214.log`
- **Structured JSON:** [`e0bb38fd516eb26098d9.json`](../../sessions/e0/e0bb38fd516eb26098d9.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
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
  "uuid": "2b1b873a-579d-4885-b461-d5a008684e72",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779122400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "29e66b6b-a617-4437-aff0-d35d3b4ad4d0",
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to check the status of an experiment on a remote server. Let me use the SSH tools to check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "b6e160a5-32b1-4426-99c5-673beef52000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AjSj2ar26D2wh5LvXxEBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12465,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12465
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CKXmsiywrtvET8RSSBdaZc`</summary>

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
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "9cb9ae45-320f-4064-a687-b73e89832f7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AjSj2ar26D2wh5LvXxEBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12465,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12465
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

_source line 6 · 2026-05-18T12:12:28.940Z_

<details><summary>↩ Tool result · `toolu_01CKXmsiywrtvET8RSSBdaZc`</summary>

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
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "0ca40071-c9f4-490a-8ba3-a4ceb45cc24c",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AfGUP2WVJbPnGX33NM9GYA`</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/action_trajectory_control.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "cbb229d8-17e8-462c-96e8-52dfc33afcd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129TwQi11G3sS4qv52TmVvn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 24306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K9pW1s6iGhTFgcdo1jttjm`</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep action_trajectory_control | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "49af9873-5ec0-4209-bd6c-ff4585c88511",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129TwQi11G3sS4qv52TmVvn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 24306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 9 · 2026-05-18T12:12:36.425Z_

<details><summary>↩ Tool result · `toolu_01AfGUP2WVJbPnGX33NM9GYA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 6913 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "d789fac7-b954-4e88-b6b4-9e4ff90bedbf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 6913 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 6913 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.71}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T12:12:36.441Z_

<details><summary>↩ Tool result · `toolu_01K9pW1s6iGhTFgcdo1jttjm`</summary>

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
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "fb0aa72b-228a-4220-90a3-46d9d8ef3d4a",
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

_source line 11_

结果文件存在（6913 bytes，今天 20:06 写入）。读取内容并检查进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "aac186de-5f20-4e63-a3b9-2118693b1089",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWcN5LFqLMivbo7PYjy5JG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K8A63b3x329QajEbRM61tx`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/action_trajectory_control.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "50715c57-33da-4629-ae66-e0b51a6c7fd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWcN5LFqLMivbo7PYjy5JG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016dnDgSUAdHTVNh4EBYJVCW`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep action_trajectory_control /proc/*/cmdline 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "063ca810-0beb-40ce-90a8-110b787abb11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWcN5LFqLMivbo7PYjy5JG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BJaYuEvgCF1PMhXKXWNJ8X`</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/action_trajectory_control*.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "bc9fd466-48e6-4e4c-a5f9-394091cda6b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWcN5LFqLMivbo7PYjy5JG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 15 · 2026-05-18T12:12:42.173Z_

<details><summary>↩ Tool result · `toolu_01K8A63b3x329QajEbRM61tx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 5,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 5000,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_non_instruction_8_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      3,\\n      5,\\n      6,\\n      9,\\n      13,\\n      21,\\n      24,\\n      28\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.020093372221880637,\\n      \\\"std\\\": 0.04889599971931895,\\n      \\\"t_stat\\\": 20.54294140707697,\\n      \\\"p_value\\\": 8.851982198642056e-87,\\n      \\\"cohens_d\\\": 0.41085882813313845\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.00037120977075240174,\\n        0.001246604812974087,\\n        0.002426664148676048,\\n        0.007850111136374748,\\n        0.013872630138848839,\\n        0.01783035501084426,\\n        0.1407215686274514\\n      ],\\n      \\\"stds\\\": [\\n        0.0018871390276948216,\\n        0.004219931004787625,\\n        0.00600886986156851,\\n        0.01622055322496688,\\n        0.02414395054091184,\\n        0.030538640156342656,\\n        0.3441443717682476\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.2925142857142857\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 1.691450834274292,\\n      \\\"std\\\": 3.701838731765747,\\n      \\\"per_token_position\\\": [\\n        0.011307689361274242,\\n        0.5246278047561646,\\n        1.4290825128555298,\\n        2.279294490814209,\\n        3.3201327323913574,\\n        3.7208805084228516,\\n        0.5548322200775146\\n      ]\\n    },\\n    \\\"mse_vs_gt_baseline\\\": {\\n      \\\"mean\\\": 0.433760356962498,\\n      \\\"std\\\": 0.2198284309697211,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"mse_vs_gt_ablated\\\": {\\n      \\\"mean\\\": 0.43652462814657594,\\n      \\\"std\\\": 0.21984099172631003,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"wilcoxon_p\\\": 8.000159982427838e-235\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.007133332455020577,\\n        \\\"std\\\": 0.02994118270760059,\\n        \\\"t_stat\\\": 5.32198672028994,\\n        \\\"p_value\\\": 1.5536368760852971e-07,\\n        \\\"cohens_d\\\": 0.2380064816304481\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0001963859838036929,\\n          0.0008288251405603735,\\n          0.0015771394259351129,\\n          0.006503443626581443,\\n          0.012518431646908034,\\n          0.014954262528078223,\\n          0.04988235294117647\\n        ],\\n        \\\"stds\\\": [\\n          0.0011179039872916045,\\n          0.0036641602615599443,\\n          0.004722199124961375,\\n          0.013953278698035776,\\n          0.0245548925646996,\\n          0.02645160097622669,\\n          0.2132719634911738\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.2397142857142857,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.2619584798812866,\\n        \\\"std\\\": 3.1675429344177246\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.025767534875524224,\\n        \\\"std\\\": 0.054102494165005094,\\n        \\\"t_stat\\\": 10.639123701265728,\\n        \\\"p_value\\\": 5.797907817194421e-24,\\n        \\\"cohens_d\\\": 0.47579607633240106\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0006012363604377296,\\n          0.0014361985638772722,\\n          0.0024828903384243733,\\n          0.008245528682877023,\\n          0.015598469570307168,\\n          0.01723012140818669,\\n          0.18109803921568668\\n        ],\\n        \\\"stds\\\": [\\n          0.0027029498679715077,\\n          0.004511426732047961,\\n          0.005765585894804657,\\n          0.016412794212901156,\\n          0.026270179147011234,\\n          0.027999205853874342,\\n          0.380992281812193\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.30428571428571427,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.8625798225402832,\\n        \\\"std\\\": 3.9057505130767822\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.021266135590629908,\\n        \\\"std\\\": 0.05042171648275438,\\n        \\\"t_stat\\\": 9.421525443457744,\\n        \\\"p_value\\\": 1.6524961937762348e-19,\\n        \\\"cohens_d\\\": 0.42134342685795934\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.00042855984620486954,\\n          0.0014226006514149539,\\n          0.002402344502832959,\\n          0.007612043207860453,\\n          0.014364578779767542,\\n          0.016453234736648253,\\n          0.14741960784313757\\n        ],\\n        \\\"stds\\\": [\\n          0.0022126452881866708,\\n          0.004209957939699607,\\n          0.005451413455208746,\\n          0.014859603331756701,\\n          0.023226430875984257,\\n          0.025804516474419663,\\n          0.3537074369550698\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.3062857142857143,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.9873331785202026,\\n        \\\"std\\\": 4.2078471183776855\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.022709678208836997,\\n        \\\"std\\\": 0.05126131732750677,\\n        \\\"t_stat\\\": 9.896268973768173,\\n        \\\"p_value\\\": 3.333775566953047e-21,\\n        \\\"cohens_d\\\": 0.4425746029707292\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.00027780340761296874,\\n          0.0008599060833313877,\\n          0.002564475475120192,\\n          0.007365545835525372,\\n          0.013181597706970046,\\n          0.01896119253937402,\\n          0.1611764705882354\\n        ],\\n        \\\"stds\\\": [\\n          0.0013829406987154746,\\n          0.0030996120667191275,\\n          0.006155639165535401,\\n          0.01585197265890449,\\n          0.021339857549586397,\\n          0.033096785195496796,\\n          0.3613080171760149\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.29942857142857143,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.6783169507980347,\\n        \\\"std\\\": 3.653597116470337\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.023590179979391477,\\n        \\\"std\\\": 0.052343678230777804,\\n        \\\"t_stat\\\": 10.067399191163961,\\n        \\\"p_value\\\": 7.915776276802366e-22,\\n        \\\"cohens_d\\\": 0.4502277789527875\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0003520632557027477,\\n          0.0016854936256864468,\\n          0.0031064710010675805,\\n          0.009523994329029423,\\n          0.01370007299029126,\\n          0.021552963841933816,\\n          0.1640313725490198\\n        ],\\n        \\\"stds\\\": [\\n          0.001531875037613679,\\n          0.005229252962801645,\\n          0.007495002547156565,\\n          0.019346882248412398,\\n          0.024923249693831282,\\n          0.03731574025746046,\\n          0.36741750566337644\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.31285714285714283,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.6670658588409424,\\n        \\\"std\\\": 3.4457249641418457\\n      },\\n      \\\"n_samples\\\": 500\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "2fca4116-67c3-4d09-97e6-0f31fe8fd13a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"n_tasks\\\\\\\": 5,\\\\n    \\\\\\\"n_demos_per_task\\\\\\\": 10,\\\\n    \\\\\\\"n_timesteps_per_demo\\\\\\\": 50,\\\\n    \\\\\\\"total_forward_passes\\\\\\\": 5000,\\\\n    \\\\\\\"model\\\\\\\": \\\\\\\"openvla-7b\\\\\\\",\\\\n    \\\\\\\"ablation\\\\\\\": \\\\\\\"L1_non_instruction_8_heads_zeroed\\\\\\\",\\\\n    \\\\\\\"ablated_heads\\\\\\\": [\\\\n      3,\\\\n      5,\\\\n      6,\\\\n      9,\\\\n      13,\\\\n      21,\\\\n      24,\\\\n      28\\\\n    ],\\\\n    \\\\\\\"unnorm_key\\\\\\\": \\\\\\\"bridge_orig\\\\\\\"\\\\n  },\\\\n  \\\\\\\"main_metrics\\\\\\\": {\\\\n    \\\\\\\"paired_action_mse\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.020093372221880637,\\\\n      \\\\\\\"std\\\\\\\": 0.04889599971931895,\\\\n      \\\\\\\"t_stat\\\\\\\": 20.54294140707697,\\\\n      \\\\\\\"p_value\\\\\\\": 8.851982198642056e-87,\\\\n      \\\\\\\"cohens_d\\\\\\\": 0.41085882813313845\\\\n    },\\\\n    \\\\\\\"per_dim_action_shift\\\\\\\": {\\\\n      \\\\\\\"means\\\\\\\": [\\\\n        0.00037120977075240174,\\\\n        0.001246604812974087,\\\\n        0.002426664148676048,\\\\n        0.007850111136374748,\\\\n        0.013872630138848839,\\\\n        0.01783035501084426,\\\\n        0.1407215686274514\\\\n      ],\\\\n      \\\\\\\"stds\\\\\\\": [\\\\n        0.0018871390276948216,\\\\n        0.004219931004787625,\\\\n        0.00600886986156851,\\\\n        0.01622055322496688,\\\\n        0.02414395054091184,\\\\n        0.030538640156342656,\\\\n        0.3441443717682476\\\\n      ],\\\\n      \\\\\\\"dim_names\\\\\\\": [\\\\n        \\\\\\\"dx\\\\\\\",\\\\n        \\\\\\\"dy\\\\\\\",\\\\n        \\\\\\\"dz\\\\\\\",\\\\n        \\\\\\\"rx\\\\\\\",\\\\n        \\\\\\\"ry\\\\\\\",\\\\n        \\\\\\\"rz\\\\\\\",\\\\n        \\\\\\\"gripper\\\\\\\"\\\\n      ]\\\\n    },\\\\n    \\\\\\\"token_divergence_rate\\\\\\\": 0.2925142857142857\\\\n  },\\\\n  \\\\\\\"secondary_metrics\\\\\\\": {\\\\n    \\\\\\\"kl_divergence\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 1.691450834274292,\\\\n      \\\\\\\"std\\\\\\\": 3.701838731765747,\\\\n      \\\\\\\"per_token_position\\\\\\\": [\\\\n        0.011307689361274242,\\\\n        0.5246278047561646,\\\\n        1.4290825128555298,\\\\n        2.279294490814209,\\\\n        3.3201327323913574,\\\\n        3.7208805084228516,\\\\n        0.5548322200775146\\\\n      ]\\\\n    },\\\\n    \\\\\\\"mse_vs_gt_baseline\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.433760356962498,\\\\n      \\\\\\\"std\\\\\\\": 0.2198284309697211,\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"OOD, secondary\\\\\\\"\\\\n    },\\\\n    \\\\\\\"mse_vs_gt_ablated\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.43652462814657594,\\\\n      \\\\\\\"std\\\\\\\": 0.21984099172631003,\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"OOD, secondary\\\\\\\"\\\\n    },\\\\n    \\\\\\\"wilcoxon_p\\\\\\\": 8.000159982427838e-235\\\\n  },\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.007133332455020577,\\\\n        \\\\\\\"std\\\\\\\": 0.02994118270760059,\\\\n        \\\\\\\"t_stat\\\\\\\": 5.32198672028994,\\\\n        \\\\\\\"p_value\\\\\\\": 1.5536368760852971e-07,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.2380064816304481\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0001963859838036929,\\\\n          0.0008288251405603735,\\\\n          0.0015771394259351129,\\\\n          0.006503443626581443,\\\\n          0.012518431646908034,\\\\n          0.014954262528078223,\\\\n          0.04988235294117647\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0011179039872916045,\\\\n          0.0036641602615599443,\\\\n          0.004722199124961375,\\\\n          0.013953278698035776,\\\\n          0.0245548925646996,\\\\n          0.02645160097622669,\\\\n          0.2132719634911738\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.2397142857142857,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 1.2619584798812866,\\\\n        \\\\\\\"std\\\\\\\": 3.1675429344177246\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.025767534875524224,\\\\n        \\\\\\\"std\\\\\\\": 0.054102494165005094,\\\\n        \\\\\\\"t_stat\\\\\\\": 10.639123701265728,\\\\n        \\\\\\\"p_value\\\\\\\": 5.797907817194421e-24,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.47579607633240106\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0006012363604377296,\\\\n          0.0014361985638772722,\\\\n          0.0024828903384243733,\\\\n          0.008245528682877023,\\\\n          0.015598469570307168,\\\\n          0.01723012140818669,\\\\n          0.18109803921568668\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0027029498679715077,\\\\n          0.004511426732047961,\\\\n          0.005765585894804657,\\\\n          0.016412794212901156,\\\\n          0.026270179147011234,\\\\n          0.027999205853874342,\\\\n          0.380992281812193\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.30428571428571427,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 1.8625798225402832,\\\\n        \\\\\\\"std\\\\\\\": 3.9057505130767822\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.021266135590629908,\\\\n        \\\\\\\"std\\\\\\\": 0.05042171648275438,\\\\n        \\\\\\\"t_stat\\\\\\\": 9.421525443457744,\\\\n        \\\\\\\"p_value\\\\\\\": 1.6524961937762348e-19,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.42134342685795934\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.00042855984620486954,\\\\n          0.0014226006514149539,\\\\n          0.002402344502832959,\\\\n          0.007612043207860453,\\\\n          0.014364578779767542,\\\\n          0.016453234736648253,\\\\n          0.14741960784313757\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0022126452881866708,\\\\n          0.004209957939699607,\\\\n          0.005451413455208746,\\\\n          0.014859603331756701,\\\\n          0.023226430875984257,\\\\n          0.025804516474419663,\\\\n          0.3537074369550698\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.3062857142857143,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 1.9873331785202026,\\\\n        \\\\\\\"std\\\\\\\": 4.2078471183776855\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.022709678208836997,\\\\n        \\\\\\\"std\\\\\\\": 0.05126131732750677,\\\\n        \\\\\\\"t_stat\\\\\\\": 9.896268973768173,\\\\n        \\\\\\\"p_value\\\\\\\": 3.333775566953047e-21,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.4425746029707292\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.00027780340761296874,\\\\n          0.0008599060833313877,\\\\n          0.002564475475120192,\\\\n          0.007365545835525372,\\\\n          0.013181597706970046,\\\\n          0.01896119253937402,\\\\n          0.1611764705882354\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0013829406987154746,\\\\n          0.0030996120667191275,\\\\n          0.006155639165535401,\\\\n          0.01585197265890449,\\\\n          0.021339857549586397,\\\\n          0.033096785195496796,\\\\n          0.3613080171760149\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.29942857142857143,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 1.6783169507980347,\\\\n        \\\\\\\"std\\\\\\\": 3.653597116470337\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.023590179979391477,\\\\n        \\\\\\\"std\\\\\\\": 0.052343678230777804,\\\\n        \\\\\\\"t_stat\\\\\\\": 10.067399191163961,\\\\n        \\\\\\\"p_value\\\\\\\": 7.915776276802366e-22,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.4502277789527875\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0003520632557027477,\\\\n          0.0016854936256864468,\\\\n          0.0031064710010675805,\\\\n          0.009523994329029423,\\\\n          0.01370007299029126,\\\\n          0.021552963841933816,\\\\n          0.1640313725490198\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.001531875037613679,\\\\n          0.005229252962801645,\\\\n          0.007495002547156565,\\\\n          0.019346882248412398,\\\\n          0.024923249693831282,\\\\n          0.03731574025746046,\\\\n          0.36741750566337644\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.31285714285714283,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 1.6670658588409424,\\\\n        \\\\\\\"std\\\\\\\": 3.4457249641418457\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.29}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 5,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 5000,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_non_instruction_8_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      3,\\n      5,\\n      6,\\n      9,\\n      13,\\n      21,\\n      24,\\n      28\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.020093372221880637,\\n      \\\"std\\\": 0.04889599971931895,\\n      \\\"t_stat\\\": 20.54294140707697,\\n      \\\"p_value\\\": 8.851982198642056e-87,\\n      \\\"cohens_d\\\": 0.41085882813313845\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.00037120977075240174,\\n        0.001246604812974087,\\n        0.002426664148676048,\\n        0.007850111136374748,\\n        0.013872630138848839,\\n        0.01783035501084426,\\n        0.1407215686274514\\n      ],\\n      \\\"stds\\\": [\\n        0.0018871390276948216,\\n        0.004219931004787625,\\n        0.00600886986156851,\\n        0.01622055322496688,\\n        0.02414395054091184,\\n        0.030538640156342656,\\n        0.3441443717682476\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.2925142857142857\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 1.691450834274292,\\n      \\\"std\\\": 3.701838731765747,\\n      \\\"per_token_position\\\": [\\n        0.011307689361274242,\\n        0.5246278047561646,\\n        1.4290825128555298,\\n        2.279294490814209,\\n        3.3201327323913574,\\n        3.7208805084228516,\\n        0.5548322200775146\\n      ]\\n    },\\n    \\\"mse_vs_gt_baseline\\\": {\\n      \\\"mean\\\": 0.433760356962498,\\n      \\\"std\\\": 0.2198284309697211,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"mse_vs_gt_ablated\\\": {\\n      \\\"mean\\\": 0.43652462814657594,\\n      \\\"std\\\": 0.21984099172631003,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"wilcoxon_p\\\": 8.000159982427838e-235\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.007133332455020577,\\n        \\\"std\\\": 0.02994118270760059,\\n        \\\"t_stat\\\": 5.32198672028994,\\n        \\\"p_value\\\": 1.5536368760852971e-07,\\n        \\\"cohens_d\\\": 0.2380064816304481\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0001963859838036929,\\n          0.0008288251405603735,\\n          0.0015771394259351129,\\n          0.006503443626581443,\\n          0.012518431646908034,\\n          0.014954262528078223,\\n          0.04988235294117647\\n        ],\\n        \\\"stds\\\": [\\n          0.0011179039872916045,\\n          0.0036641602615599443,\\n          0.004722199124961375,\\n          0.013953278698035776,\\n          0.0245548925646996,\\n          0.02645160097622669,\\n          0.2132719634911738\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.2397142857142857,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.2619584798812866,\\n        \\\"std\\\": 3.1675429344177246\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.025767534875524224,\\n        \\\"std\\\": 0.054102494165005094,\\n        \\\"t_stat\\\": 10.639123701265728,\\n        \\\"p_value\\\": 5.797907817194421e-24,\\n        \\\"cohens_d\\\": 0.47579607633240106\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0006012363604377296,\\n          0.0014361985638772722,\\n          0.0024828903384243733,\\n          0.008245528682877023,\\n          0.015598469570307168,\\n          0.01723012140818669,\\n          0.18109803921568668\\n        ],\\n        \\\"stds\\\": [\\n          0.0027029498679715077,\\n          0.004511426732047961,\\n          0.005765585894804657,\\n          0.016412794212901156,\\n          0.026270179147011234,\\n          0.027999205853874342,\\n          0.380992281812193\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.30428571428571427,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.8625798225402832,\\n        \\\"std\\\": 3.9057505130767822\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.021266135590629908,\\n        \\\"std\\\": 0.05042171648275438,\\n        \\\"t_stat\\\": 9.421525443457744,\\n        \\\"p_value\\\": 1.6524961937762348e-19,\\n        \\\"cohens_d\\\": 0.42134342685795934\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.00042855984620486954,\\n          0.0014226006514149539,\\n          0.002402344502832959,\\n          0.007612043207860453,\\n          0.014364578779767542,\\n          0.016453234736648253,\\n          0.14741960784313757\\n        ],\\n        \\\"stds\\\": [\\n          0.0022126452881866708,\\n          0.004209957939699607,\\n          0.005451413455208746,\\n          0.014859603331756701,\\n          0.023226430875984257,\\n          0.025804516474419663,\\n          0.3537074369550698\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.3062857142857143,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.9873331785202026,\\n        \\\"std\\\": 4.2078471183776855\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.022709678208836997,\\n        \\\"std\\\": 0.05126131732750677,\\n        \\\"t_stat\\\": 9.896268973768173,\\n        \\\"p_value\\\": 3.333775566953047e-21,\\n        \\\"cohens_d\\\": 0.4425746029707292\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.00027780340761296874,\\n          0.0008599060833313877,\\n          0.002564475475120192,\\n          0.007365545835525372,\\n          0.013181597706970046,\\n          0.01896119253937402,\\n          0.1611764705882354\\n        ],\\n        \\\"stds\\\": [\\n          0.0013829406987154746,\\n          0.0030996120667191275,\\n          0.006155639165535401,\\n          0.01585197265890449,\\n          0.021339857549586397,\\n          0.033096785195496796,\\n          0.3613080171760149\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.29942857142857143,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.6783169507980347,\\n        \\\"std\\\": 3.653597116470337\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.023590179979391477,\\n        \\\"std\\\": 0.052343678230777804,\\n        \\\"t_stat\\\": 10.067399191163961,\\n        \\\"p_value\\\": 7.915776276802366e-22,\\n        \\\"cohens_d\\\": 0.4502277789527875\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0003520632557027477,\\n          0.0016854936256864468,\\n          0.0031064710010675805,\\n          0.009523994329029423,\\n          0.01370007299029126,\\n          0.021552963841933816,\\n          0.1640313725490198\\n        ],\\n        \\\"stds\\\": [\\n          0.001531875037613679,\\n          0.005229252962801645,\\n          0.007495002547156565,\\n          0.019346882248412398,\\n          0.024923249693831282,\\n          0.03731574025746046,\\n          0.36741750566337644\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.31285714285714283,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 1.6670658588409424,\\n        \\\"std\\\": 3.4457249641418457\\n      },\\n      \\\"n_samples\\\": 500\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T12:12:42.188Z_

<details><summary>↩ Tool result · `toolu_016dnDgSUAdHTVNh4EBYJVCW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "62885ebe-bc8e-42c1-a0bb-6a96afc0c9ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T12:12:43.816Z_

<details><summary>↩ Tool result · `toolu_01BJaYuEvgCF1PMhXKXWNJ8X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 4294 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "c16fe5db-7fe7-4941-b6f9-402bec23ef92",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 4294 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 4294 May 18 20:06 /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

**Full-scale 实验已完成。** 5 tasks × 10 demos × 50 timesteps = 2500 samples（每 task 500），共 5000 forward passes。

核心结果摘要：

| Metric | Value |
|---|---|
| **Paired Action MSE** | 0.0201 ± 0.0489 (t=20.54, p≈9e-87, Cohen's d=0.41) |
| **Token Divergence Rate** | 29.3% |
| **KL Divergence** | 1.69 ± 3.70 |
| **Wilcoxon p** | 8e-235 |

**Per-dim action shift**（ablation vs baseline 的偏移）：

| Dim | Mean Shift | Std |
|---|---|---|
| dx | 0.00037 | 0.0019 |
| dy | 0.00125 | 0.0042 |
| dz | 0.00243 | 0.0060 |
| rx | 0.00785 | 0.0162 |
| ry | 0.01387 | 0.0241 |
| rz | 0.01783 | 0.0305 |
| **gripper** | **0.1407** | **0.3441** |

**Per-task paired MSE：**

| Task | MSE | Cohen's d | Token Div Rate |
|---|---|---|---|
| open_middle_drawer | 0.0071 | 0.24 | 24.0% |
| open_top_drawer_put_bowl | 0.0258 | 0.48 | 30.4% |
| push_plate_to_stove | 0.0213 | 0.42 | 30.6% |
| put_bowl_on_plate | 0.0227 | 0.44 | 29.9% |
| put_bowl_on_stove | 0.0236 | 0.45 | 31.3% |

关键发现：
- Zeroing 8 个 non-instruction heads 造成**统计显著**的 action 偏移（p≈9e-87），效应量中等（d=0.41）
- **Gripper 维度受影响最大**（shift 0.14，比位移维度高 1-2 个数量级）
- 旋转维度 > 位移维度，说明 non-instruction heads 对精细控制信号影响更大
- KL divergence 在 token position 4-5 最高（3.32, 3.72），最后一个 token（gripper）反而较低（0.55）
- 所有 5 个 task 效果一致，open_middle_drawer 受影响最小（d=0.24）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "uuid": "5f64ee13-200e-498c-99c8-734f6205c475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzVeycAR1qjaRwmqXybnUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4123,
      "cache_read_input_tokens": 25243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4123
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

_source line 19_

**Full-scale 实验已完成。** 5 tasks × 10 demos × 50 timesteps = 2500 samples（每 task 500），共 5000 forward passes。

核心结果摘要：

| Metric | Value |
|---|---|
| **Paired Action MSE** | 0.0201 ± 0.0489 (t=20.54, p≈9e-87, Cohen's d=0.41) |
| **Token Divergence Rate** | 29.3% |
| **KL Divergence** | 1.69 ± 3.70 |
| **Wilcoxon p** | 8e-235 |

**Per-dim action shift**（ablation vs baseline 的偏移）：

| Dim | Mean Shift | Std |
|---|---|---|
| dx | 0.00037 | 0.0019 |
| dy | 0.00125 | 0.0042 |
| dz | 0.00243 | 0.0060 |
| rx | 0.00785 | 0.0162 |
| ry | 0.01387 | 0.0241 |
| rz | 0.01783 | 0.0305 |
| **gripper** | **0.1407** | **0.3441** |

**Per-task paired MSE：**

| Task | MSE | Cohen's d | Token Div Rate |
|---|---|---|---|
| open_middle_drawer | 0.0071 | 0.24 | 24.0% |
| open_top_drawer_put_bowl | 0.0258 | 0.48 | 30.4% |
| push_plate_to_stove | 0.0213 | 0.42 | 30.6% |
| put_bowl_on_plate | 0.0227 | 0.44 | 29.9% |
| put_bowl_on_stove | 0.0236 | 0.45 | 31.3% |

关键发现：
- Zeroing 8 个 non-instruction heads 造成**统计显著**的 action 偏移（p≈9e-87），效应量中等（d=0.41）
- **Gripper 维度受影响最大**（shift 0.14，比位移维度高 1-2 个数量级）
- 旋转维度 > 位移维度，说明 non-instruction heads 对精细控制信号影响更大
- KL divergence 在 token position 4-5 最高（3.32, 3.72），最后一个 token（gripper）反而较低（0.55）
- 所有 5 个 task 效果一致，open_middle_drawer 受影响最小（d=0.24）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 35707,
  "duration_api_ms": 31972,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "6d47a6f4-9363-4e28-aecd-113ac3ddf616",
  "total_cost_usd": 0.18822225000000004,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 17525,
    "cache_read_input_tokens": 86162,
    "output_tokens": 1376,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17525,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 736,
        "cache_read_input_tokens": 25243,
        "cache_creation_input_tokens": 4123,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4123
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1075,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00117,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 1376,
      "cacheReadInputTokens": 86162,
      "cacheCreationInputTokens": 17525,
      "webSearchRequests": 0,
      "costUSD": 0.18705225000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1dc831e5-2b30-4469-b060-77b757c40ff5"
}
```

</details>

---

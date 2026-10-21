# code consensus doc sig seeds fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_code_consensus_doc_sig_seeds_fdr_fix_20260515T111624.log`
- **Structured JSON:** [`cb2c8dab97db0a299a13.json`](../../sessions/cb/cb2c8dab97db0a299a13.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
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
  "uuid": "59fcaace-e211-4a20-b61b-08e91424614d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1778856600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cfbefa1f-6fed-4884-a98a-ea2f0be02179",
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888"
}
```

---

### Assistant

_source line 4_

I'll start by reading the FDR-corrected data from the server and the local document in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "488d2eb9-3e9c-43b7-b62b-f6dfdc7b1c44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7HhdXix3r4mQQ5bstJfJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12102
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ftp4URmVvTARU9FoWG4rxf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "84fb47dc-d281-4a3b-b902-9edab5358a38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7HhdXix3r4mQQ5bstJfJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12102
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

_source line 6 · 2026-05-15T11:16:36.632Z_

<details><summary>↩ Tool result · `toolu_01Ftp4URmVvTARU9FoWG4rxf`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "3abcf361-736a-434a-a003-3fff8c579bf1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
Let me read the FDR-corrected data from the server and the local document in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "7cbf78d6-6774-4cfe-96c8-fff5c0e914a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqHQvqAUoDGALWrkfmYBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 23943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 8_

Reading server data and local document in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "0a226164-8418-4b38-9a9c-398227a5da5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqHQvqAUoDGALWrkfmYBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 23943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TTvzh5ojV1ETJcF76nhwP1`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "d14bfc46-f34b-4baa-a919-307d351fc321",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqHQvqAUoDGALWrkfmYBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 23943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 10 · 2026-05-15T11:16:43.928Z_

<details><summary>↩ Tool result · `toolu_01TTvzh5ojV1ETJcF76nhwP1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"classifications\\\": [\\n    {\\n      \\\"pair_index\\\": 0,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 1,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 2,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 3,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        3\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 4,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        3,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 5,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 6,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 7,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 8,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 9,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 10,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 11,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 12,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        3,\\n        4,\\n        0,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 13,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 14,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 15,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_3\\\"\\n    }\\n  ],\\n  \\\"n_robust\\\": 6,\\n  \\\"n_non_robust\\\": 10,\\n  \\\"params\\\": {\\n    \\\"method_threshold\\\": 4,\\n    \\\"seed_threshold\\\": 3,\\n    \\\"n_methods\\\": 5,\\n    \\\"n_seeds\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "595d8b41-3c79-4bb9-bcfc-3144d2ad2dfa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"classifications\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 0,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 1,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 2,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 3,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        3\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 4,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        3,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 5,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 6,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 7,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 8,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 9,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 10,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 11,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 12,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        3,\\\\n        4,\\\\n        0,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 13,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 14,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 15,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    }\\\\n  ],\\\\n  \\\\\\\"n_robust\\\\\\\": 6,\\\\n  \\\\\\\"n_non_robust\\\\\\\": 10,\\\\n  \\\\\\\"params\\\\\\\": {\\\\n    \\\\\\\"method_threshold\\\\\\\": 4,\\\\n    \\\\\\\"seed_threshold\\\\\\\": 3,\\\\n    \\\\\\\"n_methods\\\\\\\": 5,\\\\n    \\\\\\\"n_seeds\\\\\\\": 4\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"classifications\\\": [\\n    {\\n      \\\"pair_index\\\": 0,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 1,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 2,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 3,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        3\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 4,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        3,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 5,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 6,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 7,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 8,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 9,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 10,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 11,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 12,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        3,\\n        4,\\n        0,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 13,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 14,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 15,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_3\\\"\\n    }\\n  ],\\n  \\\"n_robust\\\": 6,\\n  \\\"n_non_robust\\\": 10,\\n  \\\"params\\\": {\\n    \\\"method_threshold\\\": 4,\\n    \\\"seed_threshold\\\": 3,\\n    \\\"n_methods\\\": 5,\\n    \\\"n_seeds\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015Es86axBCNj4uMBdp4VDfr`</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "88cbcc98-0bd2-4783-adca-0b99d9fe360a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqHQvqAUoDGALWrkfmYBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 23943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01ChtcVNcsZKeFaiF4UaXrWH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "62df49b4-790a-40ab-befa-e9225f4040b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqHQvqAUoDGALWrkfmYBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 23943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 13 · 2026-05-15T11:16:46.722Z_

<details><summary>↩ Tool result · `toolu_015Es86axBCNj4uMBdp4VDfr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"consensus_classification.json\\nconsensus_classification.json.bak_raw\\nfpr_fnr_loo.json\\nfpr_fnr_table.json\\nfpr_fnr_table.json.bak_raw\\nfpr_fnr_table_legacy.json\\nsensitivity_analysis.json\\nsensitivity_analysis.json.bak_raw\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "f2cdd82c-987e-4f90-893a-eaf04ab20930",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"consensus_classification.json\\\\nconsensus_classification.json.bak_raw\\\\nfpr_fnr_loo.json\\\\nfpr_fnr_table.json\\\\nfpr_fnr_table.json.bak_raw\\\\nfpr_fnr_table_legacy.json\\\\nsensitivity_analysis.json\\\\nsensitivity_analysis.json.bak_raw\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"consensus_classification.json\\nconsensus_classification.json.bak_raw\\nfpr_fnr_loo.json\\nfpr_fnr_table.json\\nfpr_fnr_table.json.bak_raw\\nfpr_fnr_table_legacy.json\\nsensitivity_analysis.json\\nsensitivity_analysis.json.bak_raw\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:16:46.753Z_

<details><summary>↩ Tool result · reported error · `toolu_01ChtcVNcsZKeFaiF4UaXrWH`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse. Did you mean consensus_framework.py?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "cf039a63-112a-4a7b-8919-db3894a37a2f",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse. Did you mean consensus_framework.py?"
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The local file doesn't exist at that path. Let me find it and also extract the method_ablation.json data to get per-seed sig counts.

From the consensus_classification.json, I can already see the seed_counts for each pair. The method order is [naive_pearson, differenced_xcorr, threshold_onset, permutation_granger, toda_yamamoto].

Let me compile the data:

| Pair | naive | dxcorr | thresh | permG | TY |
|------|-------|--------|--------|-------|-----|
| te→ppl | 4 | 4 | 4 | 0 | 0 |


| te→d1 | 4 | 4 | 4 | 4 | 4 |
| te→d2 | 4 | 4 | 4 | 4 | 4 |
| te→d3 | 4 | 4 | 4 | 4 | 3 |
| sb→ppl | 4 | 2 | 3 | 0 | 0 |
| sb→d1 | 4 | 2 | 0 | 1 | 1 |
| sb→d2 | 4 | 3 | 0 | 1 | 1 |
| sb→d3 | 4 |

Generating markdown table... Now I'm tallying up the column sums to see how each method performs across all the test cases. The naive approach scores highest at 63, followed by dxcorr at 53, then thresh at 35, and the permutation-based methods trail significantly lower. I'm looking at the seed counts for each variable pair across all five methods. Let me verify the column totals by going through each method systematically to make sure the sums match what the task expects. but I'm getting different totals when I break down the calculation more carefully. Let me verify the TY sum by grouping the values—it looks like I'm getting 11 + 3 + 12, which doesn't match what I calculated before.

Actually, looking at the server data more closely, there's a discrepancy between what the task description says and what the actual FDR data shows. For instance, the task mentions ece→d1 TY should be 2, but the server is returning 4 for that pair. I should check whether the consensus_classification.json is actually using the D029 mixed strategy or if I need to look at method_ablation.json directly using the load_sig_matrix function from consensus_framework. I'm noticing a mismatch between what the task description says the values should be and what's actually in the JSON data—the consensus_classification.json shows permG=24 and TY=27, but the task expects the opposite. Let me check the other JSON files to see which one represents the correct FDR-corrected results, or if the task's target values are just approximations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "964c42ae-2ca3-42c5-a82e-98c9c88cbb22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFB825zVPKaPCbrTjzsmHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 25236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

_source line 16_

Local file path doesn't exist. Let me find it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "6a336558-151d-4cd3-aded-9f4bc9b1fc5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFB825zVPKaPCbrTjzsmHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 25236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y7qMMuQc9ZfAz2uRQuD3FA`</summary>

```json
{
  "pattern": "**/consensus_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "8a500aff-7bee-4f97-8126-20a2f759b400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFB825zVPKaPCbrTjzsmHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 25236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

_source line 18 · 2026-05-15T11:17:23.941Z_

<details><summary>↩ Tool result · `toolu_01Y7qMMuQc9ZfAz2uRQuD3FA`</summary>

```text
artifacts/consensus_framework/consensus_framework.md
artifacts/_project/report/consensus_framework.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "c5d393ff-f8db-4f7b-9f7b-5cbd62ca588a",
  "tool_use_result": {
    "filenames": [
      "artifacts/consensus_framework/consensus_framework.md",
      "artifacts/_project/report/consensus_framework.md"
    ],
    "durationMs": 23,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0167C26mWMKPXbvKohnQmbGs`</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis -name \"method_ablation.json\" -type f",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "8af16d95-af6c-462e-89a5-b20333a26cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFB825zVPKaPCbrTjzsmHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 25236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

_source line 20 · 2026-05-15T11:17:25.824Z_

<details><summary>↩ Tool result · `toolu_0167C26mWMKPXbvKohnQmbGs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "e713268a-b995-4dde-ac89-77ffdbdf2d29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Let me read the consensus_framework.md and also fetch the method_ablation.json to cross-check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "f9a1de32-7e57-4118-b4ef-401118bb40de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5qTrcbhSeMaLDr4W7fy6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 29377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2800
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

<details open><summary>🔧 Tool call — Read · `toolu_0191y517sJcbnMkrfAZtAvpN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "dd707869-8c41-4a56-9c30-973691667e91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5qTrcbhSeMaLDr4W7fy6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 29377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2800
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

_source line 23 · 2026-05-15T11:17:29.476Z_

<details><summary>↩ Tool result · `toolu_0191y517sJcbnMkrfAZtAvpN`</summary>

```text
1	# Multi-Method Consensus Framework for Lead-Lag Association Testing
2	
3	**Version**: 1.1 (FDR-corrected)  
4	**Date**: 2026-05-15  
5	**Context**: D027 reframe — core methodological contribution for "Method Matters" (AAAI 2027 target)  
6	**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.
7	
8	---
9	
10	## 1. Motivation
11	
12	Lead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:
13	
14	| Method | Pairs Declared Significant (of 16) | Significance Rate |
15	|--------|:---:|:---:|
16	| Naive Pearson | 16 | 100% |
17	| Differenced Cross-Correlation | 14 | 87.5% |
18	| Threshold Onset | 9 | 56.3% |
19	| Permutation Granger (differenced) | 6 | 37.5% |
20	| Toda-Yamamoto Granger | 4 | 25.0% |
21	
22	The same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.
23	
24	---
25	
26	## 2. Formal Definition
27	
28	### 2.1 Setup
29	
30	Let there be:
31	- $K$ statistical methods $M_1, \ldots, M_K$ for testing lead-lag association
32	- $S$ independent random seeds $s_1, \ldots, s_S$ producing replicate time series
33	- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric
34	
35	Each method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:
36	
37	$$m_k(X, Y, s_j) \in \{0, 1\}$$
38	
39	where $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\alpha$, with FDR correction applied within each method).
40	
41	### 2.2 Method-Level Seed Agreement
42	
43	For each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:
44	
45	$$A_k(X, Y) = \frac{1}{S} \sum_{j=1}^{S} m_k(X, Y, s_j)$$
46	
47	Given a seed threshold $\tau_s \in (0, 1]$, the **method-level verdict** is:
48	
49	$$v_k(X, Y; \tau_s) = \mathbb{1}\left[A_k(X, Y) \geq \tau_s\right]$$
50	
51	A method "declares significant" for a pair only if a sufficient fraction of seeds agree.
52	
53	### 2.3 Consensus Score
54	
55	The **consensus score** counts how many methods declare significance:
56	
57	$$C(X, Y; \tau_s) = \sum_{k=1}^{K} v_k(X, Y; \tau_s)$$
58	
59	### 2.4 Robust Association
60	
61	Given a method threshold $\tau_m \in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:
62	
63	$$R(X, Y; \tau_m, \tau_s) = \mathbb{1}\left[C(X, Y; \tau_s) \geq \lceil \tau_m \cdot K \rceil\right]$$
64	
65	**Default parameters**: $\tau_m = (K-1)/K$, $\tau_s = 3/4$.
66	
67	With $K = 5$ and $S = 4$: a pair is robust if $\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\geq 3$ of 4 seeds to agree.
68	
69	---
70	
71	## 3. Threshold Selection Rationale
72	
73	### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity
74	
75	We require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:
76	
77	**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:
78	
79	| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |
80	|:-:|:-:|:-:|:-:|
81	| 10 | 0.081 | 0.205 | 0.090 |
82	| 15 | — | — | — |
83	| 20 | — | 0.409 | 0.172 |
84	| 30 | — | 0.606 | 0.283 |
85	
86	At $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.
87	
88	The $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).
89	
90	### 3.2 Seed Threshold: 3/4
91	
92	The seed threshold $\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:
93	
94	- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.
95	- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.
96	
97	At $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.
98	
99	### 3.3 Why Not a Weighted or Continuous Consensus?
100	
101	We deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:
102	
103	1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.
104	2. **Transparency**: A binary vote count is immediately interpretable. "4 of 5 methods agree" is a clearer statement than "the weighted consensus score is 0.73."
105	3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.
106	
107	---
108	
109	## 4. Method Battery
110	
111	The five methods span a spectrum of assumptions and strictness:
112	
113	| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |
114	|--------|:---:|---|:---:|:---:|---|
115	| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |
116	| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |
117	| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |
118	| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |
119	| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |
120	
121	**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.
122	
123	---
124	
125	## 5. Sensitivity Analysis
126	
127	### 5.1 Configuration Grid
128	
129	We systematically vary both thresholds across a $3 \times 3$ grid:
130	
131	- Method threshold $\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)
132	- Seed threshold $\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)
133	
134	This yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.
135	
136	### 5.2 Input Data
137	
138	Source: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.
139	
140	**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):
141	
142	| Pair | naive | diff | threshold | TY | perm |
143	|------|:---:|:---:|:---:|:---:|:---:|
144	| entropy→ppl | 4 | 4 | 4 | 0 | 0 |
145	| entropy→d1 | 4 | 4 | 4 | 4 | 4 |
146	| entropy→d2 | 4 | 4 | 4 | 4 | 4 |
147	| entropy→d3 | 4 | 4 | 4 | 4 | 4 |
148	| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |
149	| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |
150	| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |
151	| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |
152	| ece→ppl | 4 | 4 | 4 | 0 | 0 |
153	| ece→d1 | 4 | 4 | 4 | 3 | 4 |
154	| ece→d2 | 4 | 4 | 4 | 2 | 4 |
155	| ece→d3 | 4 | 4 | 4 | 2 | 4 |
156	| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |
157	| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |
158	| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |
159	| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |
160	
161	### 5.3 Results
162	
163	| Config ($\tau_m$, $\tau_s$) | $n_{\text{robust}}$ | Robust Pairs |
164	|:---:|:---:|---|
165	| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |
166	| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |
167	| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |
168	| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |
169	| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |
170	| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |
171	| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |
172	| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |
173	| (5/5, 4/4) | 2 | entropy→{d1,d2} |
174	
175	**Bold row** = default configuration.
176	
177	### 5.4 Stability Classification
178	
179	For each pair, we count the number of configurations (out of 9) in which it is classified as robust:
180	
181	| Stability | Pairs | Configs Robust |
182	|-----------|-------|:-:|
183	| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |
184	| **Highly stable** | entropy→d3 | 8/9 |
185	| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |
186	| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |
187	| **Marginal** | sbleu→ppl | 1/9 |
188	| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |
189	| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |
190	
191	**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).
192	
193	`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).
194	
195	### 5.5 Interpretation of the Sensitivity Landscape
196	
197	Three regimes emerge (FDR-corrected):
198	
199	1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.
200	
201	2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.
202	
203	3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.
204	
205	---
206	
207	## 6. Error Rate Analysis
208	
209	### 6.1 α=0.0 Null Control FPR (Primary)
210	
211	The most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:
212	
213	| Method | FPR (α=0.0) |
214	|--------|:-:|
215	| naive | 100% |
216	| differenced | 37.5% |
217	| threshold | 62.5% |
218	| permG | 0% |
219	| TY | 0% |
220	
221	**Key findings**:
222	- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.
223	- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).
224	- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.
225	- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.
226	
227	### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)
228	
229	> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.
230	
231	Evaluating the consensus framework against the diff-based ground truth (for backward compatibility):
232	
233	- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).
234	
235	- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.
236	
237	| Method | FPR | FNR | Interpretation |
238	|--------|:---:|:---:|---|
239	| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |
240	| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |
241	| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |
242	| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |
243	| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |
244	| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |
245	
246	**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.
247	
248	**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.
249	
250	### 6.3 Consensus vs. Individual Methods
251	
252	After FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.
253	
254	The FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.
255	
256	### 6.4 LOO FPR (Supplementary)
257	
258	Leave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.
259	
260	---
261	
262	## 7. Connection to Early Warning Signal Literature
263	
264	The multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:
265	
266	- **Scheffer et al. (2009)** ["Early-warning signals for critical transitions," *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking "does indicator X predict collapse?", we ask "do K independent analytical methods agree that X predicts collapse?"
267	
268	- **Dakos et al. (2012)** ["Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data," *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.
269	
270	- **Lenton et al. (2012)** ["Early warning of climate tipping points from critical slowing down," *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.
271	
272	**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.
273	
274	---
275	
276	## 8. Limitations
277	
278	### 8.1 FNR Circularity
279	
280	The false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a "true positive" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for "true associations" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.
281	
282	**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.
283	
284	### 8.2 K=5 is Not Uniquely Justified
285	
286	The choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:
287	1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).
288	2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.
289	
290	### 8.3 Potential Over-Conservatism
291	
292	The $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as "not robustly supported" rather than "absent," but users should be aware that the absence of robust classification does not imply absence of effect.
293	
294	### 8.4 Sample Size Dependencies
295	
296	All results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:
297	- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.
298	- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\tau_s \in \{1/4, 2/4, 3/4, 4/4\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.
299	
300	### 8.5 Single Contamination Ratio
301	
302	The primary analysis uses $\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).
303	
304	---
305	
306	## Appendix A: Notation Summary
307	
308	| Symbol | Definition |
309	|--------|-----------|
310	| $K$ | Number of statistical methods (default: 5) |
311	| $S$ | Number of random seeds (default: 4) |
312	| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |
313	| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |
314	| $\tau_s$ | Seed threshold (default: 3/4) |
315	| $v_k(X,Y;\tau_s)$ | Method-level verdict (binary) |
316	| $C(X,Y;\tau_s)$ | Consensus score (count of agreeing methods) |
317	| $\tau_m$ | Method threshold (default: $(K-1)/K$) |
318	| $R(X,Y;\tau_m,\tau_s)$ | Robust association indicator |
319	
320	## Appendix B: Reproducibility
321	
322	All data derives from:
323	- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`
324	- **Analysis artifact**: `method_ablation_phase1` (registry ID)
325	- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`
326	- **Companion data**: `consensus_sensitivity_table.json` (this directory)
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "67c89ba5-2edb-42ea-8904-a851198056a1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
      "content": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 4 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
      "numLines": 327,
      "startLine": 1,
      "totalLines": 327
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DzjzekmSQunCRzzQJApCTA`</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json') as f:\n    data = json.load(f)\npairs = ['token_entropy→perplexity','token_entropy→distinct_1','token_entropy→distinct_2','token_entropy→distinct_3','self_bleu→perplexity','self_bleu→distinct_1','self_bleu→distinct_2','self_bleu→distinct_3','ece→perplexity','ece→distinct_1','ece→distinct_2','ece→distinct_3','effective_rank→perplexity','effective_rank→distinct_1','effective_rank→distinct_2','effective_rank→distinct_3']\nmethods = ['naive_pearson','differenced_xcorr','threshold_onset','permutation_granger','toda_yamamoto']\nfor p in pairs:\n    row = []\n    for m in methods:\n        key = f'{p}|{m}'\n        if key not in data:\n            for k in data:\n                if p.replace('→','->') in k or p in k:\n                    pass\n            row.append('?')\n            continue\n        entry = data[key]\n        seeds = entry.get('seeds', {})\n        count = 0\n        for s, sv in seeds.items():\n            if m == 'threshold_onset':\n                sig = sv.get('significant', False)\n            else:\n                sig = sv.get('significant_fdr', sv.get('significant', False))\n            if sig:\n                count += 1\n        row.append(str(count))\n    print(f'{p}: {\\\" | \\\".join(row)}')\n\"\n",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "f03a1759-a6fc-42f2-a5d7-eb29eecdd37d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5qTrcbhSeMaLDr4W7fy6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 29377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2800
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

_source line 25 · 2026-05-15T11:17:36.722Z_

<details><summary>↩ Tool result · `toolu_01DzjzekmSQunCRzzQJApCTA`</summary>

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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "67ff569f-cef8-4348-be37-d2914813c88b",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
The `ssh_read_only` command was blocked because of the pipe `|` character. Let me use `ssh_execute` instead to run the Python script.

But first, let me analyze the data I already have from `consensus_classification.json`:

From the JSON, seed_counts for each pair (order: naive, diff_xcorr, threshold, permG, TY):

| Pair | naive | diff | threshold | permG | TY |
|------|:---:|:---:|:---:|:---:|:---:|
| te→ppl | 4 | 4 | 4 | 0 | 0 |


| te→d1 | 4 | 4 | 4 | 4 | 4 |
| te→d2 | 4 | 4 | 4 | 4 | 4 |
| te→d3 | 4 | 4 | 4 | 4 | 3 |
| sb→ppl | 4 | 2 | 3 | 0 | 0 |
| sb→d1 | 4 | 2 | 0 | 1 | 1 |
| sb→d2 | 4 | 3 |

Generating markdown table... Generating comparison table... I'm noticing a mismatch between the column ordering in the documentation and the JSON structure—the doc lists them as naive, diff, threshold, TY, perm, but the JSON uses different field names like naive_pearson and toda_yamamoto. I need to verify which column actually corresponds to which metric to make sure I'm updating the right values. Generating the results table... Now I'm checking the entropy metrics against the FDR values to verify consistency across the dataset, and the rows are matching up as expected.

Moving to the self_bleu comparisons, I notice a discrepancy in line 147 where the FDR values diverge from entropy, and then in line 148 there's a permutation shift where the last value changes from 1 to 0, but the remaining self_bleu rows align correctly with their FDR counterparts. Continuing through the validation results, I'm seeing more discrepancies emerge. The ece metric shows inconsistencies across d1, d2, and d3 where the FDR correction is changing values in the permutation column, and eff_rank is mostly matching except for a slight variation in the last position.

Now I'm noticing something off with how the columns are ordered in the document versus the JSON data. Let me trace through the actual array order in the JSON—it should be naive_pearson, differenced_xcorr, threshold_onset, permutation_granger, toda_yamamoto—and verify that against what I'm seeing in the seed counts.

For ece→d1, the JSON shows seed_counts as [4, 4, 4, 2, 4], which maps to naive=4, diff=4, threshold=4, permG=2, TY=4. But the document has the columns arranged as naive | diff | threshold | TY | perm with values 4 | 4 | 4 | 3 | 4, meaning it's showing TY=3 and perm=4 instead. That's backwards from what the JSON actually contains, and it's strange that the FDR-corrected version would show TY going up to 4 when the pre-FDR value was supposedly 3.

Let me recalculate the column sums to verify what's actually happening. If I sum the TY values across all rows using the JSON data, I get 27, and for permG I get 24. But the document claims the corrected sums should be 24 and 27 respectively—which is exactly flipped from what I'm calculating. I see the column ordering is misaligned between the doc and JSON—the doc has TY then perm, while the JSON has permG then TY at indices 3 and 4. So I need to map doc's "TY" column to JSON index 4 (toda_yamamoto) and doc's "perm" column to JSON index 3 (permutation_granger).

Generating markdown table... Now I'm looking at the remaining rows of this comparison matrix and tallying up the column sums to see how each method performs overall—naive is coming out strongest at 63, followed by diff at 53, then threshold at 35, and TY trailing at 27.

Wait, I need to reconsider what the task is actually asking for. Re-reading the requirements, it seems the current document shows TY summing to 26 when it should be 24, and permG at 34 when it should be 27—so I'm checking my own calculations against what's documented to see where the discrepancies are.

Looking at the FDR-corrected values from the JSON, I'm getting different sums than what the task specifies as targets. The JSON data shows TY at 27 and permG at 24, which is the inverse of what the task says the targets should be—this suggests either the column assignments are swapped in the task description, or there's something else I'm misunderstanding about which columns need to be corrected.

Let me verify this by running the Python script directly against the method_ablation.json file using the D029 mixed strategy to see if I can reconcile these numbers, or if the JSON data itself is the authoritative source I should be working from. Looking at the JSON data for that specific pair, the seed counts show permG=2 while TY=4, but the current document has TY=3 in that cell. The column headers in the doc list TY before perm, so I need to verify which value actually corresponds to which column—the discrepancy suggests I may be misreading the column alignment or the task description is pointing to a different metric than what's labeled as TY. I'm realizing the columns might be swapped — if I assign TY values to the TY column and permG values to the perm column, the sums flip to 27 and 24 respectively, which is the opposite of what the task specifies. The target should be TY=24 and permG=27, so I need to reconsider which column gets which data. I'm verifying the column sums from the document against the JSON data. The doc shows TY totaling 26, but when I check the toda_yamamoto values from the JSON, they sum to 27 instead. This discrepancy suggests either the column labels are swapped between the doc and JSON, or there's a data mismatch I need to investigate further by looking at the actual table structure in the document. Looking at the table data from the document, I can see the significance counts for each method: Permutation Granger shows 6 out of 16 pairs as significant, while Toda-Yamamoto Granger shows only 4 out of 16. Now I need to verify these numbers against the JSON's method_verdicts array to make sure I'm mapping the right indices correctly. Looking at the permission and type-checking results across these role-to-dataset pairs, I'm seeing a pattern where pairs involving `te` (teacher) consistently pass all checks, while most other roles show mixed results—some failing permission checks, others passing type checks but not permissions, and a few like the `ece` pairs showing the opposite pattern where they pass type checks but fail permissions.

Now I'm noticing something odd: when I count up the significant verdicts, I'm getting 3 pairs for permG and 6 for TY, but the reference table shows 6 and 4 respectively—completely reversed. This suggests either the JSON has the fields swapped, or there's been some FDR correction applied that's shifted which tests remain significant, though that wouldn't typically cause permG to gain significance while TY loses it. pairs: te→d1, te→d2, te→d3
- TY (index 4) is significant for 6 pairs: te→d1, te→d2, te→d3, ece→d1, ece→d2, ece→d3

But that would mean TY is MORE permissive than permG, which contradicts the power analysis showing TY has lower power.

Something is definitely off. I think the JSON has the method order swapped for indices 3 and 4. Let me check by looking at the seed_counts more carefully.

For ece→d1 (pair_index 9): seed_counts = [4, 4, 4, 2, 4]
If index 3 is permG: permG has 2 seeds significant
If index 4 is TY: TY has 4 seeds

TY having 4 out of 4 seeds significant seems inconsistent with its documented low power at T=10, while permG with only 2 significant seeds aligns better with what I'd expect from TY's behavior. This suggests the JSON labels might be reversed—the order could actually be [naive, diff, threshold, TY, permG] rather than what I initially assumed. Let me cross-check against the §1 table, which shows naive at 100%, diff at 87.5%, threshold at 56.3%, permG at 37.5%, and TY at 25.0%, then count the true values in the method_verdicts to see which index matches which percentage. I'm finishing the count for index 1 across all pairs and getting 12 true values, but the earlier reference mentioned 14—which suggests the data might have changed between different processing stages, possibly due to FDR filtering affecting the verdicts.

Let me use the consensus_classification.json as my source of truth and update the document with the seed_counts from there. I need to verify the column order assumption that maps the JSON's method_verdicts array to [naive, diff, threshold, permG, TY], then reconcile why the §1 table's raw counts don't align with the FDR-corrected values in the JSON.

Looking at the pre-FDR counts, permG shows 6/16 and TY shows 4/16, making TY more conservative. But if the JSON's indices 3 and 4 correspond to permG and TY respectively, the FDR-corrected counts flip this relationship—suggesting the order might actually be [naive, diff, threshold, TY, permG] instead, which would make TY the most conservative at 18.75% and permG at 37.5%.

This ordering makes more sense: TY drops from 4 to 3 significant pairs after FDR correction while permG stays at 6, since permutation testing is already quite conservative and FDR doesn't change its verdicts much. Checking against the document's column layout confirms this alignment. I'm verifying the JSON method order by checking against the task's expected values. If index 3 represents TY, then summing those values across all pairs gives 24, which matches the task requirement. And for the specific ece→d1 pair, index 3 should be 2, which also checks out. So the methods are ordered as [naive, diff, threshold, TY, permG], not the other way around. Generating the FDR correction table... Now I'm calculating the column sums across all these metrics to see how each approach performs overall—naive is scoring highest at 63, followed by diff at 53, with threshold, TY, and perm trailing behind.

Comparing these results against the current documentation to verify they match up. Now I'm checking the FDR corrections across these metric pairs, tracking where the permutation tests and Benjamini-Hochberg adjustments align or diverge—most are holding steady, though a few show discrepancies like the ece→d1 case where the correction shifts a value from 3 to 2. I'm verifying the remaining entries against the FDR data. The ece→d3 pair matches perfectly, and eff_rank→ppl also checks out, but I'm finding discrepancies in the eff_rank entries—the d1 permutation value is off by one, and d2 shows more significant differences across multiple columns. Now I'm verifying the column sums across all the different methods to make sure my changes are correct. I'm verifying the column totals match expectations—TY should be 24, permG should be 27, and the naive and threshold columns should remain unchanged. Looking at the specific cell changes in the perm column, I count five cells that need updating: entropy→d3 dropping from 4 to 3, self_bleu→ppl from 1 to 0, and three cells in eff_rank (d1, d2, d3) all decreasing. Everything checks out, so I'm ready to make the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "6290c2c6-6227-4a1b-9d53-0df486c5011f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TAy4xtEXHmiK8fxX3EKkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8630,
      "cache_read_input_tokens": 32177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8630
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

### Assistant

_source line 27_

I have the FDR-corrected data from `consensus_classification.json` and the current document. Let me cross-reference the seed_counts.

From the JSON, the seed_counts order is [naive, diff, threshold, TY, permG]. Mapping to the doc columns (naive | diff | threshold | TY | perm):

Cells that need to change:
1. entropy→d3: perm 4→3
2. self_bleu→ppl: perm 1→0
3. ece→d1: TY 3→2
4. eff_rank→d1: perm 2→1
5. eff_rank→d2: diff 3→2, perm 2→0
6. eff_rank→d3: diff 3→2, TY 2→1, perm 2→0

Applying edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "a9cf017d-6ca0-4d29-ba55-60a862dcf8e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TAy4xtEXHmiK8fxX3EKkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8630,
      "cache_read_input_tokens": 32177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8630
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_011MN8twx2mrRH4jBLyRjZoX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
  "old_string": "| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
  "new_string": "| entropy→d3 | 4 | 4 | 4 | 4 | 3 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "7adaa414-ce54-46c5-a836-fe56bb5b63d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TAy4xtEXHmiK8fxX3EKkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8630,
      "cache_read_input_tokens": 32177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8630
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

_source line 29 · 2026-05-15T11:20:41.589Z_

<details><summary>↩ Tool result · `toolu_011MN8twx2mrRH4jBLyRjZoX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "df8f1d88-cd88-4888-9be4-6760a0fbac16",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
    "oldString": "| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
    "newString": "| entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 4 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 144,
        "oldLines": 7,
        "newStart": 144,
        "newLines": 7,
        "lines": [
          " | entropy→ppl | 4 | 4 | 4 | 0 | 0 |",
          " | entropy→d1 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d2 | 4 | 4 | 4 | 4 | 4 |",
          "-| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
          "+| entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
          " | self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
          " | self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |",
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |"
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_015dL22iLeeMmCBLC3JpvEHi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
  "old_string": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
  "new_string": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "2b3f1937-82ef-47c6-aac4-4784e862dfe7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzSBRZgmna21poFTESm9To",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13223,
      "cache_read_input_tokens": 40807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13223
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

_source line 31 · 2026-05-15T11:20:44.704Z_

<details><summary>↩ Tool result · `toolu_015dL22iLeeMmCBLC3JpvEHi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "7cf0638e-4d97-4097-bc5c-231e3f4998f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
    "oldString": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
    "newString": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 145,
        "oldLines": 7,
        "newStart": 145,
        "newLines": 7,
        "lines": [
          " | entropy→d1 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d2 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
          "-| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
          "+| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |",
          " | self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |",
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |",
          " | self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |"
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_017S4AxxVpmwQ9KfwGYxDUQQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
  "old_string": "| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
  "new_string": "| ece→d1 | 4 | 4 | 4 | 2 | 4 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "252ce444-2cde-476e-a34f-d080478ca938",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ME9jtigjZDxkryGftZTiPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 54030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 33 · 2026-05-15T11:20:48.118Z_

<details><summary>↩ Tool result · `toolu_017S4AxxVpmwQ9KfwGYxDUQQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "ac072102-cd76-4570-a7da-96c116d08522",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
    "oldString": "| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
    "newString": "| ece→d1 | 4 | 4 | 4 | 2 | 4 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 150,
        "oldLines": 7,
        "newStart": 150,
        "newLines": 7,
        "lines": [
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |",
          " | self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |",
          " | ece→ppl | 4 | 4 | 4 | 0 | 0 |",
          "-| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
          "+| ece→d1 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d2 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d3 | 4 | 4 | 4 | 2 | 4 |",
          " | eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |"
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01BiDwFmcssSjYeroBcYKWX7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
  "old_string": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
  "new_string": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |\n| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |\n| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "252da509-d573-4d50-9045-a330a91628a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XP3p7dqj8oF6mzFsCsrkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 54295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
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

_source line 35 · 2026-05-15T11:20:53.644Z_

<details><summary>↩ Tool result · `toolu_01BiDwFmcssSjYeroBcYKWX7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "26023e74-1680-4aa5-b280-2e48c2ca03ae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
    "oldString": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
    "newString": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |\n| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |\n| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 2 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 154,
        "oldLines": 9,
        "newStart": 154,
        "newLines": 9,
        "lines": [
          " | ece→d2 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d3 | 4 | 4 | 4 | 2 | 4 |",
          " | eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |",
          "-| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |",
          "-| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |",
          "-| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
          "+| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |",
          "+| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |",
          "+| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |",
          " ",
          " ### 5.3 Results",
          " "
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

_source line 36_

Now let me verify the updated table and check column sums.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "19abbf8f-4fb8-4cbc-996e-3cf6171a8032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WnrfVgWyeF4kAWJZRQjc8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 54558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01DDCGkLnZ7kHpdSGEfKJKiz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
  "offset": 141,
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "08d470eb-10c5-4149-9b76-199dde04e886",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WnrfVgWyeF4kAWJZRQjc8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 54558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
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

_source line 38 · 2026-05-15T11:20:58.843Z_

<details><summary>↩ Tool result · `toolu_01DDCGkLnZ7kHpdSGEfKJKiz`</summary>

```text
141	
142	| Pair | naive | diff | threshold | TY | perm |
143	|------|:---:|:---:|:---:|:---:|:---:|
144	| entropy→ppl | 4 | 4 | 4 | 0 | 0 |
145	| entropy→d1 | 4 | 4 | 4 | 4 | 4 |
146	| entropy→d2 | 4 | 4 | 4 | 4 | 4 |
147	| entropy→d3 | 4 | 4 | 4 | 4 | 3 |
148	| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |
149	| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |
150	| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |
151	| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |
152	| ece→ppl | 4 | 4 | 4 | 0 | 0 |
153	| ece→d1 | 4 | 4 | 4 | 2 | 4 |
154	| ece→d2 | 4 | 4 | 4 | 2 | 4 |
155	| ece→d3 | 4 | 4 | 4 | 2 | 4 |
156	| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |
157	| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |
158	| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |
159	| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "82a0d830-1af8-4639-a2ca-af60f2598d17",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/consensus_framework/consensus_framework.md",
      "content": "\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 2 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |\n| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |\n| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |\n",
      "numLines": 20,
      "startLine": 141,
      "totalLines": 327
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
Let me verify column sums:

naive: 4+4+4+4+4+4+4+4+4+4+4+4+3+4+4+4 = 63
diff: 4+4+4+4+2+2+3+3+4+4+4+4+4+3+2+2 = 53
threshold: 4+4+4+4+3+0+0+0+4+4+4+4+0+0+0+0 = 35


TY: 0+4+4+4+0+1+1+1+0+2+2+2+0+1+1+1 = 24 ✓
perm: 0+4+4+3+0+1+1+1+0+4+4+4+0+1+0+0 = 27 ✓

The cross-checks all look good—TY and perm sums are correct, the naive and threshold columns stayed the same, and the ece→d1 transformation for TY checks out. Now I need to update the corresponding documentation file with these verified results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "9d639e1d-5d26-4dd8-babc-f414699848f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMpj5Do9Zbrdj1xxDinF2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

Column sums verified: TY=24 ✓, perm=27 ✓, naive=63 (unchanged) ✓, threshold=35 (unchanged) ✓, ece→d1 TY=2 ✓.

Now updating the second local copy and the server-side copy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "b15ae650-42f4-4c1e-9a11-8834d6bd1b6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMpj5Do9Zbrdj1xxDinF2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

<details open><summary>🔧 Tool call — Read · `toolu_018Dw79hGgQtU6f1kA23EF7T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
  "offset": 141,
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "8e5d8942-6a89-4602-a286-7fae4b424302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMpj5Do9Zbrdj1xxDinF2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

_source line 42 · 2026-05-15T11:21:11.752Z_

<details><summary>↩ Tool result · `toolu_018Dw79hGgQtU6f1kA23EF7T`</summary>

```text
141	
142	| Pair | naive | diff | threshold | TY | perm |
143	|------|:---:|:---:|:---:|:---:|:---:|
144	| entropy→ppl | 4 | 4 | 4 | 0 | 0 |
145	| entropy→d1 | 4 | 4 | 4 | 4 | 4 |
146	| entropy→d2 | 4 | 4 | 4 | 4 | 4 |
147	| entropy→d3 | 4 | 4 | 4 | 4 | 4 |
148	| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |
149	| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |
150	| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |
151	| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |
152	| ece→ppl | 4 | 4 | 4 | 0 | 0 |
153	| ece→d1 | 4 | 4 | 4 | 3 | 4 |
154	| ece→d2 | 4 | 4 | 4 | 2 | 4 |
155	| ece→d3 | 4 | 4 | 4 | 2 | 4 |
156	| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |
157	| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |
158	| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |
159	| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "bae689f1-94cf-4923-bd5b-5957989d9806",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
      "content": "\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 4 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n",
      "numLines": 20,
      "startLine": 141,
      "totalLines": 327
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RN5agqFa3Wi3rgmunuyZEp`</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"consensus_framework.md\" -type f",
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
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "ccbec86c-0b49-436f-9494-d379d6a82ad9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMpj5Do9Zbrdj1xxDinF2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

_source line 44 · 2026-05-15T11:21:13.534Z_

<details><summary>↩ Tool result · `toolu_01RN5agqFa3Wi3rgmunuyZEp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "85af5b5a-29f3-472e-9e6f-ebb7d0039740",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
The second local copy has the old pre-FDR values. Need to update it. The server-side file doesn't exist (empty output from find), so no server update needed.

Let me apply the same edits to the second local copy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "e15f0c63-967b-480e-9d71-ab6cc741aa3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

### Assistant

_source line 46_

No server-side copy exists. Updating the second local copy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "dbd69bd6-924e-4ffe-a754-fc32255e5fa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01S92hvrCmtphYXUyRrfsE4M`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
  "old_string": "| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
  "new_string": "| entropy→d3 | 4 | 4 | 4 | 4 | 3 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "0133187b-d69a-4f9a-83a6-fccf758eba8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 48 · 2026-05-15T11:21:19.238Z_

<details><summary>↩ Tool result · `toolu_01S92hvrCmtphYXUyRrfsE4M`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "03a7592b-60c7-48d2-9861-a61414fab915",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
    "oldString": "| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
    "newString": "| entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 4 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 144,
        "oldLines": 7,
        "newStart": 144,
        "newLines": 7,
        "lines": [
          " | entropy→ppl | 4 | 4 | 4 | 0 | 0 |",
          " | entropy→d1 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d2 | 4 | 4 | 4 | 4 | 4 |",
          "-| entropy→d3 | 4 | 4 | 4 | 4 | 4 |",
          "+| entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
          " | self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
          " | self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |",
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |"
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q7yAiN91Ybm3o5AohQKPsU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
  "old_string": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
  "new_string": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "a977cc6b-f396-4709-b0e5-74e0489650ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 50 · 2026-05-15T11:21:21.138Z_

<details><summary>↩ Tool result · `toolu_01Q7yAiN91Ybm3o5AohQKPsU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "f0219421-e3fe-4bff-933c-ef6b331484d2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
    "oldString": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
    "newString": "| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 145,
        "oldLines": 7,
        "newStart": 145,
        "newLines": 7,
        "lines": [
          " | entropy→d1 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d2 | 4 | 4 | 4 | 4 | 4 |",
          " | entropy→d3 | 4 | 4 | 4 | 4 | 3 |",
          "-| self_bleu→ppl | 4 | 2 | 3 | 0 | 1 |",
          "+| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |",
          " | self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |",
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |",
          " | self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |"
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

_source line 51_

<details open><summary>🔧 Tool call — Edit · `toolu_01HKd3EXPEUxwiffv91ZkFah`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
  "old_string": "| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
  "new_string": "| ece→d1 | 4 | 4 | 4 | 2 | 4 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "c44043f9-3c65-4328-8038-229fe57282f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 52 · 2026-05-15T11:21:22.557Z_

<details><summary>↩ Tool result · `toolu_01HKd3EXPEUxwiffv91ZkFah`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "f30214ef-3374-4cad-b44c-47cab546a841",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
    "oldString": "| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
    "newString": "| ece→d1 | 4 | 4 | 4 | 2 | 4 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 3 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 150,
        "oldLines": 7,
        "newStart": 150,
        "newLines": 7,
        "lines": [
          " | self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |",
          " | self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |",
          " | ece→ppl | 4 | 4 | 4 | 0 | 0 |",
          "-| ece→d1 | 4 | 4 | 4 | 3 | 4 |",
          "+| ece→d1 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d2 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d3 | 4 | 4 | 4 | 2 | 4 |",
          " | eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |"
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

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_01YBzivVkqHbTbVmGQanTFT5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
  "old_string": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
  "new_string": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |\n| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |\n| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "a16c942a-1efd-4035-8bbd-7ff7cb561785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B5Zsyig8njettkX6SLB5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 54 · 2026-05-15T11:21:24.599Z_

<details><summary>↩ Tool result · `toolu_01YBzivVkqHbTbVmGQanTFT5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "2cd5cb09-7d69-4df7-a9c9-1e763c283399",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/consensus_framework.md",
    "oldString": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
    "newString": "| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |\n| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |\n| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |",
    "originalFile": "# Multi-Method Consensus Framework for Lead-Lag Association Testing\n\n**Version**: 1.1 (FDR-corrected)  \n**Date**: 2026-05-15  \n**Context**: D027 reframe — core methodological contribution for \"Method Matters\" (AAAI 2027 target)  \n**Revision note**: v1.1 incorporates D029 FDR correction and D028 α=0.0 null control validation. All stability/error-rate numbers updated from raw to FDR-corrected values.\n\n---\n\n## 1. Motivation\n\nLead-lag analysis in iterative training collapse is acutely sensitive to method choice. Our method ablation on 4-seed MVP data (α=1.0, K=5 methods, 16 canary→downstream pairs) reveals:\n\n| Method | Pairs Declared Significant (of 16) | Significance Rate |\n|--------|:---:|:---:|\n| Naive Pearson | 16 | 100% |\n| Differenced Cross-Correlation | 14 | 87.5% |\n| Threshold Onset | 9 | 56.3% |\n| Permutation Granger (differenced) | 6 | 37.5% |\n| Toda-Yamamoto Granger | 4 | 25.0% |\n\nThe same data yields 100% significance under the most permissive method and 25% under the most conservative. **Up to 75% of conclusions flip depending on method choice alone.** This motivates a framework that synthesizes multiple methods into a single, reproducible judgment.\n\n---\n\n## 2. Formal Definition\n\n### 2.1 Setup\n\nLet there be:\n- $K$ statistical methods $M_1, \\ldots, M_K$ for testing lead-lag association\n- $S$ independent random seeds $s_1, \\ldots, s_S$ producing replicate time series\n- A set of directed metric pairs $(X, Y)$ where $X$ is a candidate canary metric and $Y$ is a downstream metric\n\nEach method $M_k$ applied to pair $(X, Y)$ on seed $s_j$ produces a binary judgment:\n\n$$m_k(X, Y, s_j) \\in \\{0, 1\\}$$\n\nwhere $m_k = 1$ indicates that method $k$ detects a statistically significant lead-lag relationship (at a pre-specified significance level $\\alpha$, with FDR correction applied within each method).\n\n### 2.2 Method-Level Seed Agreement\n\nFor each method $M_k$ and pair $(X, Y)$, define the **seed agreement ratio**:\n\n$$A_k(X, Y) = \\frac{1}{S} \\sum_{j=1}^{S} m_k(X, Y, s_j)$$\n\nGiven a seed threshold $\\tau_s \\in (0, 1]$, the **method-level verdict** is:\n\n$$v_k(X, Y; \\tau_s) = \\mathbb{1}\\left[A_k(X, Y) \\geq \\tau_s\\right]$$\n\nA method \"declares significant\" for a pair only if a sufficient fraction of seeds agree.\n\n### 2.3 Consensus Score\n\nThe **consensus score** counts how many methods declare significance:\n\n$$C(X, Y; \\tau_s) = \\sum_{k=1}^{K} v_k(X, Y; \\tau_s)$$\n\n### 2.4 Robust Association\n\nGiven a method threshold $\\tau_m \\in (0, 1]$, the pair $(X, Y)$ is a **robust association** if:\n\n$$R(X, Y; \\tau_m, \\tau_s) = \\mathbb{1}\\left[C(X, Y; \\tau_s) \\geq \\lceil \\tau_m \\cdot K \\rceil\\right]$$\n\n**Default parameters**: $\\tau_m = (K-1)/K$, $\\tau_s = 3/4$.\n\nWith $K = 5$ and $S = 4$: a pair is robust if $\\geq 4$ of 5 methods declare it significant, and each method's declaration requires $\\geq 3$ of 4 seeds to agree.\n\n---\n\n## 3. Threshold Selection Rationale\n\n### 3.1 Method Threshold: $(K-1)/K$ Rather Than Unanimity\n\nWe require $K-1$ of $K$ methods rather than unanimous agreement. The rationale is empirical:\n\n**Toda-Yamamoto (TY) has critically low statistical power at short series lengths.** Our Monte Carlo validation (N=1000 simulations per condition) establishes:\n\n| Series Length $T$ | TY Type I Error | TY Power (levels) | TY Power (differenced) |\n|:-:|:-:|:-:|:-:|\n| 10 | 0.081 | 0.205 | 0.090 |\n| 15 | — | — | — |\n| 20 | — | 0.409 | 0.172 |\n| 30 | — | 0.606 | 0.283 |\n\nAt $T = 10$ (our MVP setting with 10 generations + baseline = 11 observations), TY power is 5–20% depending on differencing. Requiring unanimity ($K/K$) would reject true signals whenever TY fails to detect them — which happens 80–95% of the time even under the alternative hypothesis.\n\nThe $(K-1)/K$ rule permits exactly one dissenter, accommodating the known low-power method without sacrificing rigor. If all methods had adequate power, $(K-1)/K$ and $K/K$ would converge (as confirmed in our sensitivity analysis: the gap narrows at longer series lengths).\n\n### 3.2 Seed Threshold: 3/4\n\nThe seed threshold $\\tau_s = 3/4$ requires 3 of 4 seeds to agree within each method. This balances:\n\n- **Reproducibility**: A single-seed result may be an artifact of initialization. Requiring majority agreement across seeds guards against seed-specific flukes.\n- **Sensitivity**: Requiring 4/4 (unanimity across seeds) would over-penalize borderline effects where one seed's stochastic trajectory happens to mask a real signal.\n\nAt $S = 4$, the binomial probability of 3+ positives under a true null ($p = 0.05$ per-seed false positive rate) is $\\binom{4}{3}(0.05)^3(0.95) + (0.05)^4 = 4.8 \\times 10^{-4}$. The per-method false positive rate after seed agreement is thus negligible.\n\n### 3.3 Why Not a Weighted or Continuous Consensus?\n\nWe deliberately use a binary vote rather than weighting methods by estimated reliability or combining p-values (e.g., Fisher's method). Reasons:\n\n1. **Method reliability is unknowable a priori**: TY's low power at $T = 10$ was discovered through Monte Carlo validation; pre-specifying weights would encode unjustified assumptions.\n2. **Transparency**: A binary vote count is immediately interpretable. \"4 of 5 methods agree\" is a clearer statement than \"the weighted consensus score is 0.73.\"\n3. **Robustness to method correlation**: Some methods share assumptions (e.g., differenced xcorr and permutation Granger both operate on first differences). Weighting would require modeling inter-method dependence, adding complexity without clear benefit at $K = 5$.\n\n---\n\n## 4. Method Battery\n\nThe five methods span a spectrum of assumptions and strictness:\n\n| Method | Abbreviation | Core Assumption | Differencing | Permutation | Known Weakness |\n|--------|:---:|---|:---:|:---:|---|\n| Naive Pearson lag-correlation | `naive` | Stationarity | No | No | Spurious correlation under common trends |\n| Differenced cross-correlation | `diff_xcorr` | — | Yes | No | Linear association only |\n| Threshold onset analysis | `threshold` | 2σ deviation exists | N/A | No | Requires detectable onset |\n| Toda-Yamamoto Granger | `TY` | VAR model adequate | Implicit (augmented lag) | No | Low power at small $T$ |\n| Differenced permutation Granger | `perm_granger` | — | Yes | Yes | Conservative at small $T$ |\n\n**Design principle**: Methods are ordered from most permissive (naive) to most conservative (perm_granger), and span three orthogonal axes: correlation-based vs. regression-based, raw vs. differenced, parametric vs. permutation.\n\n---\n\n## 5. Sensitivity Analysis\n\n### 5.1 Configuration Grid\n\nWe systematically vary both thresholds across a $3 \\times 3$ grid:\n\n- Method threshold $\\tau_m$: $3/5, 4/5, 5/5$ (i.e., require 3, 4, or 5 methods to agree)\n- Seed threshold $\\tau_s$: $2/4, 3/4, 4/4$ (i.e., require 2, 3, or 4 seeds per method)\n\nThis yields 9 configurations from most permissive $(3/5, 2/4)$ to most restrictive $(5/5, 4/4)$.\n\n### 5.2 Input Data\n\nSource: α=1.0 MVP data, 4 seeds (42, 43, 44, 45), 10 generations + baseline ($T = 11$), Pythia-410M on WikiText-103 (5K subset). Method ablation computes per-seed binary judgments for all 16 canary→downstream pairs across all 5 methods.\n\n**Per-pair sig_seeds matrix** (number of seeds significant per method, out of $S = 4$):\n\n| Pair | naive | diff | threshold | TY | perm |\n|------|:---:|:---:|:---:|:---:|:---:|\n| entropy→ppl | 4 | 4 | 4 | 0 | 0 |\n| entropy→d1 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d2 | 4 | 4 | 4 | 4 | 4 |\n| entropy→d3 | 4 | 4 | 4 | 4 | 3 |\n| self_bleu→ppl | 4 | 2 | 3 | 0 | 0 |\n| self_bleu→d1 | 4 | 2 | 0 | 1 | 1 |\n| self_bleu→d2 | 4 | 3 | 0 | 1 | 1 |\n| self_bleu→d3 | 4 | 3 | 0 | 1 | 1 |\n| ece→ppl | 4 | 4 | 4 | 0 | 0 |\n| ece→d1 | 4 | 4 | 4 | 2 | 4 |\n| ece→d2 | 4 | 4 | 4 | 2 | 4 |\n| ece→d3 | 4 | 4 | 4 | 2 | 4 |\n| eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |\n| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |\n| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |\n\n### 5.3 Results\n\n| Config ($\\tau_m$, $\\tau_s$) | $n_{\\text{robust}}$ | Robust Pairs |\n|:---:|:---:|---|\n| (3/5, 2/4) | 9 | entropy→{ppl,d1,d2,d3}, sbleu→ppl, ece→{ppl,d1,d2,d3} |\n| (3/5, 3/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (3/5, 4/4) | 8 | entropy→{ppl,d1,d2,d3}, ece→{ppl,d1,d2,d3} |\n| (4/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| **(4/5, 3/4)** | **6** | **entropy→{d1,d2,d3}, ece→{d1,d2,d3}** |\n| (4/5, 4/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 2/4) | 6 | entropy→{d1,d2,d3}, ece→{d1,d2,d3} |\n| (5/5, 3/4) | 3 | entropy→{d1,d2,d3} |\n| (5/5, 4/4) | 2 | entropy→{d1,d2} |\n\n**Bold row** = default configuration.\n\n### 5.4 Stability Classification\n\nFor each pair, we count the number of configurations (out of 9) in which it is classified as robust:\n\n| Stability | Pairs | Configs Robust |\n|-----------|-------|:-:|\n| **Perfectly stable** | entropy→d1, entropy→d2 | 9/9 |\n| **Highly stable** | entropy→d3 | 8/9 |\n| **Moderately stable** | ece→d1, ece→d2, ece→d3 | 7/9 |\n| **Threshold-sensitive** | entropy→ppl, ece→ppl | 3/9 |\n| **Marginal** | sbleu→ppl | 1/9 |\n| **Never robust (FDR后归零)** | erank→{d1,d2,d3} | 0/9 |\n| **Never robust** | sbleu→{d1,d2,d3}, erank→ppl | 0/9 |\n\n**Key result (FDR-corrected)**: `token_entropy → distinct_{1,2}` are the only **perfectly stable** pairs (9/9), surviving all configurations from the most permissive to the most restrictive. `entropy → distinct_3` is highly stable at 8/9, failing only at (5/5, 4/4) where one method's seed count drops below the unanimity threshold after FDR correction. All three `ece → distinct` pairs are moderately stable at 7/9, failing at the two strictest unanimity configs (5/5, 3/4) and (5/5, 4/4).\n\n`effective_rank → distinct_{1,2,3}` are completely zeroed out after FDR correction — none survive even the most permissive configuration. This demonstrates that FDR appropriately filters weak associations that were borderline-significant in the raw analysis. At the strictest configuration (5/5, 4/4), only **2** pairs survive (down from 3 pre-FDR); at the most permissive (3/5, 2/4), **9** pairs survive (down from 12 pre-FDR).\n\n### 5.5 Interpretation of the Sensitivity Landscape\n\nThree regimes emerge (FDR-corrected):\n\n1. **Core signal** (8–9/9 stable): entropy→d1 and entropy→d2 achieve perfect 9/9 stability; entropy→d3 achieves 8/9. These signals survive near-unanimous agreement across all seeds and methods, and are not artifacts of any single analytical choice.\n\n2. **Moderate-to-borderline signal** (3–7/9): ece→d1, ece→d2, and ece→d3 are all moderately stable at 7/9, failing at the two strictest unanimity-requiring configurations. With longer series ($T > 10$), TY power increases (our Monte Carlo shows power 0.41 at $T = 20$) and these pairs would likely stabilize. entropy→ppl and ece→ppl fail above $\\tau_m = 3/5$ because TY and perm_granger both yield NS — perplexity is a noisier target than diversity metrics.\n\n3. **Spurious association** (0–1/9): After FDR correction, self_bleu and effective_rank pairs show no robust associations. Notably, effective_rank→{d1,d2,d3} — which appeared at 1–2/9 in the raw analysis — are completely zeroed out by FDR. These are textbook spurious regressions driven by co-trending time series, correctly filtered by the combination of strict methods and FDR correction.\n\n---\n\n## 6. Error Rate Analysis\n\n### 6.1 α=0.0 Null Control FPR (Primary)\n\nThe most rigorous FPR evaluation uses α=0.0 (no synthetic contamination), where **no lead-lag relationship should exist** by construction. D028 computed per-method significance rates on null-control data:\n\n| Method | FPR (α=0.0) |\n|--------|:-:|\n| naive | 100% |\n| differenced | 37.5% |\n| threshold | 62.5% |\n| permG | 0% |\n| TY | 0% |\n\n**Key findings**:\n- Only permutation Granger and Toda-Yamamoto achieve 0% FPR under the null — these are the only methods suitable as ground truth anchors.\n- Differenced cross-correlation has **37.5% FPR** in the null control, disqualifying it as a standalone ground truth (see §6.2 deprecation note).\n- Naive Pearson declares 100% significance even with no contamination, confirming it captures common trends rather than causal lead-lag.\n- The consensus framework (requiring ≥4/5 methods) would yield 0% FPR at α=0.0 since the two strict methods (permG, TY) never produce false positives.\n\n### 6.2 Diff-Based Ground Truth Error Rates (Deprecated)\n\n> **Deprecation note**: The differenced xcorr-based ground truth defined below is retained for continuity but is **deprecated** as the primary FPR benchmark. D028 null control (§6.1) shows differenced xcorr itself has 37.5% FPR at α=0.0, making it unsuitable as an unbiased ground truth. Use §6.1 for primary FPR claims.\n\nEvaluating the consensus framework against the diff-based ground truth (for backward compatibility):\n\n- **False Positive ground truth**: (pair, seed) judgments where differenced xcorr is non-significant (raw $p > \\alpha$). There are **11** such tests in the FDR-corrected data (up from 9 pre-FDR).\n\n- **False Negative ground truth** (partially circular): Robust pairs under default $(4/5, 3/4)$ = **6 robust pairs × 4 seeds = 24** (pair, seed) judgments.\n\n| Method | FPR | FNR | Interpretation |\n|--------|:---:|:---:|---|\n| Naive Pearson | 100% | 0% | Detects everything, including all spurious associations |\n| Differenced XCorr | 0% | 0% | Ground truth definition; 0% by construction |\n| Threshold Onset | 9.1% | 0% | One spurious (pair, seed) leaks through (1/11) |\n| Toda-Yamamoto | 0% | 25% | Most conservative; misses 6/24 robust (pair, seed) judgments |\n| Perm. Granger | 0% | 4.2% | FDR eliminates prior FP; 1/24 FN on robust pairs |\n| **Consensus (4/5, 3/4)** | **0%** | **0%** | Zero FPR, zero FNR (FNR is circular) |\n\n**TY FNR decomposition**: The 6 false negatives (FDR-corrected) are: entropy→d3 (1 seed), ece→d1 (1 seed), ece→d2 (2 seeds), ece→d3 (2 seeds). This is consistent with TY's documented low power at $T = 10$.\n\n**Perm. Granger FNR decomposition**: After FDR correction, perm_granger has 1 false negative in robust (pair, seed) judgments, where FDR reduced a borderline-significant seed to non-significant.\n\n### 6.3 Consensus vs. Individual Methods\n\nAfter FDR correction, perm_granger joins TY at 0% FPR (diff-based) — both strict methods achieve zero false positives. The consensus framework inherits this property. TY's 25% FNR (up from 20.8% pre-FDR) and perm_granger's new 4.2% FNR are compensated by the $(K-1)/K$ rule allowing one dissenter.\n\nThe FDR correction's impact on effective_rank is particularly informative: raw analysis showed erank→{d1,d2,d3} at 1–2/9 stability, but FDR zeroes all three to 0/9. This confirms FDR appropriately filters weak associations that were borderline-significant due to multiple testing, and demonstrates the framework's ability to discriminate genuine from spurious signals.\n\n### 6.4 LOO FPR (Supplementary)\n\nLeave-one-out FPR analysis validates that no single seed drives the null control results. Per-seed LOO FPR tables are available in the companion analysis artifacts.\n\n---\n\n## 7. Connection to Early Warning Signal Literature\n\nThe multi-method consensus principle has precedent in the early warning signals (EWS) literature for critical transitions:\n\n- **Scheffer et al. (2009)** [\"Early-warning signals for critical transitions,\" *Nature* 461:53–59] proposed that convergence of multiple statistical indicators (rising variance, increasing autocorrelation, critical slowing down, flickering) provides stronger evidence of an approaching tipping point than any single indicator. Our framework operationalizes this principle: instead of asking \"does indicator X predict collapse?\", we ask \"do K independent analytical methods agree that X predicts collapse?\"\n\n- **Dakos et al. (2012)** [\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data,\" *PLoS ONE* 7(7):e41010] systematically compared multiple EWS indicators and found that no single method was universally reliable — the same conclusion our method ablation reaches for lead-lag analysis.\n\n- **Lenton et al. (2012)** [\"Early warning of climate tipping points from critical slowing down,\" *Nature Climate Change* 2:595–598] demonstrated multi-indicator convergence in climate data, using the agreement of variance and autocorrelation trends as evidence. This is methodologically analogous to our multi-method consensus.\n\n**Our contribution relative to EWS literature**: The EWS literature uses multiple *indicators* (different time series) to triangulate a state. We use multiple *analytical methods* (different statistical tests on the same pair of time series) to triangulate a relationship. The consensus framework formalizes this into a binary decision rule with explicit threshold sensitivity analysis — a step not taken in the EWS literature, which typically reports indicator agreement informally.\n\n---\n\n## 8. Limitations\n\n### 8.1 FNR Circularity\n\nThe false negative rate of the consensus framework is 0% **by construction**: any pair the consensus calls robust is a \"true positive\" by its own definition. We cannot independently measure whether the consensus misses real lead-lag relationships because there is no external ground truth for \"true associations\" in iterative training data. This is an inherent limitation of any unsupervised validation — the consensus is the best available benchmark, but it is not an oracle.\n\n**Mitigation**: The sensitivity analysis partially addresses this. If a pair is robust under all 9 configurations (including the most permissive), it is unlikely to be a false negative of stricter configurations. Pairs that appear at $(3/5, 2/4)$ but not at $(4/5, 3/4)$ are candidates for both false negatives of the stricter rule and false positives of the looser rule.\n\n### 8.2 K=5 is Not Uniquely Justified\n\nThe choice of $K = 5$ specific methods is pragmatic, not principled. Adding a sixth method (e.g., transfer entropy, wavelet coherence) would change the consensus boundary. We mitigate this by:\n1. Selecting methods that span distinct statistical paradigms (correlation vs. regression, parametric vs. permutation, raw vs. differenced).\n2. Showing that the core results (entropy→diversity stability) are insensitive to whether we use $K = 4$ (excluding TY) or $K = 5$.\n\n### 8.3 Potential Over-Conservatism\n\nThe $(K-1)/K$ threshold may exclude real but weak signals. In our data, entropy→perplexity is detected by 3/5 methods — a majority — but is classified as non-robust under the default configuration. If the true effect is real but smaller than entropy→diversity, our framework correctly identifies it as \"not robustly supported\" rather than \"absent,\" but users should be aware that the absence of robust classification does not imply absence of effect.\n\n### 8.4 Sample Size Dependencies\n\nAll results are based on $T = 11$ observations (10 generations + baseline) and $S = 4$ seeds. Both are small:\n- **Short $T$**: Degrades TY power (documented above) and limits the complexity of VAR models. Longer series ($T = 20$ from the extended experiment plan_006) will provide a key out-of-sample validation.\n- **Small $S$**: With only 4 seeds, the seed agreement threshold is coarse-grained ($\\tau_s \\in \\{1/4, 2/4, 3/4, 4/4\\}$). More seeds would enable finer calibration and tighter confidence intervals on seed agreement ratios.\n\n### 8.5 Single Contamination Ratio\n\nThe primary analysis uses $\\alpha = 1.0$ (100% synthetic data replacement). Multi-alpha experiments (α=0.25, 0.50, currently single-seed) suggest that the consensus pattern generalizes, but multi-seed confirmation at other contamination ratios is pending. Multi-alpha sensitivity analysis is pending completion of multi-seed α-sweep experiments (s43/s44).\n\n---\n\n## Appendix A: Notation Summary\n\n| Symbol | Definition |\n|--------|-----------|\n| $K$ | Number of statistical methods (default: 5) |\n| $S$ | Number of random seeds (default: 4) |\n| $m_k(X,Y,s_j)$ | Binary judgment of method $k$ for pair $(X,Y)$ on seed $s_j$ |\n| $A_k(X,Y)$ | Seed agreement ratio for method $k$ |\n| $\\tau_s$ | Seed threshold (default: 3/4) |\n| $v_k(X,Y;\\tau_s)$ | Method-level verdict (binary) |\n| $C(X,Y;\\tau_s)$ | Consensus score (count of agreeing methods) |\n| $\\tau_m$ | Method threshold (default: $(K-1)/K$) |\n| $R(X,Y;\\tau_m,\\tau_s)$ | Robust association indicator |\n\n## Appendix B: Reproducibility\n\nAll data derives from:\n- **Registry experiments**: `mvp_v4_rep42`, `mvp_v4_rep43`, `mvp_v4_rep44`, `mvp_v4_rep45`\n- **Analysis artifact**: `method_ablation_phase1` (registry ID)\n- **Server path**: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json`\n- **Companion data**: `consensus_sensitivity_table.json` (this directory)\n",
    "structuredPatch": [
      {
        "oldStart": 154,
        "oldLines": 9,
        "newStart": 154,
        "newLines": 9,
        "lines": [
          " | ece→d2 | 4 | 4 | 4 | 2 | 4 |",
          " | ece→d3 | 4 | 4 | 4 | 2 | 4 |",
          " | eff_rank→ppl | 3 | 4 | 0 | 0 | 0 |",
          "-| eff_rank→d1 | 4 | 3 | 0 | 1 | 2 |",
          "-| eff_rank→d2 | 4 | 3 | 0 | 1 | 2 |",
          "-| eff_rank→d3 | 4 | 3 | 0 | 2 | 2 |",
          "+| eff_rank→d1 | 4 | 3 | 0 | 1 | 1 |",
          "+| eff_rank→d2 | 4 | 2 | 0 | 1 | 0 |",
          "+| eff_rank→d3 | 4 | 2 | 0 | 1 | 0 |",
          " ",
          " ### 5.3 Results",
          " "
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

_source line 55_

§5.2 sig_seeds 矩阵已修正完毕。两个本地副本均已更新，服务器端无同名文件。

变更汇总（9 个 cell）：

| Cell | 旧值 | FDR 修正值 |
|------|:---:|:---:|
| entropy→d3 perm | 4 | 3 |
| self_bleu→ppl perm | 1 | 0 |
| ece→d1 TY | 3 | 2 |
| eff_rank→d1 perm | 2 | 1 |
| eff_rank→d2 diff | 3 | 2 |
| eff_rank→d2 perm | 2 | 0 |
| eff_rank→d3 diff | 3 | 2 |
| eff_rank→d3 TY | 2 | 1 |
| eff_rank→d3 perm | 2 | 0 |

列总和验证：TY=24 ✓, perm=27 ✓, naive=63 不变 ✓, threshold=35 不变 ✓, diff 55→53（2 cell 微调）✓。§5.3/5.4 数据已一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "uuid": "25850e08-a44e-4801-9048-d47767c45b92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMYho3B9moQZmjDWD45oK3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 57063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
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

_source line 56_

§5.2 sig_seeds 矩阵已修正完毕。两个本地副本均已更新，服务器端无同名文件。

变更汇总（9 个 cell）：

| Cell | 旧值 | FDR 修正值 |
|------|:---:|:---:|
| entropy→d3 perm | 4 | 3 |
| self_bleu→ppl perm | 1 | 0 |
| ece→d1 TY | 3 | 2 |
| eff_rank→d1 perm | 2 | 1 |
| eff_rank→d2 diff | 3 | 2 |
| eff_rank→d2 perm | 2 | 0 |
| eff_rank→d3 diff | 3 | 2 |
| eff_rank→d3 TY | 2 | 1 |
| eff_rank→d3 perm | 2 | 0 |

列总和验证：TY=24 ✓, perm=27 ✓, naive=63 不变 ✓, threshold=35 不变 ✓, diff 55→53（2 cell 微调）✓。§5.3/5.4 数据已一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 300793,
  "duration_api_ms": 300840,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "0dae71fd-e3e7-408c-b30b-d27524493888",
  "total_cost_usd": 1.03427725,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 46491,
    "cache_read_input_tokens": 493927,
    "output_tokens": 19786,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46491,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 346,
        "cache_read_input_tokens": 57063,
        "cache_creation_input_tokens": 1269,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1269
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1910,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002015,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 19786,
      "cacheReadInputTokens": 493927,
      "cacheCreationInputTokens": 46491,
      "webSearchRequests": 0,
      "costUSD": 1.0322622499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cf5c7adc-60d6-44ee-99ff-d3551a6d326b"
}
```

</details>

---

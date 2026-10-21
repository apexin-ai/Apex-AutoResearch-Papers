# analysis ood baseline check and cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_ood_baseline_check_and_cleanup_20260515T130851.log`
- **Structured JSON:** [`3652e3f65e848663d0bf.json`](../../sessions/36/3652e3f65e848663d0bf.json)

## Before a recorded user message

54 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
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
  "uuid": "8ca100f9-ea62-46b4-8ce8-885bc5edf0fa",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778850600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7d0a7b28-e488-465e-9068-39f89c6136cd",
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this into parallel tasks. I need to:

1. Search for "0.335" on the remote server and locally
2. Check exp_012 results for baseline calculation
3. Check and delete the stale discussion.tex

Let me start by searching both locally and on the remote server in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "87573d57-9bf2-4aab-852d-a2fd1261c1e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiQyNDeDmD5vxCRuHENwrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11542,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11542
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

先并行搜索本地和远程的 "0.335"，同时检查过期文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "8a7150fb-a4fb-47cb-b22a-f29783715805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiQyNDeDmD5vxCRuHENwrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11542,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11542
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XKzbZF4Cah6ri4TFToEYyG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "aef3fe38-3d3b-48b2-a91c-b8dff5e3f8df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiQyNDeDmD5vxCRuHENwrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11542,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11542
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

_source line 7 · 2026-05-15T13:09:03.866Z_

<details><summary>↩ Tool result · `toolu_01XKzbZF4Cah6ri4TFToEYyG`</summary>

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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "8a37633b-ecce-43c9-8a1b-8b021d2177b3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017A3rk3bjErUmzV6Nqrc1J9`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0.335\" /root/autodl-tmp/struct_self_consist_ie/paper/ /root/autodl-tmp/struct_self_consist_ie/sections/ /root/autodl-tmp/struct_self_consist_ie/*.tex",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "0df62ed7-f15b-471e-bf8d-0bceb93cf81c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yr6qmFS38H1HTM6oDSwu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 23243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MU2T6mUd2BcstoJTBxYV1b`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/discussion.tex",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "afdf5cab-77da-4412-a38d-bebbeb675384",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yr6qmFS38H1HTM6oDSwu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 23243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 10 · 2026-05-15T13:09:08.872Z_

<details><summary>↩ Tool result · `toolu_017A3rk3bjErUmzV6Nqrc1J9`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/struct_self_consist_ie/paper/: No such file or directory\\ngrep: /root/autodl-tmp/struct_self_consist_ie/sections/: No such file or directory\\ngrep: /root/autodl-tmp/struct_self_consist_ie/*.tex: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "e49349da-580b-4831-8c4f-c2140269b879",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"grep: /root/autodl-tmp/struct_self_consist_ie/paper/: No such file or directory\\\\ngrep: /root/autodl-tmp/struct_self_consist_ie/sections/: No such file or directory\\\\ngrep: /root/autodl-tmp/struct_self_consist_ie/*.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/struct_self_consist_ie/paper/: No such file or directory\\ngrep: /root/autodl-tmp/struct_self_consist_ie/sections/: No such file or directory\\ngrep: /root/autodl-tmp/struct_self_consist_ie/*.tex: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_017ebqg1DLRHR2wAdSULf2iT`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "ddda7806-6bf4-4a1c-8898-9d1f72b77c95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yr6qmFS38H1HTM6oDSwu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 23243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 12 · 2026-05-15T13:09:09.287Z_

<details><summary>↩ Tool result · `toolu_01MU2T6mUd2BcstoJTBxYV1b`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/discussion.tex': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "ed1763b5-a440-4f70-92dc-dcceeb26cabc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/discussion.tex': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/discussion.tex': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T13:09:09.328Z_

<details><summary>↩ Tool result · `toolu_017ebqg1DLRHR2wAdSULf2iT`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
docs/paper/sections/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/related_work.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/main.tex
docs/paper/sections/appendix.tex
docs/paper/sections/discussion.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "9e53c4ae-30de-4599-b3ac-a91e74e62b2a",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T093336/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/dream_reports/dream_20260514T203201/best/paper.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T203201/worst/paper.tex",
      "artifacts/bootstrap_ci_tables.tex",
      "docs/paper/abstract.tex",
      "docs/paper/discussion.tex",
      "docs/paper/conclusion.tex",
      "artifacts/dream_reports/dream_20260515T092545/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T092545/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T092545/worst/paper.tex",
      "artifacts/_project/paper/freeform_ablation_appendix_table.tex",
      "artifacts/freeform_ablation_appendix_table.tex",
      "docs/paper/sections/method.tex",
      "artifacts/_project/paper/n_scaling_appendix_tables.tex",
      "artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex",
      "artifacts/n_scaling_appendix_tables.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/experiments.tex"
    ],
    "durationMs": 32,
    "numFiles": 38,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

远程没有 paper/sections 目录，discussion.tex 也不存在。搜索本地 tex 文件和远程项目目录结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "12913e90-0317-4a0c-82f8-1e4fb1eac6f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gsYJ2bbEETA6VrVidAGLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 24227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01NqtixMiEPw2ox29mQEDp95`</summary>

```json
{
  "pattern": "0\\.335",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.tex",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "e9d462bb-ea69-4693-94b5-3f43ff6dbb1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gsYJ2bbEETA6VrVidAGLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 24227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 16 · 2026-05-15T13:09:13.928Z_

<details><summary>↩ Tool result · `toolu_01NqtixMiEPw2ox29mQEDp95`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex:279:Notably, on the full RE set, FK actually \emph{outperforms} SJ ($\rhofk\!=\!0.296$ vs.\ $\rhosj\!=\!0.268$) because all-zero instances contribute perfect FK agreement. However, the conditional analysis reverses this: $\rhosj^{\text{cond}}\!=\!0.398$ vs.\ $\rhofk^{\text{cond}}\!=\!0.335$ ($\Delta\!=\!+0.063$), confirming that SJ provides superior signal within the model's capability range.
artifacts/dream_reports/dream_20260515T092545/median/paper.tex:216:\paragraph{Structural signals under free-form.} Table~\ref{tab:freeform-signals} compares all signals across regimes. Structural consistency signals show slight degradation under free-form decoding (SJ: $0.360 \to 0.335$, voting: $0.379 \to 0.358$), likely due to increased output diversity when constraints are removed. Log-probability is the primary beneficiary of free-form generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "d7c09641-c425-4b47-97e9-10290ec6b430",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/dream_reports/dream_20260514T093336/best/paper.tex:279:Notably, on the full RE set, FK actually \\emph{outperforms} SJ ($\\rhofk\\!=\\!0.296$ vs.\\ $\\rhosj\\!=\\!0.268$) because all-zero instances contribute perfect FK agreement. However, the conditional analysis reverses this: $\\rhosj^{\\text{cond}}\\!=\\!0.398$ vs.\\ $\\rhofk^{\\text{cond}}\\!=\\!0.335$ ($\\Delta\\!=\\!+0.063$), confirming that SJ provides superior signal within the model's capability range.\nartifacts/dream_reports/dream_20260515T092545/median/paper.tex:216:\\paragraph{Structural signals under free-form.} Table~\\ref{tab:freeform-signals} compares all signals across regimes. Structural consistency signals show slight degradation under free-form decoding (SJ: $0.360 \\to 0.335$, voting: $0.379 \\to 0.358$), likely due to increased output diversity when constraints are removed. Log-probability is the primary beneficiary of free-form generation.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_013fJBWN3zydD3zrAFJGBUkE`</summary>

```json
{
  "pattern": "0\\.335",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.md",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "d3c84b76-383f-41cc-99f6-f49fa545ca4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gsYJ2bbEETA6VrVidAGLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 24227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 18 · 2026-05-15T13:09:15.170Z_

<details><summary>↩ Tool result · `toolu_013fJBWN3zydD3zrAFJGBUkE`</summary>

```text
artifacts/3seed_ner_summary.md:12:| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |
artifacts/review_reports/round_7_consistency.md:104:| B4 | 无来源不明的 "0.335" | **PASS** | 全文 grep 无匹配 |
artifacts/3seed_summary/3seed_5signal_tables.md:9:| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |
artifacts/exp_001_seed456_v2_ner/report/3seed_ner_summary.md:12:| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |
artifacts/n16_5signal_comparison.md:54:| voting_conf | 0.3473 | 0.3356 | -0.0117 | 0.7059 | 0.6988 | -0.0071 |
artifacts/_project/report/3seed_5signal_tables.md:9:| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |
artifacts/_project/report/round_7_consistency_de165f.md:104:| B4 | 无来源不明的 "0.335" | **PASS** | 全文 grep 无匹配 |
artifacts/_project/report/n16_5signal_comparison.md:54:| voting_conf | 0.3473 | 0.3356 | -0.0117 | 0.7059 | 0.6988 | -0.0071 |
artifacts/_project/report/round_7_consistency.md:104:| B4 | 无来源不明的 "0.335" | **PASS** | 全文 grep 无匹配 |
task_context/director.md:10:- OOD 对比禁止使用 "in-domain avg ρ=0.335" 这个数字——来源不明，Reviewer 已 flag。论文中改为逐信号列举并溯源到 Table 1
task_context/agent.md:12:- exp_011_ood_conll_to_scierc 实际应为 negative（entity schema 不兼容致灾难性失败），Reviewer 要求修正 registry conclusion + 去掉论文中不可验证的 "in-domain 0.335" 对比
task_context/agent.md:37:- Reviewer warnings 修复：exp_011_ood_conll_to_scierc conclusion 改 negative + 去掉 "in-domain 0.335" 不明来源对比
task_context/agent.md:44:- D072 patch 完成 → spawn 补充 patch Worker（OOD section 重写去掉 0.335 + 加 parse rate 99.95% finding + N=16 三种子数据 + appendix tables 整合）
task_context/history/agent/loop_7.md:45:- **Registry 清理指示** → exp_011_ood_conll_to_scierc conclusion 需从 "success" 改 "negative"（ROADMAP 待修复项）；OOD in-domain baseline "0.335" 来源不明需核实
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "9425bfc1-8d13-4c29-9cd5-7f149f520b1f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/3seed_ner_summary.md:12:| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |\nartifacts/review_reports/round_7_consistency.md:104:| B4 | 无来源不明的 \"0.335\" | **PASS** | 全文 grep 无匹配 |\nartifacts/3seed_summary/3seed_5signal_tables.md:9:| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |\nartifacts/exp_001_seed456_v2_ner/report/3seed_ner_summary.md:12:| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |\nartifacts/n16_5signal_comparison.md:54:| voting_conf | 0.3473 | 0.3356 | -0.0117 | 0.7059 | 0.6988 | -0.0071 |\nartifacts/_project/report/3seed_5signal_tables.md:9:| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |\nartifacts/_project/report/round_7_consistency_de165f.md:104:| B4 | 无来源不明的 \"0.335\" | **PASS** | 全文 grep 无匹配 |\nartifacts/_project/report/n16_5signal_comparison.md:54:| voting_conf | 0.3473 | 0.3356 | -0.0117 | 0.7059 | 0.6988 | -0.0071 |\nartifacts/_project/report/round_7_consistency.md:104:| B4 | 无来源不明的 \"0.335\" | **PASS** | 全文 grep 无匹配 |\ntask_context/director.md:10:- OOD 对比禁止使用 \"in-domain avg ρ=0.335\" 这个数字——来源不明，Reviewer 已 flag。论文中改为逐信号列举并溯源到 Table 1\ntask_context/agent.md:12:- exp_011_ood_conll_to_scierc 实际应为 negative（entity schema 不兼容致灾难性失败），Reviewer 要求修正 registry conclusion + 去掉论文中不可验证的 \"in-domain 0.335\" 对比\ntask_context/agent.md:37:- Reviewer warnings 修复：exp_011_ood_conll_to_scierc conclusion 改 negative + 去掉 \"in-domain 0.335\" 不明来源对比\ntask_context/agent.md:44:- D072 patch 完成 → spawn 补充 patch Worker（OOD section 重写去掉 0.335 + 加 parse rate 99.95% finding + N=16 三种子数据 + appendix tables 整合）\ntask_context/history/agent/loop_7.md:45:- **Registry 清理指示** → exp_011_ood_conll_to_scierc conclusion 需从 \"success\" 改 \"negative\"（ROADMAP 待修复项）；OOD in-domain baseline \"0.335\" 来源不明需核实",
    "numLines": 14
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016Efa7JT2dYVk5h3MNwsHwM`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.tex\" -type f",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "1f5a17a3-88a4-405f-8198-c99bf41bb411",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gsYJ2bbEETA6VrVidAGLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 24227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 20 · 2026-05-15T13:09:15.947Z_

<details><summary>↩ Tool result · `toolu_016Efa7JT2dYVk5h3MNwsHwM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_tables.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "d50a78d3-ac49-429b-a2e2-6527651b1b6b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_tables.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_tables.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EE8eEWuiAsLJVVoJw1BLQw`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.py\" -path \"*/exp_012*\" -type f",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "5981a032-7a8e-4e87-9df9-b1f37d8ee34d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gsYJ2bbEETA6VrVidAGLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 24227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 22 · 2026-05-15T13:09:16.794Z_

<details><summary>↩ Tool result · `toolu_01EE8eEWuiAsLJVVoJw1BLQw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "ae853558-14ab-4b2c-819a-c9479d6c5a31",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what I've found:

1. **"0.335" in tex files**: Only found in dream_reports (auto-generated drafts), not in the actual paper sections. The round_7_consistency.md review report says "PASS — 全文 grep 无匹配" meaning it was already removed from the paper.

2. **"0.335" in md files**: 
   - Found in `3seed_ner_summary.md` as EM signal value (0.335 for one seed)
   - The task_context files document that "0.335" was flagged as having unknown provenance and should be removed
   - round_7_consistency.md confirms it was already cleaned from the paper

3. **Remote server**: Only one tex file exists (`bootstrap_ci_tables.tex`), no paper/ or sections/ directory. No discussion.tex exists.

4. **No exp_012 python files found** on server. Now I'm calculating the exp_012 values to trace where "0.335" comes from—averaging the structural rho values across four signals gives me approximately 0.325, which is close to but not exactly 0.335.

Looking at the 3seed data more carefully, I notice that EM has a value of 0.335 in the first seed, which matches what the user mentioned. But when I check the exp_012 values they provided and recalculate the averages, I'm getting different numbers than expected, so there's a discrepancy I need to resolve. I'm tracking down where 0.335 actually comes from. Looking at the dream reports, I see it appears as the SJ score under free-form decoding in one report, and as the FK conditional rho value in another—both from different ablation experiments rather than the OOD averages I was calculating.

Let me check the actual exp_012 results to see if there's a different set of values that might explain this discrepancy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "f16d2f3b-189b-4626-8254-f486d8d9a0da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ftv1ttuC397TjgjDDNZeQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 25483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2105
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

_source line 24_

在本地 tex 文件中未找到 "0.335" 出现在正式论文 sections 中（仅在 dream_reports 自动草稿里）。review 报告已确认论文中已无此数字。让我继续验证 exp_012 的计算和查看更多上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "505a39e5-60a4-4dde-82a6-c9b785bda6ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ftv1ttuC397TjgjDDNZeQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 25483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2105
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

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_014rrw4vAhf3nXSsvoxZBsm7`</summary>

```json
{
  "pattern": "0\\.335",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.json",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "39a1fe2a-6dd9-41f8-b804-d945a14bb0dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ftv1ttuC397TjgjDDNZeQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 25483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2105
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

_source line 26 · 2026-05-15T13:09:43.741Z_

<details><summary>↩ Tool result · `toolu_014rrw4vAhf3nXSsvoxZBsm7`</summary>

```text
artifacts/exp_016_signal_ensemble/report/logistic_ensemble.json:568:      0.3353,
logs/workers/worker_analysis_3seed_summary_20260514T183119_result.json:2:[Omitted long matching line]
artifacts/data/bootstrap_ci_summary.json:231:            "logprob": {"rho": 0.3058, "ci_95": [0.2764, 0.335]}
artifacts/data/qwen_scierc_3seed_em_voting.json:64:          "ece": 0.3355
artifacts/data/qwen_scierc_3seed_em_voting.json:200:          0.3355,
artifacts/dream_reports/dream_20260514T093336/best/experiment_data.json:214:      "re_cond_rho_fk": 0.335,
artifacts/dream_reports/dream_20260515T092545/median/experiment_data.json:319:      "freeform_ner_sj_rho": 0.335,
artifacts/dream_reports/dream_20260515T092545/median/experiment_data.json:527:            0.335,
artifacts/analysis_lp_range_cdf.json:790:      0.33575317604355714,
artifacts/_project/data/bootstrap_ci_summary.json:210:            "logprob": {"rho": 0.3058, "ci_95": [0.2764, 0.335]}
artifacts/_project/data/analysis_lp_range_cdf.json:790:      0.33575317604355714,
logs/workers/worker_paper_figures_core_3figures_20260514T210514_result.json:2:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330_result.json:2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "f4d86ecb-1345-40a1-b7e5-41ffdbefb8fe",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/exp_016_signal_ensemble/report/logistic_ensemble.json:568:      0.3353,\nlogs/workers/worker_analysis_3seed_summary_20260514T183119_result.json:2:[Omitted long matching line]\nartifacts/data/bootstrap_ci_summary.json:231:            \"logprob\": {\"rho\": 0.3058, \"ci_95\": [0.2764, 0.335]}\nartifacts/data/qwen_scierc_3seed_em_voting.json:64:          \"ece\": 0.3355\nartifacts/data/qwen_scierc_3seed_em_voting.json:200:          0.3355,\nartifacts/dream_reports/dream_20260514T093336/best/experiment_data.json:214:      \"re_cond_rho_fk\": 0.335,\nartifacts/dream_reports/dream_20260515T092545/median/experiment_data.json:319:      \"freeform_ner_sj_rho\": 0.335,\nartifacts/dream_reports/dream_20260515T092545/median/experiment_data.json:527:            0.335,\nartifacts/analysis_lp_range_cdf.json:790:      0.33575317604355714,\nartifacts/_project/data/bootstrap_ci_summary.json:210:            \"logprob\": {\"rho\": 0.3058, \"ci_95\": [0.2764, 0.335]}\nartifacts/_project/data/analysis_lp_range_cdf.json:790:      0.33575317604355714,\nlogs/workers/worker_paper_figures_core_3figures_20260514T210514_result.json:2:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330_result.json:2:[Omitted long matching line]",
    "numLines": 13
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_017aKx1dALZNAWSbvsNKoqRj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/3seed_ner_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "f71b3939-639f-475a-8150-753dd0f7fbb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ftv1ttuC397TjgjDDNZeQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 25483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2105
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

_source line 28 · 2026-05-15T13:09:44.273Z_

<details><summary>↩ Tool result · `toolu_017aKx1dALZNAWSbvsNKoqRj`</summary>

```text
1	# 3-Seed NER N=16 Full 5-Signal Summary
2	
3	Dataset: SciERC NER | N=16 samples | Temperature=1.0 | Seeds: 42, 123, 456
4	
5	## Table 1: Spearman ρ (Full Split, n=529)
6	
7	| Signal      | seed42 | seed123 | seed456 | Mean±SD         | CV    |
8	|-------------|--------|---------|---------|-----------------|-------|
9	| SJ          | 0.428  | 0.424   | 0.384   | 0.412±0.025     | 6.0%  |
10	| FK          | 0.281  | 0.275   | 0.223   | 0.260±0.032     | 12.2% |
11	| logprob     | 0.219  | 0.251   | 0.232   | 0.234±0.016     | 6.8%  |
12	| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |
13	| voting_conf | 0.441  | 0.413   | 0.411   | 0.422±0.017     | 3.9%  |
14	
15	## Table 2: Spearman ρ (Conditional Split, greedy F1>0)
16	
17	| Signal      | seed42 (n=477) | seed123 (n=477) | seed456 (n=479) | Mean±SD         | CV    |
18	|-------------|----------------|-----------------|-----------------|-----------------|-------|
19	| SJ          | 0.369          | 0.376           | 0.349           | 0.365±0.014     | 3.7%  |
20	| FK          | 0.193          | 0.178           | 0.157           | 0.176±0.019     | 10.5% |
21	| logprob     | 0.156          | 0.173           | 0.171           | 0.167±0.009     | 5.5%  |
22	| EM          | 0.415          | 0.404           | 0.406           | 0.408±0.006     | 1.5%  |
23	| voting_conf | 0.353          | 0.339           | 0.346           | 0.346±0.007     | 2.0%  |
24	
25	## Table 3: AUROC (Full Split)
26	
27	| Signal      | seed42 | seed123 | seed456 | Mean±SD         |
28	|-------------|--------|---------|---------|-----------------|
29	| SJ          | 0.737  | 0.736   | 0.711   | 0.728±0.015     |
30	| FK          | 0.610  | 0.627   | 0.577   | 0.605±0.025     |
31	| logprob     | 0.587  | 0.606   | 0.594   | 0.596±0.010     |
32	| EM          | 0.790  | 0.781   | 0.768   | 0.780±0.011     |
33	| voting_conf | 0.734  | 0.717   | 0.712   | 0.721±0.012     |
34	
35	## Table 4: AUROC (Conditional Split)
36	
37	| Signal      | seed42 | seed123 | seed456 | Mean±SD         |
38	|-------------|--------|---------|---------|-----------------|
39	| SJ          | 0.719  | 0.721   | 0.699   | 0.713±0.013     |
40	| FK          | 0.589  | 0.605   | 0.561   | 0.585±0.023     |
41	| logprob     | 0.569  | 0.584   | 0.576   | 0.577±0.008     |
42	| EM          | 0.797  | 0.787   | 0.780   | 0.788±0.009     |
43	| voting_conf | 0.712  | 0.698   | 0.694   | 0.701±0.010     |
44	
45	## Table 5: Structural > Surface 判定 (SJ vs FK, Full ρ)
46	
47	| Seed    | SJ ρ  | FK ρ  | Δ(SJ−FK) | Structural > Surface? |
48	|---------|-------|-------|-----------|-----------------------|
49	| seed42  | 0.428 | 0.281 | +0.147    | YES                   |
50	| seed123 | 0.424 | 0.275 | +0.149    | YES                   |
51	| seed456 | 0.384 | 0.223 | +0.160    | YES                   |
52	| **Mean**| 0.412 | 0.260 | +0.152    | **ALL 3/3 PASS**      |
53	
54	## Analysis
55	
56	### Seed Robustness Ranking (by CV of Full ρ)
57	1. **EM** — CV=3.5% (most stable)
58	2. **voting_conf** — CV=3.9%
59	3. **SJ** — CV=6.0%
60	4. **logprob** — CV=6.8%
61	5. **FK** — CV=12.2% (least stable)
62	
63	In conditional split, EM is even more stable (CV=1.5%).
64	
65	### SJ ρ Variability
66	- Mean=0.412, SD=0.025, CV=6.0%
67	- seed42–seed123 Δ=0.004 (near-identical, consistent with ROADMAP)
68	- seed456 drops to 0.384 (Δ=0.044 from seed42)
69	- ROADMAP reported "Δ<0.004" based on 2 seeds — 3rd seed reveals more variance than anticipated
70	
71	### Signal Rankings by Mean ρ
72	- **Full**: voting_conf (0.422) > SJ (0.412) > EM (0.329) > FK (0.260) > logprob (0.234)
73	- **Conditional**: EM (0.408) > SJ (0.365) > voting_conf (0.346) > FK (0.176) > logprob (0.167)
74	
75	### Signal Rankings by Mean AUROC
76	- **Full**: EM (0.780) > SJ (0.728) > voting_conf (0.721) > FK (0.605) > logprob (0.596)
77	- **Conditional**: EM (0.788) > SJ (0.713) > voting_conf (0.701) > FK (0.585) > logprob (0.577)
78	
79	### Key Findings
80	1. **Structural > Surface holds across all 3 seeds** — SJ consistently beats FK by ρ Δ≈0.15
81	2. **EM is the most seed-robust signal** (lowest CV across both splits and both metrics), but it's a discrete signal with limited dynamic range
82	3. **voting_conf ranks #1 in full ρ**, slightly above SJ — both are structural consistency measures
83	4. **EM dominates AUROC** across all splits, suggesting it's the best binary discriminator for perfect-F1 instances
84	5. **FK and logprob are consistently weakest** — surface-level signals have both lower correlation and lower stability
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "7c2d6e2d-78fb-4bbb-90e6-2bf66868cabf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/3seed_ner_summary.md",
      "content": "# 3-Seed NER N=16 Full 5-Signal Summary\n\nDataset: SciERC NER | N=16 samples | Temperature=1.0 | Seeds: 42, 123, 456\n\n## Table 1: Spearman ρ (Full Split, n=529)\n\n| Signal      | seed42 | seed123 | seed456 | Mean±SD         | CV    |\n|-------------|--------|---------|---------|-----------------|-------|\n| SJ          | 0.428  | 0.424   | 0.384   | 0.412±0.025     | 6.0%  |\n| FK          | 0.281  | 0.275   | 0.223   | 0.260±0.032     | 12.2% |\n| logprob     | 0.219  | 0.251   | 0.232   | 0.234±0.016     | 6.8%  |\n| EM          | 0.335  | 0.337   | 0.316   | 0.329±0.011     | 3.5%  |\n| voting_conf | 0.441  | 0.413   | 0.411   | 0.422±0.017     | 3.9%  |\n\n## Table 2: Spearman ρ (Conditional Split, greedy F1>0)\n\n| Signal      | seed42 (n=477) | seed123 (n=477) | seed456 (n=479) | Mean±SD         | CV    |\n|-------------|----------------|-----------------|-----------------|-----------------|-------|\n| SJ          | 0.369          | 0.376           | 0.349           | 0.365±0.014     | 3.7%  |\n| FK          | 0.193          | 0.178           | 0.157           | 0.176±0.019     | 10.5% |\n| logprob     | 0.156          | 0.173           | 0.171           | 0.167±0.009     | 5.5%  |\n| EM          | 0.415          | 0.404           | 0.406           | 0.408±0.006     | 1.5%  |\n| voting_conf | 0.353          | 0.339           | 0.346           | 0.346±0.007     | 2.0%  |\n\n## Table 3: AUROC (Full Split)\n\n| Signal      | seed42 | seed123 | seed456 | Mean±SD         |\n|-------------|--------|---------|---------|-----------------|\n| SJ          | 0.737  | 0.736   | 0.711   | 0.728±0.015     |\n| FK          | 0.610  | 0.627   | 0.577   | 0.605±0.025     |\n| logprob     | 0.587  | 0.606   | 0.594   | 0.596±0.010     |\n| EM          | 0.790  | 0.781   | 0.768   | 0.780±0.011     |\n| voting_conf | 0.734  | 0.717   | 0.712   | 0.721±0.012     |\n\n## Table 4: AUROC (Conditional Split)\n\n| Signal      | seed42 | seed123 | seed456 | Mean±SD         |\n|-------------|--------|---------|---------|-----------------|\n| SJ          | 0.719  | 0.721   | 0.699   | 0.713±0.013     |\n| FK          | 0.589  | 0.605   | 0.561   | 0.585±0.023     |\n| logprob     | 0.569  | 0.584   | 0.576   | 0.577±0.008     |\n| EM          | 0.797  | 0.787   | 0.780   | 0.788±0.009     |\n| voting_conf | 0.712  | 0.698   | 0.694   | 0.701±0.010     |\n\n## Table 5: Structural > Surface 判定 (SJ vs FK, Full ρ)\n\n| Seed    | SJ ρ  | FK ρ  | Δ(SJ−FK) | Structural > Surface? |\n|---------|-------|-------|-----------|-----------------------|\n| seed42  | 0.428 | 0.281 | +0.147    | YES                   |\n| seed123 | 0.424 | 0.275 | +0.149    | YES                   |\n| seed456 | 0.384 | 0.223 | +0.160    | YES                   |\n| **Mean**| 0.412 | 0.260 | +0.152    | **ALL 3/3 PASS**      |\n\n## Analysis\n\n### Seed Robustness Ranking (by CV of Full ρ)\n1. **EM** — CV=3.5% (most stable)\n2. **voting_conf** — CV=3.9%\n3. **SJ** — CV=6.0%\n4. **logprob** — CV=6.8%\n5. **FK** — CV=12.2% (least stable)\n\nIn conditional split, EM is even more stable (CV=1.5%).\n\n### SJ ρ Variability\n- Mean=0.412, SD=0.025, CV=6.0%\n- seed42–seed123 Δ=0.004 (near-identical, consistent with ROADMAP)\n- seed456 drops to 0.384 (Δ=0.044 from seed42)\n- ROADMAP reported \"Δ<0.004\" based on 2 seeds — 3rd seed reveals more variance than anticipated\n\n### Signal Rankings by Mean ρ\n- **Full**: voting_conf (0.422) > SJ (0.412) > EM (0.329) > FK (0.260) > logprob (0.234)\n- **Conditional**: EM (0.408) > SJ (0.365) > voting_conf (0.346) > FK (0.176) > logprob (0.167)\n\n### Signal Rankings by Mean AUROC\n- **Full**: EM (0.780) > SJ (0.728) > voting_conf (0.721) > FK (0.605) > logprob (0.596)\n- **Conditional**: EM (0.788) > SJ (0.713) > voting_conf (0.701) > FK (0.585) > logprob (0.577)\n\n### Key Findings\n1. **Structural > Surface holds across all 3 seeds** — SJ consistently beats FK by ρ Δ≈0.15\n2. **EM is the most seed-robust signal** (lowest CV across both splits and both metrics), but it's a discrete signal with limited dynamic range\n3. **voting_conf ranks #1 in full ρ**, slightly above SJ — both are structural consistency measures\n4. **EM dominates AUROC** across all splits, suggesting it's the best binary discriminator for perfect-F1 instances\n5. **FK and logprob are consistently weakest** — surface-level signals have both lower correlation and lower stability\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01MjPdQSsFtbbcTw3RUHiTBn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/3seed_5signal_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "7ea330b2-bdf3-45da-b848-aac1fd97c995",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ftv1ttuC397TjgjDDNZeQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 25483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2105
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

_source line 30 · 2026-05-15T13:09:44.699Z_

<details><summary>↩ Tool result · `toolu_01MjPdQSsFtbbcTw3RUHiTBn`</summary>

```text
1	# NER 3-Seed 5-Signal Summary (SciERC, N=16, T=1.0, 551 instances)
2	
3	## Table 1: Spearman ρ (Full, n=529)
4	
5	| Signal | seed42 | seed123 | seed456 | Mean | SD |
6	|-------------|--------|---------|---------|-------|-------|
7	| voting_conf | 0.441 | 0.413 | 0.411 | 0.422 | 0.017 |
8	| SJ | 0.428 | 0.424 | 0.384 | 0.412 | 0.025 |
9	| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |
10	| FK | 0.281 | 0.275 | 0.223 | 0.260 | 0.032 |
11	| logprob | 0.219 | 0.251 | 0.232 | 0.234 | 0.016 |
12	
13	## Table 2: Spearman ρ (Conditional, n≈477-479)
14	
15	| Signal | seed42 | seed123 | seed456 | Mean | SD |
16	|-------------|--------|---------|---------|-------|-------|
17	| EM | 0.415 | 0.404 | 0.406 | 0.408 | 0.006 |
18	| SJ | 0.369 | 0.376 | 0.349 | 0.365 | 0.014 |
19	| voting_conf | 0.353 | 0.339 | 0.346 | 0.346 | 0.007 |
20	| FK | 0.193 | 0.178 | 0.157 | 0.176 | 0.019 |
21	| logprob | 0.156 | 0.173 | 0.171 | 0.166 | 0.009 |
22	
23	## Table 3: AUROC (Full, n=529)
24	
25	| Signal | seed42 | seed123 | seed456 | Mean | SD |
26	|-------------|--------|---------|---------|-------|-------|
27	| EM | 0.790 | 0.781 | 0.768 | 0.780 | 0.011 |
28	| SJ | 0.737 | 0.736 | 0.711 | 0.728 | 0.015 |
29	| voting_conf | 0.734 | 0.717 | 0.712 | 0.721 | 0.012 |
30	| FK | 0.610 | 0.627 | 0.577 | 0.605 | 0.025 |
31	| logprob | 0.587 | 0.606 | 0.594 | 0.596 | 0.010 |
32	
33	## Table 4: AUROC (Conditional, n≈477-479)
34	
35	| Signal | seed42 | seed123 | seed456 | Mean | SD |
36	|-------------|--------|---------|---------|-------|-------|
37	| EM | 0.797 | 0.787 | 0.780 | 0.788 | 0.009 |
38	| SJ | 0.719 | 0.721 | 0.699 | 0.713 | 0.013 |
39	| voting_conf | 0.712 | 0.698 | 0.694 | 0.701 | 0.010 |
40	| FK | 0.589 | 0.605 | 0.561 | 0.585 | 0.023 |
41	| logprob | 0.569 | 0.584 | 0.576 | 0.577 | 0.008 |
42	
43	## Key Findings
44	
45	- **structural > surface: 3/3 seeds.** SJ beats FK in all seeds; all structure-based signals (EM, SJ, voting_conf) beat logprob.
46	- **Ranking stability:** Top-3 (EM, SJ, voting_conf) vs bottom-2 (FK, logprob) is perfectly consistent across all seeds and both splits.
47	- **Conditional split ranking is perfectly consistent:** EM > SJ > voting_conf > FK > logprob in all 3 seeds.
48	- **EM leads in AUROC** (0.780 full, 0.788 conditional) despite mid-tier ρ — it's the best binary discriminator.
49	- **voting_conf and SJ trade #1 in full ρ** — practically tied (0.422 vs 0.412), but SJ has higher SD (0.025 vs 0.017).
50	- **FK and logprob are the weakest signals** with mean ρ < 0.26 full, < 0.18 conditional.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "b117a7f2-afa5-42b3-a5ed-d0d3b491d0cb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/3seed_5signal_tables.md",
      "content": "# NER 3-Seed 5-Signal Summary (SciERC, N=16, T=1.0, 551 instances)\n\n## Table 1: Spearman ρ (Full, n=529)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| voting_conf | 0.441 | 0.413 | 0.411 | 0.422 | 0.017 |\n| SJ | 0.428 | 0.424 | 0.384 | 0.412 | 0.025 |\n| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |\n| FK | 0.281 | 0.275 | 0.223 | 0.260 | 0.032 |\n| logprob | 0.219 | 0.251 | 0.232 | 0.234 | 0.016 |\n\n## Table 2: Spearman ρ (Conditional, n≈477-479)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.415 | 0.404 | 0.406 | 0.408 | 0.006 |\n| SJ | 0.369 | 0.376 | 0.349 | 0.365 | 0.014 |\n| voting_conf | 0.353 | 0.339 | 0.346 | 0.346 | 0.007 |\n| FK | 0.193 | 0.178 | 0.157 | 0.176 | 0.019 |\n| logprob | 0.156 | 0.173 | 0.171 | 0.166 | 0.009 |\n\n## Table 3: AUROC (Full, n=529)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.790 | 0.781 | 0.768 | 0.780 | 0.011 |\n| SJ | 0.737 | 0.736 | 0.711 | 0.728 | 0.015 |\n| voting_conf | 0.734 | 0.717 | 0.712 | 0.721 | 0.012 |\n| FK | 0.610 | 0.627 | 0.577 | 0.605 | 0.025 |\n| logprob | 0.587 | 0.606 | 0.594 | 0.596 | 0.010 |\n\n## Table 4: AUROC (Conditional, n≈477-479)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.797 | 0.787 | 0.780 | 0.788 | 0.009 |\n| SJ | 0.719 | 0.721 | 0.699 | 0.713 | 0.013 |\n| voting_conf | 0.712 | 0.698 | 0.694 | 0.701 | 0.010 |\n| FK | 0.589 | 0.605 | 0.561 | 0.585 | 0.023 |\n| logprob | 0.569 | 0.584 | 0.576 | 0.577 | 0.008 |\n\n## Key Findings\n\n- **structural > surface: 3/3 seeds.** SJ beats FK in all seeds; all structure-based signals (EM, SJ, voting_conf) beat logprob.\n- **Ranking stability:** Top-3 (EM, SJ, voting_conf) vs bottom-2 (FK, logprob) is perfectly consistent across all seeds and both splits.\n- **Conditional split ranking is perfectly consistent:** EM > SJ > voting_conf > FK > logprob in all 3 seeds.\n- **EM leads in AUROC** (0.780 full, 0.788 conditional) despite mid-tier ρ — it's the best binary discriminator.\n- **voting_conf and SJ trade #1 in full ρ** — practically tied (0.422 vs 0.412), but SJ has higher SD (0.025 vs 0.017).\n- **FK and logprob are the weakest signals** with mean ρ < 0.26 full, < 0.18 conditional.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check what the exp_012 results look like to verify the user's numbers. Let me search for exp_012 results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "52582547-3be0-4da9-b4e2-71e287ed59d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cug91gbKEmWyMrUdmxyzp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 27588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

_source line 32_

现在让我查看 exp_012 的原始数据，验证用户提供的数值，并检查 "0.335" 的可能计算来源。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "5639aad4-3b8d-4b44-b69c-4c50d5c207ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cug91gbKEmWyMrUdmxyzp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 27588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

<details open><summary>🔧 Tool call — Grep · `toolu_01L9psEWEj6PpL6GG9pqzLUk`</summary>

```json
{
  "pattern": "exp_012.*rerun|rerun.*1024",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.md",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "a9583f1d-b06a-488c-ab22-66320817517e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cug91gbKEmWyMrUdmxyzp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 27588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

_source line 34 · 2026-05-15T13:09:50.072Z_

<details><summary>↩ Tool result · `toolu_01L9psEWEj6PpL6GG9pqzLUk`</summary>

```text
Found 37 files
artifacts/_project/report/round_7_consistency_de165f.md
artifacts/_project/report/round_7_consistency.md
artifacts/review_reports/round_7_consistency.md
task_context/agent.md
task_context/history/agent/loop_7.md
artifacts/_project/report/multiseed_flip_overlap_analysis.md
artifacts/multiseed_flip_overlap_analysis.md
artifacts/_project/report/freeform_ablation_deep_analysis.md
artifacts/freeform_ablation_deep_analysis.md
task_context/history/director/loop_3.md
paper_framing.md
artifacts/dream_reports/dream_20260515T092545/worst/paper_framing.md
artifacts/exp_freeform_ablation/report/freeform_ablation_results.md
artifacts/freeform_ablation_results.md
artifacts/dream_reports/dream_20260515T092545/median/paper_framing.md
artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md
task_context/history/agent/loop_6_1778848220.md
artifacts/_project/report/vc_implementation_rho_diff.md
artifacts/vc_implementation_rho_diff.md
artifacts/_project/data/tost_breakpoint_delta_star.md
artifacts/tost_breakpoint_delta_star.md
task_context/history/agent/loop_6.md
artifacts/_project/report/logprob_tie_analysis_n529.md
artifacts/_project/report/re_nonzero_selection_n397.md
artifacts/_project/report/logprob_tie_analysis.md
artifacts/logprob_tie_analysis.md
artifacts/_project/report/re_nonzero_selection_analysis.md
artifacts/re_nonzero_selection_analysis.md
memory.md
artifacts/_project/report/multi_seed_stability_table.md
artifacts/multi_seed_stability_table.md
artifacts/exp_018_provenance_report.md
artifacts/exp_018/report/exp_018_provenance_report.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_5.md
task_context/history/agent/loop_3_1778814715.md
task_context/history/agent/loop_4.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "a5329e53-ac85-4728-ac54-8e91257181b8",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/report/round_7_consistency_de165f.md",
      "artifacts/_project/report/round_7_consistency.md",
      "artifacts/review_reports/round_7_consistency.md",
      "task_context/agent.md",
      "task_context/history/agent/loop_7.md",
      "artifacts/_project/report/multiseed_flip_overlap_analysis.md",
      "artifacts/multiseed_flip_overlap_analysis.md",
      "artifacts/_project/report/freeform_ablation_deep_analysis.md",
      "artifacts/freeform_ablation_deep_analysis.md",
      "task_context/history/director/loop_3.md",
      "paper_framing.md",
      "artifacts/dream_reports/dream_20260515T092545/worst/paper_framing.md",
      "artifacts/exp_freeform_ablation/report/freeform_ablation_results.md",
      "artifacts/freeform_ablation_results.md",
      "artifacts/dream_reports/dream_20260515T092545/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md",
      "task_context/history/agent/loop_6_1778848220.md",
      "artifacts/_project/report/vc_implementation_rho_diff.md",
      "artifacts/vc_implementation_rho_diff.md",
      "artifacts/_project/data/tost_breakpoint_delta_star.md",
      "artifacts/tost_breakpoint_delta_star.md",
      "task_context/history/agent/loop_6.md",
      "artifacts/_project/report/logprob_tie_analysis_n529.md",
      "artifacts/_project/report/re_nonzero_selection_n397.md",
      "artifacts/_project/report/logprob_tie_analysis.md",
      "artifacts/logprob_tie_analysis.md",
      "artifacts/_project/report/re_nonzero_selection_analysis.md",
      "artifacts/re_nonzero_selection_analysis.md",
      "memory.md",
      "artifacts/_project/report/multi_seed_stability_table.md",
      "artifacts/multi_seed_stability_table.md",
      "artifacts/exp_018_provenance_report.md",
      "artifacts/exp_018/report/exp_018_provenance_report.md",
      "task_context/history/reviewer/loop_5.md",
      "task_context/history/agent/loop_5.md",
      "task_context/history/agent/loop_3_1778814715.md",
      "task_context/history/agent/loop_4.md"
    ],
    "numFiles": 37
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_016DjRyXPUkS7ydXLaoN3W8g`</summary>

```json
{
  "pattern": "in-domain.*0\\.335|0\\.335.*in-domain",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "269369c5-985c-45f1-b740-c22c6917e9a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cug91gbKEmWyMrUdmxyzp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 27588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

_source line 36 · 2026-05-15T13:09:51.668Z_

<details><summary>↩ Tool result · `toolu_016DjRyXPUkS7ydXLaoN3W8g`</summary>

```text
artifacts/dream_reports/dream_20260515T092545/logs/review_median.log:16:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:5:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:12:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:13:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:21:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:27:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/phase2_median_attempt0.log:4:[Omitted long matching line]
artifacts/dream_reports/dream_20260515T092545/logs/phase2_median_attempt0.log:5:[Omitted long matching line]
task_context/history/agent/loop_7.md:45:- **Registry 清理指示** → exp_011_ood_conll_to_scierc conclusion 需从 "success" 改 "negative"（ROADMAP 待修复项）；OOD in-domain baseline "0.335" 来源不明需核实
task_context/director.md:10:- OOD 对比禁止使用 "in-domain avg ρ=0.335" 这个数字——来源不明，Reviewer 已 flag。论文中改为逐信号列举并溯源到 Table 1
task_context/agent.md:12:- exp_011_ood_conll_to_scierc 实际应为 negative（entity schema 不兼容致灾难性失败），Reviewer 要求修正 registry conclusion + 去掉论文中不可验证的 "in-domain 0.335" 对比
task_context/agent.md:37:- Reviewer warnings 修复：exp_011_ood_conll_to_scierc conclusion 改 negative + 去掉 "in-domain 0.335" 不明来源对比
logs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:1:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:11:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:55:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:58:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:80:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:15:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:63:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:104:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:114:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:185:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:213:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:227:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:232:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:578:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:592:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:606:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:613:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:618:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:727:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:317:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:351:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:353:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:355:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:360:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:361:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:363:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:364:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:365:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:370:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:378:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:398:[Omitted long matching line]
logs/chats/archive/cron_hook_exp_018_llama_scierc_seed456_r1024_20260515T123841_368523.jsonl:73:[Omitted long matching line]
logs/chats/archive/cron_hook_exp_018_llama_scierc_seed456_r1024_20260515T123841_368523.jsonl:96:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T123212_169592.jsonl:1779:[Omitted long matching line]
logs/chats/archive/cron_hook_exp_018_llama_scierc_seed42_r1024_20260515T123020_062696.jsonl:75:[Omitted long matching line]
logs/chats/archive/cron_hook_exp_018_llama_scierc_seed42_r1024_20260515T123020_062696.jsonl:96:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:1:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:11:[Omitted long matching line]
logs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:16:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4726:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4743:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4764:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4766:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4767:[Omitted long matching line]
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4777:[Omitted long matching line]
logs/chats/worker_review_round7_consistency_20260515T124330.jsonl:61:[Omitted long matching line]
logs/chats/worker_review_round7_consistency_20260515T124330.jsonl:65:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:1:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:23:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:33:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:40:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:69:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:78:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:106:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:140:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:163:[Omitted long matching line]
logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:195:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330.log:54:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330.log:84:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330.log:85:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330.log:88:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330.log:89:[Omitted long matching line]
logs/workers/worker_analysis_ood_baseline_check_and_cleanup_20260515T130851.log:18:[Omitted long matching line]
logs/workers/worker_review_round7_consistency_20260515T124330_result.json:2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "8a31b577-dc2f-4d42-afae-464d9a4db759",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/dream_reports/dream_20260515T092545/logs/review_median.log:16:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:5:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:12:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:13:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:21:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/paper_agent_median.log:27:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/phase2_median_attempt0.log:4:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T092545/logs/phase2_median_attempt0.log:5:[Omitted long matching line]\ntask_context/history/agent/loop_7.md:45:- **Registry 清理指示** → exp_011_ood_conll_to_scierc conclusion 需从 \"success\" 改 \"negative\"（ROADMAP 待修复项）；OOD in-domain baseline \"0.335\" 来源不明需核实\ntask_context/director.md:10:- OOD 对比禁止使用 \"in-domain avg ρ=0.335\" 这个数字——来源不明，Reviewer 已 flag。论文中改为逐信号列举并溯源到 Table 1\ntask_context/agent.md:12:- exp_011_ood_conll_to_scierc 实际应为 negative（entity schema 不兼容致灾难性失败），Reviewer 要求修正 registry conclusion + 去掉论文中不可验证的 \"in-domain 0.335\" 对比\ntask_context/agent.md:37:- Reviewer warnings 修复：exp_011_ood_conll_to_scierc conclusion 改 negative + 去掉 \"in-domain 0.335\" 不明来源对比\nlogs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:1:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:11:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:55:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:58:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed456_r1024.jsonl:80:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:15:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:63:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:104:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:114:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:185:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:213:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:227:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl:232:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:578:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:592:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:606:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:613:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:618:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl:727:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:317:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:351:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:353:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:355:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:360:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:361:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:363:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:364:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:365:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:370:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:378:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T123722_244476.jsonl:398:[Omitted long matching line]\nlogs/chats/archive/cron_hook_exp_018_llama_scierc_seed456_r1024_20260515T123841_368523.jsonl:73:[Omitted long matching line]\nlogs/chats/archive/cron_hook_exp_018_llama_scierc_seed456_r1024_20260515T123841_368523.jsonl:96:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T123212_169592.jsonl:1779:[Omitted long matching line]\nlogs/chats/archive/cron_hook_exp_018_llama_scierc_seed42_r1024_20260515T123020_062696.jsonl:75:[Omitted long matching line]\nlogs/chats/archive/cron_hook_exp_018_llama_scierc_seed42_r1024_20260515T123020_062696.jsonl:96:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:1:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:11:[Omitted long matching line]\nlogs/chats/cron_hook_exp_018_llama_scierc_seed42_r1024.jsonl:16:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4726:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4743:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4764:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4766:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4767:[Omitted long matching line]\nlogs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl:4777:[Omitted long matching line]\nlogs/chats/worker_review_round7_consistency_20260515T124330.jsonl:61:[Omitted long matching line]\nlogs/chats/worker_review_round7_consistency_20260515T124330.jsonl:65:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:1:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:23:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:33:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:40:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:69:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:78:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:106:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:140:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:163:[Omitted long matching line]\nlogs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:195:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330.log:54:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330.log:84:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330.log:85:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330.log:88:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330.log:89:[Omitted long matching line]\nlogs/workers/worker_analysis_ood_baseline_check_and_cleanup_20260515T130851.log:18:[Omitted long matching line]\nlogs/workers/worker_review_round7_consistency_20260515T124330_result.json:2:[Omitted long matching line]",
    "numLines": 76
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01Rb9hvtXTvmh1uoqZqYtqM1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "218da4dd-0247-4ffe-912f-237e33380f04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cug91gbKEmWyMrUdmxyzp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 27588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

_source line 38 · 2026-05-15T13:09:51.960Z_

<details><summary>↩ Tool result · `toolu_01Rb9hvtXTvmh1uoqZqYtqM1`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\ref{app:n_scaling}. A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances separates binary success detection (can the model extract \textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.
79	This reshuffles signal rankings (Figure~\ref{fig:signal_heatmap}, right).
80	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
81	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
82	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
83	
84	%% ============================================================
85	\subsection{The Correlation-Selection Gap}
86	\label{sec:selection_gap}
87	
88	\begin{figure*}[t]
89	\centering
90	\includegraphics[width=\textwidth]{fig_selection_gap}
91	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
92	\label{fig:selection_gap}
93	\end{figure*}
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\ref{eq:voting}).}
99	\label{tab:selection}
100	\begin{tabular}{lcc}
101	\toprule
102	Method & NER F1 & RE F1 \\
103	\midrule
104	Oracle & 0.776 & 0.585 \\
105	\midrule
106	LP           & \textbf{0.650} & 0.395 \\
107	SJ       & 0.645 & 0.386 \\
108	EM        & 0.636 & 0.372 \\
109	VC                 & 0.634 & 0.359 \\
110	\midrule
111	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
112	Random             & 0.608 & 0.354 \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
118	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
119	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
120	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
121	
122	\paragraph{No significant improvement over greedy.}
123	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
124	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
125	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
126	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\ref{app:lp_failure_stability}).
127	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
128	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{significantly below} greedy ($\Delta{=}{-}2.6$~pp, $p{<}0.03$ across 3 seeds).
129	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
130	
131	\paragraph{Quality estimation $\neq$ output selection.}
132	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
133	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
134	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
135	
136	%% ============================================================
137	\subsection{Robustness}
138	\label{sec:robustness_main}
139	
140	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
141	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
142	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "30e317ed-4143-4ebd-9867-2a872031c237",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}. A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{Semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances separates binary success detection (can the model extract \\textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.\nThis reshuffles signal rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\\ref{eq:voting}).}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\\ref{app:lp_failure_stability}).\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{significantly below} greedy ($\\Delta{=}{-}2.6$~pp, $p{<}0.03$ across 3 seeds).\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nOn RE, only VC consistently outperforms LP ($\\Delta\\rho{=}{+}0.012$, preliminary).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
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
Now I have a clear picture. Let me search for the exp_012 data specifically to check the numbers the user provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "50c3685a-974e-4a7c-8e6a-e5c06080d151",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YeZZNRXZiJnbyK4MDaYRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9662,
      "cache_read_input_tokens": 33020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9662
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

论文正文 tex 中没有 "0.335"。让我检查 exp_012 的原始数值来验证用户提供的计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "be9483a1-26fb-4c79-8e00-4f838a3ac87f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YeZZNRXZiJnbyK4MDaYRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9662,
      "cache_read_input_tokens": 33020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9662
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

<details open><summary>🔧 Tool call — Grep · `toolu_012X3iJ8AbGSiovtnkz99hDs`</summary>

```json
{
  "pattern": "exp_012.*NER|SJ.*0\\.359|FK.*0\\.266|EM.*0\\.294|VC.*0\\.379",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.md",
  "output_mode": "files_with_matches",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "86db29c6-6aa1-461b-b745-5b1948c3ab2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YeZZNRXZiJnbyK4MDaYRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9662,
      "cache_read_input_tokens": 33020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9662
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

_source line 42 · 2026-05-15T13:09:59.099Z_

<details><summary>↩ Tool result · `toolu_012X3iJ8AbGSiovtnkz99hDs`</summary>

```text
Found 10 files limit: 10
artifacts/_project/report/round_7_consistency_de165f.md
artifacts/_project/report/round_7_consistency.md
artifacts/review_reports/round_7_consistency.md
artifacts/_project/report/d072_paper_patch_inventory.md
artifacts/d072_paper_patch_inventory.md
paper_framing.md
artifacts/exp_freeform_ablation/report/freeform_ablation_results.md
artifacts/freeform_ablation_results.md
artifacts/_project/report/vc_implementation_rho_diff.md
artifacts/vc_implementation_rho_diff.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "0f2a0053-50dd-44b3-a3fe-fe275d801b4b",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/report/round_7_consistency_de165f.md",
      "artifacts/_project/report/round_7_consistency.md",
      "artifacts/review_reports/round_7_consistency.md",
      "artifacts/_project/report/d072_paper_patch_inventory.md",
      "artifacts/d072_paper_patch_inventory.md",
      "paper_framing.md",
      "artifacts/exp_freeform_ablation/report/freeform_ablation_results.md",
      "artifacts/freeform_ablation_results.md",
      "artifacts/_project/report/vc_implementation_rho_diff.md",
      "artifacts/vc_implementation_rho_diff.md"
    ],
    "numFiles": 10,
    "appliedLimit": 10
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_0157gxkpHYJEPtZaiYT74EWp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "2ddef85f-4e17-463f-bf03-c3e6219f3eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YeZZNRXZiJnbyK4MDaYRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9662,
      "cache_read_input_tokens": 33020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9662
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

_source line 44 · 2026-05-15T13:09:59.695Z_

<details><summary>↩ Tool result · `toolu_0157gxkpHYJEPtZaiYT74EWp`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled NER ablation (\S\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{Connection to MBR decoding.}
20	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
21	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
22	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
23	
24	\paragraph{Score compression under free-form decoding.}\label{sec:ablation}
25	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
26	We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
27	For NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.
28	However, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).
29	This reversal falls within the NER bootstrap 95\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.
30	The NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.
31	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
32	
33	\paragraph{Task-specific decoding interactions.}
34	The free-form ablation reveals divergent behavior across tasks.
35	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
36	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
37	This interaction does not generalize to NER, where selection remains negligible under both regimes.
38	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
39	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
40	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
41	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
42	
43	\paragraph{Methodological implications.}
44	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
45	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.
46	Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
47	Our findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.
48	Whether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "49d17ece-ca30-4475-9083-835e0b6f6324",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) with lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\\varepsilon{=}0.05$ threshold at which 60\\% of instances are effectively tied, and 75\\% of pairwise comparisons fall within $|\\Delta|{<}0.026$ (Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled NER ablation (\\S\\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression under free-form decoding.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nFor NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.\nHowever, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).\nThis reversal falls within the NER bootstrap 95\\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.\nThe NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.\nCross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\nOur findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.\nWhether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
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
Now I have the full picture. Let me check the OOD appendix section to see how in-domain is referenced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "d99f2a11-5b10-45e1-9099-b79ba6aecf22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbBeLvf3vpiQHR7EWkgHcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 42682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2771
      },
      "output_tokens": 8,
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

### Assistant

_source line 46_

论文 discussion.tex 第 46 行提到 OOD 对比："VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain"——用的是 0.379 而非 0.335。让我检查 OOD appendix 部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "b9b691f6-3dc9-48eb-8510-2c235db6af73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbBeLvf3vpiQHR7EWkgHcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 42682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2771
      },
      "output_tokens": 8,
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

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01CuXPDVCkfBhV5wfYoBmGXU`</summary>

```json
{
  "pattern": "in-domain|ood|OOD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "glob": "*.tex",
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
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "663bc379-c0e3-44d3-97db-bc561c5ecf41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbBeLvf3vpiQHR7EWkgHcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 42682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2771
      },
      "output_tokens": 8,
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

_source line 48 · 2026-05-15T13:10:05.399Z_

<details><summary>↩ Tool result · `toolu_01CuXPDVCkfBhV5wfYoBmGXU`</summary>

```text
docs/paper/sections/discussion.tex:46:Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
docs/paper/sections/appendix.tex:22:LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
docs/paper/sections/appendix.tex:642:\section{Cross-Dataset OOD Analysis}\label{app:ood}
docs/paper/sections/appendix.tex:644:To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
docs/paper/sections/appendix.tex:649:\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
docs/paper/sections/appendix.tex:650:\label{tab:ood}
docs/paper/sections/appendix.tex:667:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
docs/paper/sections/appendix.tex:673:Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "03cd32c0-52b6-4492-8f27-4d80e4a5ad22",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/discussion.tex:46:Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\ndocs/paper/sections/appendix.tex:22:LP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\ndocs/paper/sections/appendix.tex:642:\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\ndocs/paper/sections/appendix.tex:644:To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\ndocs/paper/sections/appendix.tex:649:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\ndocs/paper/sections/appendix.tex:650:\\label{tab:ood}\ndocs/paper/sections/appendix.tex:667:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\ndocs/paper/sections/appendix.tex:673:Under this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).",
    "numLines": 8
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01FzYrvVoEDq4deRQfRFyvLw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "958e7342-e032-47e8-9eb5-6dbe3c72956b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbBeLvf3vpiQHR7EWkgHcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 42682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2771
      },
      "output_tokens": 8,
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

_source line 50 · 2026-05-15T13:10:05.979Z_

<details><summary>↩ Tool result · `toolu_01FzYrvVoEDq4deRQfRFyvLw`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
82	
83	\paragraph{Transfer across model families.}
84	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$).
85	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
86	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
87	
88	\section{Calibration Analysis}\label{app:calibration}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{fig_reliability}
93	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
94	\label{fig:reliability}
95	\end{figure*}
96	
97	Reliability diagrams use 10 equal-width bins.
98	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
99	
100	\section{Additional Analyses}\label{app:additional}
101	
102	\paragraph{Per-relation diagnostic.}
103	RE signal degradation is relation-specific.
104	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
105	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
106	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
107	
108	\paragraph{Capability stratification.}
109	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
110	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
111	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
112	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
113	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
114	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
115	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
116	
117	\paragraph{Length vs.\ log-probability.}
118	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
123	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
124	\label{fig:length_logprob_scatter}
125	\end{figure}
126	
127	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
128	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
130	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
131	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
132	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
133	Evaluation circularity is negligible.
134	
135	\paragraph{Conditional filtering details.}
136	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
137	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
138	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
139	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
140	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
141	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
142	
143	\paragraph{WNUT-17 full signal analysis.}
144	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
145	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
146	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
147	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
153	\label{tab:wnut}
154	\begin{tabular}{lccccc}
155	\toprule
156	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
157	\midrule
158	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
159	FK      & .125 & .001 & .555 & .169 & .002 \\
160	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
161	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
162	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{Cross-configuration selection analysis.}
168	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
169	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
170	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
171	
172	\begin{table*}[t]
173	\centering
174	\small
175	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
176	\label{tab:cross_selection}
177	\begin{tabular}{llccccccc}
178	\toprule
179	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
180	\midrule
181	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
182	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
183	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
184	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
185	\bottomrule
186	\end{tabular}
187	\end{table*}
188	
189	\paragraph{Diminishing returns of $N$-scaling.}
190	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
191	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
192	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
193	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
194	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
195	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
196	
197	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
198	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
199	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
200	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
201	This reinforces the core finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
202	
203	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
204	
205	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
206	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
207	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
208	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
214	\label{tab:bootstrap_signal_ci}
215	\begin{tabular}{lcc}
216	\toprule
217	Signal & $\rho$ & 95\% CI \\
218	\midrule
219	VC & +0.379 & [+0.299, +0.456] \\
220	SJ & +0.360 & [+0.277, +0.437] \\
221	EM & +0.295 & [+0.212, +0.371] \\
222	FK & +0.267 & [+0.176, +0.354] \\
223	LP & +0.205 & [+0.119, +0.291] \\
224	\bottomrule
225	\end{tabular}
226	
227	\vspace{0.5em}
228	
229	\begin{tabular}{lccc}
230	\toprule
231	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
232	\midrule
233	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
234	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
235	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
236	\bottomrule
237	\end{tabular}
238	
239	\smallskip
240	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
241	\end{table}
242	
243	\section{Diversity and Selection Analysis}\label{app:diversity}
244	
245	\paragraph{Output diversity quantification.}
246	Table~\ref{tab:diversity} summarizes output diversity across configurations.
247	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
248	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
249	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
250	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
256	\label{tab:diversity}
257	\begin{tabular}{lcc}
258	\toprule
259	Config & Identical & Unique \\
260	\midrule
261	Qwen/SciERC & 11\% & 43\% \\
262	LLaMA/SciERC & 18\% & 39\% \\
263	Qwen/CoNLL & 57\% & --- \\
264	LLaMA/CoNLL & 88\% & --- \\
265	WNUT-17 & 55\% & --- \\
266	\bottomrule
267	\end{tabular}
268	\end{table}
269	
270	\paragraph{Oracle-improvable fraction.}
271	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
272	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
273	
274	\paragraph{Diversity-stratified selection gap.}
275	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
276	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
277	This rules out insufficient diversity as an explanation for the correlation-selection gap.
278	
279	\paragraph{TOST equivalence testing.}
280	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
281	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
282	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
283	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
284	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
285	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
286	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
287	
288	\begin{table}[t]
289	\centering
290	\small
291	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
292	\label{tab:tost}
293	\begin{tabular}{l cccc cccc}
294	\toprule
295	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
296	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
297	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
298	\midrule
299	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
300	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
301	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
302	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
303	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
304	\bottomrule
305	\end{tabular}
306	\end{table}
307	
308	\section{Multi-Seed Stability}\label{app:multiseed}
309	
310	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
311	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
312	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
313	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
319	\label{tab:multiseed}
320	\begin{tabular}{lccccc}
321	\toprule
322	& LP & FK & SJ & VC & EM \\
323	\midrule
324	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
325	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
326	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
327	\midrule
328	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
329	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
330	\midrule
331	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
332	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
333	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\section{Training Configuration}\label{app:training}
339	
340	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
346	\label{tab:training}
347	\begin{tabular}{ll}
348	\toprule
349	Parameter & Value \\
350	\midrule
351	LoRA rank / $\alpha$ & 32 / 64 \\
352	LoRA target & All linear modules \\
353	LoRA dropout & 0 \\
354	Optimizer & AdamW \\
355	Learning rate & 2e-4, cosine schedule \\
356	Warmup ratio & 0.1 \\
357	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
358	Epochs & 5 \\
359	Max sequence length & 2048 \\
360	Precision & bf16 \\
361	Gradient checkpointing & Enabled \\
362	Max gradient norm & 1.0 \\
363	Training seed & 42 \\
364	Framework & LLaMA Factory \\
365	\midrule
366	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
367	SciERC split & 1861 / 275 / 551 \\
368	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
369	& eval\_steps${=}$200, save\_limit${=}$5 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\paragraph{Prompt template.}
375	For NER, we use a structured prompt:
376	\begin{quote}
377	\small
378	\texttt{System:} You are an expert in Named Entity Recognition.\\
379	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
380	Text: \texttt{\{input\_text\}}\\
381	Entity types: \texttt{\{schema\_types\}}
382	\end{quote}
383	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
384	
385	\paragraph{Constrained decoding.}
386	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
387	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
388	
389	\section{Log-Probability Score Compression}\label{app:logprob_ties}
390	
391	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
392	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
393	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
394	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
395	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
396	
397	\begin{figure}[t]
398	\centering
399	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
400	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
401	\label{fig:lp_range_cdf}
402	\end{figure}
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
408	\label{tab:logprob_ties}
409	\begin{tabular}{lc}
410	\toprule
411	$\varepsilon$ threshold & Tied instances (\%) \\
412	\midrule
413	0.01 & 1.1\% \\
414	0.05 & 60.3\% \\
415	0.1  & ${\sim}$84\% \\
416	0.5  & ${\sim}$99\% \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	\paragraph{Non-tied subset.}
422	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
423	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
424	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
425	
426	\section{RE Conditional Selection}\label{app:re_conditional_selection}
427	
428	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
429	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
430	All five signals underperform greedy on both subsets.
431	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
432	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
433	
434	\begin{table}[t]
435	\centering
436	\small
437	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
438	\label{tab:re_cond_selection}
439	\begin{tabular}{lcc}
440	\toprule
441	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
442	\midrule
443	Oracle & 0.585 & 0.757 \\
444	\midrule
445	LP & 0.395 & 0.600 \\
446	SJ & 0.386 & 0.604 \\
447	EM & 0.372 & 0.583 \\
448	VC & 0.359 & 0.574 \\
449	\midrule
450	Greedy & 0.404 & 0.674 \\
451	\bottomrule
452	\end{tabular}
453	\end{table}
454	
455	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
456	
457	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
458	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
459	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
460	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
461	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
462	
463	\begin{table*}[t]
464	\centering
465	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
466	\label{tab:freeform_ablation}
467	
468	\vspace{2pt}
469	{\small\textsc{Panel A: Logprob Distribution}}
470	\vspace{2pt}
471	
472	\begin{tabular}{lccc}
473	\toprule
474	Metric & Constrained & Free-form & $\Delta$ \\
475	\midrule
476	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
477	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
478	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
479	\bottomrule
480	\end{tabular}
481	
482	\vspace{8pt}
483	
484	{\small\textsc{Panel B: Selection F1}}
485	\vspace{2pt}
486	
487	\begin{tabular}{llccc}
488	\toprule
489	Task & Method & Constrained & Free-form & $\Delta$ \\
490	\midrule
491	\multirow{3}{*}{NER}
492	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
493	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
494	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
495	\midrule
496	\multirow{3}{*}{RE}
497	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
498	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
499	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
500	\bottomrule
501	\end{tabular}
502	
503	\vspace{8pt}
504	
505	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
506	\vspace{2pt}
507	
508	\begin{tabular}{l ccc ccc}
509	\toprule
510	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
511	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
512	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
513	\midrule
514	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
515	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
516	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
517	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
518	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
519	\bottomrule
520	\end{tabular}
521	
522	\vspace{8pt}
523	
524	{\small\textsc{Panel D: Parse Rate (Free-form)}}
525	\vspace{2pt}
526	
527	\begin{tabular}{lc}
528	\toprule
529	Metric & Value \\
530	\midrule
531	Total samples          & 4408 \\
532	Parse rate             & 99.95\% \\
533	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
534	\bottomrule
535	\end{tabular}
536	
537	\end{table*}
538	
539	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
540	
541	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
542	
543	\paragraph{Pairwise overlap.}
544	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
545	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
546	
547	\paragraph{Instance complexity drives failure.}
548	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
549	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
550	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
551	
552	\begin{table}[t]
553	\centering
554	\small
555	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
556	\label{tab:stable_failures}
557	\begin{tabular}{lcccc}
558	\toprule
559	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
560	\midrule
561	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
562	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
563	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
564	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
565	\bottomrule
566	\end{tabular}
567	\end{table}
568	
569	\paragraph{Flip instances.}
570	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
571	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
572	
573	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
574	
575	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
576	
577	\begin{table}[t]
578	\centering
579	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
580	\label{tab:n-scaling}
581	\small
582	\begin{tabular}{l ccc ccc}
583	\toprule
584	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
585	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
586	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
587	\midrule
588	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
589	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
590	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
591	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
592	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
593	\midrule
594	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
595	\bottomrule
596	\end{tabular}
597	\end{table}
598	
599	\begin{table}[t]
600	\centering
601	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
602	\label{tab:ranking-stability}
603	\small
604	\begin{tabular}{ll cc l}
605	\toprule
606	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
607	\midrule
608	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
609	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
610	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
611	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
612	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
613	\bottomrule
614	\end{tabular}
615	\end{table}
616	
617	\begin{table}[t]
618	\centering
619	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
620	\label{tab:sigma-comparison}
621	\small
622	\begin{tabular}{l cc cc}
623	\toprule
624	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
625	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
626	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
627	\midrule
628	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
629	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
630	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
631	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
632	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
633	\midrule
634	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
635	\bottomrule
636	\end{tabular}
637	\end{table}
638	
639	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
640	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
641	
642	\section{Cross-Dataset OOD Analysis}\label{app:ood}
643	
644	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
645	
646	\begin{table}[t]
647	\centering
648	\small
649	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
650	\label{tab:ood}
651	\begin{tabular}{l ccc ccc}
652	\toprule
653	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
654	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
655	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
656	\midrule
657	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
658	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
659	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
660	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
661	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
662	\bottomrule
663	\end{tabular}
664	\end{table}
665	
666	\paragraph{Wider-to-narrower schema transfer.}
667	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
668	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
669	
670	\paragraph{Narrower-to-wider schema transfer (excluded).}
671	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
672	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
673	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
674	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
675	
676	\paragraph{Asymmetry interpretation.}
677	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
678	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
679	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "7a848607-d9e3-499e-9020-382d5559e774",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as population standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the core finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n",
      "numLines": 679,
      "startLine": 1,
      "totalLines": 679
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete picture. Let me summarize the findings:

### Sub-task A: Provenance of "0.335"

**Current paper status**: "0.335" does NOT appear anywhere in the current paper tex files (experiments.tex, discussion.tex, appendix.tex). The round_7_consistency review confirmed "PASS — 全文 grep 无匹配". It has already been cleaned out.

**Where "0.335" appears in data files**:
1. **EM NER seed42 ρ = 0.335** (3seed_ner_summary.md, Table 1) — this is the EM signal's Spearman ρ for seed42 on full split NER


2. **dream_reports**: freeform SJ NER ρ = 0.335 (dream median), FK conditional RE ρ = 0.335 (dream best) — these are auto-generated draft values

**What was the "in-domain avg ρ=0.335"?**

Looking at the user's calculation for exp_012_rerun_1024 NER avg structural rho with the four signals (SJ 0.3599, FK 0.2665, EM 0.2945, VC 0.3792), the arithmetic mean comes to approximately 0.3250, which doesn't match 0.335 exactly.

Now I'm checking whether these values actually correspond to the N=8 seed=42 data from Table 1 in experiments.tex — the numbers line up closely (SJ ≈ 0.360, FK ≈ 0.267, EM ≈ 0.295, VC ≈ 0.379), and there's also an LP signal at 0.205 that could be included in a five-signal average, which would give around 0.3011.

Looking at the N=16 scaling data from the appendix, the three-seed mean across all five signals comes to about 0.3055, which is notably lower than 0.335. When I pull the individual seed=42 results for N=16 from the summary file, I'm seeing different values again (SJ at 0.428, FK at 0.281), suggesting there might be variation across different experimental runs or configurations I need to reconcile. I'm working through the N=16 3-seed mean calculations now, and I'm noticing the values are clustering around 0.33-0.34, which aligns closely with what I saw in the earlier seed42 analysis. Let me verify these numbers more carefully by recalculating the mean from the individual signal scores. Let me check the user's actual numbers from Table 1 with seed=42: adding up SJ, FK, EM, and VC gives 1.3001, which averages to 0.325 for four signals, and including LP pushes it to 0.301 for five signals—neither matches 0.335.

Looking at the n-scaling data, the most likely source is the EM NER value at N=16 with seed=42, which is 0.335. Someone probably cited this single signal value as an in-domain average instead of clarifying it was just EM, or they used a slightly different subset of values. The 3-seed mean for NER at N=16 rounds to 0.336, which is close but not exact—0.335 is the direct match from the EM seed=42 N=16 result. The most likely explanation for that 0.335 value is either a single seed result from EM NER at N=16 that got cited as an average, or a rounding artifact from the N=16 all-signal mean around 0.336. Since the source files indicate this has already been cleaned from the paper during review, I can move forward with writing up the report. The discussion.tex file doesn't exist on the server anymore, so I'll need to focus on what's actually available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "1f7eb193-c08c-4f3b-a3a3-71adf022c22a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011doMbewuY9KDhV5ZEM2RF6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19171,
      "cache_read_input_tokens": 45453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19171
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

_source line 52_

全部信息已收集完毕。

## 报告

### 子任务 A: "0.335" 溯源

**论文现状**: "0.335" **不存在于**当前论文任何 tex 文件中（experiments.tex / discussion.tex / appendix.tex 均无匹配）。round_7_consistency review 已确认 "PASS — 全文 grep 无匹配"。此数字已被清除。

**"0.335" 在数据文件中的出现**:
- `3seed_ner_summary.md`: **EM NER seed42 N=16 ρ = 0.335**（单信号单种子值）
- dream_reports 自动草稿中出现两次（freeform SJ → 0.335、RE conditional FK → 0.335），均为生成内容

**用户要求的计算验证**:

| 计算方式 | 公式 | 结果 |
|---------|------|------|
| 4 structural avg (N=8, seed42) | (SJ 0.3599 + FK 0.2665 + EM 0.2945 + VC 0.3792) / 4 | **0.325** |
| 5 signal avg (N=8, seed42) | (0.3599 + 0.2665 + 0.2052 + 0.2945 + 0.3792) / 5 | **0.301** |
| N=16 3-seed 5-signal mean (n-scaling table) | mean row | **0.336** |

**最可能来源**: "in-domain avg ρ=0.335" 是 **EM NER seed42 N=16 的单信号值 (0.335)** 被误标为 "avg ρ"，或者是 N=16 全信号均值 0.336 的近似取整。无论哪种，都不是可引用的 "in-domain average"。

**结论**: 论文中已无此数字，无需进一步修正。OOD section 现在使用逐信号列举（如 discussion.tex:46 的 "VC ρ=0.469 OOD vs. 0.379 in-domain"），溯源至 Table 1，是正确做法。

### 子任务 B: 删除 discussion.tex

`/root/autodl-tmp/struct_self_consist_ie/discussion.tex` **不存在**于远程服务器。`ls` 返回 "No such file or directory"。整个 paper/sections 目录也不存在于服务器——论文源文件仅在本地 `docs/paper/` 下。无需操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "uuid": "6bee99e7-b69f-4496-94cf-daf997f4f0b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011doMbewuY9KDhV5ZEM2RF6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19171,
      "cache_read_input_tokens": 45453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19171
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

### Runtime record

_source line 53_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778868600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d421f3b5-8df1-4478-96af-2ab1642398a8",
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3"
}
```

---

### Task result

_source line 54_

全部信息已收集完毕。

## 报告

### 子任务 A: "0.335" 溯源

**论文现状**: "0.335" **不存在于**当前论文任何 tex 文件中（experiments.tex / discussion.tex / appendix.tex 均无匹配）。round_7_consistency review 已确认 "PASS — 全文 grep 无匹配"。此数字已被清除。

**"0.335" 在数据文件中的出现**:
- `3seed_ner_summary.md`: **EM NER seed42 N=16 ρ = 0.335**（单信号单种子值）
- dream_reports 自动草稿中出现两次（freeform SJ → 0.335、RE conditional FK → 0.335），均为生成内容

**用户要求的计算验证**:

| 计算方式 | 公式 | 结果 |
|---------|------|------|
| 4 structural avg (N=8, seed42) | (SJ 0.3599 + FK 0.2665 + EM 0.2945 + VC 0.3792) / 4 | **0.325** |
| 5 signal avg (N=8, seed42) | (0.3599 + 0.2665 + 0.2052 + 0.2945 + 0.3792) / 5 | **0.301** |
| N=16 3-seed 5-signal mean (n-scaling table) | mean row | **0.336** |

**最可能来源**: "in-domain avg ρ=0.335" 是 **EM NER seed42 N=16 的单信号值 (0.335)** 被误标为 "avg ρ"，或者是 N=16 全信号均值 0.336 的近似取整。无论哪种，都不是可引用的 "in-domain average"。

**结论**: 论文中已无此数字，无需进一步修正。OOD section 现在使用逐信号列举（如 discussion.tex:46 的 "VC ρ=0.469 OOD vs. 0.379 in-domain"），溯源至 Table 1，是正确做法。

### 子任务 B: 删除 discussion.tex

`/root/autodl-tmp/struct_self_consist_ie/discussion.tex` **不存在**于远程服务器。`ls` 返回 "No such file or directory"。整个 paper/sections 目录也不存在于服务器——论文源文件仅在本地 `docs/paper/` 下。无需操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 126305,
  "duration_api_ms": 126743,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "02ec7640-681a-4831-ac2f-7ab5807e0ae3",
  "total_cost_usd": 0.62061225,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 52923,
    "cache_read_input_tokens": 233397,
    "output_tokens": 6863,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52923,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3080,
        "cache_read_input_tokens": 45453,
        "cache_creation_input_tokens": 19171,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 19171
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1395,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00151,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 6863,
      "cacheReadInputTokens": 233397,
      "cacheCreationInputTokens": 52923,
      "webSearchRequests": 0,
      "costUSD": 0.61910225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "43f857d9-1ca8-45f7-b85d-c7ecb6f25aba"
}
```

</details>

---

# analysis paper consistency check — Part 1 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[Transcript overview](../analysis-paper-consistency-check.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/a0/a0ec28134f509e749c31.json)

## Before a recorded user message

## Before a recorded user message

25 recorded events


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
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
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
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "c64f482e-d444-4a52-8634-cfaaf5a562b6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779150000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "13617372-cf47-4cf5-b948-7aef6f9d9cda",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a comprehensive paper consistency check task. Let me break it down:

1. Read all .tex files from the paper directory
2. Read the registry for experiment metrics
3. Check numerical consistency
4. Check wording consistency
5. Check cross-references
6. Try to compile
7. Write a report

Let me start by reading the paper files and the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "87bd3e4c-81a9-4abb-b87d-6cb485427e0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019trixcLoaAZZh35YPqEhyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
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


### Assistant

_source line 5_

开始全面一致性检查。先并行读取论文文件和实验 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e2396233-4127-4a7b-a03f-88f9f899e667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019trixcLoaAZZh35YPqEhyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
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


### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_01UsJr2vx71P7MKf4dZJErsB`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "abb64635-7d81-4934-9e26-e0ac163a730b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019trixcLoaAZZh35YPqEhyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
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

_source line 7 · 2026-05-18T19:27:32.221Z_

<details><summary>↩ Tool result · reported error · `toolu_01UsJr2vx71P7MKf4dZJErsB`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1fff7dc0-5375-40fb-b838-f32f7cee2cd0",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd."
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01S5SAAFqrER29JXnvvTcKmM`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "65b64dc0-0016-42dd-aca4-e720c248dff1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019trixcLoaAZZh35YPqEhyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
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

_source line 9 · 2026-05-18T19:27:33.223Z_

<details><summary>↩ Tool result · reported error · `toolu_01S5SAAFqrER29JXnvvTcKmM`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "d5bf21d4-903d-4922-877c-6f515c925c57",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd."
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015AzV1nFrDEoibLvx1Uqigm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "696b3204-2217-467f-9618-27fe4865851d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019trixcLoaAZZh35YPqEhyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
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

_source line 11 · 2026-05-18T19:27:33.376Z_

<details><summary>↩ Tool result · `toolu_015AzV1nFrDEoibLvx1Uqigm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "26d25401-a0e5-4257-b166-61f5007177fe",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist at the expected local path. Let me search for where the paper files actually are, and also read the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "422d3607-e2ec-4add-9553-3a8376c9ba0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9kzqHKvQE9ZczqFxHMeC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
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

论文目录不存在于预期路径。搜索实际位置，同时读取 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "8d76025a-8d6a-4854-bf35-33b0178efd9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9kzqHKvQE9ZczqFxHMeC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
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

<details open><summary>🔧 Tool call — Glob · `toolu_014Tk2HnVpkMsrQFaLctV5Fi`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "320bd314-dad4-4e9c-a48f-c05834a00102",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9kzqHKvQE9ZczqFxHMeC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
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

_source line 15 · 2026-05-18T19:27:37.270Z_

<details><summary>↩ Tool result · `toolu_014Tk2HnVpkMsrQFaLctV5Fi`</summary>

```text
docs/paper/corl_example.tex
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/median/paper.tex
artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
artifacts/dream_reports/dream_20260516T011810/best/paper.tex
artifacts/dream_reports/dream_20260516T011810/median/paper.tex
artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method_a6c062.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/introduction_fccb56.tex
docs/paper-a-plus-backup/abstract.tex
docs/paper-a-plus-backup/appendix.tex
docs/paper-a-plus-backup/conclusion.tex
docs/paper-a-plus-backup/corl_example.tex
docs/paper-a-plus-backup/discussion.tex
docs/paper-a-plus-backup/experiments.tex
docs/paper-a-plus-backup/introduction.tex
docs/paper-a-plus-backup/main.tex
docs/paper-a-plus-backup/method.tex
docs/paper-a-plus-backup/related_work.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ecf8556d-1d14-4797-ad00-acdcf813f080",
  "tool_use_result": {
    "filenames": [
      "docs/paper/corl_example.tex",
      "artifacts/dream_reports/dream_20260515T222933/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T222933/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T222933/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T011810/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T011810/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T011810/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/method_a6c062.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/introduction_fccb56.tex",
      "docs/paper-a-plus-backup/abstract.tex",
      "docs/paper-a-plus-backup/appendix.tex",
      "docs/paper-a-plus-backup/conclusion.tex",
      "docs/paper-a-plus-backup/corl_example.tex",
      "docs/paper-a-plus-backup/discussion.tex",
      "docs/paper-a-plus-backup/experiments.tex",
      "docs/paper-a-plus-backup/introduction.tex",
      "docs/paper-a-plus-backup/main.tex",
      "docs/paper-a-plus-backup/method.tex",
      "docs/paper-a-plus-backup/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "docs/paper/abstract.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      "docs/paper/discussion.tex",
      "docs/paper/introduction.tex"
    ],
    "durationMs": 17,
    "numFiles": 33,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GMx9WV68qfLsstRXqMibP7`</summary>

```json
{
  "project": "vla-ssd",
  "limit": 0,
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
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7f6b0075-c51e-429d-abac-6ec563998ded",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9kzqHKvQE9ZczqFxHMeC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
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

_source line 17 · 2026-05-18T19:27:38.674Z_

<details><summary>↩ Tool result · `toolu_01GMx9WV68qfLsstRXqMibP7`</summary>

```text
Error: result (157,911 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0b43b2d6-3eba-4129-80be-548220a673e1",
  "tool_use_result": {
    "content": "Error: result (157,911 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"specificity_control_action\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:28:45.197Z\", \"updated_at\": \"2026-05-18T18:45:03.767Z\", \"hypothesis\": \"Bottom-24 non-instruction heads should cause significantly less action shift (d << 0.65) than top-24 instruction-dominant heads when ablated, confirming that instruction-action coupling is specific to identified heads rather than a general property of any 24 heads.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl python -u scripts/specificity_control_action.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 1500, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"libero_goal 3 tasks x 10 demos x 50 timesteps\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/specificity_control_action.log\"}, \"conclusion\": \"negative\", \"notes\": \"Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.\", \"metrics\": {\"cohens_d\": 0.565, \"paired_mse\": 0.034, \"token_divergence\": 0.598, \"kl_divergence\": 4.166, \"top24_d\": 0.65, \"bottom24_d\": 0.565, \"ratio\": 1.15, \"per_task_d\": {\"cabinet\": 0.405, \"bowl\": 0.628, \"plate\": 0.659}}, \"completed_at\": \"2026-05-18T18:45:03.767Z\"}, \"counterfactual_instruction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:52:52.867Z\", \"updated_at\": \"2026-05-18T17:31:39.989Z\", \"hypothesis\": \"L1 instruction-dominant heads perform instruction-specific routing: changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically different action outputs compared to correct instruction, with wrong and empty causing larger divergence than shuffled or paraphrased.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 6000, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log\"}, \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_counterfactual_instruction_20260518T165804.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:31:15.868Z\", \"notes\": \"4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim.\"}, \"attention_decomposition\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:52:54.658Z\", \"updated_at\": \"2026-05-18T17:20:35.567Z\", \"hypothesis\": \"Instruction-dominant heads (24/32 at L1) allocate significantly more attention mass to instruction tokens than control heads (8/32), confirming that the head classification reflects genuine functional specialization in attention routing\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"python3 attention_decomposition_and_r2.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/attention/\", \"data_count\": \"5 trained samples + 32-head untrained data\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"existing attention data\", \"eval_data\": \"L1 attention summaries\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/attention_decomposition.json\", \"log_path\": \"/root/vla-ssd/scripts/attention_decomposition_and_r2.py\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:20:32.623Z\", \"notes\": \"B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json\"}, \"action_metrics_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:52:53.825Z\", \"updated_at\": \"2026-05-18T17:16:37.223Z\", \"hypothesis\": \"Extended analysis of existing action trajectory data: (1) per-dimension MAE reveals which action dimensions are most affected by L1 instruction-head ablation, (2) action direction cosine similarity shows whether ablation changes action direction vs magnitude, providing mechanistic detail beyond aggregate Cohen's d.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"python3 (CPU-only, from existing JSONs)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 5000, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"N/A (analysis only)\", \"eval_data\": \"action_trajectory_analysis.json + action_trajectory_control.json\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_metrics_extended.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:16:32.376Z\", \"notes\": \"Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x, dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x. Cosine similarity NOT computable: source JSONs only have aggregated stats, no raw per-sample action vectors.\"}, \"cross_layer_L13_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:35:44.057Z\", \"updated_at\": \"2026-05-18T16:56:23.782Z\", \"hypothesis\": \"L13 full-layer ablation (all 32 heads) produces near-zero action divergence (d ≈ 0), confirming the cross-layer causal gradient: L1 (d=0.65) >> L8 >> L13 (≈0). Based on R² gradient prediction: L13 Δ≈0 vs L1 Δ=+0.059.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u scripts/action_trajectory_L13_ablation.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps = 2500 samples\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.log\"}, \"conclusion\": \"negative\", \"notes\": \"M006/D064: L13 full-layer ablation d=0.668 ≈ L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-18T16:26:04.650Z\"}, \"cross_layer_L8_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:35:43.212Z\", \"updated_at\": \"2026-05-18T16:33:44.948Z\", \"hypothesis\": \"L8 full-layer ablation (all 32 heads) produces significantly smaller action divergence (d << 0.65) than L1 instruction-head ablation (24 heads, d=0.65), demonstrating that L1's causal impact on action output is layer-position-specific, not merely a function of head count. Based on R² gradient prediction: L8 Δ=+0.018 vs L1 Δ=+0.059.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 2500, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"}, \"conclusion\": \"negative\", \"notes\": \"M006/D064: L8 full-layer ablation d=0.652 ≈ L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-18T16:26:02.700Z\"}, \"dose_response_curve\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:07:22.213Z\", \"updated_at\": \"2026-05-18T16:32:50.159Z\", \"hypothesis\": \"If instruction routing is a learned collective function, progressively ablating more L1 heads (sorted by instruction attention fraction) should produce monotonically increasing action divergence (dose-response curve). 8 conditions: top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed, coordinated mechanism.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions 20,24,28,32 (cuda:1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:26:06.324Z\", \"notes\": \"单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at ~12-16 heads\"}, \"permutation_test_I2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:07:21.232Z\", \"updated_at\": \"2026-05-18T15:13:25.536Z\", \"hypothesis\": \"Permutation test validates that observed CV difference (instruction 1.30 vs control 2.74) and I² difference (instruction 0.87 vs control 0.78) are not explained by random head assignment. Shuffling head labels 1000x and recomputing metrics produces null distribution; observed values should fall in extreme tail (p < 0.05).\", \"parent\": \"action_trajectory_cpu_analysis\", \"spec\": {\"command\": \"python scripts/permutation_test_I2.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json\", \"data_count\": \"5 tasks x 2 conditions + 7 dims x 2 conditions\", \"model_name\": \"n/a (statistical test)\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/permutation_test_I2.json\", \"checkpoint_source\": \"n/a\", \"eval_data\": \"action_trajectory_extended_analysis.json\"}, \"metrics\": {\"cv_exact_paired_p\": 0.0156, \"cv_mc_unpaired_p\": 0.0048, \"cv_7d_p\": 0.0078, \"I2_exact_paired_p\": 0.1562, \"I2_mc_unpaired_p\": 0.1434, \"cv_null_mean\": 0, \"cv_null_std\": 0.6756, \"I2_null_mean\": 0, \"I2_null_std\": 0.2468}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:13:25.536Z\"}, \"action_trajectory_cpu_analysis\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:35:44.880Z\", \"updated_at\": \"2026-05-18T14:29:42.691Z\", \"hypothesis\": \"Extended analysis of existing action trajectory data: (1) temporal coherence — L1 ablation disrupts step-to-step action autocorrelation more than control, (2) bootstrap CI on per-head effect size — formal test of whether instruction heads per-head d (0.027) differs significantly from control heads per-head d (0.051).\", \"parent\": \"action_trajectory_control\", \"metrics\": {\"bootstrap_per_head_d\": {\"instruction_24h\": {\"mean\": 0.0271, \"ci_95\": [0.0258, 0.0285]}, \"control_8h\": {\"mean\": 0.0514, \"ci_95\": [0.0478, 0.0551]}, \"difference_ctrl_minus_inst\": {\"mean\": 0.0244, \"ci_95\": [0.0203, 0.0281]}, \"task_paired_t\": {\"t\": 7.356, \"p\": 0.0018}, \"all_5_tasks_ctrl_gt_inst\": true, \"interpretation\": \"Control heads ~1.9x per-head effect; instruction heads achieve larger total via 24-head collective coordination\"}, \"temporal_coherence_proxy\": {\"per_dim_cv_instruction\": 1.3, \"per_dim_cv_control\": 2.74, \"cross_task_I2_instruction\": 0.87, \"cross_task_I2_control\": 0.78, \"interpretation\": \"Instruction ablation produces more consistent (low CV) and more task-dependent (high I²) perturbation, consistent with structured language-dependent computation\"}, \"result_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json\"}, \"conclusion\": \"success\", \"notes\": \"Per-head effect formally confirmed: control heads ~1.9x stronger per-head (d=0.051 vs 0.027, p=0.0018). But instruction heads show qualitatively different perturbation: more consistent across dimensions (CV 1.30 vs 2.74) and more task-dependent (I²=0.87 vs 0.78). Instruction heads mediate structured, coordinated computation rather than individual strong effects.\"}, \"action_trajectory_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:34:36.585Z\", \"updated_at\": \"2026-05-18T12:59:24.419Z\", \"hypothesis\": \"Ablating 8 non-instruction heads (control) produces significantly smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant heads, proving the action output effect is instruction-specific rather than generic perturbation.\", \"parent\": \"action_trajectory_analysis\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"47936\", \"log_path\": \"~/runs/vla-ssd/action_trajectory_control.log\", \"submitted_at\": \"2026-05-18T11:53:06.410Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T11:42:54.772Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T11:42:57.559215+00:00\"}]}, \"metrics\": {\"paired_action_mse\": {\"mean\": 0.0201, \"std\": 0.0489, \"t_stat\": 20.54, \"p_value\": 9e-87, \"cohens_d\": 0.41}, \"token_divergence_rate\": 0.293, \"per_dim_action_shift\": {\"dx\": 0.00037, \"dy\": 0.00125, \"dz\": 0.00243, \"rx\": 0.00785, \"ry\": 0.01387, \"rz\": 0.01783, \"gripper\": 0.1407}, \"kl_divergence\": {\"mean\": 1.69, \"std\": 3.7}, \"wilcoxon_p\": 8e-235, \"config\": {\"n_tasks\": 5, \"n_demos_per_task\": 10, \"n_timesteps_per_demo\": 50, \"total_forward_passes\": 5000, \"ablated_heads\": [3, 5, 6, 9, 13, 21, 24, 28]}, \"per_task\": {\"open_middle_drawer\": {\"mse\": 0.0071, \"cohens_d\": 0.24, \"token_div\": 0.24}, \"open_top_drawer_put_bowl\": {\"mse\": 0.0258, \"cohens_d\": 0.48, \"token_div\": 0.304}, \"push_plate_to_stove\": {\"mse\": 0.0213, \"cohens_d\": 0.42, \"token_div\": 0.306}, \"put_bowl_on_plate\": {\"mse\": 0.0227, \"cohens_d\": 0.44, \"token_div\": 0.299}, \"put_bowl_on_stove\": {\"mse\": 0.0236, \"cohens_d\": 0.45, \"token_div\": 0.313}}, \"comparison_vs_instruction_ablation\": {\"instruction_24heads_mse\": 0.0416, \"control_8heads_mse\": 0.0201, \"mse_ratio\": 2.07, \"instruction_token_div\": 0.723, \"control_token_div\": 0.293, \"div_ratio\": 2.47, \"instruction_kl\": 5.079, \"control_kl\": 1.69, \"kl_ratio\": 3, \"instruction_gripper\": 0.291, \"control_gripper\": 0.141, \"gripper_ratio\": 2.07, \"head_count_ratio\": 3, \"note\": \"Ratios (2.0-3.0x) are at or below head count ratio (3:1), meaning per-head effect of control heads is comparable to instruction heads\"}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T11:45:26.662Z\", \"notes\": \"Control ablation (8 non-instruction heads) also produces significant action divergence (d=0.41, 29.3% token divergence). Per-head effect comparable to instruction heads (0.00250 vs 0.00175). Specificity hypothesis not confirmed. Effect distributed across L1.\"}, \"behavioral_pilot_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:40:18.951Z\", \"updated_at\": \"2026-05-18T12:05:59.890Z\", \"hypothesis\": \"Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.\", \"parent\": \"behavioral_pilot_w4\", \"conclusion\": \"killed\", \"notes\": \"Director 确认放弃 behavioral rollout（mujoco 版本不匹配）。Phase 1 SR=0/3，fine-tuned checkpoint 加载成功但 action[0] 锁定在 0.236，Blackwell GPU 需要 device_map 绕过 segfault，可能影响 inference。不再投入。\"}, \"action_trajectory_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:35:18.923Z\", \"updated_at\": \"2026-05-18T11:02:27.281Z\", \"hypothesis\": \"L1 instruction-dominant head ablation significantly changes OpenVLA action predictions (measured by action token divergence and per-dimension MSE), demonstrating that instruction routing heads directly influence model output, not just intermediate representations.\", \"parent\": \"ablation_50demos_main\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions\", \"model_name\": \"OpenVLA-7b (openvla-7b base pretrained)\", \"seed\": \"42\", \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"LIBERO-Goal demo observations (open-loop, no execution)\", \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log\"}, \"metrics\": {\"paired_action_mse\": {\"mean\": 0.0416, \"std\": 0.0639, \"t_stat\": 32.56, \"p_value\": 3.99e-194, \"cohens_d\": 0.651}, \"token_divergence_rate\": 0.723, \"per_dim_action_shift_means\": [0.0019, 0.0053, 0.0076, 0.0206, 0.0307, 0.0339, 0.2907], \"per_dim_names\": [\"dx\", \"dy\", \"dz\", \"rx\", \"ry\", \"rz\", \"gripper\"], \"kl_divergence\": {\"mean\": 5.079, \"std\": 4.961}, \"mse_vs_gt_baseline\": 0.432, \"mse_vs_gt_ablated\": 0.436, \"wilcoxon_p\": 0, \"n_tasks\": 5, \"n_samples\": 2500, \"all_tasks_significant\": true, \"per_task_cohens_d_range\": [0.433, 0.729], \"result_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:02:27.281Z\"}, \"behavioral_pilot_w4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:34:21.677Z\", \"updated_at\": \"2026-05-18T10:34:21.649Z\", \"hypothesis\": \"Ablating L1 instruction-dominant heads (24/32) during VLA inference changes task success rate, providing behavioral evidence that attention head specialization has functional consequences beyond representation-level metrics.\", \"parent\": \"ablation_50demos_main\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && MUJOCO_GL=egl HDF5_USE_FILE_LOCKING=FALSE PYTHONUNBUFFERED=1 python /root/vla-ssd/scripts/behavioral_pilot.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"24738\", \"log_path\": \"~/runs/vla-ssd/behavioral_pilot_w4.log\", \"submitted_at\": \"2026-05-18T10:23:14.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"3 tasks x 10 episodes x 2 conditions = 60 episodes\", \"model_name\": \"OpenVLA-7b (openvla-7b)\", \"seed\": \"42\", \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"LIBERO-Goal benchmark (3 selected tasks, 300 max steps per episode)\", \"wall_clock_seconds\": 508.3, \"gpu_hours\": 0.14}, \"reproduce\": {\"finished_at\": \"2026-05-18T10:31:41.576Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T10:31:43.232Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T10:31:45.660946+00:00\"}]}, \"notes\": \"OpenVLA bridge_orig unnorm_key 与 LIBERO action space 不兼容，baseline SR=0/6，实验前提不成立。两个进程被 SIGHUP 终止。Checkpoint 是 base pretrained（OXE 970K），未在 LIBERO fine-tune，无 LoRA adapter，norm_stats 无 LIBERO key。\"}, \"behavioral_pilot\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:25:24.217Z\", \"updated_at\": \"2026-05-18T09:25:31.366Z\", \"hypothesis\": \"Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.\", \"parent\": \"ablation_50demos_main\"}, \"threecond_multiseed_r2_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:04:22.860Z\", \"updated_at\": \"2026-05-18T09:11:34.295Z\", \"hypothesis\": \"Multi-seed action probes (3 seeds, sequential split matching original experiment) will confirm trained > llama2base > untrained R² gradient with low seed variance, validating single-seed findings are robust and not split-dependent.\", \"parent\": \"threecond_multiseed_r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe_v2.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 3 conditions\", \"model_name\": \"ActionMLPProbe(4096->256->7)\", \"seed\": \"42,123,456\", \"split\": \"sequential_80_20_no_shuffle\", \"r2_space\": \"original_denormalized\", \"checkpoint_source\": \"pre-extracted features from openvla-7b / openvla-7b-untrained / openvla-7b-llama2base\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos, sequential split demo_0-39 train / demo_40-49 val)\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:47:23.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:47:26.372903+00:00\"}]}, \"metrics\": {\"conditions\": [\"untrained\", \"llama2base\", \"trained\"], \"seeds\": [42, 123, 456], \"trained_peak\": {\"layer\": 9, \"mean_R2\": 0.643, \"std\": 0.014}, \"L0_baseline\": {\"mean_R2\": 0.645, \"std\": 0.008, \"note\": \"three conditions consistent at L0\"}, \"pattern_L1_L15\": \"U&lt;L&lt;T\", \"pattern_L16_L25\": \"L≈T>>U\", \"pattern_L32\": \"reversal\", \"split\": \"sequential (demo_0-39 train, demo_40-49 val)\", \"r2_space\": \"original (denormalized)\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:10:58.657Z\", \"notes\": \"v2 修正版（顺序 split + 反归一化 R²）。trained peak L9 0.643±0.014, llama2base peak L12 0.634±0.013, untrained peak L1 0.547±0.008 (排除 L32 异常 0.589±0.007)。L0=0.645 三条件一致（共享 vision encoder）。trained-llama2base gap small (0.009 at peak, n=3), direction consistent。llama2base v2=0.634 vs llama2base_action_probe registry peak L4=0.6447，差距 0.010 在 seed 方差内，一致。untrained 中间层崩溃（负 R² + 高方差）是最强信号。\"}, \"threecond_multiseed_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:09:57.814Z\", \"updated_at\": \"2026-05-18T08:50:31.406Z\", \"hypothesis\": \"Multi-seed action probes will confirm that trained models yield higher per-layer R² than untrained/llama2base with low variance across seeds, validating that the single-seed result is robust.\", \"parent\": \"llama2base_action_probe\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T06:44:28.859Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 3 conditions\", \"model_name\": \"ActionMLPProbe(4096->256->7)\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"pre-extracted features from openvla-7b / openvla-7b-untrained / openvla-7b-llama2base\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos each, 80/20 split)\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed.log\"}, \"conclusion\": \"killed\", \"metrics\": {\"conditions\": [\"untrained\", \"llama2base\", \"trained\"], \"seeds\": [42, 123, 456], \"trained_peak\": {\"layer\": 10, \"mean_R2\": 0.548, \"std\": 0.012}, \"llama2base_peak\": {\"layer\": 0, \"mean_R2\": 0.538, \"std\": 0.015}, \"untrained_peak\": {\"layer\": 0, \"mean_R2\": 0.538, \"std\": 0.015}, \"L0_shared_baseline\": 0.538, \"pattern_trained\": \"mild inverted-U, peak L10\", \"pattern_llama2base\": \"stable monotonic decline\", \"pattern_untrained\": \"high variance, deep layer collapse\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed.json\"}, \"completed_at\": \"2026-05-18T07:40:45.586Z\", \"notes\": \"⚠️ SUPERSEDED by threecond_multiseed_r2_v2 — R² 偏低因 train/val split 用了 random shuffle 而非顺序切分。原实验用顺序切分（demo_0-39 train, demo_40-49 val），multi-seed 脚本误用了 rng.shuffle，导致 R² 系统性偏低（peak 0.548 vs 0.655）。\"}, \"random_subset_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:25:38.132Z\", \"updated_at\": \"2026-05-18T08:27:15.118Z\", \"hypothesis\": \"Random subsets of 24 heads yield higher action R² increase than instruction-dominant 24 heads, indicating dominant heads serve dual routing-encoding function rather than pure capacity trade-off\", \"parent\": \"ablation_50demos_main\", \"spec\": {\"command\": \"python scripts/random_subset_ablation.py --n_demos 50 --n_random 10 --output /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"ActionMLPProbe(4096->256->7) with L1 head ablation\", \"seed\": \"10 random seeds for subset selection\", \"checkpoint_source\": \"pre-extracted features from openvla-7b (trained)\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos, sequential split)\", \"checkpoint_path\": \"N/A (probe experiment, no checkpoint saved)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\"}, \"metrics\": {\"baseline_r2\": 0.517, \"dominant_24_delta\": 0.042, \"random_24_mean_delta\": 0.077, \"random_24_std_delta\": 0.013, \"z_score\": -2.73, \"p_value\": 0.003, \"n_random_seeds\": 10, \"interpretation\": \"dominant-24 heads NOT special - any 24/32 heads ablation produces similar or larger R² increase\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\", \"figure_path\": \"/root/autodl-tmp/vla-ssd/results/figures/fig_random_subset_ablation.pdf\"}, \"conclusion\": \"success\", \"notes\": \"Plan C (D061) 核心证据。Dominant-24 heads 不具有特异性——10 组随机 24-head 子集的 R² 增量均高于 dominant-24（z=-2.73, p=0.003）。支持 dual routing-encoding function 解释。\", \"completed_at\": \"2026-05-18T08:27:15.118Z\"}, \"linear_probe_last_preaction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:11:47.015Z\", \"updated_at\": \"2026-05-18T07:40:44.628Z\", \"hypothesis\": \"The inverted-U R2 curve and trained > untrained pattern observed with MLP probes at the last_preaction token position will persist with a linear probe (Linear(4096,7)), confirming these patterns are not artifacts of probe capacity.\", \"parent\": \"plan_011_fulllayer_r2\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T06:44:29.493Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/linear_probe_last_preaction.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 2 conditions x 33 layers\", \"model_name\": \"Linear(4096,7)\", \"seed\": 42, \"checkpoint_source\": \"fulllayer_action_probe features (pre-extracted)\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/logs/linear_probe_last_preaction.log\"}, \"conclusion\": \"success\", \"metrics\": {\"readout\": \"last_preaction\", \"probe_type\": \"linear\", \"trained_peak_layer\": 13, \"trained_peak_R2\": 0.596, \"untrained_peak_layer\": 1, \"untrained_peak_R2\": 0.492, \"inverted_U_trained\": true, \"trained_gt_untrained_at_peak\": true, \"bootstrap_best_vs_best\": {\"delta\": 0.103, \"ci\": [0.056, 0.167], \"p\": 0}, \"bootstrap_same_layer_trained_peak\": {\"delta\": 0.513, \"ci\": [0.314, 0.789], \"p\": 0}, \"mlp_trained_peak_R2_L13\": 0.678, \"linear_vs_mlp_gap_at_peak\": -0.082, \"result_path\": \"/root/autodl-tmp/vla-ssd/results/linear_probe_last_preaction.json\"}, \"completed_at\": \"2026-05-18T07:40:44.628Z\"}, \"fulllayer_action_probe\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:50:36.813Z\", \"updated_at\": \"2026-05-17T22:50:53.991Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/vla-ssd/scripts/fulllayer_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"700649\", \"log_path\": \"~/runs/vla-ssd/fulllayer_action_probe.log\", \"submitted_at\": \"2026-05-16T03:50:36.686Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"superseded — fulllayer_action_probe.json already exists in results/functional_validation/\"}, \"l1_head_ablation_control8\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:29:35.542Z\", \"updated_at\": \"2026-05-17T22:50:53.077Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13 --output /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"905194\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_control8.log\", \"submitted_at\": \"2026-05-17T18:29:35.353Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"superseded by ablation_50demos_control8 (DONE, success)\"}, \"l1_head_ablation_50demos\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:36:35.829Z\", \"updated_at\": \"2026-05-17T22:50:51.655Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"905824\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_50demos.log\", \"submitted_at\": \"2026-05-17T18:36:35.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"superseded by ablation_50demos_main (DONE, success)\"}, \"llama2base_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:54:26.047Z\", \"updated_at\": \"2026-05-17T22:02:32.172Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/llama2base_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"pid\": \"913312\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json\", \"submitted_at\": \"2026-05-17T20:55:56.743Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks\", \"model_name\": \"meta-llama/Llama-2-7b-hf (via OpenVLA architecture)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe experiment, no checkpoint)\", \"wall_clock_seconds\": 3995.4, \"gpu_hours\": 1.11}, \"hypothesis\": \"Llama-2 base (pretrained LLM, no VLA training) action R² follows the three-condition gradient: untrained < llama2base < trained, completing the C2 evidence chain for action encoding specialization.\", \"reproduce\": {\"finished_at\": \"2026-05-17T21:57:33.185Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:57:38.637406+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"L1_untrained_R2\": 0.5546, \"L1_llama2base_R2\": 0.6366, \"L1_trained_R2\": 0.6331, \"peak_untrained\": {\"layer\": \"L0\", \"R2\": 0.6403}, \"peak_llama2base\": {\"layer\": \"L4\", \"R2\": 0.6447}, \"peak_trained\": {\"layer\": \"L8\", \"R2\": 0.6553}, \"mean_all_untrained\": 0.4491, \"mean_all_llama2base\": 0.6014, \"mean_all_trained\": 0.5849, \"mean_L2_L9_untrained\": 0.5294, \"mean_L2_L9_llama2base\": 0.6347, \"mean_L2_L9_trained\": 0.6463, \"pattern_L2_L9\": \"U&lt;L&lt;T (19/21 layers)\", \"pattern_L1\": \"U&lt;L≈T (pretraining near ceiling)\", \"pattern_late\": \"L>T (VLA repurposes late layers)\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json\"}, \"completed_at\": \"2026-05-17T22:02:32.172Z\"}, \"ablation_50demos_main\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:53:20.415Z\", \"updated_at\": \"2026-05-17T21:49:51.638Z\", \"hypothesis\": \"50-demo full-data ablation: L1 instruction-dominant heads capacity trade-off (R² increase under ablation) persists with adequate probe training data, eliminating underfitting confound from 5-demo version.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 3 conditions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json\"}, \"metrics\": {\"baseline_L1\": 0.5567, \"baseline_L8\": 0.6199, \"baseline_L13\": 0.6763, \"all24_L1\": 0.6153, \"all24_L8\": 0.6377, \"all24_L13\": 0.6762, \"all32_L1\": 0.5823, \"all32_L8\": 0.6311, \"all32_L13\": 0.6636, \"all24_vs_baseline_L1_delta\": 0.0585, \"all24_vs_baseline_L1_p\": 0, \"all24_vs_baseline_L1_CI\": [0.042, 0.0752], \"all24_vs_control8_L1_delta\": 0.0421, \"all24_vs_control8_L1_p\": 0, \"all24_vs_control8_L1_CI\": [0.0286, 0.0563]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:49:51.638Z\"}, \"ablation_p2_demo_sensitivity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:17:17.306Z\", \"updated_at\": \"2026-05-17T20:06:06.549Z\", \"spec\": {\"command\": \"subsample 25 from 50 demos, reuse existing extracted features\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"720669\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/results.json\", \"submitted_at\": \"2026-05-16T10:17:17.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/\", \"data_count\": \"25 demos/task x 10 tasks\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis-only)\", \"wall_clock_seconds\": 121729.4, \"gpu_hours\": 33.81}, \"hypothesis\": \"C3 inverted-U RSA pattern (image_mean, trained) is stable under reduced data (25 demos/task subsample from 50), confirming it is not an artifact of sample size.\", \"notes\": \"v1 killed — RSA used wrong method (demo-mean-then-distance). Replaced by ablation_p2_demo_sensitivity_v2 with correct Method B (timestep-wise pdist). Probe was correct, only RSA fixed.\", \"conclusion\": \"success\", \"metrics\": {\"rsa_peak_layer\": \"L12\", \"rsa_peak_rho\": 0.6059, \"rsa_peak_rho_50demo\": 0.6282, \"r2_peak_layer\": \"L11\", \"r2_peak\": 0.6088, \"r2_peak_50demo\": 0.6587, \"rsa_profile_corr\": 0.9696, \"r2_profile_corr\": 0.8189, \"pattern\": \"inverted-U preserved\"}, \"completed_at\": \"2026-05-17T20:06:06.549Z\"}, \"ablation_50demos_control8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:53:21.900Z\", \"updated_at\": \"2026-05-17T19:57:09.980Z\", \"hypothesis\": \"Ablating 8 non-dominant L1 heads (control) should NOT increase action R², proving the capacity trade-off is specific to instruction-dominant heads.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 1 condition\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\"}, \"metrics\": {\"ablate_control8_L1_R2\": 0.5732, \"ablate_control8_L1_CI\": [0.5149, 0.6321], \"ablate_control8_L8_R2\": 0.6311, \"ablate_control8_L8_CI\": [0.5773, 0.6834], \"ablate_control8_L13_R2\": 0.6787, \"ablate_control8_L13_CI\": [0.6322, 0.7255]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:57:09.980Z\"}, \"l1_head_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:59:16.298Z\", \"updated_at\": \"2026-05-17T16:02:05.924Z\", \"hypothesis\": \"L1 instruction-dominant heads (24/32 with >50% text attention) are causally necessary for instruction routing: ablating their instruction attention should collapse downstream instruction classification accuracy from ~100% to near-chance, while ablating non-dominant heads (control) should have minimal effect. This upgrades C2 (front-loaded routing) from correlational to partially causal.\", \"notes\": \"D057. Results: Classification 1.0 all conditions (instruction identity via residual stream). Action probe R²: L1 baseline=0.256 → ablate_all24=0.363 (Δ=+0.107, p<0.0001, CI [0.063,0.153]) → ablate_all32=0.375 (Δ=+0.119, p<0.0001, CI [0.065,0.167]). L8/L13 ns. Interpretation: L1 instruction-attending heads trade capacity between instruction routing and action encoding. Ablation frees capacity → L1 action R² increases. Deep layers unaffected. Monkey-patch verified working (diagnostic: inst attn → 0, cosine sim = 0.973).\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T12:00:40.435Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe.py --readout_layers 1 8 13 --demos_per_task 5 2>&1 | tee /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_log.txt\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"896931\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation.log\", \"submitted_at\": \"2026-05-17T14:49:06.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4379.9, \"gpu_hours\": 1.22}, \"metrics\": {\"classification_v2\": {\"baseline\": {\"L1\": 1, \"L8\": 1, \"L16\": 1, \"L31\": 1}, \"ablate_all24\": {\"L1\": 1, \"L8\": 1, \"L16\": 1, \"L31\": 1}, \"ablate_all32\": {\"L1\": 1, \"L8\": 1, \"L16\": 1, \"L31\": 1}, \"ablate_top5\": {\"L1\": 1, \"L8\": 1, \"L16\": 1, \"L31\": 1}, \"ablate_control8\": {\"L1\": 1, \"L8\": 1, \"L16\": 1, \"L31\": 1}}, \"action_probe_R2\": {\"baseline\": {\"L1\": 0.2558, \"L8\": 0.4401, \"L13\": 0.524}, \"ablate_all24\": {\"L1\": 0.3627, \"L8\": 0.4496, \"L13\": 0.5194}, \"ablate_all32\": {\"L1\": 0.3747, \"L8\": 0.4449, \"L13\": 0.5184}}, \"diagnostic\": {\"monkey_patch\": \"verified_working\", \"ablated_inst_attn\": 0, \"baseline_inst_attn\": 0.029, \"hidden_cosine_sim\": 0.973}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only experiment, no checkpoint produced)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/\", \"completed_at\": \"2026-05-17T16:02:05.924Z\"}, \"cross_inst_spatial_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:17:05.826Z\", \"updated_at\": \"2026-05-17T09:38:04.530Z\", \"hypothesis\": \"LIBERO-Spatial cross-instruction probe: trained VLA should show same token specialization as LIBERO-Goal (last_preaction=100% classification at all layers, image_mean=10% chance). Cross-benchmark replication strengthens C1 claim that readout token is instruction-conditioned while image tokens are instruction-blind.\", \"metrics\": {\"trained_image_mean\": {\"L0\": 0.1, \"L1\": 0.1, \"L4\": 0.1, \"L8\": 0.1, \"L12\": 0.1, \"L16\": 0.1, \"L20\": 0.1, \"L24\": 0.1, \"L28\": 0.1, \"L31\": 0.101}, \"trained_last_preaction\": {\"L0\": 0.1, \"L1\": 0.989, \"L4\": 1, \"L8\": 1, \"L12\": 1, \"L16\": 1, \"L20\": 1, \"L24\": 1, \"L28\": 1, \"L31\": 1}, \"untrained_image_mean\": {\"L0\": 0.1, \"L1\": 0.1, \"L4\": 0.1, \"L8\": 0.101, \"L12\": 0.099, \"L16\": 0.1, \"L20\": 0.099, \"L24\": 0.1, \"L28\": 0.1, \"L31\": 0.1}, \"untrained_last_preaction\": {\"L0\": 0.1, \"L1\": 0.995, \"L4\": 0.862, \"L8\": 0.683, \"L12\": 0.795, \"L16\": 0.765, \"L20\": 0.689, \"L24\": 0.777, \"L28\": 0.76, \"L31\": 0.754}}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_libero_spatial_cross_instruction_probe_20260517T085642.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:38:04.530Z\"}, \"plan010_rsa_spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:25:55.349Z\", \"updated_at\": \"2026-05-17T08:10:18.180Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"708431\", \"log_path\": \"~/runs/vla-ssd/plan010_rsa_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:55.106Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92663.1, \"gpu_hours\": 25.74}, \"hypothesis\": \"LIBERO-Spatial RSA cross-benchmark validation: trained VLA should show inverted-U RSA profile (peak mid-layers) consistent with LIBERO-Long, confirming representation-action alignment pattern generalizes to spatial reasoning tasks.\", \"metrics\": {\"trained_image_mean\": {\"best_layer\": \"L14\", \"RSA\": 0.6911}, \"trained_last_preaction\": {\"best_layer\": \"L15\", \"RSA\": 0.6945}, \"untrained_image_mean\": {\"best_layer\": \"L0\", \"RSA\": 0.6523}, \"untrained_last_preaction\": {\"best_layer\": \"L1\", \"RSA\": 0.6659}}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_libero_spatial.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/logs/rsa_spatial.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T08:10:18.180Z\"}, \"plan010_action_probe_spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:25:57.604Z\", \"updated_at\": \"2026-05-17T08:10:17.302Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"708576\", \"log_path\": \"~/runs/vla-ssd/plan010_action_probe_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:57.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92659.9, \"gpu_hours\": 51.48}, \"hypothesis\": \"LIBERO-Spatial cross-benchmark validation: trained VLA action probe should show inverted-U profile (peak mid-layers) consistent with LIBERO-Long, confirming functional specialization generalizes across spatial reasoning tasks. Untrained should peak at L0 (vision encoder only).\", \"metrics\": {\"trained_image_mean\": {\"best_layer\": \"L13\", \"R2\": 0.6963}, \"trained_last_preaction\": {\"best_layer\": \"L21\", \"R2\": 0.6748}, \"untrained_image_mean\": {\"best_layer\": \"L0\", \"R2\": 0.6732}, \"untrained_last_preaction\": {\"best_layer\": \"L1\", \"R2\": 0.6348}, \"bootstrap_significance\": \"p < 0.001 for all trained vs untrained comparisons\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T08:10:17.302Z\"}, \"llama2_base_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:08:39.367Z\", \"updated_at\": \"2026-05-17T06:43:03.341Z\", \"hypothesis\": \"Instruction routing (25/32 heads attending to instruction tokens) is primarily learned through VLA fine-tuning, not inherited from language pretraining. Llama-2-7B base (no VLA training) injected into OpenVLA should show intermediate attention patterns between untrained-VLA (0/32 heads) and trained-VLA (25/32 heads), proving VLA training amplifies routing beyond pretraining baseline.\", \"parent\": \"cross_inst_extract_trained\", \"spec\": {\"command\": \"python create_llama2_base_openvla.py + cross_instruction_extract_dense.py --condition llama2base + l1_attention_visualization.py --condition llama2base\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/\", \"data_count\": 500, \"model_name\": \"openvla-7b-llama2base (Llama-2-7B base weights injected into OpenVLA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/\", \"eval_data\": \"LIBERO cross-instruction 10 tasks × 50 demos (same as cross_inst_extract_trained)\"}, \"metrics\": {\"l1_heads_gt50pct\": {\"trained\": 25, \"untrained\": 0, \"llama2base\": 9}, \"l1_mean_text_attn\": {\"trained\": 0.577, \"untrained\": 0.117, \"llama2base\": 0.365}, \"l1_mean_image_attn\": {\"trained\": 0.213, \"untrained\": 0.878, \"llama2base\": 0.617}, \"dense_probe_L1_acc\": {\"trained\": 0.996, \"untrained\": 1, \"llama2base\": 0.802}, \"dense_probe_L2_acc\": {\"trained\": 1, \"untrained\": 1, \"llama2base\": 0.987}, \"dense_probe_L8_acc\": {\"trained\": 1, \"untrained\": 0.986, \"llama2base\": 0.999}, \"dense_probe_L16_acc\": {\"trained\": 1, \"untrained\": 0.92, \"llama2base\": 1}, \"dense_probe_L31_acc\": {\"trained\": 1, \"untrained\": 0.82, \"llama2base\": 1}, \"llama2base_instruction_heads\": [0, 15, 16, 17, 18, 23, 25, 26, 27], \"full_profile\": \"llama2base saturates at L5 (99.8-100%), NO deep-layer degradation unlike untrained (82% at L31)\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_llama2_base_probe_continue_20260517T054618.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:09:38.453Z\"}, \"rsa_cosine_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:12:08.680Z\", \"updated_at\": \"2026-05-17T02:58:05.071Z\", \"hypothesis\": \"RSA inverted-U pattern replicates with cosine action distance: peak ρ within 0.05 of euclidean peak, peak layer within ±3 layers. PASS: qualitative shape preserved. FAIL: cosine RSA shows flat/monotonic profile (no inverted-U).\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_cosine_action_metric.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/ablations/rsa_cosine_metric.json\", \"conclusion\": \"success\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_ablation_p0_cosine_metric_20260516T083517.log\", \"completed_at\": \"2026-05-16T10:12:58.780Z\"}, \"rsa_permutation_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:12:11.653Z\", \"updated_at\": \"2026-05-17T02:58:03.126Z\", \"hypothesis\": \"RSA observed ρ exceeds 95th percentile of 1000-permutation null distribution at every layer where ρ>0.10 (p<0.05). PASS: all key layers (L4-L24) significant. FAIL: any layer in peak region fails significance test.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_permutation_null.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/ablations/rsa_permutation_null.json\", \"conclusion\": \"success\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_ablation_p4_permutation_20260516T085748.log\", \"completed_at\": \"2026-05-16T10:12:59.991Z\"}, \"ablation_p1_seed_robustness\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:19:20.517Z\", \"updated_at\": \"2026-05-17T02:58:00.332Z\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/probe_seed_robustness.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"718019\", \"log_path\": \"~/runs/vla-ssd/ablation_p1_seed_robustness.log\", \"submitted_at\": \"2026-05-16T09:19:20.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features, probe only)\", \"seed\": \"multi: [0,1,2,3,42]\", \"wall_clock_seconds\": 3828.3, \"gpu_hours\": 1.06}, \"hypothesis\": \"Probe R² peak layer is consistent (±2 layers) and peak R² coefficient of variation CV<0.10 across 5 random seeds. PASS: peak layer stable AND CV<0.10. FAIL: peak layer variance >3 layers OR CV>0.15.\", \"metrics\": {\"seeds\": [0, 1, 2, 3, 42], \"peak_layer_per_seed\": [9, 16, 9, 10, 9], \"peak_r2_per_seed\": [0.6534, 0.6549, 0.6529, 0.6531, 0.6587], \"peak_layer_mean\": 10.6, \"peak_layer_std\": 2.73, \"peak_r2_mean\": 0.6546, \"peak_r2_std\": 0.0022, \"per_layer_std_range\": [0.0022, 0.0086], \"runtime_seconds\": 845.7, \"condition\": \"trained_image_mean\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/ablations/probe_seed_robustness.json\", \"completed_at\": \"2026-05-16T10:23:08.674Z\"}, \"ablation_p2_demo_sensitivity_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:34:16.651Z\", \"updated_at\": \"2026-05-17T02:57:57.883Z\", \"spec\": {\"command\": \"python scripts/ablations/demo_sensitivity.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"722187\", \"log_path\": \"~/runs/vla-ssd/ablation_p2_demo_sensitivity_v2.log\", \"submitted_at\": \"2026-05-16T10:34:16.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features, RSA+probe)\", \"seed\": 42, \"wall_clock_seconds\": 41519.1, \"gpu_hours\": 11.53}, \"hypothesis\": \"RSA inverted-U pattern (peak at L12, ρ>0.35) persists when demo count is halved (25 demos). PASS: peak layer within ±3 layers AND peak ρ within 0.05 AND profile correlation r>0.90. FAIL: peak shift >5 layers OR ρ drops >0.10 OR r<0.80.\", \"metrics\": {\"rsa_profile_correlation\": 0.9696, \"probe_profile_correlation\": 0.8189, \"rsa_peak_50demos\": {\"layer\": 12, \"rsa\": 0.6282}, \"rsa_peak_25demos\": {\"layer\": 12, \"rsa\": 0.6059}, \"probe_peak_50demos\": {\"layer\": 9, \"r2\": 0.6587}, \"probe_peak_25demos\": {\"layer\": 11, \"r2\": 0.6088}, \"n_layers\": 33, \"elapsed_seconds\": 1583.8, \"conclusion_summary\": \"Inverted-U highly stable under halved data. RSA profile r=0.97, peak L12 unchanged. Probe profile r=0.82, peak shifts L9→L11 but shape preserved.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/ablations/demo_sensitivity_25.json\", \"log_path\": \"~/runs/vla-ssd/ablation_p2_demo_sensitivity_v2.log\", \"completed_at\": \"2026-05-16T22:06:15.579Z\"}, \"p0_functional_action_delta_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:21:52.667Z\", \"updated_at\": \"2026-05-17T02:57:48.392Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action-delta prediction (Δa = a_{t+1}-a_t) on SigLIP+projector output features. Removes autocorrelation. Compare with LLM best (L14, R²=0.059) and DINO (R²=0.060). Also tests image_mean aggregation.\", \"metrics\": {\"projector\": {\"mean_R2\": 0.1181, \"overall_R2\": 0.1053}, \"trained_image_mean_L14\": {\"mean_R2\": 0.1215, \"overall_R2\": 0.1091}, \"untrained_best_L0\": {\"mean_R2\": 0.1174, \"overall_R2\": 0.107}, \"bootstrap_proj_vs_trained\": {\"delta\": -0.0034, \"ci_95\": [-0.0066, 0.0005], \"p_value\": 0.04}, \"note\": \"image_mean R² (~0.12) substantially higher than last_preaction (~0.06). Per-dim: dz=0.46, dx=0.29, dy=0.25 most predictable.\", \"gate\": \"Projector (0.118) ≈ LLM (0.122), gap tiny (Δ=0.003). Consistent with redistribution narrative.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json\", \"completed_at\": \"2026-05-15T23:45:44.568Z\", \"notes\": \"Delta probe: projector (0.118) BELOW LLM (0.122), CI=[-0.007, +0.001] 含 0, p=0.04. 差异不显著。论文需如实汇报：raw action PASS (projector > image_mean), delta BELOW (差异不显著)。双维度呈现。\", \"parent\": \"p0_functional_action_probe\"}, \"p0_functional_probe_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:47:31.973Z\", \"updated_at\": \"2026-05-17T02:57:47.705Z\", \"hypothesis\": \"V2 corrected functional probe: (1) Add projector vs image_mean_L19 bootstrap CI as primary gate (0.706 vs 0.683), (2) Add DINO action probe for three-way comparison, (3) Diagnose untrained L10/L11 anomaly (R² drops from 0.632 to 0.029). Re-dream prerequisite.\", \"metrics\": {\"bootstrap_proj_vs_image_mean_L19\": {\"proj_mean_R2\": 0.7063, \"image_mean_L19_mean_R2\": 0.6832, \"delta\": 0.0231, \"ci_95\": [0.0105, 0.0367], \"p_value\": 0.001, \"gate\": \"PASS — CI lower bound > 0\"}, \"dino_action\": {\"mean_R2\": 0.7116, \"feature_key\": \"cls_token\"}, \"dino_action_delta\": {\"mean_R2\": 0.1}, \"bootstrap_dino_vs_proj\": {\"delta\": 0.005, \"ci_95\": [-0.008, 0.019], \"p_value\": 0.22, \"significant\": false}, \"three_way_ordering\": \"DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)\", \"untrained_L10_L11_diagnosis\": {\"verdict\": \"pathological_random_init\", \"detail\": \"Feature stats normal (no NaN/Inf/zeros, std~5), but probe R² drops L9=0.632→L10=0.029. Random LLM weights create non-decodable representations at these layers.\"}, \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json\", \"completed_at\": \"2026-05-15T23:52:03.717Z\", \"parent\": \"p0_functional_action_probe\"}, \"d027_trained_no_inst_rsa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:10:55.271Z\", \"updated_at\": \"2026-05-17T02:57:46.208Z\", \"hypothesis\": \"D027 Exp-2: Extract trained VLA features with empty instruction on LIBERO-Goal, run RSA. Completes the 2×2 matrix (training × instruction). Expected: trained no-inst RSA ≈ untrained no-inst (0.4802), further confirming training is irrelevant to representational structure.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_features.py --task_instruction '' + python /root/vla-ssd/rsa_analysis.py (trained no-inst)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (trained, no instruction)\", \"model_name\": \"openvla/openvla-7b (trained, empty instruction)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_trained_no_inst.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"trained_no_inst_peak_rsa\": 0.489, \"trained_no_inst_peak_layer\": 30, \"full_2x2_matrix\": {\"trained_with_inst\": 0.4876, \"trained_no_inst\": 0.489, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"dino\": 0.388}, \"training_effect_with_inst\": 0.003, \"training_effect_no_inst\": 0.0088, \"instruction_effect_trained\": -0.0014, \"instruction_effect_untrained\": 0.0044, \"bootstrap_delta_ci\": \"[-0.058, 0.072] includes 0\", \"conclusion_summary\": \"All 4 conditions converge in 0.48-0.49 band. Neither training nor instruction has meaningful effect on RSA.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:16:04.389Z\", \"parent\": \"d027_siglip_only_rsa\"}, \"d021_output_head_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:17.179Z\", \"updated_at\": \"2026-05-17T02:57:45.273Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences per layer (Frobenius norm ratio). PASS: output head norm ratio >> LLM deep layer mean (>3x), confirming shallow adaptation. FAIL: differences uniformly distributed.\", \"spec\": {\"command\": \"python output_head_analysis.py (load trained + untrained state_dicts, compute per-layer Frobenius norm ratio)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/ + openvla-7b-untrained/\", \"data_count\": \"2 models x ~7B params each\", \"model_name\": \"openvla/openvla-7b vs openvla-7b-untrained weight comparison\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/output_head_analysis.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"note\": \"Worker: worker_ssh_output-head-analysis_20260515T200957. CPU-only analysis. PASS: output head norm ratio > 3x LLM layer mean.\"}, \"metrics\": {\"group_summary\": {\"vision\": {\"count\": 685, \"mean_rel_change\": 0, \"cos_sim\": 1, \"verdict\": \"IDENTICAL\"}, \"projector\": {\"count\": 6, \"mean_rel_change\": 0, \"cos_sim\": 1.001, \"verdict\": \"IDENTICAL\"}, \"embedding\": {\"count\": 1, \"rel_change\": 1.3287, \"cos_sim\": -0.0001}, \"llm\": {\"count\": 288, \"mean_rel_change\": 1.3156, \"std\": 0.3759, \"cos_sim\": 0.2178, \"range\": [1.22, 1.37]}, \"llm_final_norm\": {\"count\": 1, \"rel_change\": 0.8628, \"cos_sim\": 0.998}, \"head_lm_head\": {\"count\": 1, \"rel_change\": 1.4754, \"cos_sim\": 0.0002}}, \"head_vs_llm_ratio\": 1.12, \"shallow_adaptation_gate\": \"FAIL (ratio 1.12x, threshold 3x)\", \"key_finding_1\": \"Vision backbone + Projector IDENTICAL between trained and untrained (rel_change=0, cos_sim=1.0)\", \"key_finding_2\": \"LLM weight diffs uniformly distributed across all 32 layers (rel_change 1.22-1.37), head not special\", \"key_finding_3\": \"Shared frozen components (SigLIP + projector) explain WHY trained ≈ untrained in representation structure — regardless of LLM weights\", \"caveat\": \"Comparison is pretrained Llama + fine-tune vs random init, not fine-tuned vs pre-fine-tuning. Differences dominated by pretrained vs random.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T20:18:12.515Z\", \"parent\": \"d027_siglip_only_rsa\"}, \"d021_instruction_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:15.503Z\", \"updated_at\": \"2026-05-17T02:57:44.318Z\", \"hypothesis\": \"D021 Exp-1 (HARD GATE): Instruction Ablation on untrained VLA. Replace instruction with empty string, extract LIBERO-Goal features, run RSA. Gate (D023 relative): PASS = no-inst RSA significantly below with-inst (Δ>0.10, bootstrap CI excludes 0) AND no-inst RSA ≤ DINO RSA + 0.05. FAIL = no-inst RSA ≥ with-inst RSA − 0.05. PASS → lock Option B. FAIL → fallback Option A.\", \"spec\": {\"command\": \"python scripts/extract_features_no_instruction.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50 && python rsa_analysis.py (no-inst features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (no instruction)\", \"model_name\": \"openvla/openvla-7b-untrained (empty instruction ablation)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_no_instruction.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\", \"note\": \"Worker: worker_ssh_instruction-ablation_20260515T200929. Gate: PASS = Δ(with-no)>0.10 + CI excludes 0 + no-inst ≤ DINO+0.05. FAIL = no-inst ≥ with-inst−0.05.\"}, \"metrics\": {\"no_inst_untrained_peak_rsa\": 0.4802, \"with_inst_untrained_peak_rsa\": 0.4846, \"with_inst_trained_peak_rsa\": 0.4876, \"dino_rsa\": 0.388, \"delta_with_minus_no_inst\": 0.0044, \"gate_threshold_delta\": 0.1, \"gate_threshold_no_inst_max\": 0.438, \"gate_judgment\": \"FAIL — Δ=0.0044 << 0.10; no_inst=0.4802 >> DINO+0.05=0.438\", \"interpretation\": \"Removing instruction text does NOT collapse RSA. Untrained VLA action-relevant structure is vision-driven, not instruction-driven. Option B framing falsified.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T22:06:08.026Z\", \"parent\": \"d027_siglip_only_rsa\"}, \"lg_pca1024_linear_pertimestep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:39:51.209Z\", \"updated_at\": \"2026-05-17T02:57:42.915Z\", \"hypothesis\": \"D018 Exp-2: PCA-1024 + Linear Probe per-timestep (10 bins). Tests whether trained VLA shows stronger goal encoding than untrained at early timesteps (visual ambiguity highest). Success: t=0 bin Δ(trained-untrained) > 15pp.\", \"spec\": {\"command\": \"python pca_linear_probe_pertimestep.py --trained_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --untrained_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --dino_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --pca_dim 1024 --output /root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos, best layer features, 10 timestep bins\", \"model_name\": \"LogisticRegression (PCA-1024), per-timestep evaluation\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\"}, \"metrics\": {\"bin_0_trained\": 0.9992, \"bin_0_untrained\": 1, \"bin_0_dino\": 0.354, \"bin_0_delta_TU\": -0.0008, \"overall_trained\": 0.9999, \"overall_untrained\": 1, \"overall_dino\": 0.8397, \"per_bin\": {\"0\": {\"trained\": 0.9992, \"untrained\": 1, \"dino\": 0.354}, \"1\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.7662}, \"2\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8244}, \"3\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8676}, \"4\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8575}, \"5\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.8903}, \"6\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9618}, \"7\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9574}, \"8\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.969}, \"9\": {\"trained\": 1, \"untrained\": 1, \"dino\": 0.9676}}, \"gate_exp2\": \"FAIL\", \"gate_exp2_delta\": -0.0008, \"gate_exp2_threshold\": 0.15}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T19:40:23.583Z\", \"parent\": \"lg_extract_trained\"}, \"lg_rsa_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:51.878Z\", \"updated_at\": \"2026-05-17T02:57:41.972Z\", \"hypothesis\": \"D019/D020: RSA on LIBERO-Goal features. Same-scene/different-goal cross-goal RSA: representation RDM vs action RDM correlation. Gates (D020): G1 trained best-layer RSA ρ > 0.15; G2 Δρ(trained-untrained) > 0.08 with bootstrap 95% CI excluding 0; G3 trained ρ > DINO ρ (any positive margin).\", \"spec\": {\"command\": \"python rsa_analysis.py (full run on LIBERO-Goal features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers (VLA) / 1 layer (DINO)\", \"model_name\": \"RSA: Spearman(repr_RDM, action_RDM) per layer + CKA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"trained_peak_rsa\": 0.4876, \"trained_peak_layer\": 9, \"untrained_peak_rsa\": 0.4846, \"untrained_peak_layer\": 12, \"dino_rsa\": 0.388, \"delta_TU_at_trained_peak\": 0.003, \"delta_TU_range\": [-0.0722, 0.0109], \"layers_trained_gt_untrained\": 4, \"layers_total\": 33, \"per_phase\": {\"early\": {\"trained\": 0.3197, \"untrained\": 0.4148, \"dino\": 0.4909}, \"mid\": {\"trained\": 0.5231, \"untrained\": 0.5248, \"dino\": 0.4132}, \"late\": {\"trained\": 0.4758, \"untrained\": 0.4592, \"dino\": 0.2601}}, \"cka_range\": [0.687, 0.86], \"gate_G1_D020\": \"PASS (0.4876 > 0.15)\", \"gate_G2_D020\": \"FAIL (Δρ=0.003, threshold 0.08)\", \"gate_G3_D020\": \"PASS (0.4876 > 0.388, margin +0.0996)\", \"interpretation\": \"Architecture matters (VLA >> DINO), training doesn't (trained ≈ untrained). Instruction input adds action-relevant structure, but LLM training does not improve it.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T20:05:37.885Z\", \"parent\": \"lg_extract_trained\"}, \"lg_gc_trained_frame0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:27:20.212Z\", \"updated_at\": \"2026-05-17T02:57:34.120Z\", \"hypothesis\": \"Frame-0-only goal classification on trained VLA features (33 layers). Tests instruction encoding when visual states are most similar across goals. Key layer curve: L0=10%, L1=39%, L2=58%, L3+=100%.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_frames 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (frame 0 only)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features frame-0 only\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Frame-0 layer curve: L0=10%, L1=39%, L2=58%, L3+=100%. Shows 3+ layers needed for instruction integration at max visual ambiguity. Worker: worker_ssh_initial-frame-gc\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained_frame0.log\"}, \"metrics\": {\"trained_best_layer\": 3, \"trained_best_acc\": 1, \"trained_best_f1\": 1, \"untrained_best_layer\": 2, \"untrained_best_acc\": 1, \"untrained_best_f1\": 1, \"dino_best_acc\": 0.15, \"dino_best_f1\": 0.0911, \"n_classes\": 10, \"n_train\": 400, \"n_val\": 100, \"trained_layer_curve\": {\"L0\": 0.1, \"L1\": 0.39, \"L2\": 0.58, \"L3\": 1, \"L4_to_L18\": 1, \"L19\": 1, \"L28\": 1, \"L31\": 1, \"L32\": 1}, \"untrained_layer_curve\": {\"L0\": 0.1, \"L1\": 0.95, \"L2\": 1, \"L3\": 0.99, \"L19\": 0.91, \"L28\": 0.9, \"L31\": 0.88, \"L32\": 0.98}, \"sanity_gc_frame0\": \"PASS (DINO 15% <= 25%)\", \"g3_gc_frame0\": \"FAIL (Δ=0pp, both 100%)\", \"key_finding\": \"DINO 15% at t=0 confirms visual ambiguity. But MLP+4096 probe capacity still saturates both VLA models. Trained VLA more stable across layers (100% L3+) vs untrained (88-100% oscillation in deep layers). Needs PCA+linear verification.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:36:26.561Z\", \"parent\": \"lg_gc_trained\"}, \"lg_gc_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:53:30.361Z\", \"updated_at\": \"2026-05-17T02:57:33.216Z\", \"hypothesis\": \"DINO-V2 LIBERO-Goal goal classification probe (Sanity-GC gate). DINO acc must be ≤ 25% (10-class random=10%). If DINO > 25%, goals are visually distinguishable and experiment premise is challenged.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"635723\", \"log_path\": \"~/runs/vla-ssd/lg_gc_dino.log\", \"submitted_at\": \"2026-05-15T17:54:11.228Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer x 1024 dim\", \"model_name\": \"GoalClassificationProbe MLP (1024->256->10), DINO-V2 features\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/goal_classification/\", \"wall_clock_seconds\": 386.6, \"gpu_hours\": 0.11}, \"conclusion\": \"success\", \"metrics\": {\"best_accuracy\": 0.8626, \"best_traj_accuracy\": 1, \"best_macro_f1\": 0.8412, \"n_classes\": 10, \"num_layers\": 1, \"feature_dim\": 1024, \"gate_Sanity_GC\": \"FAIL\", \"note\": \"DINO acc 86.26% >> 25% threshold. Goals are visually distinguishable. Sanity-GC gate FAILED.\"}, \"completed_at\": \"2026-05-15T18:00:37.784Z\", \"parent\": \"lg_dino_extract\"}, \"lg_gc_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:51:49.753Z\", \"updated_at\": \"2026-05-17T02:57:32.214Z\", \"hypothesis\": \"Goal classification probe on untrained VLA LIBERO-Goal features (33 layers). Baseline for G2-GC gate: Δ(trained-untrained) best-layer acc > 25pp. Untrained VLA with random LLM should show lower goal classification accuracy.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), untrained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_untrained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_untrained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"pid\": 635369, \"reproduce\": {\"finished_at\": \"2026-05-15T18:01:11.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:01:12.865150+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"worst_layer\": 31, \"worst_accuracy\": 0.9971, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": 0.9998, \"11\": 0.9998, \"12\": 0.9999, \"13\": 0.9999, \"14\": 0.9996, \"15\": 0.9996, \"16\": 0.9998, \"17\": 0.9994, \"18\": 0.9989, \"19\": 0.9992, \"20\": 0.9995, \"21\": 0.9993, \"22\": 0.9996, \"23\": 0.9991, \"24\": 0.9994, \"25\": 0.9988, \"26\": 0.9993, \"27\": 0.9993, \"28\": 0.9986, \"29\": 0.9984, \"30\": 0.9977, \"31\": 0.9971, \"32\": 0.9991}, \"gate_G2_GC\": \"FAIL\", \"gate_G2_GC_delta\": 0, \"gate_G2_GC_threshold\": 0.25, \"layer0_detail\": \"predicts_only_class1_acc_0.158_random_level\", \"comparison\": {\"trained_best_acc\": 1, \"untrained_best_acc\": 1, \"dino_best_acc\": 0.8626, \"delta_trained_untrained\": 0, \"delta_trained_dino\": 0.1374}, \"interpretation\": \"Untrained VLA (random LLM) achieves identical 100% goal classification from layer 1+. G2-GC FAIL: Δ=0pp (threshold 25pp). Goal classification is NOT a valid discriminator between trained and untrained VLA — the MLP probe on 4096-dim features trivially separates 10 classes even from random projections.\"}, \"completed_at\": \"2026-05-15T18:03:31.246Z\", \"parent\": \"lg_extract_untrained\"}, \"lg_gc_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:42:55.296Z\", \"updated_at\": \"2026-05-17T02:57:31.289Z\", \"hypothesis\": \"Goal classification probe on trained VLA LIBERO-Goal features (33 layers). Gate G1-GC: best-layer acc > 40%. Core evidence for instruction encoding in VLA representations.\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T17:43:12.537Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\\\"\", \"finished_at\": \"2026-05-15T17:51:48.066Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir .../trained_libero_goal/ --output_dir .../results/trained_libero_goal/ --probe_type goal_classification --data_dir .../libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained.log\"}, \"pid\": \"634360\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:51:52.405382+00:00\"}]}, \"metrics\": {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": 1, \"11\": 1, \"12\": 1, \"13\": 1, \"14\": 1, \"15\": 1, \"16\": 1, \"17\": 1, \"18\": 1, \"19\": 1, \"20\": 1, \"21\": 1, \"22\": 1, \"23\": 1, \"24\": 1, \"25\": 1, \"26\": 1, \"27\": 1, \"28\": 1, \"29\": 1, \"30\": 1, \"31\": 1, \"32\": 1}, \"layer0_detail\": \"predicts_only_class1_acc_0.158\", \"layer1_epochs\": 13, \"layers_2_32_epochs\": 6, \"gate_G1_GC\": \"PASS\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:54:35.688Z\", \"parent\": \"lg_extract_trained\"}, \"cross_inst_extract_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:44:47.908Z\", \"updated_at\": \"2026-05-17T02:57:30.333Z\", \"hypothesis\": \"Untrained VLA baseline: without task-specific training, instruction-conditioned features should show minimal instruction encoding (near chance-level 10% accuracy)\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition untrained --gpu 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 frames × 10 instructions\", \"model_name\": \"openvla-7b (untrained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/untrained_cross_inst.h5\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/untrained_cross_inst.h5\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/untrained_extract.log\", \"completed_at\": \"2026-05-16T23:55:13.039Z\", \"parent\": \"cross_inst_extract_trained\"}, \"cross_inst_extract_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:44:47.190Z\", \"updated_at\": \"2026-05-17T02:57:29.382Z\", \"hypothesis\": \"Trained VLA features encode instruction identity: same frame with different instructions should produce distinguishable representations, especially in mid-to-late layers where action planning occurs\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition trained --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 frames × 10 instructions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/trained_cross_inst.h5\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/trained_cross_inst.h5\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/trained_extract.log\", \"completed_at\": \"2026-05-16T23:50:31.538Z\", \"parent\": \"qa_probe_classification\"}, \"openvla-untrained-extract\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T10:07:29.551Z\", \"updated_at\": \"2026-05-17T02:57:23.574Z\", \"notes\": \"1. 当前 untrained checkpoint 未使用固定 seed（init_untrained.py 缺 torch.manual_seed），但 checkpoint 已持久化到 /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/，可复现。脚本已补 seed=42 供将来使用。2. 日志中 mode=trained 为 extract_features.py 默认值，实际使用的是 openvla-7b-untrained checkpoint。3. EXIT_CODE=130 是 Worker(fix-extraction-restart) 主动 kill 以修复 I/O 瓶颈（264次 .cpu() → 2次/batch，52x 加速）。4. fix-extraction-restart Worker 补完 LIVING_ROOM_SCENE6 + STUDY_SCENE1（18.5 min），最终 10/10 tasks 全部完成。features/untrained/ 现有 10 个 .h5 文件，每个 50 demos。\", \"reproduce\": {\"finished_at\": \"2026-05-15T12:54:22.478Z\"}, \"failure_reason\": \"EXIT_CODE=130 (SIGINT / Ctrl-C)\", \"completed_at\": \"2026-05-15T12:54:27.745Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:54:28.598354+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"1. 当前 untrained checkpoint 未使用固定 seed（init_untrained.py 缺 torch.manual_seed），但 checkpoint 已持久化到 /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/，可复现。脚本已补 seed=42 供将来使用。2. 日志中 mode=trained 为 extract_features.py 默认值，实际使用的是 openvla-7b-untrained checkpoint。3. EXIT_CODE=130 是 Worker(fix-extraction-restart) 主动 kill 以修复 I/O 瓶颈（264次 .cpu() → 2次/batch）。8/10 tasks 已完成，剩 LIVING_ROOM_SCENE6 和 STUDY_SCENE1。Worker 正在修复脚本后重启提取剩余 2 tasks。\"}}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"total_size_gb\": 52, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"io_fix_speedup\": \"52x (0.8→42 step/s)\", \"reextracted_tasks\": [\"LIVING_ROOM_SCENE6\", \"STUDY_SCENE1\"], \"reextraction_time_min\": 18.5}, \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir features/untrained/ --gpu 0 --max_demos 50 (retry: reextracted LIVING_ROOM_SCENE6 + STUDY_SCENE1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b-untrained (LLM 6.74B random from_config, Vision 0.80B preserved)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"log_path\": \"~/runs/vla-ssd/openvla-untrained-extract.log\"}, \"hypothesis\": \"Infrastructure: extract untrained OpenVLA hidden states as baseline for training-effect comparison. Success: per-layer features saved matching trained extraction dimensions.\"}, \"openvla-trained-extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:01:11.067Z\", \"updated_at\": \"2026-05-17T02:57:22.867Z\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b --output_dir features/trained/ --gpu 0 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"27091\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"submitted_at\": \"2026-05-15T10:01:11.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"notes\": \"transformers 版本差异: 模型期望 4.40.1, 实际 4.57.6。trained/untrained 使用同一版本，对比有效。复现时需注意版本匹配。\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"wall_clock_seconds\": 11497.6, \"gpu_hours\": 3.19}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:07:39.142Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:07:39.880750+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"total_size_gb\": 53, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"extraction_time_min\": 185.3, \"exit_code\": 0}, \"completed_at\": \"2026-05-15T13:12:48.634Z\", \"hypothesis\": \"Infrastructure: extract trained OpenVLA hidden states for initial RSA and probe experiments. Success: per-layer features saved for all demos/tasks.\"}, \"lg_extract_untrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:42:35.326Z\", \"updated_at\": \"2026-05-17T02:57:20.969Z\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"finished_at\": \"2026-05-15T17:41:31.327Z\"}, \"failure_reason\": \"Traceback → -packages/urllib3/util/connection.py\\\", line 85, in create_connection raise err File \\\"/root/miniconda3/lib/python3.12/site-packages/urllib3/util/connection.py\\\", line 73, in create_connection sock.connect(sa) OSError: [Errno 101] Network is unreachable\", \"completed_at\": \"2026-05-15T16:54:31.908Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:54:33.449692+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:41:32.343537+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 同 lg_extract_trained — AutoProcessor.from_pretrained() 网络不可达。提取进度到 22%。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\"}}, \"notes\": \"失败原因: 同 lg_extract_trained — AutoProcessor.from_pretrained() 网络不可达。提取进度到 22%。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"note\": \"--gpu 0 + CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\"}, \"pid\": 627335, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 2/10 from first run + 8/10 from retry.\"}, \"hypothesis\": \"Infrastructure prerequisite: extract untrained VLA features (all 33 layers × 50 demos × 10 tasks) for downstream comparison with trained. Success: all features saved without error, shapes match trained extraction.\"}, \"lg_extract_trained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:42:33.477Z\", \"updated_at\": \"2026-05-17T02:57:19.550Z\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"finished_at\": \"2026-05-15T17:39:24.617Z\"}, \"failure_reason\": \"Traceback → -packages/urllib3/util/connection.py\\\", line 85, in create_connection raise err File \\\"/root/miniconda3/lib/python3.12/site-packages/urllib3/util/connection.py\\\", line 73, in create_connection sock.connect(sa) OSError: [Errno 101] Network is unreachable\", \"completed_at\": \"2026-05-15T16:54:26.701Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:54:27.826438+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:39:25.096897+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: AutoProcessor.from_pretrained() 连接 huggingface.co 失败 (Network is unreachable)，AutoDL 服务器网络未启用代理。日志显示提取进度到 52%（open_the_top_drawer task），说明模型可能从缓存加载成功但后续网络调用导致崩溃。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835\"}}, \"notes\": \"Retry #1 after local_files_only fix. PID 627256 restarted ~17:00 UTC. Script skips completed h5 files (3/10 done from first run).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"wall_clock_seconds\": 3204, \"gpu_hours\": 0.89}, \"pid\": 627256, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"extraction_time_min\": 53.4, \"feature_dim\": 4096, \"num_layers\": 33, \"dtype\": \"float16\", \"demos_per_task\": 50, \"exit_code\": 0, \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"note\": \"Retry after local_files_only fix. 3/10 from first run + 7/10 from retry.\"}, \"hypothesis\": \"Infrastructure prerequisite: extract trained VLA features (all 33 layers × 50 demos × 10 tasks) for downstream goal classification and RSA analysis. Success: all features saved without error, shapes verified.\"}, \"dinov2_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:05.849Z\", \"updated_at\": \"2026-05-17T02:57:18.145Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type temporal_distance --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = 138,090 frames\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large, 304.4M params)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/\", \"feature_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (503MB, 10 .pt files)\", \"probe_config\": \"MLP (1 hidden layer) trained with Adam + early stopping, task-level 80/20 split, distance-stratified sampling (10 bins x 50 pairs/bin/traj)\", \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"extraction_time\": \"795.8s, 174 fps, batch_size=32\"}, \"conclusion\": \"success\", \"metrics\": {\"temporal_distance_rho\": 0.833, \"temporal_distance_rho_pooled\": 0.833, \"per_task_rho_mean\": 0.9008, \"per_task_rho_range\": [0.41, 0.68], \"per_task_n_pairs\": 500, \"R2\": 0.687, \"MAE\": 0.127, \"feature_dim\": 1024, \"num_layers\": 1, \"probe_type\": \"mlp_adam_early_stopping\", \"training_time_seconds\": 7.5, \"note\": \"pooled ρ=0.833 inflated by cross-task variance; per-task mean ρ=0.9008 is correct comparison baseline (updated per D005/D006)\", \"subtask_macro_auc\": 0.9717, \"subtask_auc_per_predicate\": {\"subtask_0\": 0.9694, \"subtask_1\": 0.9739}, \"subtask_labels\": \"auto-extracted from MuJoCo state transitions (2 subtasks per task)\", \"subtask_probe_type\": \"sklearn_logistic_regression_lbfgs\", \"control_b_label_permutation_rho\": 0.039, \"control_b_label_permutation_per_task_mean\": 0.039, \"control_b_label_permutation_R2\": -0.052, \"cross_traj_rho\": 0.65, \"cross_traj_note\": \"supplementary analysis, not control; visual progress transfers across trajectories\"}, \"completed_at\": \"2026-05-15T11:24:37.420Z\", \"hypothesis\": \"DINOv2 single-layer RSA establishes vision-only floor for action-geometry encoding. Expected: RSA ρ comparable to VLA early layers (~0.45-0.50). If DINOv2 ρ > VLA peak → vision encoder alone captures action geometry, VLA LLM adds no value.\"}, \"plan_012_clip_vit_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:30:24.984Z\", \"updated_at\": \"2026-05-17T02:57:15.291Z\", \"spec\": {\"command\": \"python scripts/extract_features_clip.py + python scripts/rsa_clip.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos = 63728 frames\", \"model_name\": \"CLIP ViT-L/14 (openai)\", \"seed\": 42, \"checkpoint_path\": \"/root/vla-ssd/checkpoints/clip-vit-large-patch14/\", \"log_path\": \"/tmp/clip_extract.log\"}, \"metrics\": {\"unified_probe_hyperparams\": \"epochs=50,patience=5,lr=1e-3,batch=256,hidden=256,seed=42\", \"projector_mean_R2\": 0.6298, \"dino_cls_mean_R2\": 0.6343, \"clip_cls_mean_R2\": 0.5866, \"vla_image_mean_L19_mean_R2\": 0.5986, \"vla_last_preaction_L19_mean_R2\": 0.6711, \"ordering\": \"vla_last_preaction_L19 > dino_cls ≈ projector > vla_image_mean_L19 > clip_cls\", \"projector_vs_dino_p\": 0.557, \"projector_vs_clip_p\": 0, \"clip_vs_dino_p\": 0, \"projector_vs_vla_imL19_p\": 0, \"projector_vs_vla_lpL19_p\": 0.002}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:38:19.559Z\", \"hypothesis\": \"CLIP ViT-L control: if RSA inverted-U pattern appears in a vision-language model NOT finetuned for action, then the pattern is not VLA-training-specific but a general property of pretrained vision encoders. FAIL: CLIP RSA shows flat/monotonic profile (no inverted-U) → pattern is VLA-training-specific.\"}, \"qa_probe_classification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:57:02.141Z\", \"updated_at\": \"2026-05-17T02:08:15.690Z\", \"hypothesis\": \"QA Probe: Test whether VLA LLM layers encode high-level task understanding (progress/subtask classification), not just low-level action prediction. If trained deep layers >> DINO/Projector on progress classification, LLM training provides semantic understanding. If DINO matches, vision encoder already encodes this information.\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"744973\", \"log_path\": \"~/runs/vla-ssd/qa_probe_classification.log\", \"submitted_at\": \"2026-05-16T22:02:46.068Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 demos, 4-class progress + binary subtask\", \"model_name\": \"openvla-7b (trained + untrained)\", \"seed\": 42, \"wall_clock_seconds\": 14729.6, \"gpu_hours\": 4.09}, \"conclusion\": \"success\", \"metrics\": {\"progress_best_acc\": 0.8632, \"progress_best_layer\": \"L20_trained\", \"subtask_best_acc\": 0.9367, \"subtask_best_layer\": \"L16/L20_trained\", \"dino_progress\": 0.8272, \"dino_subtask\": 0.9209}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json\", \"completed_at\": \"2026-05-17T02:08:15.690Z\"}, \"rsa_per_dof_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:12:10.054Z\", \"updated_at\": \"2026-05-16T10:17:33.878Z\", \"hypothesis\": \"Per-DoF RSA decomposition: action dimension breakdown (xyz/rpy/gripper). Tests whether a single DoF drives the RSA signal.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_per_dof.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/ablations/rsa_per_dof.json\", \"conclusion\": \"success\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_ablation_p3_per_dof_20260516T085732.log\", \"completed_at\": \"2026-05-16T10:12:59.376Z\"}, \"plan_010_extract_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:18:41.215Z\", \"updated_at\": \"2026-05-16T08:58:07.063Z\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"705603\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log\", \"submitted_at\": \"2026-05-16T05:18:41.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": 500, \"model_name\": \"openvla-7b (LIBERO-Goal fine-tuned)\", \"seed\": 42, \"wall_clock_seconds\": 11701.5, \"gpu_hours\": 3.25}, \"hypothesis\": \"Sub-experiment of plan_010: Extract trained VLA (LIBERO-Goal fine-tuned) features on LIBERO-Spatial. 33 layers, image_mean + last_preaction, 50 demos/task.\", \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"output_size_gb\": 24, \"output_dir\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_spatial/\", \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"num_layers\": 33, \"demos_per_task\": 50}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_spatial/\", \"completed_at\": \"2026-05-16T08:33:42.558Z\"}, \"plan_010_extract_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:18:42.360Z\", \"updated_at\": \"2026-05-16T08:33:46.777Z\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"705681\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_untrained.log\", \"submitted_at\": \"2026-05-16T05:18:42.203Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": 500, \"model_name\": \"openvla-7b-untrained (random LLM + preserved SigLIP)\", \"seed\": 42, \"wall_clock_seconds\": 11704.6, \"gpu_hours\": 3.25}, \"hypothesis\": \"Sub-experiment of plan_010: Extract untrained VLA (random LLM + preserved SigLIP) features on LIBERO-Spatial. 33 layers, image_mean + last_preaction, 50 demos/task.\", \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": \"10/10\", \"output_size_gb\": 25, \"output_dir\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/\", \"feature_keys\": [\"image_mean\", \"last_preaction\"], \"num_layers\": 33, \"demos_per_task\": 50}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/\", \"completed_at\": \"2026-05-16T08:33:46.777Z\"}, \"plan_010_libero_spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:54:15.423Z\", \"updated_at\": \"2026-05-16T07:49:47.514Z\", \"hypothesis\": \"Cross-benchmark validation on LIBERO-Spatial: do the core patterns (C1 vision encoder dominance, C2 LLM inverted-U transformation, C3 training redistribution) replicate on a different LIBERO suite? Trained model is LIBERO-Goal fine-tuned (out-of-distribution for Spatial), testing generalization of representational structure.\", \"spec\": {\"command\": \"extract_features.py × 2 (trained cuda:0 + untrained cuda:1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": \"10 tasks × 50 demos = 500 demos\", \"model_name\": \"OpenVLA-7B trained (LIBERO-Goal fine-tuned) + untrained (random LLM)\", \"seed\": \"N/A (feature extraction)\", \"checkpoint_path\": \"features → trained_libero_spatial/ + untrained_libero_spatial/\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log + plan_010_extract_untrained.log\", \"sub_experiments\": [\"plan_010_extract_trained (cuda:0, PID 705603)\", \"plan_010_extract_untrained (cuda:1, PID 705681)\"]}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:29:27.206Z\", \"notes\": \"LIBERO-Spatial cross-benchmark validation complete. All three Core Claims replicate. Inverted-U (C2) confirmed on both RSA and R². Training redistribution (C3) confirmed — peaks shift from L0 to L13-15. Key: Spatial best-vs-best RSA Δ=+0.023, CI=[0.012, 0.036], p<0.001 (SIGNIFICANT) — contrasts with Goal's n.s. result (Δ=+0.017, CI=[-0.0002, 0.035]). Goal was underpowered; Spatial detects significance. Training effect is real but small.\", \"metrics\": {\"rsa\": {\"trained_image_mean_peak\": {\"layer\": 14, \"rsa\": 0.6911}, \"trained_last_preaction_peak\": {\"layer\": 15, \"rsa\": 0.6945}, \"untrained_image_mean_peak\": {\"layer\": 0, \"rsa\": 0.6523}, \"untrained_last_preaction_peak\": {\"layer\": 1, \"rsa\": 0.6659}, \"pattern\": \"trained inverted-U confirmed, untrained flat/declining\"}, \"action_probe\": {\"trained_image_mean_peak\": {\"layer\": 13, \"R2\": 0.6963}, \"trained_last_preaction_peak\": {\"layer\": 21, \"R2\": 0.6748}, \"untrained_image_mean_peak\": {\"layer\": 0, \"R2\": 0.6732}, \"untrained_last_preaction_peak\": {\"layer\": 1, \"R2\": 0.6348}, \"untrained_lastpre_collapse\": \"L5-L31 R2 approx -0.015, only L32 recovers to 0.621\"}, \"bootstrap\": {\"best_vs_best_imgmean\": {\"delta\": 0.023, \"ci_95\": [0.012, 0.036], \"p\": 0.001}, \"best_vs_best_lastpre\": {\"delta\": 0.04, \"ci_95\": [0.019, 0.057], \"p\": 0.0004}, \"same_layer_L13_imgmean\": {\"delta\": 0.711, \"ci_95\": [0.685, 0.74], \"p\": 0.001}, \"same_layer_L21_lastpre\": {\"delta\": 0.37, \"ci_95\": [0.317, 0.427], \"p\": 0.001}}, \"cross_benchmark\": {\"rsa_peak_goal\": \"L12\", \"rsa_peak_spatial\": \"L14-15\", \"probe_peak_goal\": \"L8-13\", \"probe_peak_spatial\": \"L13-21\", \"consistency\": \"high — peak layers within 2-layer range\"}, \"result_files\": [\"/root/autodl-tmp/vla-ssd/results/rsa/rsa_libero_spatial.json\", \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json\"]}}, \"plan_013_branch_split\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:04:25.014Z\", \"updated_at\": \"2026-05-16T05:05:17.493Z\", \"hypothesis\": \"Branch-split RSA: separate DINOv2 branch (first 1024d) and SigLIP branch (last 1152d) from Prismatic fused backbone (2176d projector input). Quantify each component's contribution to action-aligned geometry. Method B, 50 demos/task, 10 LIBERO-Goal tasks.\", \"spec\": {\"command\": \"python rsa_branch_split.py + extract_fused_backbone.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/\", \"data_count\": \"50 demos/task × 10 tasks, 2176d patch_mean\", \"model_name\": \"Prismatic DinoSigLIP fused backbone (DINOv2 1024d + SigLIP 1152d)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json\", \"log_path\": \"/root/vla-ssd/scripts/rsa_branch_split.py\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:05:03.394Z\", \"metrics\": {\"dinov2_branch_rsa\": 0.619, \"siglip_branch_rsa\": 0.621, \"fused_2176d_rsa\": 0.634, \"post_projector_4096d_rsa\": 0.615, \"standalone_dino_cls_rsa\": 0.692, \"standalone_dino_patch_mean_rsa\": 0.631, \"key_findings\": [\"DINOv2 ≈ SigLIP in fused backbone (delta < 0.002)\", \"Fused > either branch (complementary benefit)\", \"Projector compresses 0.634→0.615\", \"Standalone DINO cls > in-backbone DINOv2 (different extraction layer)\"], \"result_file\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json\"}}, \"d041_method_b_rsa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:04:24.314Z\", \"updated_at\": \"2026-05-16T05:05:13.600Z\", \"hypothesis\": \"Unified Method B RSA across all VLA conditions (6 conditions × 33 layers, trained/untrained × with_inst/no_inst, plus baselines). Foundation for paper Table 1. Method B: within-task pairing, cosine rep distance, euclidean action distance, N_SAMPLE=20, Spearman, 50 demos/task.\", \"spec\": {\"command\": \"python rsa_unified_vla.py + rsa_definitive_recalc.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/ + untrained + baselines\", \"data_count\": \"50 demos/task × 10 tasks\", \"model_name\": \"OpenVLA-7B trained/untrained + DINO/CLIP/SigLIP baselines\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:05:02.793Z\", \"metrics\": {\"trained_image_mean_peak\": {\"layer\": 12, \"rsa\": 0.6282}, \"trained_last_preaction_peak\": {\"layer\": 12, \"rsa\": 0.6425}, \"untrained_image_mean_peak\": {\"layer\": 0, \"rsa\": 0.6117}, \"untrained_last_preaction_peak\": {\"layer\": 1, \"rsa\": 0.6262}, \"baselines\": {\"dino_cls\": 0.6915, \"dino_patch_mean\": 0.6307, \"siglip_projector\": 0.615, \"clip_cls\": 0.557}, \"bootstrap_best_vs_best_imgmean\": {\"delta\": 0.017, \"ci_95\": [-0.0002, 0.035], \"significant\": false}, \"bootstrap_best_vs_best_lastpre\": {\"delta\": 0.016, \"ci_95\": [0.0001, 0.031], \"significant\": \"marginal\"}, \"bootstrap_same_layer_L12_imgmean\": {\"delta\": 0.079, \"p\": 0.0001}, \"bootstrap_same_layer_L12_lastpre\": {\"delta\": 0.047, \"p\": 0.0001}, \"result_files\": [\"/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json\", \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json\"]}}, \"plan_011_fulllayer_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:45:03.186Z\", \"updated_at\": \"2026-05-16T04:45:43.247Z\", \"hypothesis\": \"Full-layer R² scan (L0-L32) for trained/untrained × image_mean/last_preaction. Key question: does R² peak align with RSA peak at L12, or diverge (e.g., L19 as in current single-layer data)? RSA-R² peak alignment/misalignment itself is a finding for Claim 2 (redistribution mechanism).\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/fulllayer_action_probe.py\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4 conditions\", \"model_name\": \"MLP action probe (4096-256-7)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/runs/vla-ssd/fulllayer_action_probe.log\"}, \"conclusion\": \"success\", \"metrics\": {\"trained_image_mean_peak\": {\"layer\": 8, \"mean_R2\": 0.6553}, \"trained_last_preaction_peak\": {\"layer\": 13, \"mean_R2\": 0.6779}, \"untrained_image_mean_peak\": {\"layer\": 0, \"mean_R2\": 0.6403}, \"untrained_last_preaction_peak\": {\"layer\": 32, \"mean_R2\": 0.6093}, \"bootstrap_best_vs_best\": {\"image_mean\": {\"delta\": 0.0149, \"p\": 0.006}, \"last_preaction\": {\"delta\": 0.0686, \"p\": 0.0001}}, \"bootstrap_same_layer\": {\"image_mean_L8\": {\"delta\": 0.1229, \"p\": 0.0001}, \"last_preaction_L13\": {\"delta\": 1.0071, \"p\": 0.0001, \"note\": \"large delta suggests untrained L13 R2 near -0.33 (collapsed layer)\"}}, \"rsa_vs_r2_peak_comparison\": {\"trained_imgmean\": \"RSA peak L12, R2 peak L8 — 4-layer offset\", \"trained_lastpre\": \"RSA peak L12, R2 peak L13 — near-aligned\", \"untrained_imgmean\": \"RSA peak L0, R2 peak L0 — aligned\", \"untrained_lastpre\": \"RSA peak L1, R2 peak L32 — maximally divergent\"}, \"runtime_minutes\": 19.5, \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json\"}, \"checkpoint_path\": \"N/A (probe models not saved)\", \"log_path\": \"/root/runs/vla-ssd/fulllayer_action_probe.log\", \"completed_at\": \"2026-05-16T04:45:35.164Z\", \"notes\": \"checkpoint_path: N/A (probe experiment, no persistent model)\"}, \"unified_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:42.255Z\", \"updated_at\": \"2026-05-16T03:32:36.703Z\", \"hypothesis\": \"Unified hyperparameter action probe (50ep/patience5/seed42) across all vision encoders on LIBERO-Goal. Resolves cross-experiment R² incomparability caused by differing probe configs. Tests geometric-functional dissociation: does VL pretraining RSA advantage translate to R² advantage?\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/unified_action_probe.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{clip,dino,trained,siglip}/\", \"data_count\": 63728, \"model_name\": \"MLP(input→256→7)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe, no checkpoint saved)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T02:17:24.362Z\", \"metrics\": {\"hyperparams\": {\"epochs\": 50, \"patience\": 5, \"lr\": 0.001, \"hidden\": 256, \"seed\": 42, \"target\": \"a_{t+1}\", \"target_verified\": true, \"note\": \"All probes (original + unified) use same target feat[t]→act[t+1]. Confirmed by code audit.\"}, \"results\": {\"vla_last_preaction_L19\": {\"mean_R2\": 0.6711, \"overall_R2\": 0.7234}, \"dino_cls\": {\"mean_R2\": 0.6343, \"overall_R2\": 0.7012}, \"projector\": {\"mean_R2\": 0.6298, \"overall_R2\": 0.6992}, \"vla_image_mean_L19\": {\"mean_R2\": 0.5986, \"overall_R2\": 0.677}, \"clip_cls\": {\"mean_R2\": 0.5866, \"overall_R2\": 0.6602}}, \"bootstrap_pairwise\": {\"projector_vs_dino\": {\"delta\": -0.0045, \"p\": 0.557, \"significant\": false}, \"projector_vs_clip\": {\"delta\": 0.043, \"p\": 0.001, \"significant\": true}, \"dino_vs_clip\": {\"delta\": 0.048, \"p\": 0.001, \"significant\": true}, \"projector_vs_vla_image_mean\": {\"delta\": 0.031, \"p\": 0.001, \"significant\": true}, \"last_preaction_vs_projector\": {\"delta\": 0.041, \"p\": 0.002, \"significant\": true}}}, \"notes\": \"D041 confirmed: unified_rsa_results.json uses 50 demos/task (Method B), consistent with all standalone baselines. n_demos verified from server-side h5 files. Key results: trained image_mean peak L12=0.6282, last_preaction peak L12=0.6425. D040 (L9-only 10-demo \\\"readout RSA training degradation\\\") superseded — L9 is not peak, trained peak is L12. Bootstrap CI (best-vs-best): image_mean Δ=+0.017 CI=[-0.0002,+0.035] n.s.; last_preaction Δ=+0.016 CI=[+0.0001,+0.031] marginal. Same-layer L12: image_mean Δ=+0.079 p<0.0001; last_preaction Δ=+0.047 p<0.0001. Training redistributes peak from L0→L12, does not create new information.\"}, \"lg_instruction_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:57.146Z\", \"updated_at\": \"2026-05-16T01:38:26.242Z\", \"hypothesis\": \"D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.\", \"conclusion\": \"killed\", \"notes\": \"Duplicate of d021_instruction_ablation. Superseded by Director-specified ID. Cleaned up per D028.\", \"completed_at\": \"2026-05-16T01:38:26.242Z\"}, \"lg_output_head_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.398Z\", \"updated_at\": \"2026-05-16T01:38:25.425Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".\", \"conclusion\": \"killed\", \"notes\": \"Duplicate of d021_output_head_analysis. Superseded by Director-specified ID. Cleaned up per D028.\", \"completed_at\": \"2026-05-16T01:38:25.425Z\"}, \"plan_008_random_inst_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:57:16.908Z\", \"updated_at\": \"2026-05-16T01:16:03.037Z\", \"hypothesis\": \"Plan_008 (Claim 3): Random instruction control. Replace real instruction with random gibberish (random_s0) or word-shuffled version (shuffled). If RSA ≈ normal instruction (0.488) → instruction content irrelevant, supports invariance. If RSA drops significantly → instruction content matters.\", \"spec\": {\"command\": \"python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0}, \"notes\": \"RSA instruction control completed. All 4 conditions peak at L16. Deltas vs normal: empty=-0.0165, random_s0=-0.0053, shuffled=-0.0056. Max |Δ|=0.0165 (well within 0.02 threshold). Instruction content is irrelevant to representation-action alignment structure. Result file: /root/autodl-tmp/vla-ssd/results/rsa/rsa_instruction_control_last_preaction.json\", \"metrics\": {\"normal_peak_rsa\": 0.4888, \"normal_peak_layer\": 16, \"empty_peak_rsa\": 0.4723, \"empty_peak_layer\": 16, \"random_s0_peak_rsa\": 0.4835, \"random_s0_peak_layer\": 16, \"shuffled_peak_rsa\": 0.4832, \"shuffled_peak_layer\": 16, \"delta_empty_vs_normal\": -0.0165, \"delta_random_s0_vs_normal\": -0.0053, \"delta_shuffled_vs_normal\": -0.0056, \"max_absolute_delta\": 0.0165, \"instruction_invariant\": true}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_instruction_control_last_preaction.json\", \"log_path\": \"/tmp/rsa_ic2.log\", \"completed_at\": \"2026-05-16T01:16:03.037Z\"}, \"untrained_last_preaction_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:08:56.469Z\", \"updated_at\": \"2026-05-16T00:14:01.670Z\", \"spec\": {\"command\": \"python scripts/action_probe.py --features untrained --feature_key last_preaction\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-untrained\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/\"}, \"metrics\": {\"untrained_last_preaction_L19_mean_R2\": 0.325, \"trained_last_preaction_L19_mean_R2\": 0.7309, \"projector_mean_R2\": 0.706, \"delta_trained_vs_untrained_L19\": 0.406, \"untrained_best_layer\": \"L32\", \"untrained_best_R2\": 0.6858, \"delta_best_vs_best\": 0.0452, \"bootstrap_ci_trained_vs_untrained\": {\"trained_L19_mean_R2\": 0.7309, \"untrained_L32_mean_R2\": 0.6858, \"observed_delta\": 0.0452, \"ci_95\": [0.0321, 0.0585], \"p_value\": 0.0001, \"ci_excludes_0\": true, \"all_10_tasks_positive\": true, \"per_task_delta_range\": [0.02, 0.083], \"n_bootstrap\": 10000}, \"conclusion_summary\": \"Untrained best last_preaction R²=0.686 < trained 0.731 (Δ=0.045, CI=[0.032,0.059], p<0.0001). Redistribution is training-dependent.\"}, \"hypothesis\": \"C001 control: Untrained VLA last_preaction action probe. If untrained last_preaction R² < projector (0.706) → redistribution is training-dependent. If ≈ projector → architectural.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis experiment)\", \"completed_at\": \"2026-05-16T00:11:13.235Z\"}, \"plan_009_cka_verification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:43:19.084Z\", \"updated_at\": \"2026-05-16T00:03:29.018Z\", \"hypothesis\": \"Plan 009: CKA verification — replicate RSA findings with CKA metric to ensure conclusions are not metric-dependent. CPU-only, uses existing features. SigLIP+projector CKA should show same dominance pattern as RSA.\", \"spec\": {\"command\": \"python scripts/cka_analysis.py (CPU-only, multiple conditions)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,siglip_only,dino}_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/cka_verification/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:03:19.946Z\", \"metrics\": {\"linear_cka\": {\"untrained_img_mean_L23\": 0.0894, \"trained_img_mean_L23\": 0.0834, \"projector\": 0.0809, \"dino\": 0.0664, \"trained_last_preaction_L32\": 0.127}, \"rdm_cka\": {\"trained_img_mean_L23\": 0.2599, \"projector\": 0.2568, \"untrained_img_mean_L23\": 0.2464, \"dino\": 0.2408, \"trained_last_preaction_L32\": 0.2898}, \"findings\": \"DINO lowest across all metrics (robust). last_preaction >> image_mean (redistribution confirmed). Projector vs trained gap compressed in CKA vs RSA (metric-dependent).\"}}, \"p0_functional_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:21:52.011Z\", \"updated_at\": \"2026-05-15T23:47:31.338Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action prediction probe on SigLIP+projector output features. If projector R² ≥ LLM best layer (0.683) → smoking gun functional validation. If < LLM but > DINO (0.676) → partial. If ≤ DINO → degradation claim needs reeval. Also tests image_mean aggregation from LLM hidden states.\", \"metrics\": {\"projector\": {\"mean_R2\": 0.7063, \"overall_R2\": 0.7169, \"grip_acc\": 0.9221}, \"image_mean_trained_L19\": {\"mean_R2\": 0.6832, \"overall_R2\": 0.6961, \"grip_acc\": 0.9182}, \"image_mean_trained_L23\": {\"mean_R2\": 0.5736, \"overall_R2\": 0.59, \"grip_acc\": 0.8924}, \"llm_last_preaction_L19\": {\"mean_R2\": 0.7309, \"overall_R2\": 0.7397, \"grip_acc\": 0.9184}, \"untrained_image_mean_L0\": {\"mean_R2\": 0.7136, \"overall_R2\": 0.7234, \"grip_acc\": 0.9218}, \"bootstrap_ci_proj_vs_llm_last_preaction\": {\"delta\": -0.0246, \"ci_95\": [-0.04, -0.009], \"p_value\": 0.0014}, \"gate_judgment\": \"PASS — projector 0.706 ≥ 0.683 threshold. But LLM last_preaction (0.731) > projector (0.706), p=0.001.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (probe evaluation)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json\", \"completed_at\": \"2026-05-15T23:43:02.159Z\", \"notes\": \"V1 完成但缺统计检验：(1) 缺 projector vs image_mean_L19 bootstrap CI (主比较 0.706 vs 0.683), (2) 缺 DINO probe, (3) untrained L10/L11 异常需排查。V2 修正版见 p0_functional_probe_v2。\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:44:40.511Z\", \"updated_at\": \"2026-05-15T22:49:25.162Z\", \"hypothesis\": \"P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014 vs untrained RSA=0.4847, Δ=+0.017. Task-level resampling bootstrap 95% CI. If CI excludes 0 → Claim 3 needs minor adjustment (\\\"minimal but detectable\\\"). If CI includes 0 → Claim 3 \\\"invariance\\\" holds.\", \"metrics\": {\"image_mean\": {\"delta\": 0.0206, \"ci_95\": [-0.0314, 0.0638], \"p_value\": 0.2, \"significant\": false}, \"last_preaction\": {\"delta\": 0.0076, \"ci_95\": [-0.0395, 0.0558], \"p_value\": 0.37, \"significant\": false}, \"n_bootstrap\": 10000, \"n_tasks\": 10, \"conclusion\": \"Both CIs include 0. Training effect not significant under task-level bootstrap. Claim 3 invariance holds.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (statistical test)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json\", \"completed_at\": \"2026-05-15T22:49:25.162Z\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:33:21.471Z\", \"updated_at\": \"2026-05-15T22:43:41.904Z\", \"hypothesis\": \"P0 CRITICAL: Verify Claim 2 (LLM degrades action alignment 0.615→0.488) is not an aggregation artifact. SigLIP uses mean pooling, VLA used last_preaction. Re-run RSA with image_mean feature key for trained with-inst and untrained with-inst. If image_mean RSA ≈ 0.61 → Claim 2 is artifact. If ≈ 0.49 → Claim 2 holds.\", \"metrics\": {\"trained_image_mean_rsa\": 0.5014, \"trained_image_mean_peak_layer\": 23, \"trained_last_preaction_rsa\": 0.4876, \"untrained_image_mean_rsa\": 0.4847, \"untrained_image_mean_peak_layer\": 23, \"untrained_last_preaction_rsa\": 0.4846, \"siglip_projector_rsa\": 0.6153, \"gap_siglip_vs_image_mean\": 0.1139, \"verdict\": \"Claim 2 HOLDS — image_mean RSA (0.5014) ≈ last_preaction (0.4876), both far below SigLIP (0.6153). Aggregation artifact hypothesis rejected.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (verification task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json\", \"completed_at\": \"2026-05-15T22:42:57.560Z\", \"notes\": \"额外发现 (SSH worker): image_mean 聚合下 trained-untrained delta = +0.017 (L23)，比 last_preaction 的 +0.003 明显更大。Training 增强了 image token 表征的 action 相关性，但信号在 last_preaction (序列末位 token) 中被稀释。Trained 呈 inverted-U 曲线 (L0=0.45→L23=0.50→L32=0.44)，untrained 近乎平坦 (0.47-0.48)。Layer 0 trained=untrained=0.4509 (LLM 处理前一致)。\"}, \"plan_003_perlayer_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:49.507Z\", \"updated_at\": \"2026-05-15T22:35:08.118Z\", \"hypothesis\": \"D028 plan_003: Per-layer RSA degradation curve. Track RSA from SigLIP+projector output (L0=0.615) through LLM layers 1-32 (~0.48). If monotonic decrease → LLM progressively degrades action alignment. If non-monotonic → some layers partially recover. Supports Claim 2 (LLM degrades action-relevant structure).\", \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"perlayer_summary\": {\"with_inst_trained\": {\"peak_rsa\": 0.4876, \"peak_layer\": 9, \"proj_to_l1_drop\": 0.2036, \"pattern\": \"non_monotonic\"}, \"with_inst_untrained\": {\"peak_rsa\": 0.4846, \"peak_layer\": 12, \"proj_to_l1_drop\": 0.1512, \"pattern\": \"non_monotonic\"}, \"no_inst_trained\": {\"peak_rsa\": 0.489, \"peak_layer\": 30, \"proj_to_l1_drop\": 0.2526, \"pattern\": \"predominantly_increasing\"}, \"no_inst_untrained\": {\"peak_rsa\": 0.4802, \"peak_layer\": 6, \"proj_to_l1_drop\": 0.1374, \"pattern\": \"non_monotonic\"}}, \"total_degradation_range\": [0.126, 0.135], \"key_findings\": [\"Proj→L1 is the biggest RSA drop (0.13-0.25, ~20-40%)\", \"L0 (embedding) is anomaly (RSA≈0 for trained), structure recovers at L1\", \"No-inst trained is unique: predominantly increasing L1→L30\", \"All LLM layers RSA >> DINO (0.388)\", \"Total degradation ~0.13: best LLM layer still 0.13 below projector output\"], \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json\", \"completed_at\": \"2026-05-15T22:35:08.118Z\"}, \"d027_siglip_only_rsa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:10:53.129Z\", \"updated_at\": \"2026-05-15T22:25:27.345Z\", \"hypothesis\": \"D027 Exp-1 (SMOKING GUN): Extract SigLIP+projector output features (LLM input embeddings) from VLA architecture on LIBERO-Goal, run RSA. If SigLIP-only RSA ≈ 0.45-0.50 → confirms vision encoder is the source of action-relevant structure (LLM is passthrough). If RSA ≈ 0.39 (DINO level) → projector/LLM architecture contributes, need reanalysis.\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_siglip_features.py + python /root/vla-ssd/rsa_siglip_only.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/siglip_only_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer (projector output, 4096 dim)\", \"model_name\": \"openvla/openvla-7b SigLIP+projector only (no LLM forward)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_siglip_only.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}, \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"bootstrap_95_ci\": [0.5257, 0.6954], \"comparison\": {\"siglip_projector\": 0.6153, \"trained_with_inst\": 0.4876, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"trained_no_inst\": 0.489, \"dino\": 0.388}, \"llm_degradation\": \"LLM reduces RSA from 0.615 (projector output) to ~0.488 (LLM hidden states)\", \"gate_judgment\": \"PASS — SigLIP+projector RSA=0.6153 >> 0.45-0.50 threshold. Vision encoder is the source of action-relevant structure. LLM is not passthrough but actually degrades action alignment.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:25:27.345Z\"}, \"lg_shuffled_token_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:27:18.397Z\", \"updated_at\": \"2026-05-15T19:48:27.481Z\", \"hypothesis\": \"Control: token-shuffled goal classification on trained VLA features. Shuffling token order destroys positional/sequential info. NOTE: uses bare task name prompt (not formatted prompt like main pipeline) — results not directly comparable.\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --shuffle_tokens\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (token-shuffled)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features with shuffled tokens\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Control: uses bare task name prompt (NOT formatted prompt). Results not directly comparable to main pipeline. Worker: worker_ssh_shuffled-tokens-control\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_shuffled_token_control.log\"}, \"conclusion\": \"killed\", \"notes\": \"实验从未实际启动：GPU 0%，输出目录不存在。Worker 可能在 Agent OOM kill 前未完成提交。加之 prompt format 不一致（bare task name vs formatted prompt），参考价值有限。标记 CANCELLED per D019 Reviewer 审查。\", \"completed_at\": \"2026-05-15T19:48:27.481Z\"}, \"lg_dino_extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:42:52.995Z\", \"updated_at\": \"2026-05-15T17:56:18.045Z\", \"hypothesis\": \"DINO-V2 LIBERO-Goal feature extraction — vision-only baseline for Goal Classification gate (Sanity-GC: DINO acc ≤ 25%)\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:43:09.957Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\\\"\", \"finished_at\": \"2026-05-15T17:49:37.592Z\", \"training_hours\": 0.11}, \"spec\": {\"command\": \"python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"log_path\": \"~/runs/vla-ssd/lg_dino_extract.log\"}, \"pid\": \"634279\", \"log_path\": \"~/runs/vla-ssd/lg_dino_extract.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:49:38.728557+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"tasks_completed\": 10, \"tasks_total\": 10, \"demos_per_task\": 50, \"total_frames\": 63728, \"feature_dim\": 1024, \"dtype\": \"float16\", \"feature_keys\": [\"cls_token\", \"patch_mean\"], \"file_count\": 10, \"total_size_mb\": 234, \"extraction_fps\": 183, \"extraction_time_s\": 347.3}, \"completed_at\": \"2026-05-15T17:53:27.460Z\"}, \"mvp2_action_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:10:18.939Z\", \"updated_at\": \"2026-05-15T17:30:12.186Z\", \"hypothesis\": \"VLA trained model hidden states encode action prediction knowledge (next action a_{t+1}) that untrained VLA and DINO-V2 lack. Gates: G1 R²>0.3, G2 Δ(trained-untrained)>0.15, G3 Δ(trained-DINO)>0.15\", \"parent\": \"mvp_001\", \"metrics\": {\"copy_baseline_R2\": 0.975, \"copy_baseline_per_task_mean_R2\": 0.972, \"random_frame_baseline_R2\": -0.91, \"random_frame_per_task_mean_R2\": -0.977, \"copy_baseline_per_dim_R2\": {\"dx\": 0.979, \"dy\": 0.988, \"dz\": 0.982, \"drx\": 0.971, \"dry\": 0.966, \"drz\": 0.991, \"grip\": 0.949}, \"note\": \"LIBERO action autocorrelation very high — copy a_t predicts a_{t+1} at R²=0.975. Action probe R² must be interpreted relative to this ceiling. Key comparison remains trained-vs-untrained Δ, not absolute R².\"}, \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - parent experiment, superseded by LIBERO-Goal pivot (D015)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"notes\": \"Superseded by LIBERO-Goal pivot (D015). Sub-experiments (mvp2_action_trained/untrained/dino, mvp2_delta_trained/untrained/dino) all completed as DONE. Parent umbrella experiment killed per Director instruction.\", \"completed_at\": \"2026-05-15T17:30:12.186Z\"}, \"lg_extract_untrained_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:23.059Z\", \"updated_at\": \"2026-05-15T17:11:52.014Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA. Fixed local_files_only=True. Continues from 2/10 tasks (skip existing).\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_untrained after local_files_only fix. Script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1.\", \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:43.781Z\", \"notes\": \"Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.\"}, \"lg_extract_trained_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:18.970Z\", \"updated_at\": \"2026-05-15T17:11:51.155Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. Fixed local_files_only=True. Continues from 3/10 tasks (skip existing).\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_trained after local_files_only fix. Script skips completed .h5 files.\", \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:42.929Z\", \"notes\": \"Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.\"}, \"lg_extract_untrained_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:27.492Z\", \"updated_at\": \"2026-05-15T17:11:50.295Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA (random LLM + preserved SigLIP). Baseline for instruction probing.\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_untrained after network failure, script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"pid\": 627335, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:42.431Z\", \"notes\": \"Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.\"}, \"lg_extract_trained_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:23.268Z\", \"updated_at\": \"2026-05-15T17:11:49.214Z\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. OOD test. Fix: local_files_only=True, skip logic resumes from completed tasks.\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_trained after network failure\"}, \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"pid\": 627256, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:11:41.473Z\", \"notes\": \"Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.\"}, \"mvp2_delta_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:23:29.771Z\", \"updated_at\": \"2026-05-15T16:00:24.789Z\", \"hypothesis\": \"DINO-V2 action-delta baseline (single layer) — establishes vision-only floor for G3 action-delta comparison\", \"parent\": \"mvp2_action_probe\", \"metrics\": {\"overall_R2\": 0.0604, \"per_task_mean_R2\": 0.0609, \"gripper_accuracy\": 0.57, \"per_dim_R2\": {\"dx\": 0.1744, \"dy\": 0.2588, \"dz\": 0.3745, \"drx\": 0.084, \"dry\": 0.0563, \"drz\": 0.1765, \"gripper\": 0.0365}, \"num_layers\": 1, \"feature_dim\": 1024}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_delta --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\"}, \"completed_at\": \"2026-05-15T16:00:24.789Z\"}, \"mvp2_delta_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:42:59.680Z\", \"updated_at\": \"2026-05-15T15:23:24.627Z\", \"hypothesis\": \"Action-delta prediction (Δa = a_{t+1}-a_t) on untrained VLA. Baseline for G2-delta comparison — expected lower R² than trained\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"617923\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_untrained.log\", \"submitted_at\": \"2026-05-15T14:43:14.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + actions from libero_10\", \"wall_clock_seconds\": 2409.9, \"gpu_hours\": 0.67}, \"metrics\": {\"best_layer\": 32, \"per_task_mean_R2\": 0.0485, \"overall_R2\": 0.0485, \"per_dim_R2_at_best\": {\"note\": \"L32 only layer with signal; L5-L28 all ≈ 0\"}, \"layer_stability\": \"catastrophic — layers 5-28 all R²≈0, only L1-L4 and L32 have signal\", \"collapsed_layers\": \"5,6,7,8,9,10,11,12,13,14,15,17,18,26,28\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/action_delta/\", \"completed_at\": \"2026-05-15T15:23:24.627Z\"}, \"mvp2_delta_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:42:58.840Z\", \"updated_at\": \"2026-05-15T15:23:24.190Z\", \"hypothesis\": \"Action-delta prediction (Δa = a_{t+1}-a_t) removes autocorrelation. 33-layer sweep on trained VLA. Gate G1-delta: peak R²>0.05, G2-delta: Δ(trained-untrained)>0.03 in ≥5/10 tasks\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"617841\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_trained.log\", \"submitted_at\": \"2026-05-15T14:43:13.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ + actions from libero_10\", \"wall_clock_seconds\": 2410.9, \"gpu_hours\": 0.67}, \"metrics\": {\"best_layer\": 14, \"per_task_mean_R2\": 0.0594, \"overall_R2\": 0.0594, \"per_dim_R2_at_best\": {\"dx\": 0.1783, \"dy\": 0.2665, \"dz\": 0.3576, \"drx\": 0.0942, \"dry\": 0.0511, \"drz\": 0.1735, \"gripper\": 0.0357}, \"layer_stability\": \"stable plateau 0.04-0.06 across layers 5-30, smooth curve\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/action_delta/\", \"completed_at\": \"2026-05-15T15:23:24.190Z\"}, \"mvp2_action_dino\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:22:11.911Z\", \"updated_at\": \"2026-05-15T15:19:25.002Z\", \"hypothesis\": \"DINO-V2 ViT-L/14 action prediction baseline (single cls_token layer) — establishes vision-only floor for Gate G3 comparison\", \"parent\": \"mvp2_action_probe\", \"conclusion\": \"success\", \"metrics\": {\"overall_R2\": 0.6689, \"per_task_mean_R2\": 0.6759, \"gripper_accuracy\": 0.9001, \"epochs\": 17, \"training_time_seconds\": 7.3, \"num_layers\": 1, \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"probe_type\": \"MLP action probe (1024->256->7)\"}, \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (10 tasks H5) + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\"}, \"completed_at\": \"2026-05-15T14:22:47.835Z\"}, \"mvp2_action_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:44.922Z\", \"updated_at\": \"2026-05-15T14:46:17.287Z\", \"hypothesis\": \"Untrained VLA (random LLM + preserved vision) 33-layer action prediction baseline — expected lower R² than trained, establishing Δ for Gate G2\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"613477\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_untrained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), untrained openvla features\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}, \"metrics\": {\"best_layer\": 32, \"per_task_mean_R2\": 0.6164, \"overall_R2\": 0.6067, \"gripper_accuracy\": 0.8726, \"per_dim_R2_at_best\": {\"dx\": 0.5345, \"dy\": 0.7067, \"dz\": 0.5102, \"drx\": 0.3658, \"dry\": 0.2037, \"drz\": 0.6361, \"gripper\": 0.6066}, \"layers_unstable_range\": \"0.05-0.62 (many layers R²<0.25, probe likely not converging)\", \"layer_stability\": \"very low — wildly oscillating, multiple collapsed layers\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/action_prediction/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:46:17.287Z\"}, \"mvp2_action_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:17:43.720Z\", \"updated_at\": \"2026-05-15T14:46:16.968Z\", \"hypothesis\": \"VLA trained model 33-layer action prediction sweep: per-layer R² distribution reveals where action knowledge is encoded. Gate G1: R²>0.3, G2: Δ(trained-untrained)>0.15\", \"parent\": \"mvp2_action_probe\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"613335\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_trained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), trained on openvla-7b features\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}, \"metrics\": {\"best_layer\": 19, \"per_task_mean_R2\": 0.6831, \"overall_R2\": 0.677, \"gripper_accuracy\": 0.8989, \"per_dim_R2_at_best\": {\"dx\": 0.5885, \"dy\": 0.7629, \"dz\": 0.5854, \"drx\": 0.3712, \"dry\": 0.1649, \"drz\": 0.6654, \"gripper\": 0.6815}, \"layers_stable_range\": \"0.45-0.68 (31/33 layers > untrained)\", \"layer_stability\": \"high — smooth R² curve across all 33 layers\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/action_prediction/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:46:16.968Z\"}, \"mvp_controlb_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:13:48.663Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-untrained\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\"}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mean_rho_across_layers\": 0.0003, \"mean_task_rho_across_layers\": 0.0003, \"best_layer_rho\": 0.0085, \"best_layer\": 1, \"mean_R2\": -0.0092, \"mean_MAE\": 0.2482, \"rho_std\": 0.0034, \"constant_prediction_layers\": 21, \"normal_experiment_rho\": 0.933, \"rho_ratio_normal_vs_shuffled\": 3110}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.504Z\"}, \"mvp_controlb_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:13:46.328Z\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-trained\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\"}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mean_rho_across_layers\": 0.0012, \"mean_task_rho_across_layers\": 0.0011, \"best_layer_rho\": 0.0123, \"best_layer\": 8, \"mean_R2\": -0.0041, \"mean_MAE\": 0.2478, \"rho_std\": 0.0051, \"all_layers_abs_rho_below_0.013\": true, \"normal_experiment_rho\": 0.955, \"rho_ratio_normal_vs_shuffled\": 783}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.105Z\"}, \"mvp_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:55:16.912Z\", \"updated_at\": \"2026-05-15T14:01:25.245Z\", \"hypothesis\": \"OpenVLA 7B 隐状态编码了 task-progress 信息（temporal distance），且信号来自 task-semantic content 而非 positional shortcut (RoPE)\", \"spec\": {\"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"model_name\": \"openvla/openvla-7b\", \"model_version\": \"HuggingFace main\", \"seed\": 42, \"gpu\": \"2xRTX PRO 6000\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"feature_path\": \"/root/vla-ssd/features/ (symlink to data disk)\", \"controls\": [\"Control A: timestep fraction oracle\", \"Control B: cross-trajectory shuffle\", \"Control C: untrained model baseline\", \"Control D: DINO-V2 ViT-L/14\"], \"pass_criteria\": \"best_layer rho>0.3 AND delta_rho(trained-untrained)>0.1 AND (VLA>=DINO-V2 OR subtask_AUC>0.7)\", \"command\": \"python scripts/extract_features.py (trained cuda:0 + untrained cuda:1)\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = ~125K frames\", \"phase\": \"Phase 2 feature extraction\", \"tmux_sessions\": [\"openvla-trained-extract\", \"openvla-untrained-extract\"]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T14:01:16.724Z\", \"metrics\": {\"overall_verdict\": \"FAIL\", \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"delta_rho_at_best\": 0.0427, \"dino_per_task_mean_rho\": 0.9008, \"collapsed_layers\": 16, \"healthy_layers\": 17, \"subtask_predicate_pivot_viable\": false, \"subtask_predicate_reason\": \"all LIBERO predicates visually observable, DINO AUC=0.9717\"}}, \"mvp_probe_untrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:24:31.814Z\", \"updated_at\": \"2026-05-15T13:55:20.999Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"606129\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_untrained.log\", \"submitted_at\": \"2026-05-15T13:24:31.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1638.6, \"gpu_hours\": 0.46}, \"hypothesis\": \"Control C: untrained OpenVLA (random LLM + preserved vision) temporal distance probe as baseline for Δρ comparison\", \"parent\": \"mvp_001\", \"reproduce\": {\"finished_at\": \"2026-05-15T13:46:43.876Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:46:45.174989+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.9334, \"note\": \"Control C baseline — untrained model (random LLM + preserved SigLIP vision encoder) already achieves ρ=0.933, confirming temporal distance signal is vision-dominated\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/\", \"completed_at\": \"2026-05-15T13:51:50.407Z\"}, \"mvp_probe_trained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:24:31.011Z\", \"updated_at\": \"2026-05-15T13:55:11.968Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"606050\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_trained.log\", \"submitted_at\": \"2026-05-15T13:24:30.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1634.3, \"gpu_hours\": 0.45}, \"hypothesis\": \"OpenVLA 7B trained model hidden states encode temporal distance (per-task mean ρ > 0.5), with signal from VLA training (Δρ vs untrained > 0.1)\", \"parent\": \"mvp_001\", \"reproduce\": {\"finished_at\": \"2026-05-15T13:46:42.038Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:46:42.772416+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained/temporal_distance/\", \"metrics\": {\"best_layer\": 4, \"best_per_task_mean_rho\": 0.955, \"best_pooled_rho\": 0.9556, \"delta_rho_at_best\": 0.0427, \"delta_rho_ci_95\": [0.0359, 0.0502], \"delta_rho_perm_p\": 0, \"gate1_rho_pass\": true, \"gate2_delta_pass\": false, \"gate3_dino_pass\": true, \"overall_verdict\": \"FAIL\", \"collapsed_layers\": 16, \"healthy_layers\": 17, \"dino_threshold\": 0.901, \"dino_per_task_mean_rho\": 0.9008}, \"completed_at\": \"2026-05-15T13:51:45.260Z\"}}, \"count\": 90, \"total\": 90, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3003}}"
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
The paper files are in `docs/paper/`. The registry output is too large - saved to a file. Let me now:

1. Read all the paper .tex files (in `docs/paper/`)
2. Extract metrics from the registry using jq

Let me parallelize: spawn agents for the different parts of this task.

Actually, let me think about the best approach. This is a complex multi-step task. Let me:

1. Read all paper tex files
2. Extract registry metrics
3. Do the checks

Given the complexity, I'll use multiple agents:
- Agent 1: Read all paper tex files and extract numerical values, check wording issues, check cross-references


- Agent 2: Extract registry metrics from the JSON file
- Agent 3: Try to compile the paper

Actually, let me be more strategic. The paper files are in `docs/paper/` and there are 9 tex files. I'll read them all and process the registry in parallel using agents for the heavy lifting. I'll have one agent handle numerical consistency by cross-validating the tex files against the registry, another check wording consistency across the tex files, and a third attempt compilation on the remote server, then synthesize the results.

The registry file is at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt` and the paper files are in `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/` including main.tex, related_work.tex, method.tex, abstract.tex, conclusion.tex, and experiments.

tex along with appendix.tex, discussion.tex, and introduction.tex. I also need to locate the bibliography files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c89459e5-ba37-44ea-ac2b-848b59634ef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xfs5hmtWZdDLtgjfuGc4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1259,
      "cache_read_input_tokens": 26194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1259
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

论文在 `docs/paper/`。Registry 数据量大，已存到文件。先找 bib 文件，然后并行启动多个 agent 检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "02136783-92d9-4561-a5bb-64cf63d75ad2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xfs5hmtWZdDLtgjfuGc4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1259,
      "cache_read_input_tokens": 26194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1259
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

<details open><summary>🔧 Tool call — Glob · `toolu_01DsGUgpuLzF67r3xkz9G5iC`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "65e71087-c551-4136-985d-1d14508057a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xfs5hmtWZdDLtgjfuGc4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1259,
      "cache_read_input_tokens": 26194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1259
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

_source line 21 · 2026-05-18T19:27:52.760Z_

<details><summary>↩ Tool result · `toolu_01DsGUgpuLzF67r3xkz9G5iC`</summary>

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
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7a902a3e-c4b0-4b1a-9b8c-9909fbf36885",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the locations. Let me launch 4 parallel agents:

1. Numerical consistency - read tex files and registry, cross-validate all numbers
2. Wording consistency - search for problematic patterns in tex files
3. Cross-reference check - check \ref/\label/\cite completeness
4. Compilation - try to compile on remote server

The paper dir is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/


I've got the registry file path now, so I'm ready to start all 4 agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5037d9ef-9f35-47c6-b914-d482eb8df9cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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

_source line 23_

找到了所有文件。启动 4 个并行 agent 分别检查数值、措辞、交叉引用和编译。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3ba08448-5cbf-44b8-9569-221f6d66389f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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

_source line 24_

<details open><summary>🔧 Tool call — Agent · `toolu_01UCXM3HddsVF29jR77cHjoQ`</summary>

````json
{
  "description": "Numerical consistency check",
  "prompt": "You are checking numerical consistency between a paper's .tex files and an experiment registry.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Registry data location\nThe registry JSON is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed. Use jq or python to probe and extract.\n\n## Task\n1. Read ALL .tex files and extract every quantitative number: Cohen's d values, R² values, MSE, p-values, percentages, ratios, counts, etc. Note the file and line number for each.\n\n2. Extract relevant metrics from the registry. Use bash with jq or python to parse the registry file. The key metrics to find:\n   - Cohen's d: L1 instruction 24h ablation = 0.651, control 8h = 0.41\n   - Dose-response: d=0.482(top4) → 0.639(top32)\n   - Counterfactual: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n   - Attention decomposition: instruction-dominant 62.4% vs control 44.9%\n   - Per-dim MAE ratios: translation 3-5x, rotation 1.9-2.6x\n   - Per-task R²: L1 10/10 positive, L8 8/10, L13 5/10\n   - Per-head bootstrap: instruction d=0.027, control d=0.051, p=0.0018\n   - CV permutation: p=0.016\n   - Random subset ablation: dominant Δ=0.042, random mean Δ=0.077, z=-2.73, p=0.003\n   - Specificity control: bottom-24 d=0.565 vs top-24 d=0.65 (ratio 1.15)\n   - Trained probe peak: L9 R²=0.643, untrained peak L1 R²=0.547\n   - Linear probe: trained peak L13 R²=0.596, untrained peak L1 R²=0.492\n\n3. Cross-validate: for each number in the paper, check if it matches the registry. Report mismatches.\n\n## Output format\nReturn a markdown table:\n```\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n```\nStatus should be: ✅ 匹配, ❌ 不匹配, ⚠️ 未找到registry记录\n\nAlso return a summary count of matches, mismatches, and unverified numbers."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c2cb27c3-c2dc-402f-9a0b-368c52cf7219",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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


### System

_source line 25_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Numerical consistency check",
  "task_type": "local_agent",
  "prompt": "You are checking numerical consistency between a paper's .tex files and an experiment registry.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Registry data location\nThe registry JSON is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed. Use jq or python to probe and extract.\n\n## Task\n1. Read ALL .tex files and extract every quantitative number: Cohen's d values, R² values, MSE, p-values, percentages, ratios, counts, etc. Note the file and line number for each.\n\n2. Extract relevant metrics from the registry. Use bash with jq or python to parse the registry file. The key metrics to find:\n   - Cohen's d: L1 instruction 24h ablation = 0.651, control 8h = 0.41\n   - Dose-response: d=0.482(top4) → 0.639(top32)\n   - Counterfactual: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n   - Attention decomposition: instruction-dominant 62.4% vs control 44.9%\n   - Per-dim MAE ratios: translation 3-5x, rotation 1.9-2.6x\n   - Per-task R²: L1 10/10 positive, L8 8/10, L13 5/10\n   - Per-head bootstrap: instruction d=0.027, control d=0.051, p=0.0018\n   - CV permutation: p=0.016\n   - Random subset ablation: dominant Δ=0.042, random mean Δ=0.077, z=-2.73, p=0.003\n   - Specificity control: bottom-24 d=0.565 vs top-24 d=0.65 (ratio 1.15)\n   - Trained probe peak: L9 R²=0.643, untrained peak L1 R²=0.547\n   - Linear probe: trained peak L13 R²=0.596, untrained peak L1 R²=0.492\n\n3. Cross-validate: for each number in the paper, check if it matches the registry. Report mismatches.\n\n## Output format\nReturn a markdown table:\n```\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n```\nStatus should be: ✅ 匹配, ❌ 不匹配, ⚠️ 未找到registry记录\n\nAlso return a summary count of matches, mismatches, and unverified numbers.",
  "uuid": "c25c43e6-d53e-4b77-aba6-f02bca5141a6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
````

---


## Round 1

## Round 1

33 recorded events


### User

_source line 26 · 2026-05-18T19:28:11.472Z_

You are checking numerical consistency between a paper's .tex files and an experiment registry.

## Paper files location
All .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
Files: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex

## Registry data location
The registry JSON is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt

The file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed. Use jq or python to probe and extract.

## Task
1. Read ALL .tex files and extract every quantitative number: Cohen's d values, R² values, MSE, p-values, percentages, ratios, counts, etc. Note the file and line number for each.

2. Extract relevant metrics from the registry. Use bash with jq or python to parse the registry file. The key metrics to find:
   - Cohen's d: L1 instruction 24h ablation = 0.651, control 8h = 0.41
   - Dose-response: d=0.482(top4) → 0.639(top32)
   - Counterfactual: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625
   - Attention decomposition: instruction-dominant 62.4% vs control 44.9%
   - Per-dim MAE ratios: translation 3-5x, rotation 1.9-2.6x
   - Per-task R²: L1 10/10 positive, L8 8/10, L13 5/10
   - Per-head bootstrap: instruction d=0.027, control d=0.051, p=0.0018
   - CV permutation: p=0.016
   - Random subset ablation: dominant Δ=0.042, random mean Δ=0.077, z=-2.73, p=0.003
   - Specificity control: bottom-24 d=0.565 vs top-24 d=0.65 (ratio 1.15)
   - Trained probe peak: L9 R²=0.643, untrained peak L1 R²=0.547
   - Linear probe: trained peak L13 R²=0.596, untrained peak L1 R²=0.492

3. Cross-validate: for each number in the paper, check if it matches the registry. Report mismatches.

## Output format
Return a markdown table:
```
| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |
|---|---|---|---|
```
Status should be: ✅ 匹配, ❌ 不匹配, ⚠️ 未找到registry记录

Also return a summary count of matches, mismatches, and unverified numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "6d00f835-8696-451a-b532-d0a164e7fc4a"
}
```

</details>

---


### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 16148,
    "tool_uses": 1,
    "duration_ms": 3978
  },
  "last_tool_name": "Read",
  "uuid": "401bc661-377a-4c2f-81a2-3096a7125255",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 16150,
    "tool_uses": 2,
    "duration_ms": 4339
  },
  "last_tool_name": "Read",
  "uuid": "6827283a-bf13-4112-9523-7a4ff2f487b4",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 16152,
    "tool_uses": 3,
    "duration_ms": 4907
  },
  "last_tool_name": "Read",
  "uuid": "92a75aa4-2f72-4107-9343-357016a3cae7",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 16154,
    "tool_uses": 4,
    "duration_ms": 5250
  },
  "last_tool_name": "Read",
  "uuid": "e9867607-a76e-4890-924d-d26dd9f7e757",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 16156,
    "tool_uses": 5,
    "duration_ms": 5688
  },
  "last_tool_name": "Read",
  "uuid": "18c7c0b3-8a82-42e2-859a-b46c22bfa2ff",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 16158,
    "tool_uses": 6,
    "duration_ms": 6392
  },
  "last_tool_name": "Read",
  "uuid": "3bafa2d2-4cda-47ef-ad6e-1bf93e14b12a",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 16160,
    "tool_uses": 7,
    "duration_ms": 6904
  },
  "last_tool_name": "Read",
  "uuid": "63dbc41e-4660-4f40-a345-87fe88a68957",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 16162,
    "tool_uses": 8,
    "duration_ms": 7503
  },
  "last_tool_name": "Read",
  "uuid": "040d768d-55f0-41b3-a044-87e6f0542cfb",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 16164,
    "tool_uses": 9,
    "duration_ms": 8050
  },
  "last_tool_name": "Read",
  "uuid": "ed39d6c6-4e2c-4700-930f-7facd844cf1b",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Running Parse registry JSON file",
  "usage": {
    "total_tokens": 16166,
    "tool_uses": 10,
    "duration_ms": 10315
  },
  "last_tool_name": "Bash",
  "uuid": "511f6d54-89df-4df8-8df4-a76f3c7ca1fc",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01CfubEZ1qPiySSdepPqHfXM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3fd76e2e-f411-4c3f-99be-138092a27588",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-18T19:28:15.468Z_

<details><summary>↩ Tool result · `toolu_01CfubEZ1qPiySSdepPqHfXM`</summary>

```text
1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "2aadd977-b335-46e6-8257-13ec3812c115"
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01SCqotSdfohJztHTDmijPZi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "04a9ac58-72e8-4d9b-b8fc-55c052630e4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 40 · 2026-05-18T19:28:15.818Z_

<details><summary>↩ Tool result · `toolu_01SCqotSdfohJztHTDmijPZi`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\cite{alain2017} for functional decodability.
15	
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, our framework validates architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions) due to the causal mask and frozen encoder, while the readout token maintains perfect instruction identity ($100\%$, cross-validated) from L1 onward.
18	\emph{Second}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
19	Convergent causal evidence, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
20	\emph{Third}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
21	Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
22	
23	Our contributions are: (i)~a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, validating architecture-expected specialization as a sanity check; (ii)~convergent causal evidence, from seven independent analyses on OpenVLA-7B/LIBERO, that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub; and (iii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes confirm; CKA diverges), with training primarily enhancing readout-token integration rather than visual geometry.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "13817329-a9fc-4f8b-9cb2-5aef156352bc"
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01Jtm1rMHoBJ7JCqYgzxYKaY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1c166a75-f67f-41c3-b30d-19d69863acbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-18T19:28:16.388Z_

<details><summary>↩ Tool result · `toolu_01Jtm1rMHoBJ7JCqYgzxYKaY`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
17	
18	\paragraph{Behavioral and mechanistic analysis of VLAs.}
19	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
20	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
21	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
22	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
23	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
24	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
25	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
26	
27	\paragraph{Token-level functional specialization in transformers.}
28	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
29	We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
30	
31	\paragraph{Representation similarity and probing methodology.}
32	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
33	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
34	We adopt RSA and MLP probes, with CKA in the appendix.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "dd29e9cc-c78d-4727-b7af-88533ce068c2"
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_013rus1BfRbYuEXkujvMu51X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e8fe668b-6ab1-4f32-8746-9aaefd5bc46b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-18T19:28:16.729Z_

<details><summary>↩ Tool result · `toolu_013rus1BfRbYuEXkujvMu51X`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
25	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.
26	Throughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.
27	We cross two factors: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description) in a $2\times 2$ factorial design.
28	
29	%------------------------------------------------------------------
30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to confirm that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}
40	
41	We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42	This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43	
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) confirms neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "efcb673a-ca67-4092-b309-cf577cc1484f"
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01RWPcbwUjjHxkMV4pQyhy4Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "755d3937-b6c8-45ee-a087-7827c1a69bb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 46 · 2026-05-18T19:28:17.171Z_

<details><summary>↩ Tool result · `toolu_01RWPcbwUjjHxkMV4pQyhy4Z`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confirm this, as does standalone DINOv2 ($10\%$; Appendix~\ref{sec:instruction_invariance_appendix}).
23	
24	\paragraph{Readout token as multimodal hub.}
25	Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
26	The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
27	
28	\begin{table}[t]
29	\centering
30	\caption{Cross-instruction 10-way classification (full in Appendix~\ref{sec:dense_routing}). Image\_mean: chance; readout: $100\%$ from L1 (trained) or decays.}
31	\label{tab:dense_routing_main}
32	\small
33	\begin{tabular}{lccc}
34	\toprule
35	Layer & Trained readout & Untrained readout & Image\_mean \\
36	\midrule
37	L0 & 10.0\% & 10.0\% & 10.0\% \\
38	L1 & 100.0\% & 100.0\% & 10.0\% \\
39	L4 & 100.0\% & 99.1\% & 10.0\% \\
40	L8 & 100.0\% & 95.5\% & 10.0\% \\
41	L16 & 100.0\% & 91.1\% & 10.0\% \\
42	L31 & 100.0\% & 82.0\% & 10.0\% \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	%------------------------------------------------------------------
48	\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}
49	\label{sec:learned_routing}
50	
51	\paragraph{Three-level routing gradient at L1.}
52	L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
53	
54	\paragraph{Redistribution of routing across depth.}
55	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
56	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
57	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\%--70\%; Appendix~\ref{sec:threshold_sensitivity}).
58	
59	\paragraph{Probe robustness confirms the pattern.}
60	Cross-instruction probes (Appendix Figure~\ref{fig:probe_conditions_appendix}) corroborate: VLA-trained achieves $99.6\%$ at L1; Llama-2 base starts at $80.2\%$, saturating by L5; untrained decays from $100\%$ to $82\%$ (L31).
61	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
62	
63	\paragraph{Ablation confirms routing function.}
64	We ablate attention to instruction tokens at the readout position.
65	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
66	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
67	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
68	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
69	
70	\paragraph{Action trajectory validation.}
71	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
72	
73	\paragraph{Dose-response gradient.}
74	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
75	
76	\paragraph{Counterfactual instruction analysis.}
77	To test instruction dependence, we replace the original instruction with four perturbation types.
78	All conditions produce substantial trajectory divergence: empty ($d = 0.968$), wrong task ($d = 0.844$), paraphrased ($d = 0.697$), and shuffled word order ($d = 0.625$; Table~\ref{tab:counterfactual}).
79	The ordering follows semantic distance from the original instruction.
80	L1 ablation ($d = 0.65$) falls between shuffled and paraphrased, consistent with removal of instruction signal rather than injection of noise (Appendix~\ref{sec:action_trajectory}).
81	
82	\begin{table}[t]
83	\centering
84	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
85	\label{tab:routing_gradient}
86	\small
87	\begin{tabular}{lccccc}
88	\toprule
89	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
90	\midrule
91	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
92	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
93	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
101	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
102	\label{fig:attention_profile}
103	\end{figure}
104	
105	%------------------------------------------------------------------
106	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
107	\label{sec:nonmonotonic}
108	
109	\paragraph{Vision encoder provides geometric foundation.}
110	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
111	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
112	
113	\paragraph{Middle-layer peak (metric-dependent).}
114	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
115	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
116	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
117	
118	\paragraph{Training enhances decodability, not geometry.}
119	Best-vs-best RSA gain is non-significant ($\Delta\rho = 0.017$, $3\%$; Appendix Table~\ref{tab:training_effects}); training reshapes \emph{where} geometry peaks rather than \emph{how high}.
120	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
121	The pattern replicates on LIBERO-Spatial ($p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
122	
123	\begin{table}[t]
124	\centering
125	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
126	\label{tab:rsa_overview}
127	\small
128	\begin{tabular}{lcccc}
129	\toprule
130	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
131	\midrule
132	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
133	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
134	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
135	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
136	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
137	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
138	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
139	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
140	\bottomrule
141	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
142	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
143	\end{tabular}
144	\end{table}
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
149	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
150	\label{fig:layer_curves}
151	\end{figure}
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c3534f92-56bc-41e8-9c01-0b84d224dd8e"
}
```

</details>

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01Lp3S1kYRA6RudBMMskweGA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b987c004-7cb9-4389-80c2-28dcc56923d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-18T19:28:17.871Z_

<details><summary>↩ Tool result · `toolu_01Lp3S1kYRA6RudBMMskweGA`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraphrased $>$ shuffled) follows semantic distance, with L1 ablation falling between shuffled and paraphrased, consistent with signal removal rather than noise injection.
20	The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
21	$R^2$ captures linear decodability; action output reflects the full nonlinear pass. The two are complementary.
22	
23	\paragraph{Predictions.}
24	Other decoder-only VLAs (e.g., RT-2) should show similar entry-layer routing given the shared causal-mask constraint; cross-attention architectures (e.g., $\pi_0$) should differ.
25	L1 ablation should produce measurable task degradation on instruction-discriminative tasks.
26	
27	\paragraph{Limitations and scope.}
28	We study OpenVLA-7B on LIBERO; C1 follows from shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0}, but C2 may differ across backbone scales and decoder paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
29	Our analyses are representational and open-loop; closed-loop evaluation is future work.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "67c3e79e-eec7-44a6-8af6-ce30617437c3"
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01YJ554GZrtayaABp4oaZgjF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "266452a6-3e9b-4c43-84fe-5b0bbdbeac04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-18T19:28:18.386Z_

<details><summary>↩ Tool result · `toolu_01YJ554GZrtayaABp4oaZgjF`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1a9de547-9339-4e80-a15e-4d36f9e58b10"
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01SSXYTWQ9TBCkfwa6TJpiJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "9fec2dba-7d53-44fd-a40f-38847783abd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-18T19:28:19.242Z_

<details><summary>↩ Tool result · `toolu_01SSXYTWQ9TBCkfwa6TJpiJ5`</summary>

```text
1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures rank-order geometric alignment; CKA captures global linear structure.
27	The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
32	\caption{Three similarity metrics across representation sources. \textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}
33	\label{fig:metric_comparison}
34	\end{figure}
35	
36	\subsection{Branch-Split Detailed Analysis}
37	\label{sec:branch_split_appendix}
38	
39	To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.
40	The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
41	Fusion produces a representation ($\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.
42	The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\rho = 0.615$, a drop of $\Delta = 0.019$ from the fused 2{,}176-D input.
43	
44	\subsection{RSA Across Representation Sources}
45	\label{sec:rsa_bar_appendix}
46	
47	Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
48	
49	\begin{figure}[h]
50	\centering
51	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
52	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 \texttt{cls\_token} ($\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\% bootstrap CIs.}
53	\label{fig:rsa_bar}
54	\end{figure}
55	
56	\subsection{Per-Layer RSA Profiles}
57	\label{sec:rsa_perlayer_appendix}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}
62	\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
63	\label{fig:rsa_perlayer_curve}
64	\end{figure}
65	
66	\subsection{Per-Layer Action Decoding Across Training Stages}
67	\label{sec:action_r2_threecond}
68	
69	Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
70	All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
71	The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
72	Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
73	The untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability confirms that randomly initialized Transformer layers produce destructive interference on action-relevant structure.
74	The three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.
75	The qualitative pattern is consistent across all 3 seeds.
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_action_r2_threecond.pdf}
80	\caption{Per-layer action probe $R^2$ (image\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\pm$ std).}
81	\label{fig:action_r2_threecond}
82	\end{figure}
83	
84	\subsection{Random-Subset Ablation Details}
85	\label{sec:random_subset_ablation}
86	
87	To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
88	Dominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \pm 0.013$.
89	The dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); instruction-dominant heads are thus specialized for routing rather than general-purpose computation.
90	
91	\begin{figure}[h]
92	\centering
93	\includegraphics[width=0.75\columnwidth]{figures/fig_random_subset_ablation.pdf}
94	\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with routing-first specialization of instruction-dominant heads.}
95	\label{fig:random_subset_ablation}
96	\end{figure}
97	
98	\subsection{Action Trajectory Analysis Details}
99	\label{sec:action_trajectory}
100	
101	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
102	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
103	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
104	
105	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
106	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
107	
108	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
109	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.
110	The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
111	
112	\begin{table}[h]
113	\centering
114	\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
115	\label{tab:perhead_bootstrap}
116	\small
117	\begin{tabular}{lccc}
118	\toprule
119	Group & $N$ heads & Collective $d$ & Per-head $d$ [95\% CI] \\
120	\midrule
121	Instruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\
122	Control & 8 & 0.41 & 0.051 [0.048, 0.055] \\
123	\midrule
124	Difference & --- & --- & 0.024, $p = 0.0018$ \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
130	
131	Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
132	Trajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\Delta d / \Delta 4 \approx 0.026$), a plateau at 16--20 heads ($\Delta d = 0.001$), and slow increase at 20--32.
133	
134	\begin{figure}[h]
135	\centering
136	\includegraphics[width=0.75\columnwidth]{figures/fig_dose_response.pdf}
137	\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}
138	\label{fig:dose_response}
139	\end{figure}
140	
141	\begin{table}[h]
142	\centering
143	\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\ original action sequence; 95\% bootstrap CIs ($10{,}000$ resamples).}
144	\label{tab:dose_response}
145	\small
146	\begin{tabular}{rcc}
147	\toprule
148	Heads ablated & Cohen's $d$ & 95\% CI \\
149	\midrule
150	4 & 0.482 & [0.449, 0.511] \\
151	8 & 0.508 & [0.479, 0.541] \\
152	12 & 0.560 & [0.529, 0.593] \\
153	16 & 0.592 & [0.559, 0.625] \\
154	20 & 0.593 & [0.559, 0.627] \\
155	24 & 0.611 & [0.578, 0.645] \\
156	28 & 0.619 & [0.587, 0.654] \\
157	32 & 0.639 & [0.603, 0.671] \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	\begin{table}[h]
163	\centering
164	\caption{Counterfactual instruction analysis. Cohen's $d$ and token divergence (\%) relative to original instruction. L1 ablation ($d = 0.65$) included for comparison. The ordering follows semantic distance from the original instruction.}
165	\label{tab:counterfactual}
166	\small
167	\begin{tabular}{lcc}
168	\toprule
169	Condition & Cohen's $d$ & Token div.\ (\%) \\
170	\midrule
171	Empty (no instruction) & 0.968 & 90.7 \\
172	Wrong (different task) & 0.844 & 89.5 \\
173	Paraphrased & 0.697 & 82.6 \\
174	Shuffled (random order) & 0.625 & 85.7 \\
175	\midrule
176	L1 ablation (24 heads) & 0.650 & 72.3 \\
177	\bottomrule
178	\end{tabular}
179	\end{table}
180	
181	\begin{table}[h]
182	\centering
183	\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}
184	\label{tab:action_shift_perdim}
185	\small
186	\begin{tabular}{lccccccc}
187	\toprule
188	Condition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\
189	\midrule
190	Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
191	Control (8) & --- & --- & --- & --- & --- & --- & 0.141 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\subsection{Pretrained LLM Representation Quality Under Visual Input}
197	\label{sec:ood_diagnostics}
198	
199	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
200	We evaluate three diagnostics to assess representation quality.
201	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
202	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, reflecting gradual differentiation rather than catastrophic out-of-distribution behavior.
203	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
204	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
205	
206	\begin{figure}[h]
207	\centering
208	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
209	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics confirm structured, non-degenerate representations.}
210	\label{fig:ood_diagnostics}
211	\end{figure}
212	
213	\subsection{Probe Architecture Sensitivity}
214	\label{sec:linear_probe}
215	
216	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \to 7$, $N/\text{params} \approx 2.2$).
217	The inverted-U pattern reproduces: trained image\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).
218	The trained--untrained gap is larger under the linear probe (L14: $\Delta = +0.324$) than the MLP probe (L8: $\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.
219	Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
220	For last\_preaction tokens, the linear probe also confirms the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\Delta = 0.103$ ($p < 0.001$).
221	These results confirm that our qualitative findings reflect representational structure rather than probe capacity artifacts.
222	
223	\begin{figure}[h]
224	\centering
225	\includegraphics[width=\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}
226	\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}
227	\label{fig:linear_vs_mlp}
228	\end{figure}
229	
230	\subsection{Functional Probe Comparison}
231	\label{sec:probe_bars_appendix}
232	
233	Figure~\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.
234	
235	\begin{figure}[h]
236	\centering
237	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
238	\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
239	\label{fig:probe_bars}
240	\end{figure}
241	
242	\subsection{Training Effect and Instruction Invariance}
243	\label{sec:instruction_invariance_appendix}
244	
245	Figure~\ref{fig:factorial} shows trained vs.\ untrained RSA profiles and instruction invariance.
246	Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
247	
248	\begin{figure}[h]
249	\centering
250	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
251	\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$, confirming visually grounded action geometry.}
252	\label{fig:factorial}
253	\end{figure}
254	
255	\subsection{Additional RSA Values}
256	\label{sec:additional_rsa}
257	
258	DINOv2 \texttt{patch\_mean} achieves RSA $\rho = 0.631$, between the \texttt{cls\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).
259	VLA untrained readout peaks at L1 ($\rho = 0.626$).
260	
261	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
262	\label{sec:cross_benchmark_appendix}
263	
264	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).
265	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
266	
267	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
268	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero) and confirming that the n.s.\ result on Goal reflects limited statistical power.
269	
270	Two notable differences emerge.
271	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
272	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
273	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
274	
275	\begin{figure}[t]
276	\centering
277	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
278	\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
279	\label{fig:cross_benchmark}
280	\end{figure}
281	
282	\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}
283	\label{sec:spatial_cross_instruction}
284	
285	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
286	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
287	The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
288	
289	\begin{table}[h]
290	\centering
291	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\ Table~\ref{tab:dense_routing_main}).}
292	\label{tab:spatial_cross_instruction}
293	\small
294	\begin{tabular}{llccccc}
295	\toprule
296	Token & Condition & L1 & L4 & L8 & L16 & L31 \\
297	\midrule
298	last\_preaction & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
299	last\_preaction & Untrained & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
300	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
301	image\_mean & Untrained & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
302	\bottomrule
303	\end{tabular}
304	\end{table}
305	
306	\subsection{Robustness Analyses}
307	\label{sec:robustness_appendix}
308	
309	\subsubsection{Distance Metric Invariance}
310	\label{sec:metric_invariance}
311	
312	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
313	
314	\begin{table}[h]
315	\centering
316	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
317	\label{tab:metric_invariance}
318	\small
319	\begin{tabular}{lccc}
320	\toprule
321	Condition & Eucl.\ Peak & Cos.\ Peak & Profile $r$ \\
322	\midrule
323	Trained image\_mean & L12 & L12 & 0.990 \\
324	Trained last\_preaction & L12 & L13 & 0.990 \\
325	Untrained image\_mean & L0 & L0 & 0.995 \\
326	Untrained last\_preaction & L1 & L1 & 0.992 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	\subsubsection{Per-DOF Decomposition}
332	\label{sec:perdof}
333	
334	RSA decomposition by action dimension confirms the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\rho = 0.193$), rotation (peak L12, $\rho = 0.175$), and gripper (peak L13, $\rho = 0.106$) all exhibit non-monotonic profiles.
335	Per-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.
336	
337	\subsubsection{Permutation Test}
338	\label{sec:permutation}
339	
340	Permutation testing (1{,}000 shuffles) confirms all observed RSA values are highly significant: observed $\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).
341	
342	\subsubsection{Probe Seed Sensitivity}
343	\label{sec:seed_sensitivity}
344	
345	Action probe $R^2$ is highly stable across random seeds.
346	Over 5 seeds (trained image\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\%$ ($0.655 \pm 0.002$; Table~\ref{tab:seed_sensitivity}).
347	Peak layer concentrates in the L8--L10 region ($4/5$ seeds), confirming the inverted-U shape is not a seed artifact.
348	Seed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.
349	
350	\begin{table}[h]
351	\centering
352	\caption{Probe $R^2$ peak across 5 random seeds (trained image\_mean).}
353	\label{tab:seed_sensitivity}
354	\small
355	\begin{tabular}{lcc}
356	\toprule
357	Seed & Peak Layer & Peak $R^2$ \\
358	\midrule
359	0 & L9 & 0.654 \\
360	1 & L16 & 0.656 \\
361	2 & L9 & 0.653 \\
362	3 & L10 & 0.655 \\
363	42 & L9 & 0.655 \\
364	\midrule
365	Mean$\pm$std & $10.6\pm2.7$ & $0.655\pm0.002$ \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	\subsubsection{Demonstration Subsample Sensitivity}
371	\label{sec:demo_sensitivity}
372	
373	To verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\ref{tab:demo_sensitivity}).
374	The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions, confirming high stability.
375	The probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$, reflecting greater sensitivity of $R^2$ to training set size.
376	Both metrics show reduced absolute values (RSA $-3.6\%$, $R^2$ $-7.6\%$) as expected from halved data, but the non-monotonic profile shape is preserved.
377	
378	\begin{table}[h]
379	\centering
380	\caption{Inverted-U stability under demonstration subsampling (trained image\_mean).}
381	\label{tab:demo_sensitivity}
382	\small
383	\begin{tabular}{lccc}
384	\toprule
385	Metric & 50 demos & 25 demos & $\Delta$ \\
386	\midrule
387	RSA peak layer & L12 & L12 & 0 \\
388	RSA peak $\rho$ & 0.628 & 0.606 & $-3.6\%$ \\
389	$R^2$ peak layer & L9 & L11 & $+2$ \\
390	$R^2$ peak value & 0.659 & 0.609 & $-7.6\%$ \\
391	RSA profile $r$ & --- & 0.970 & --- \\
392	$R^2$ profile $r$ & --- & 0.819 & --- \\
393	\bottomrule
394	\end{tabular}
395	\end{table}
396	
397	\subsection{Detailed Training Effects}
398	\label{sec:training_effects_appendix}
399	
400	Table~\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.
401	
402	\begin{table}[h]
403	\centering
404	\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\Delta{=}+0.017$, $3\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}
405	\label{tab:training_effects}
406	\small
407	\begin{tabular}{lccc}
408	\toprule
409	Comparison & $\Delta$ & 95\% CI & $p$ \\
410	\midrule
411	\multicolumn{4}{l}{\emph{RSA ($\rho$)}} \\
412	Best-vs-best image\_mean & $+$0.017 & incl.\ 0 & n.s. \\
413	\quad (trained L12 vs.\ untrained L0) & & & \\
414	Same-layer L12 image\_mean & $+$0.079 & excl.\ 0 & $<$0.0001 \\
415	\quad (trained vs.\ untrained) & & & \\
416	Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
417	\midrule
418	\multicolumn{4}{l}{\emph{Probe $R^2$}} \\
419	Best-vs-best image\_mean & $+$0.015 & excl.\ 0 & 0.006 \\
420	\quad (trained L8 vs.\ untrained L0) & & & \\
421	Best-vs-best readout & $+$0.069 & excl.\ 0 & $<$0.0001 \\
422	\quad (trained L13 vs.\ untrained L32) & & & \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	\subsection{Training Effect Size Summary}
428	\label{sec:training_effect_summary}
429	
430	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
431	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on last\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
432	This asymmetry confirms that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
433	
434	\begin{table}[h]
435	\centering
436	\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large, confirming that training targets readout-token information integration.}
437	\label{tab:training_effect_summary}
438	\small
439	\begin{tabular}{lccc}
440	\toprule
441	Metric & Trained & Untrained & $\Delta$ \\
442	\midrule
443	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
444	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
445	$R^2$ peak (last\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
446	Instruction routing L31 & 100\% & 82\% & $+$18pp \\
447	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
448	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	\subsection{Instruction Routing Probes}
454	\label{sec:routing_appendix}
455	
456	\subsubsection{Cross-Instruction Classification: Dense Layer Profile}
457	\label{sec:dense_routing}
458	
459	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
460	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
461	Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
462	
463	\begin{table}[h]
464	\centering
465	\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8.}
466	\label{tab:dense_routing}
467	\small
468	\begin{tabular}{lccc}
469	\toprule
470	Layer & Trained & Untrained & Image\_mean (trained) \\
471	\midrule
472	L0 & 10.0\% & 10.0\% & 10.0\% \\
473	L1 & 100.0\% & 100.0\% & 10.0\% \\
474	L2 & 100.0\% & 99.6\% & 10.0\% \\
475	L3 & 100.0\% & 99.6\% & 10.0\% \\
476	L4 & 100.0\% & 99.1\% & 10.0\% \\
477	L5 & 100.0\% & 98.2\% & 10.0\% \\
478	L6 & 100.0\% & 97.3\% & 10.0\% \\
479	L7 & 100.0\% & 96.4\% & 10.0\% \\
480	L8 & 100.0\% & 95.5\% & 10.0\% \\
481	\bottomrule
482	\end{tabular}
483	\end{table}
484	
485	\subsubsection{Cross-Instruction LOOCV Validation}
486	\label{sec:loocv}
487	
488	Leave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) confirms the cross-instruction probe result is not driven by memorization.
489	Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31, confirming perfect generalization.
490	
491	\subsubsection{QA Probe: Progress and Subtask Classification}
492	\label{sec:qa_probe}
493	
494	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\ref{tab:qa_probe}).
495	
496	\begin{table}[h]
497	\centering
498	\caption{QA probe accuracy (progress + subtask classification, best layer).}
499	\label{tab:qa_probe}
500	\small
501	\begin{tabular}{lcc}
502	\toprule
503	Source & Best Layer & Accuracy \\
504	\midrule
505	Trained last\_preaction & L20 & 86.3\% \\
506	Untrained last\_preaction & L20 & 85.3\% \\
507	DINOv2 cls\_token & --- & 82.7\% \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	\subsubsection{Cross-Instruction Probe Profiles}
513	\label{sec:probe_profiles}
514	
515	\begin{figure}[h]
516	\centering
517	\includegraphics[width=\columnwidth]{figures/fig_probe_conditions.pdf}
518	\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\%$ at L1, saturating to $100\%$. Llama-2 base starts at $80.2\%$, reaching $100\%$ by L5. Untrained starts at $100\%$ but decays to $82\%$ by L31.}
519	\label{fig:probe_conditions_appendix}
520	\end{figure}
521	
522	\subsubsection{L1 Attention Pattern Analysis}
523	\label{sec:attention_pattern}
524	
525	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
526	The three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.
527	
528	\begin{figure}[h]
529	\centering
530	\includegraphics[width=\columnwidth]{figures/fig_l1_stacked_bar.pdf}
531	\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\%$ text attention). Llama-2 base: 9/32 heads ($36.5\%$). Untrained: 0/32 heads ($11.7\%$). See Table~\ref{tab:routing_gradient} for quantitative comparison.}
532	\label{fig:attention_appendix}
533	\end{figure}
534	
535	\subsubsection{Multi-Layer Attention Patterns}
536	\label{sec:multilayer_attention}
537	
538	Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
539	The full profile confirms three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
540	
541	\begin{figure}[h]
542	\centering
543	\includegraphics[width=\columnwidth]{figures/fig_multi_layer_attn.pdf}
544	\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}
545	\label{fig:multilayer_attention}
546	\end{figure}
547	
548	\begin{table}[h]
549	\centering
550	\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
551	\label{tab:multilayer_attention}
552	\small
553	\begin{tabular}{lcccccc}
554	\toprule
555	 & \multicolumn{2}{c}{VLA Trained} & \multicolumn{2}{c}{Llama-2 base} & \multicolumn{2}{c}{Untrained} \\
556	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
557	Layer & Heads & Text\% & Heads & Text\% & Heads & Text\% \\
558	\midrule
559	L1 & \textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\
560	L8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\
561	L16 & 10/32 & 48.4 & \textbf{25/32} & 60.2 & 0/32 & 9.2 \\
562	L31 & \textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\subsubsection{Threshold Sensitivity Analysis}
568	\label{sec:threshold_sensitivity}
569	
570	The main text defines instruction-dominant heads as those allocating $>50\%$ attention to instruction tokens.
571	Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%, confirming that the 50\% threshold is not a boundary-sensitive choice.
572	
573	\begin{table}[h]
574	\centering
575	\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}
576	\label{tab:threshold_sensitivity}
577	\small
578	\begin{tabular}{lccc}
579	\toprule
580	Threshold & VLA Trained & Llama-2 base & Untrained \\
581	\midrule
582	30\% & 32 & 13 & 0 \\
583	40\% & 31 & 10 & 0 \\
584	50\% & 24 & 9 & 0 \\
585	60\% & 9 & 4 & 0 \\
586	70\% & 5 & 3 & 0 \\
587	\bottomrule
588	\end{tabular}
589	\end{table}
590	
591	\subsection{L1 Attention Decomposition by Head Group}
592	\label{sec:attention_decomp}
593	
594	Table~\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.
595	
596	\begin{table}[h]
597	\centering
598	\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}
599	\label{tab:attention_decomp}
600	\small
601	\begin{tabular}{lcccc}
602	\toprule
603	Head Group & $N$ & Instruction & Vision & BOS/Other \\
604	\midrule
605	Instruction-dominant & 24 & 62.4\% & 18.8\% & 18.8\% \\
606	Control & 8 & 44.9\% & 27.1\% & 28.0\% \\
607	\midrule
608	$\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\
609	\bottomrule
610	\end{tabular}
611	\end{table}
612	
613	\subsection{Per-Dimension Action MAE Under Head Ablation}
614	\label{sec:per_dim_mae}
615	
616	Table~\ref{tab:per_dim_mae} extends Table~\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.
617	
618	\begin{table}[h]
619	\centering
620	\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$), indicating instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
621	\label{tab:per_dim_mae}
622	\small
623	\begin{tabular}{lccc}
624	\toprule
625	Dimension & Instr.\ 24h MAE & Control 8h MAE & Ratio \\
626	\midrule
627	$dx$ & 0.00189 & 0.00037 & 5.09$\times$ \\
628	$dy$ & 0.00531 & 0.00125 & 4.26$\times$ \\
629	$dz$ & 0.00762 & 0.00243 & 3.14$\times$ \\
630	$roll$ & 0.02059 & 0.00785 & 2.62$\times$ \\
631	$pitch$ & 0.03071 & 0.01387 & 2.21$\times$ \\
632	$yaw$ & 0.03388 & 0.01783 & 1.90$\times$ \\
633	$gripper$ & 0.29072 & 0.14072 & 2.07$\times$ \\
634	\bottomrule
635	\end{tabular}
636	\end{table}
637	
638	\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
639	\label{sec:per_task_r2}
640	
641	Table~\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).
642	
643	\begin{table}[h]
644	\centering
645	\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$), confirming that instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
646	\label{tab:per_task_r2}
647	\small
648	\begin{tabular}{lccc}
649	\toprule
650	Task & Baseline $R^2$ & Ablated $R^2$ & $\Delta R^2$ \\
651	\midrule
652	open middle drawer & 0.197 & 0.221 & $+$0.024 \\
653	open top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\
654	push plate to stove & 0.190 & 0.197 & $+$0.007 \\
655	put bowl on plate & 0.375 & 0.474 & $+$0.099 \\
656	put bowl on stove & 0.235 & 0.395 & $+$0.160 \\
657	put bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\
658	put cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\
659	put wine on rack & 0.189 & 0.424 & $+$0.235 \\
660	put wine on cabinet & 0.279 & 0.353 & $+$0.074 \\
661	turn on stove & 0.385 & 0.421 & $+$0.036 \\
662	\midrule
663	Mean $\pm$ std & $0.256 \pm 0.070$ & $0.363 \pm 0.088$ & $+$0.107 \\
664	\bottomrule
665	\end{tabular}
666	\end{table}
667	
668	\subsection{Specificity Control: Top-24 vs.\ Bottom-24 Head Ablation}
669	\label{sec:specificity_control}
670	
671	To test whether ablation effects are specific to instruction-dominant heads, we compare ablating the top-24 heads (highest instruction attention fraction, i.e., the instruction-dominant group) against the bottom-24 heads (lowest instruction attention fraction).
672	The two groups overlap on 16 heads and differ only on the top-8 vs.\ bottom-8 extremes.
673	
674	\begin{table}[h]
675	\centering
676	\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
677	\label{tab:specificity_control}
678	\small
679	\begin{tabular}{lccc}
680	\toprule
681	Metric & Top-24 & Bottom-24 & Ratio \\
682	\midrule
683	Cohen's $d$ & 0.650 & 0.565 & $1.15\times$ \\
684	KL divergence & 6.50 & 4.17 & $1.56\times$ \\
685	\bottomrule
686	\end{tabular}
687	\end{table}
688	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c3eb2676-40ac-4e89-885e-dc364a3c7f1a"
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01JowE35AUBR5Mzc2zRfsbuN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "af165f80-d0da-4fab-9f8e-5e1ae72523dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 54 · 2026-05-18T19:28:19.528Z_

<details><summary>↩ Tool result · `toolu_01JowE35AUBR5Mzc2zRfsbuN`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c0ca0fd3-c100-4f70-85ab-1be060f95f3e"
}
```

</details>

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01FD4fC4mLrJ8HDwPgSXHLMS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(json.dumps(result, indent=2))\n\" 2>&1 | head -500",
  "description": "Parse registry JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f1f22862-f05d-4971-9428-56e6c07bd1fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vpY4mbqYFVqmWPTdbeZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16141,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16141,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-18T19:28:22.011Z_

<details><summary>↩ Tool result · `toolu_01FD4fC4mLrJ8HDwPgSXHLMS`</summary>

```text
{
  "success": true,
  "data": {
    "experiments": {
      "specificity_control_action": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T18:28:45.197Z",
        "updated_at": "2026-05-18T18:45:03.767Z",
        "hypothesis": "Bottom-24 non-instruction heads should cause significantly less action shift (d << 0.65) than top-24 instruction-dominant heads when ablated, confirming that instruction-action coupling is specific to identified heads rather than a general property of any 24 heads.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl python -u scripts/specificity_control_action.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": 1500,
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "libero_goal 3 tasks x 10 demos x 50 timesteps",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/specificity_control_action.log"
        },
        "conclusion": "negative",
        "notes": "Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.",
        "metrics": {
          "cohens_d": 0.565,
          "paired_mse": 0.034,
          "token_divergence": 0.598,
          "kl_divergence": 4.166,
          "top24_d": 0.65,
          "bottom24_d": 0.565,
          "ratio": 1.15,
          "per_task_d": {
            "cabinet": 0.405,
            "bowl": 0.628,
            "plate": 0.659
          }
        },
        "completed_at": "2026-05-18T18:45:03.767Z"
      },
      "counterfactual_instruction": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T16:52:52.867Z",
        "updated_at": "2026-05-18T17:31:39.989Z",
        "hypothesis": "L1 instruction-dominant heads perform instruction-specific routing: changing the instruction (wrong/empty/shuffled/paraphrased) should produce systematically different action outputs compared to correct instruction, with wrong and empty causing larger divergence than shuffled or paraphrased.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": 6000,
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log"
        },
        "checkpoint_path": "N/A (eval-only experiment)",
        "log_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_counterfactual_instruction_20260518T165804.log",
        "conclusion": "success",
        "completed_at": "2026-05-18T17:31:15.868Z",
        "notes": "4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim."
      },
      "attention_decomposition": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T16:52:54.658Z",
        "updated_at": "2026-05-18T17:20:35.567Z",
        "hypothesis": "Instruction-dominant heads (24/32 at L1) allocate significantly more attention mass to instruction tokens than control heads (8/32), confirming that the head classification reflects genuine functional specialization in attention routing",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "python3 attention_decomposition_and_r2.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/results/attention/",
          "data_count": "5 trained samples + 32-head untrained data",
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "existing attention data",
          "eval_data": "L1 attention summaries"
        },
        "checkpoint_path": "/root/autodl-tmp/vla-ssd/results/attention_decomposition.json",
        "log_path": "/root/vla-ssd/scripts/attention_decomposition_and_r2.py",
        "conclusion": "success",
        "completed_at": "2026-05-18T17:20:32.623Z",
        "notes": "B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json"
      },
      "action_metrics_extended": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T16:52:53.825Z",
        "updated_at": "2026-05-18T17:16:37.223Z",
        "hypothesis": "Extended analysis of existing action trajectory data: (1) per-dimension MAE reveals which action dimensions are most affected by L1 instruction-head ablation, (2) action direction cosine similarity shows whether ablation changes action direction vs magnitude, providing mechanistic detail beyond aggregate Cohen's d.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "python3 (CPU-only, from existing JSONs)",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/results/",
          "data_count": 5000,
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "N/A (analysis only)",
          "eval_data": "action_trajectory_analysis.json + action_trajectory_control.json",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/action_metrics_extended.json"
        },
        "conclusion": "success",
        "completed_at": "2026-05-18T17:16:32.376Z",
        "notes": "Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x, dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x. Cosine similarity NOT computable: source JSONs only have aggregated stats, no raw per-sample action vectors."
      },
      "cross_layer_L13_ablation": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T13:35:44.057Z",
        "updated_at": "2026-05-18T16:56:23.782Z",
        "hypothesis": "L13 full-layer ablation (all 32 heads) produces near-zero action divergence (d \u2248 0), confirming the cross-layer causal gradient: L1 (d=0.65) >> L8 >> L13 (\u22480). Based on R\u00b2 gradient prediction: L13 \u0394\u22480 vs L1 \u0394=+0.059.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u scripts/action_trajectory_L13_ablation.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": "5 tasks x 10 demos x 50 timesteps = 2500 samples",
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.log"
        },
        "conclusion": "negative",
        "notes": "M006/D064: L13 full-layer ablation d=0.668 \u2248 L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.",
        "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
        "completed_at": "2026-05-18T16:26:04.650Z"
      },
      "cross_layer_L8_ablation": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T13:35:43.212Z",
        "updated_at": "2026-05-18T16:33:44.948Z",
        "hypothesis": "L8 full-layer ablation (all 32 heads) produces significantly smaller action divergence (d << 0.65) than L1 instruction-head ablation (24 heads, d=0.65), demonstrating that L1's causal impact on action output is layer-position-specific, not merely a function of head count. Based on R\u00b2 gradient prediction: L8 \u0394=+0.018 vs L1 \u0394=+0.059.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": 2500,
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log"
        },
        "conclusion": "negative",
        "notes": "M006/D064: L8 full-layer ablation d=0.652 \u2248 L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.",
        "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
        "completed_at": "2026-05-18T16:26:02.700Z"
      },
      "dose_response_curve": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T15:07:22.213Z",
        "updated_at": "2026-05-18T16:32:50.159Z",
        "hypothesis": "If instruction routing is a learned collective function, progressively ablating more L1 heads (sorted by instruction attention fraction) should produce monotonically increasing action divergence (dose-response curve). 8 conditions: top-4/8/12/16/20/24/28/32. Supports C2 claim that routing is a distributed, coordinated mechanism.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions 20,24,28,32 (cuda:1)",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": "5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes",
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
        },
        "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
        "conclusion": "success",
        "completed_at": "2026-05-18T16:26:06.324Z",
        "notes": "\u5355\u8c03\u9012\u589e dose-response \u66f2\u7ebf\uff0cd=0.482(top4)\u21920.639(top32)\uff0cdiminishing returns at ~12-16 heads"
      },
      "permutation_test_I2": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T15:07:21.232Z",
        "updated_at": "2026-05-18T15:13:25.536Z",
        "hypothesis": "Permutation test validates that observed CV difference (instruction 1.30 vs control 2.74) and I\u00b2 difference (instruction 0.87 vs control 0.78) are not explained by random head assignment. Shuffling head labels 1000x and recomputing metrics produces null distribution; observed values should fall in extreme tail (p < 0.05).",
        "parent": "action_trajectory_cpu_analysis",
        "spec": {
          "command": "python scripts/permutation_test_I2.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json",
          "data_count": "5 tasks x 2 conditions + 7 dims x 2 conditions",
          "model_name": "n/a (statistical test)",
          "seed": 42,
          "checkpoint_path": "n/a",
          "log_path": "/root/autodl-tmp/vla-ssd/results/permutation_test_I2.json",
          "checkpoint_source": "n/a",
          "eval_data": "action_trajectory_extended_analysis.json"
        },
        "metrics": {
          "cv_exact_paired_p": 0.0156,
          "cv_mc_unpaired_p": 0.0048,
          "cv_7d_p": 0.0078,
          "I2_exact_paired_p": 0.1562,
          "I2_mc_unpaired_p": 0.1434,
          "cv_null_mean": 0,
          "cv_null_std": 0.6756,
          "I2_null_mean": 0,
          "I2_null_std": 0.2468
        },
        "conclusion": "success",
        "completed_at": "2026-05-18T15:13:25.536Z"
      },
      "action_trajectory_cpu_analysis": {
        "status": "PREPARING",
        "retry_count": 0,
        "created_at": "2026-05-18T13:35:44.880Z",
        "updated_at": "2026-05-18T14:29:42.691Z",
        "hypothesis": "Extended analysis of existing action trajectory data: (1) temporal coherence \u2014 L1 ablation disrupts step-to-step action autocorrelation more than control, (2) bootstrap CI on per-head effect size \u2014 formal test of whether instruction heads per-head d (0.027) differs significantly from control heads per-head d (0.051).",
        "parent": "action_trajectory_control",
        "metrics": {
          "bootstrap_per_head_d": {
            "instruction_24h": {
              "mean": 0.0271,
              "ci_95": [
                0.0258,
                0.0285
              ]
            },
            "control_8h": {
              "mean": 0.0514,
              "ci_95": [
                0.0478,
                0.0551
              ]
            },
            "difference_ctrl_minus_inst": {
              "mean": 0.0244,
              "ci_95": [
                0.0203,
                0.0281
              ]
            },
            "task_paired_t": {
              "t": 7.356,
              "p": 0.0018
            },
            "all_5_tasks_ctrl_gt_inst": true,
            "interpretation": "Control heads ~1.9x per-head effect; instruction heads achieve larger total via 24-head collective coordination"
          },
          "temporal_coherence_proxy": {
            "per_dim_cv_instruction": 1.3,
            "per_dim_cv_control": 2.74,
            "cross_task_I2_instruction": 0.87,
            "cross_task_I2_control": 0.78,
            "interpretation": "Instruction ablation produces more consistent (low CV) and more task-dependent (high I\u00b2) perturbation, consistent with structured language-dependent computation"
          },
          "result_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json"
        },
        "conclusion": "success",
        "notes": "Per-head effect formally confirmed: control heads ~1.9x stronger per-head (d=0.051 vs 0.027, p=0.0018). But instruction heads show qualitatively different perturbation: more consistent across dimensions (CV 1.30 vs 2.74) and more task-dependent (I\u00b2=0.87 vs 0.78). Instruction heads mediate structured, coordinated computation rather than individual strong effects."
      },
      "action_trajectory_control": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T11:34:36.585Z",
        "updated_at": "2026-05-18T12:59:24.419Z",
        "hypothesis": "Ablating 8 non-instruction heads (control) produces significantly smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant heads, proving the action output effect is instruction-specific rather than generic perturbation.",
        "parent": "action_trajectory_analysis",
        "spec": {
          "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\"",
          "server": "westd-19183",
          "gpu": [
            "cuda:0"
          ],
          "pid": "47936",
          "log_path": "~/runs/vla-ssd/action_trajectory_control.log",
          "submitted_at": "2026-05-18T11:53:06.410Z",
          "submitted_via": "submit_training_job",
          "backend": "tmux",
          "account": "root"
        },
        "reproduce": {
          "finished_at": "2026-05-18T11:42:54.772Z"
        },
        "extra": {
          "hook_events": [
            {
              "event": "on_complete",
              "action": "agent",
              "ts": "2026-05-18T11:42:57.559215+00:00"
            }
          ]
        },
        "metrics": {
          "paired_action_mse": {
            "mean": 0.0201,
            "std": 0.0489,
            "t_stat": 20.54,
            "p_value": 9e-87,
            "cohens_d": 0.41
          },
          "token_divergence_rate": 0.293,
          "per_dim_action_shift": {
            "dx": 0.00037,
            "dy": 0.00125,
            "dz": 0.00243,
            "rx": 0.00785,
            "ry": 0.01387,
            "rz": 0.01783,
            "gripper": 0.1407
          },
          "kl_divergence": {
            "mean": 1.69,
            "std": 3.7
          },
          "wilcoxon_p": 8e-235,
          "config": {
            "n_tasks": 5,
            "n_demos_per_task": 10,
            "n_timesteps_per_demo": 50,
            "total_forward_passes": 5000,
            "ablated_heads": [
              3,
              5,
              6,
              9,
              13,
              21,
              24,
              28
            ]
          },
          "per_task": {
            "open_middle_drawer": {
              "mse": 0.0071,
              "cohens_d": 0.24,
              "token_div": 0.24
            },
            "open_top_drawer_put_bowl": {
              "mse": 0.0258,
              "cohens_d": 0.48,
              "token_div": 0.304
            },
            "push_plate_to_stove": {
              "mse": 0.0213,
              "cohens_d": 0.42,
              "token_div": 0.306
            },
            "put_bowl_on_plate": {
              "mse": 0.0227,
              "cohens_d": 0.44,
              "token_div": 0.299
            },
            "put_bowl_on_stove": {
              "mse": 0.0236,
              "cohens_d": 0.45,
              "token_div": 0.313
            }
          },
          "comparison_vs_instruction_ablation": {
            "instruction_24heads_mse": 0.0416,
            "control_8heads_mse": 0.0201,
            "mse_ratio": 2.07,
            "instruction_token_div": 0.723,
            "control_token_div": 0.293,
            "div_ratio": 2.47,
            "instruction_kl": 5.079,
            "control_kl": 1.69,
            "kl_ratio": 3,
            "instruction_gripper": 0.291,
            "control_gripper": 0.141,
            "gripper_ratio": 2.07,
            "head_count_ratio": 3,
            "note": "Ratios (2.0-3.0x) are at or below head count ratio (3:1), meaning per-head effect of control heads is comparable to instruction heads"
          }
        },
        "conclusion": "negative",
        "completed_at": "2026-05-18T11:45:26.662Z",
        "notes": "Control ablation (8 non-instruction heads) also produces significant action divergence (d=0.41, 29.3% token divergence). Per-head effect comparable to instruction heads (0.00250 vs 0.00175). Specificity hypothesis not confirmed. Effect distributed across L1."
      },
      "behavioral_pilot_v2": {
        "status": "PREPARING",
        "retry_count": 0,
        "created_at": "2026-05-18T11:40:18.951Z",
        "updated_at": "2026-05-18T12:05:59.890Z",
        "hypothesis": "Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.",
        "parent": "behavioral_pilot_w4",
        "conclusion": "killed",
        "notes": "Director \u786e\u8ba4\u653e\u5f03 behavioral rollout\uff08mujoco \u7248\u672c\u4e0d\u5339\u914d\uff09\u3002Phase 1 SR=0/3\uff0cfine-tuned checkpoint \u52a0\u8f7d\u6210\u529f\u4f46 action[0] \u9501\u5b9a\u5728 0.236\uff0cBlackwell GPU \u9700\u8981 device_map \u7ed5\u8fc7 segfault\uff0c\u53ef\u80fd\u5f71\u54cd inference\u3002\u4e0d\u518d\u6295\u5165\u3002"
      },
      "action_trajectory_analysis": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T10:35:18.923Z",
        "updated_at": "2026-05-18T11:02:27.281Z",
        "hypothesis": "L1 instruction-dominant head ablation significantly changes OpenVLA action predictions (measured by action token divergence and per-dimension MSE), demonstrating that instruction routing heads directly influence model output, not just intermediate representations.",
        "parent": "ablation_50demos_main",
        "spec": {
          "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py\"",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/",
          "data_count": "5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions",
          "model_name": "OpenVLA-7b (openvla-7b base pretrained)",
          "seed": "42",
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "LIBERO-Goal demo observations (open-loop, no execution)",
          "checkpoint_path": "N/A (inference only)",
          "log_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log"
        },
        "metrics": {
          "paired_action_mse": {
            "mean": 0.0416,
            "std": 0.0639,
            "t_stat": 32.56,
            "p_value": 3.99e-194,
            "cohens_d": 0.651
          },
          "token_divergence_rate": 0.723,
          "per_dim_action_shift_means": [
            0.0019,
            0.0053,
            0.0076,
            0.0206,
            0.0307,
            0.0339,
            0.2907
          ],
          "per_dim_names": [
            "dx",
            "dy",
            "dz",
            "rx",
            "ry",
            "rz",
            "gripper"
          ],
          "kl_divergence": {
            "mean": 5.079,
            "std": 4.961
          },
          "mse_vs_gt_baseline": 0.432,
          "mse_vs_gt_ablated": 0.436,
          "wilcoxon_p": 0,
          "n_tasks": 5,
          "n_samples": 2500,
          "all_tasks_significant": true,
          "per_task_cohens_d_range": [
            0.433,
            0.729
          ],
          "result_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json"
        },
        "conclusion": "success",
        "completed_at": "2026-05-18T11:02:27.281Z"
      },
      "behavioral_pilot_w4": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T09:34:21.677Z",
        "updated_at": "2026-05-18T10:34:21.649Z",
        "hypothesis": "Ablating L1 instruction-dominant heads (24/32) during VLA inference changes task success rate, providing behavioral evidence that attention head specialization has functional consequences beyond representation-level metrics.",
        "parent": "ablation_50demos_main",
        "spec": {
          "command": "bash -c \"source /root/miniconda3/bin/activate base && MUJOCO_GL=egl HDF5_USE_FILE_LOCKING=FALSE PYTHONUNBUFFERED=1 python /root/vla-ssd/scripts/behavioral_pilot.py\"",
          "server": "westd-19183",
          "gpu": [
            "cuda:0"
          ],
          "pid": "24738",
          "log_path": "~/runs/vla-ssd/behavioral_pilot_w4.log",
          "submitted_at": "2026-05-18T10:23:14.928Z",
          "submitted_via": "submit_training_job",
          "backend": "tmux",
          "account": "root",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/",
          "data_count": "3 tasks x 10 episodes x 2 conditions = 60 episodes",
          "model_name": "OpenVLA-7b (openvla-7b)",
          "seed": "42",
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "LIBERO-Goal benchmark (3 selected tasks, 300 max steps per episode)",
          "wall_clock_seconds": 508.3,
          "gpu_hours": 0.14
        },
        "reproduce": {
          "finished_at": "2026-05-18T10:31:41.576Z"
        },
        "failure_reason": "EXIT_CODE=129 (non-zero)",
        "conclusion": "killed",
        "completed_at": "2026-05-18T10:31:43.232Z",
        "extra": {
          "hook_events": [
            {
              "event": "on_failed",
              "action": "agent",
              "ts": "2026-05-18T10:31:45.660946+00:00"
            }
          ]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "6a8306bf-4629-4058-9a87-dbdf85914930"
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Agent · `toolu_01JZAJ6mbk1oJw53X3udJY3y`</summary>

````json
{
  "description": "Wording consistency check",
  "prompt": "You are checking wording consistency in a paper that recently shifted its narrative from \"instruction-specific\" to \"graded distributed routing\".\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Task\nRead ALL .tex files and search for:\n\n### A. Problematic residual strong claims (mark each with file:line)\n1. \"uniquely responsible\"\n2. \"exclusively\"\n3. \"solely driven\"\n4. \"only instruction heads\"\n5. \"specific to instruction heads\" (check context - may be OK with qualifier)\n6. \"instruction-specific\" (in non-probe context, needs checking)\n7. Any wording that implies trajectory-level specificity has been confirmed\n8. Any other overly strong causal claims that don't fit \"graded distributed routing\"\n\n### B. AI writing style markers (mark each with file:line)\n1. \"—\" (em-dash, U+2014) - ALL instances must be flagged\n2. \" – \" (explanatory en-dash, U+2013, with spaces) - flag all except number ranges like \"2020–2024\"\n3. \"-ing,\" pattern (participial phrases ending sentences) - flag instances like \"..., demonstrating the...\" / \"..., highlighting the...\"\n4. Excessive \"Furthermore\" / \"Moreover\" / \"Additionally\" sequences\n5. \"It is worth noting\" / \"Notably, ...\"\n6. \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\"\n7. \"a myriad of\" / \"a plethora of\"\n\n### C. Confirm new narrative keywords exist\nSearch for presence of:\n1. \"graded\" or \"distributed\" (in routing/processing context)\n2. Qualifiers: \"primarily\", \"preferentially\", \"predominantly\", etc.\n\n## Output format\nReturn a markdown table for issues:\n```\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n```\n\nProblem types: \"残留强claim\", \"em-dash\", \"en-dash\", \"AI写作-ing\", \"AI写作过渡词\", \"AI写作用词\"\n\nAlso confirm which new narrative keywords were found and where.\n\nReturn a summary count of issues by type."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c3482798-1177-4f48-9e12-fada2350aaa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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


### System

_source line 58_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Wording consistency check",
  "task_type": "local_agent",
  "prompt": "You are checking wording consistency in a paper that recently shifted its narrative from \"instruction-specific\" to \"graded distributed routing\".\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Task\nRead ALL .tex files and search for:\n\n### A. Problematic residual strong claims (mark each with file:line)\n1. \"uniquely responsible\"\n2. \"exclusively\"\n3. \"solely driven\"\n4. \"only instruction heads\"\n5. \"specific to instruction heads\" (check context - may be OK with qualifier)\n6. \"instruction-specific\" (in non-probe context, needs checking)\n7. Any wording that implies trajectory-level specificity has been confirmed\n8. Any other overly strong causal claims that don't fit \"graded distributed routing\"\n\n### B. AI writing style markers (mark each with file:line)\n1. \"—\" (em-dash, U+2014) - ALL instances must be flagged\n2. \" – \" (explanatory en-dash, U+2013, with spaces) - flag all except number ranges like \"2020–2024\"\n3. \"-ing,\" pattern (participial phrases ending sentences) - flag instances like \"..., demonstrating the...\" / \"..., highlighting the...\"\n4. Excessive \"Furthermore\" / \"Moreover\" / \"Additionally\" sequences\n5. \"It is worth noting\" / \"Notably, ...\"\n6. \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\"\n7. \"a myriad of\" / \"a plethora of\"\n\n### C. Confirm new narrative keywords exist\nSearch for presence of:\n1. \"graded\" or \"distributed\" (in routing/processing context)\n2. Qualifiers: \"primarily\", \"preferentially\", \"predominantly\", etc.\n\n## Output format\nReturn a markdown table for issues:\n```\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n```\n\nProblem types: \"残留强claim\", \"em-dash\", \"en-dash\", \"AI写作-ing\", \"AI写作过渡词\", \"AI写作用词\"\n\nAlso confirm which new narrative keywords were found and where.\n\nReturn a summary count of issues by type.",
  "uuid": "2f027e58-a704-40e9-805d-0b2ab82f4420",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
````

---


## Round 2

## Round 2

33 recorded events


### User

_source line 59 · 2026-05-18T19:28:23.259Z_

You are checking wording consistency in a paper that recently shifted its narrative from "instruction-specific" to "graded distributed routing".

## Paper files location
All .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
Files: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex

## Task
Read ALL .tex files and search for:

### A. Problematic residual strong claims (mark each with file:line)
1. "uniquely responsible"
2. "exclusively"
3. "solely driven"
4. "only instruction heads"
5. "specific to instruction heads" (check context - may be OK with qualifier)
6. "instruction-specific" (in non-probe context, needs checking)
7. Any wording that implies trajectory-level specificity has been confirmed
8. Any other overly strong causal claims that don't fit "graded distributed routing"

### B. AI writing style markers (mark each with file:line)
1. "—" (em-dash, U+2014) - ALL instances must be flagged
2. " – " (explanatory en-dash, U+2013, with spaces) - flag all except number ranges like "2020–2024"
3. "-ing," pattern (participial phrases ending sentences) - flag instances like "..., demonstrating the..." / "..., highlighting the..."
4. Excessive "Furthermore" / "Moreover" / "Additionally" sequences
5. "It is worth noting" / "Notably, ..."
6. "delve into" / "leverage" / "utilize" / "facilitate"
7. "a myriad of" / "a plethora of"

### C. Confirm new narrative keywords exist
Search for presence of:
1. "graded" or "distributed" (in routing/processing context)
2. Qualifiers: "primarily", "preferentially", "predominantly", etc.

## Output format
Return a markdown table for issues:
```
| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |
|---|---|---|---|
```

Problem types: "残留强claim", "em-dash", "en-dash", "AI写作-ing", "AI写作过渡词", "AI写作用词"

Also confirm which new narrative keywords were found and where.

Return a summary count of issues by type.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "27bafe12-555d-4278-a37b-8387d375e10d"
}
```

</details>

---


### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 15940,
    "tool_uses": 1,
    "duration_ms": 3226
  },
  "last_tool_name": "Read",
  "uuid": "46e83c66-b729-4503-b80d-bcefe1a00cc1",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 15942,
    "tool_uses": 2,
    "duration_ms": 3745
  },
  "last_tool_name": "Read",
  "uuid": "f0c85996-49fa-4f66-ad3b-067ad745b8c5",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 15944,
    "tool_uses": 3,
    "duration_ms": 4172
  },
  "last_tool_name": "Read",
  "uuid": "2fb0e16c-0eeb-4965-b7ea-8211577798ef",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 15946,
    "tool_uses": 4,
    "duration_ms": 4644
  },
  "last_tool_name": "Read",
  "uuid": "5af67529-c3bb-4b23-97c5-d52204263d32",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 15948,
    "tool_uses": 5,
    "duration_ms": 5062
  },
  "last_tool_name": "Read",
  "uuid": "589f9a5d-8f65-4bd8-b0cd-a4358d46f8b0",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 15950,
    "tool_uses": 6,
    "duration_ms": 6025
  },
  "last_tool_name": "Read",
  "uuid": "a7923e65-d5d0-4a2c-8c83-96798bdaca1b",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 15952,
    "tool_uses": 7,
    "duration_ms": 6531
  },
  "last_tool_name": "Read",
  "uuid": "bf00b032-e961-41f7-b6a7-9fd8e3dab9c1",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 15954,
    "tool_uses": 8,
    "duration_ms": 6996
  },
  "last_tool_name": "Read",
  "uuid": "9f8e90e5-f395-406d-8ce5-bd1f24ad4796",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Running Extract all metrics from registry experiments",
  "usage": {
    "total_tokens": 52493,
    "tool_uses": 11,
    "duration_ms": 18840
  },
  "last_tool_name": "Bash",
  "uuid": "4399a2bd-c091-47e2-ad54-0946f8a55a6f",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 15956,
    "tool_uses": 9,
    "duration_ms": 7165
  },
  "last_tool_name": "Read",
  "uuid": "1cb8957a-915f-4fca-b1c1-d532704e0f22",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_013vQnjk4CGXFPwoH7guyaSx`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print experiments with metrics\nfor name, exp in result.get('experiments', {}).items():\n    if 'metrics' in exp:\n        print(f'=== {name} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print()\n    elif 'notes' in exp:\n        print(f'=== {name} (notes only) ===')\n        print(exp.get('notes', ''))\n        print()\n\" 2>&1 | tail -300",
  "description": "Extract all metrics from registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "277a2d0d-c29f-4a71-b8ba-c8814d4c1edf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ra8TJHpdb2jGbqkVe8H92f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36321,
      "cache_read_input_tokens": 16141,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36321,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 71 · 2026-05-18T19:28:30.398Z_

<details><summary>↩ Tool result · `toolu_013vQnjk4CGXFPwoH7guyaSx`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e5869c2e-b0a4-42c6-8cf5-58de16b24feb"
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01PDULGUAhkCiNsHAedFMWoq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "322522dc-8088-4a36-bef0-2ff700437af8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 73 · 2026-05-18T19:28:26.491Z_

<details><summary>↩ Tool result · `toolu_01PDULGUAhkCiNsHAedFMWoq`</summary>

```text
1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "056d1c72-f439-41c0-9b63-40536fb12de1"
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01EkS8xgyDsj49Sz4RznY5Am`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a8740ca5-caf5-400e-a3d3-b8fce289a42e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 75 · 2026-05-18T19:28:27.008Z_

<details><summary>↩ Tool result · `toolu_01EkS8xgyDsj49Sz4RznY5Am`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\cite{alain2017} for functional decodability.
15	
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, our framework validates architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions) due to the causal mask and frozen encoder, while the readout token maintains perfect instruction identity ($100\%$, cross-validated) from L1 onward.
18	\emph{Second}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
19	Convergent causal evidence, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
20	\emph{Third}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
21	Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
22	
23	Our contributions are: (i)~a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, validating architecture-expected specialization as a sanity check; (ii)~convergent causal evidence, from seven independent analyses on OpenVLA-7B/LIBERO, that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub; and (iii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes confirm; CKA diverges), with training primarily enhancing readout-token integration rather than visual geometry.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f9dbba22-f529-4cca-9d52-908379bbdd5d"
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_0146VuUEgVsC7pMPsi316GZj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "df1c33a2-272b-4617-b5d5-63d504ceb0c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 77 · 2026-05-18T19:28:27.435Z_

<details><summary>↩ Tool result · `toolu_0146VuUEgVsC7pMPsi316GZj`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
17	
18	\paragraph{Behavioral and mechanistic analysis of VLAs.}
19	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
20	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
21	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
22	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
23	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
24	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
25	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
26	
27	\paragraph{Token-level functional specialization in transformers.}
28	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
29	We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
30	
31	\paragraph{Representation similarity and probing methodology.}
32	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
33	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
34	We adopt RSA and MLP probes, with CKA in the appendix.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "02ff4845-2d08-4a3b-9868-5cb578ee68ec"
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01CdmpYqFt1rRdjsDR6Jmpef`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "8cf547f7-680c-4141-a855-94e3b9df72a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 79 · 2026-05-18T19:28:27.907Z_

<details><summary>↩ Tool result · `toolu_01CdmpYqFt1rRdjsDR6Jmpef`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
25	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.
26	Throughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.
27	We cross two factors: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description) in a $2\times 2$ factorial design.
28	
29	%------------------------------------------------------------------
30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to confirm that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}
40	
41	We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42	This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43	
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) confirms neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "da8a5393-bbc4-4b4f-a883-44ed7ace2c3b"
}
```

</details>

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_013vUguE7FwR4fh6fXiUPWvh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "855fc9db-9db8-432f-8ebe-2bc82916f8a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 81 · 2026-05-18T19:28:28.325Z_

<details><summary>↩ Tool result · `toolu_013vUguE7FwR4fh6fXiUPWvh`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confirm this, as does standalone DINOv2 ($10\%$; Appendix~\ref{sec:instruction_invariance_appendix}).
23	
24	\paragraph{Readout token as multimodal hub.}
25	Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
26	The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
27	
28	\begin{table}[t]
29	\centering
30	\caption{Cross-instruction 10-way classification (full in Appendix~\ref{sec:dense_routing}). Image\_mean: chance; readout: $100\%$ from L1 (trained) or decays.}
31	\label{tab:dense_routing_main}
32	\small
33	\begin{tabular}{lccc}
34	\toprule
35	Layer & Trained readout & Untrained readout & Image\_mean \\
36	\midrule
37	L0 & 10.0\% & 10.0\% & 10.0\% \\
38	L1 & 100.0\% & 100.0\% & 10.0\% \\
39	L4 & 100.0\% & 99.1\% & 10.0\% \\
40	L8 & 100.0\% & 95.5\% & 10.0\% \\
41	L16 & 100.0\% & 91.1\% & 10.0\% \\
42	L31 & 100.0\% & 82.0\% & 10.0\% \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	%------------------------------------------------------------------
48	\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}
49	\label{sec:learned_routing}
50	
51	\paragraph{Three-level routing gradient at L1.}
52	L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
53	
54	\paragraph{Redistribution of routing across depth.}
55	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
56	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
57	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\%--70\%; Appendix~\ref{sec:threshold_sensitivity}).
58	
59	\paragraph{Probe robustness confirms the pattern.}
60	Cross-instruction probes (Appendix Figure~\ref{fig:probe_conditions_appendix}) corroborate: VLA-trained achieves $99.6\%$ at L1; Llama-2 base starts at $80.2\%$, saturating by L5; untrained decays from $100\%$ to $82\%$ (L31).
61	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
62	
63	\paragraph{Ablation confirms routing function.}
64	We ablate attention to instruction tokens at the readout position.
65	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
66	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
67	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
68	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
69	
70	\paragraph{Action trajectory validation.}
71	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
72	
73	\paragraph{Dose-response gradient.}
74	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
75	
76	\paragraph{Counterfactual instruction analysis.}
77	To test instruction dependence, we replace the original instruction with four perturbation types.
78	All conditions produce substantial trajectory divergence: empty ($d = 0.968$), wrong task ($d = 0.844$), paraphrased ($d = 0.697$), and shuffled word order ($d = 0.625$; Table~\ref{tab:counterfactual}).
79	The ordering follows semantic distance from the original instruction.
80	L1 ablation ($d = 0.65$) falls between shuffled and paraphrased, consistent with removal of instruction signal rather than injection of noise (Appendix~\ref{sec:action_trajectory}).
81	
82	\begin{table}[t]
83	\centering
84	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
85	\label{tab:routing_gradient}
86	\small
87	\begin{tabular}{lccccc}
88	\toprule
89	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
90	\midrule
91	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
92	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
93	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
101	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
102	\label{fig:attention_profile}
103	\end{figure}
104	
105	%------------------------------------------------------------------
106	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
107	\label{sec:nonmonotonic}
108	
109	\paragraph{Vision encoder provides geometric foundation.}
110	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
111	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
112	
113	\paragraph{Middle-layer peak (metric-dependent).}
114	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
115	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
116	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
117	
118	\paragraph{Training enhances decodability, not geometry.}
119	Best-vs-best RSA gain is non-significant ($\Delta\rho = 0.017$, $3\%$; Appendix Table~\ref{tab:training_effects}); training reshapes \emph{where} geometry peaks rather than \emph{how high}.
120	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
121	The pattern replicates on LIBERO-Spatial ($p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
122	
123	\begin{table}[t]
124	\centering
125	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
126	\label{tab:rsa_overview}
127	\small
128	\begin{tabular}{lcccc}
129	\toprule
130	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
131	\midrule
132	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
133	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
134	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
135	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
136	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
137	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
138	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
139	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
140	\bottomrule
141	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
142	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
143	\end{tabular}
144	\end{table}
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
149	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
150	\label{fig:layer_curves}
151	\end{figure}
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "18eaa0dd-921e-4668-a6ed-78828a7fc09b"
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_013y8cm9A2SRCcRCAvQr2uNU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "90c06efa-ec1d-4116-95d3-7a092ce9a826",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 83 · 2026-05-18T19:28:29.288Z_

<details><summary>↩ Tool result · `toolu_013y8cm9A2SRCcRCAvQr2uNU`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraphrased $>$ shuffled) follows semantic distance, with L1 ablation falling between shuffled and paraphrased, consistent with signal removal rather than noise injection.
20	The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
21	$R^2$ captures linear decodability; action output reflects the full nonlinear pass. The two are complementary.
22	
23	\paragraph{Predictions.}
24	Other decoder-only VLAs (e.g., RT-2) should show similar entry-layer routing given the shared causal-mask constraint; cross-attention architectures (e.g., $\pi_0$) should differ.
25	L1 ablation should produce measurable task degradation on instruction-discriminative tasks.
26	
27	\paragraph{Limitations and scope.}
28	We study OpenVLA-7B on LIBERO; C1 follows from shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0}, but C2 may differ across backbone scales and decoder paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
29	Our analyses are representational and open-loop; closed-loop evaluation is future work.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b3b2898a-dc1e-4f66-a2ba-be0af2a36705"
}
```

</details>

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Read · `toolu_01J6cwiy4WmbL8Af37xxgqyM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "8a4277c9-4cc5-445d-936c-4cc22a08f581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 85 · 2026-05-18T19:28:29.793Z_

<details><summary>↩ Tool result · `toolu_01J6cwiy4WmbL8Af37xxgqyM`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "46fefd97-e5c0-4bfc-9893-67c3f2a4d729"
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_01Xk2rU6nTxgJ81RkcP4dutz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e7ab8c48-8b46-4f7f-9509-228d97b4a690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 87 · 2026-05-18T19:28:30.259Z_

<details><summary>↩ Tool result · `toolu_01Xk2rU6nTxgJ81RkcP4dutz`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "eb6d3d53-fe8e-4cbc-8c05-b6d754af70ae"
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01GAH1g3tFJzu1CMDAsWMoxU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "41dd8a8a-6677-48a2-9db9-dd322fc13fed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB2A3APvVtZmk13r2H7CE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7684,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7684,
        "ephemeral_1h_input_tokens": 0
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

_source line 89 · 2026-05-18T19:28:30.698Z_

<details><summary>↩ Tool result · `toolu_01GAH1g3tFJzu1CMDAsWMoxU`</summary>

```text
1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures rank-order geometric alignment; CKA captures global linear structure.
27	The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
32	\caption{Three similarity metrics across representation sources. \textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}
33	\label{fig:metric_comparison}
34	\end{figure}
35	
36	\subsection{Branch-Split Detailed Analysis}
37	\label{sec:branch_split_appendix}
38	
39	To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.
40	The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
41	Fusion produces a representation ($\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.
42	The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\rho = 0.615$, a drop of $\Delta = 0.019$ from the fused 2{,}176-D input.
43	
44	\subsection{RSA Across Representation Sources}
45	\label{sec:rsa_bar_appendix}
46	
47	Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
48	
49	\begin{figure}[h]
50	\centering
51	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
52	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 \texttt{cls\_token} ($\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\% bootstrap CIs.}
53	\label{fig:rsa_bar}
54	\end{figure}
55	
56	\subsection{Per-Layer RSA Profiles}
57	\label{sec:rsa_perlayer_appendix}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}
62	\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
63	\label{fig:rsa_perlayer_curve}
64	\end{figure}
65	
66	\subsection{Per-Layer Action Decoding Across Training Stages}
67	\label{sec:action_r2_threecond}
68	
69	Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
70	All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
71	The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
72	Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
73	The untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability confirms that randomly initialized Transformer layers produce destructive interference on action-relevant structure.
74	The three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.
75	The qualitative pattern is consistent across all 3 seeds.
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_action_r2_threecond.pdf}
80	\caption{Per-layer action probe $R^2$ (image\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\pm$ std).}
81	\label{fig:action_r2_threecond}
82	\end{figure}
83	
84	\subsection{Random-Subset Ablation Details}
85	\label{sec:random_subset_ablation}
86	
87	To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
88	Dominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \pm 0.013$.
89	The dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); instruction-dominant heads are thus specialized for routing rather than general-purpose computation.
90	
91	\begin{figure}[h]
92	\centering
93	\includegraphics[width=0.75\columnwidth]{figures/fig_random_subset_ablation.pdf}
94	\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with routing-first specialization of instruction-dominant heads.}
95	\label{fig:random_subset_ablation}
96	\end{figure}
97	
98	\subsection{Action Trajectory Analysis Details}
99	\label{sec:action_trajectory}
100	
101	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
102	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
103	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
104	
105	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
106	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
107	
108	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
109	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.
110	The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
111	
112	\begin{table}[h]
113	\centering
114	\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
115	\label{tab:perhead_bootstrap}
116	\small
117	\begin{tabular}{lccc}
118	\toprule
119	Group & $N$ heads & Collective $d$ & Per-head $d$ [95\% CI] \\
120	\midrule
121	Instruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\
122	Control & 8 & 0.41 & 0.051 [0.048, 0.055] \\
123	\midrule
124	Difference & --- & --- & 0.024, $p = 0.0018$ \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
130	
131	Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
132	Trajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\Delta d / \Delta 4 \approx 0.026$), a plateau at 16--20 heads ($\Delta d = 0.001$), and slow increase at 20--32.
133	
134	\begin{figure}[h]
135	\centering
136	\includegraphics[width=0.75\columnwidth]{figures/fig_dose_response.pdf}
137	\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}
138	\label{fig:dose_response}
139	\end{figure}
140	
141	\begin{table}[h]
142	\centering
143	\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\ original action sequence; 95\% bootstrap CIs ($10{,}000$ resamples).}
144	\label{tab:dose_response}
145	\small
146	\begin{tabular}{rcc}
147	\toprule
148	Heads ablated & Cohen's $d$ & 95\% CI \\
149	\midrule
150	4 & 0.482 & [0.449, 0.511] \\
151	8 & 0.508 & [0.479, 0.541] \\
152	12 & 0.560 & [0.529, 0.593] \\
153	16 & 0.592 & [0.559, 0.625] \\
154	20 & 0.593 & [0.559, 0.627] \\
155	24 & 0.611 & [0.578, 0.645] \\
156	28 & 0.619 & [0.587, 0.654] \\
157	32 & 0.639 & [0.603, 0.671] \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	\begin{table}[h]
163	\centering
164	\caption{Counterfactual instruction analysis. Cohen's $d$ and token divergence (\%) relative to original instruction. L1 ablation ($d = 0.65$) included for comparison. The ordering follows semantic distance from the original instruction.}
165	\label{tab:counterfactual}
166	\small
167	\begin{tabular}{lcc}
168	\toprule
169	Condition & Cohen's $d$ & Token div.\ (\%) \\
170	\midrule
171	Empty (no instruction) & 0.968 & 90.7 \\
172	Wrong (different task) & 0.844 & 89.5 \\
173	Paraphrased & 0.697 & 82.6 \\
174	Shuffled (random order) & 0.625 & 85.7 \\
175	\midrule
176	L1 ablation (24 heads) & 0.650 & 72.3 \\
177	\bottomrule
178	\end{tabular}
179	\end{table}
180	
181	\begin{table}[h]
182	\centering
183	\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}
184	\label{tab:action_shift_perdim}
185	\small
186	\begin{tabular}{lccccccc}
187	\toprule
188	Condition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\
189	\midrule
190	Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
191	Control (8) & --- & --- & --- & --- & --- & --- & 0.141 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\subsection{Pretrained LLM Representation Quality Under Visual Input}
197	\label{sec:ood_diagnostics}
198	
199	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
200	We evaluate three diagnostics to assess representation quality.
201	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
202	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, reflecting gradual differentiation rather than catastrophic out-of-distribution behavior.
203	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
204	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
205	
206	\begin{figure}[h]
207	\centering
208	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
209	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics confirm structured, non-degenerate representations.}
210	\label{fig:ood_diagnostics}
211	\end{figure}
212	
213	\subsection{Probe Architecture Sensitivity}
214	\label{sec:linear_probe}
215	
216	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \to 7$, $N/\text{params} \approx 2.2$).
217	The inverted-U pattern reproduces: trained image\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).
218	The trained--untrained gap is larger under the linear probe (L14: $\Delta = +0.324$) than the MLP probe (L8: $\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.
219	Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
220	For last\_preaction tokens, the linear probe also confirms the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\Delta = 0.103$ ($p < 0.001$).
221	These results confirm that our qualitative findings reflect representational structure rather than probe capacity artifacts.
222	
223	\begin{figure}[h]
224	\centering
225	\includegraphics[width=\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}
226	\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}
227	\label{fig:linear_vs_mlp}
228	\end{figure}
229	
230	\subsection{Functional Probe Comparison}
231	\label{sec:probe_bars_appendix}
232	
233	Figure~\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.
234	
235	\begin{figure}[h]
236	\centering
237	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
238	\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
239	\label{fig:probe_bars}
240	\end{figure}
241	
242	\subsection{Training Effect and Instruction Invariance}
243	\label{sec:instruction_invariance_appendix}
244	
245	Figure~\ref{fig:factorial} shows trained vs.\ untrained RSA profiles and instruction invariance.
246	Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
247	
248	\begin{figure}[h]
249	\centering
250	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
251	\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$, confirming visually grounded action geometry.}
252	\label{fig:factorial}
253	\end{figure}
254	
255	\subsection{Additional RSA Values}
256	\label{sec:additional_rsa}
257	
258	DINOv2 \texttt{patch\_mean} achieves RSA $\rho = 0.631$, between the \texttt{cls\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).
259	VLA untrained readout peaks at L1 ($\rho = 0.626$).
260	
261	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
262	\label{sec:cross_benchmark_appendix}
263	
264	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).
265	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
266	
267	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
268	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero) and confirming that the n.s.\ result on Goal reflects limited statistical power.
269	
270	Two notable differences emerge.
271	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
272	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
273	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
274	
275	\begin{figure}[t]
276	\centering
277	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
278	\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
279	\label{fig:cross_benchmark}
280	\end{figure}
281	
282	\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}
283	\label{sec:spatial_cross_instruction}
284	
285	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
286	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
287	The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
288	
289	\begin{table}[h]
290	\centering
291	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\ Table~\ref{tab:dense_routing_main}).}
292	\label{tab:spatial_cross_instruction}
293	\small
294	\begin{tabular}{llccccc}
295	\toprule
296	Token & Condition & L1 & L4 & L8 & L16 & L31 \\
297	\midrule
298	last\_preaction & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
299	last\_preaction & Untrained & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
300	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
301	image\_mean & Untrained & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
302	\bottomrule
303	\end{tabular}
304	\end{table}
305	
306	\subsection{Robustness Analyses}
307	\label{sec:robustness_appendix}
308	
309	\subsubsection{Distance Metric Invariance}
310	\label{sec:metric_invariance}
311	
312	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
313	
314	\begin{table}[h]
315	\centering
316	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
317	\label{tab:metric_invariance}
318	\small
319	\begin{tabular}{lccc}
320	\toprule
321	Condition & Eucl.\ Peak & Cos.\ Peak & Profile $r$ \\
322	\midrule
323	Trained image\_mean & L12 & L12 & 0.990 \\
324	Trained last\_preaction & L12 & L13 & 0.990 \\
325	Untrained image\_mean & L0 & L0 & 0.995 \\
326	Untrained last\_preaction & L1 & L1 & 0.992 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	\subsubsection{Per-DOF Decomposition}
332	\label{sec:perdof}
333	
334	RSA decomposition by action dimension confirms the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\rho = 0.193$), rotation (peak L12, $\rho = 0.175$), and gripper (peak L13, $\rho = 0.106$) all exhibit non-monotonic profiles.
335	Per-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.
336	
337	\subsubsection{Permutation Test}
338	\label{sec:permutation}
339	
340	Permutation testing (1{,}000 shuffles) confirms all observed RSA values are highly significant: observed $\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).
341	
342	\subsubsection{Probe Seed Sensitivity}
343	\label{sec:seed_sensitivity}
344	
345	Action probe $R^2$ is highly stable across random seeds.
346	Over 5 seeds (trained image\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\%$ ($0.655 \pm 0.002$; Table~\ref{tab:seed_sensitivity}).
347	Peak layer concentrates in the L8--L10 region ($4/5$ seeds), confirming the inverted-U shape is not a seed artifact.
348	Seed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.
349	
350	\begin{table}[h]
351	\centering
352	\caption{Probe $R^2$ peak across 5 random seeds (trained image\_mean).}
353	\label{tab:seed_sensitivity}
354	\small
355	\begin{tabular}{lcc}
356	\toprule
357	Seed & Peak Layer & Peak $R^2$ \\
358	\midrule
359	0 & L9 & 0.654 \\
360	1 & L16 & 0.656 \\
361	2 & L9 & 0.653 \\
362	3 & L10 & 0.655 \\
363	42 & L9 & 0.655 \\
364	\midrule
365	Mean$\pm$std & $10.6\pm2.7$ & $0.655\pm0.002$ \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	\subsubsection{Demonstration Subsample Sensitivity}
371	\label{sec:demo_sensitivity}
372	
373	To verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\ref{tab:demo_sensitivity}).
374	The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions, confirming high stability.
375	The probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$, reflecting greater sensitivity of $R^2$ to training set size.
376	Both metrics show reduced absolute values (RSA $-3.6\%$, $R^2$ $-7.6\%$) as expected from halved data, but the non-monotonic profile shape is preserved.
377	
378	\begin{table}[h]
379	\centering
380	\caption{Inverted-U stability under demonstration subsampling (trained image\_mean).}
381	\label{tab:demo_sensitivity}
382	\small
383	\begin{tabular}{lccc}
384	\toprule
385	Metric & 50 demos & 25 demos & $\Delta$ \\
386	\midrule
387	RSA peak layer & L12 & L12 & 0 \\
388	RSA peak $\rho$ & 0.628 & 0.606 & $-3.6\%$ \\
389	$R^2$ peak layer & L9 & L11 & $+2$ \\
390	$R^2$ peak value & 0.659 & 0.609 & $-7.6\%$ \\
391	RSA profile $r$ & --- & 0.970 & --- \\
392	$R^2$ profile $r$ & --- & 0.819 & --- \\
393	\bottomrule
394	\end{tabular}
395	\end{table}
396	
397	\subsection{Detailed Training Effects}
398	\label{sec:training_effects_appendix}
399	
400	Table~\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.
401	
402	\begin{table}[h]
403	\centering
404	\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\Delta{=}+0.017$, $3\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}
405	\label{tab:training_effects}
406	\small
407	\begin{tabular}{lccc}
408	\toprule
409	Comparison & $\Delta$ & 95\% CI & $p$ \\
410	\midrule
411	\multicolumn{4}{l}{\emph{RSA ($\rho$)}} \\
412	Best-vs-best image\_mean & $+$0.017 & incl.\ 0 & n.s. \\
413	\quad (trained L12 vs.\ untrained L0) & & & \\
414	Same-layer L12 image\_mean & $+$0.079 & excl.\ 0 & $<$0.0001 \\
415	\quad (trained vs.\ untrained) & & & \\
416	Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
417	\midrule
418	\multicolumn{4}{l}{\emph{Probe $R^2$}} \\
419	Best-vs-best image\_mean & $+$0.015 & excl.\ 0 & 0.006 \\
420	\quad (trained L8 vs.\ untrained L0) & & & \\
421	Best-vs-best readout & $+$0.069 & excl.\ 0 & $<$0.0001 \\
422	\quad (trained L13 vs.\ untrained L32) & & & \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	\subsection{Training Effect Size Summary}
428	\label{sec:training_effect_summary}
429	
430	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
431	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on last\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
432	This asymmetry confirms that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
433	
434	\begin{table}[h]
435	\centering
436	\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large, confirming that training targets readout-token information integration.}
437	\label{tab:training_effect_summary}
438	\small
439	\begin{tabular}{lccc}
440	\toprule
441	Metric & Trained & Untrained & $\Delta$ \\
442	\midrule
443	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
444	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
445	$R^2$ peak (last\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
446	Instruction routing L31 & 100\% & 82\% & $+$18pp \\
447	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
448	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	\subsection{Instruction Routing Probes}
454	\label{sec:routing_appendix}
455	
456	\subsubsection{Cross-Instruction Classification: Dense Layer Profile}
457	\label{sec:dense_routing}
458	
459	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
460	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
461	Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
462	
463	\begin{table}[h]
464	\centering
465	\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8.}
466	\label{tab:dense_routing}
467	\small
468	\begin{tabular}{lccc}
469	\toprule
470	Layer & Trained & Untrained & Image\_mean (trained) \\
471	\midrule
472	L0 & 10.0\% & 10.0\% & 10.0\% \\
473	L1 & 100.0\% & 100.0\% & 10.0\% \\
474	L2 & 100.0\% & 99.6\% & 10.0\% \\
475	L3 & 100.0\% & 99.6\% & 10.0\% \\
476	L4 & 100.0\% & 99.1\% & 10.0\% \\
477	L5 & 100.0\% & 98.2\% & 10.0\% \\
478	L6 & 100.0\% & 97.3\% & 10.0\% \\
479	L7 & 100.0\% & 96.4\% & 10.0\% \\
480	L8 & 100.0\% & 95.5\% & 10.0\% \\
481	\bottomrule
482	\end{tabular}
483	\end{table}
484	
485	\subsubsection{Cross-Instruction LOOCV Validation}
486	\label{sec:loocv}
487	
488	Leave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) confirms the cross-instruction probe result is not driven by memorization.
489	Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31, confirming perfect generalization.
490	
491	\subsubsection{QA Probe: Progress and Subtask Classification}
492	\label{sec:qa_probe}
493	
494	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\ref{tab:qa_probe}).
495	
496	\begin{table}[h]
497	\centering
498	\caption{QA probe accuracy (progress + subtask classification, best layer).}
499	\label{tab:qa_probe}
500	\small
501	\begin{tabular}{lcc}
502	\toprule
503	Source & Best Layer & Accuracy \\
504	\midrule
505	Trained last\_preaction & L20 & 86.3\% \\
506	Untrained last\_preaction & L20 & 85.3\% \\
507	DINOv2 cls\_token & --- & 82.7\% \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	\subsubsection{Cross-Instruction Probe Profiles}
513	\label{sec:probe_profiles}
514	
515	\begin{figure}[h]
516	\centering
517	\includegraphics[width=\columnwidth]{figures/fig_probe_conditions.pdf}
518	\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\%$ at L1, saturating to $100\%$. Llama-2 base starts at $80.2\%$, reaching $100\%$ by L5. Untrained starts at $100\%$ but decays to $82\%$ by L31.}
519	\label{fig:probe_conditions_appendix}
520	\end{figure}
521	
522	\subsubsection{L1 Attention Pattern Analysis}
523	\label{sec:attention_pattern}
524	
525	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
526	The three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.
527	
528	\begin{figure}[h]
529	\centering
530	\includegraphics[width=\columnwidth]{figures/fig_l1_stacked_bar.pdf}
531	\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\%$ text attention). Llama-2 base: 9/32 heads ($36.5\%$). Untrained: 0/32 heads ($11.7\%$). See Table~\ref{tab:routing_gradient} for quantitative comparison.}
532	\label{fig:attention_appendix}
533	\end{figure}
534	
535	\subsubsection{Multi-Layer Attention Patterns}
536	\label{sec:multilayer_attention}
537	
538	Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
539	The full profile confirms three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
540	
541	\begin{figure}[h]
542	\centering
543	\includegraphics[width=\columnwidth]{figures/fig_multi_layer_attn.pdf}
544	\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}
545	\label{fig:multilayer_attention}
546	\end{figure}
547	
548	\begin{table}[h]
549	\centering
550	\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
551	\label{tab:multilayer_attention}
552	\small
553	\begin{tabular}{lcccccc}
554	\toprule
555	 & \multicolumn{2}{c}{VLA Trained} & \multicolumn{2}{c}{Llama-2 base} & \multicolumn{2}{c}{Untrained} \\
556	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
557	Layer & Heads & Text\% & Heads & Text\% & Heads & Text\% \\
558	\midrule
559	L1 & \textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\
560	L8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\
561	L16 & 10/32 & 48.4 & \textbf{25/32} & 60.2 & 0/32 & 9.2 \\
562	L31 & \textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\subsubsection{Threshold Sensitivity Analysis}
568	\label{sec:threshold_sensitivity}
569	
570	The main text defines instruction-dominant heads as those allocating $>50\%$ attention to instruction tokens.
571	Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%, confirming that the 50\% threshold is not a boundary-sensitive choice.
572	
573	\begin{table}[h]
574	\centering
575	\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}
576	\label{tab:threshold_sensitivity}
577	\small
578	\begin{tabular}{lccc}
579	\toprule
580	Threshold & VLA Trained & Llama-2 base & Untrained \\
581	\midrule
582	30\% & 32 & 13 & 0 \\
583	40\% & 31 & 10 & 0 \\
584	50\% & 24 & 9 & 0 \\
585	60\% & 9 & 4 & 0 \\
586	70\% & 5 & 3 & 0 \\
587	\bottomrule
588	\end{tabular}
589	\end{table}
590	
591	\subsection{L1 Attention Decomposition by Head Group}
592	\label{sec:attention_decomp}
593	
594	Table~\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.
595	
596	\begin{table}[h]
597	\centering
598	\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}
599	\label{tab:attention_decomp}
600	\small
601	\begin{tabular}{lcccc}
602	\toprule
603	Head Group & $N$ & Instruction & Vision & BOS/Other \\
604	\midrule
605	Instruction-dominant & 24 & 62.4\% & 18.8\% & 18.8\% \\
606	Control & 8 & 44.9\% & 27.1\% & 28.0\% \\
607	\midrule
608	$\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\
609	\bottomrule
610	\end{tabular}
611	\end{table}
612	
613	\subsection{Per-Dimension Action MAE Under Head Ablation}
614	\label{sec:per_dim_mae}
615	
616	Table~\ref{tab:per_dim_mae} extends Table~\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.
617	
618	\begin{table}[h]
619	\centering
620	\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$), indicating instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
621	\label{tab:per_dim_mae}
622	\small
623	\begin{tabular}{lccc}
624	\toprule
625	Dimension & Instr.\ 24h MAE & Control 8h MAE & Ratio \\
626	\midrule
627	$dx$ & 0.00189 & 0.00037 & 5.09$\times$ \\
628	$dy$ & 0.00531 & 0.00125 & 4.26$\times$ \\
629	$dz$ & 0.00762 & 0.00243 & 3.14$\times$ \\
630	$roll$ & 0.02059 & 0.00785 & 2.62$\times$ \\
631	$pitch$ & 0.03071 & 0.01387 & 2.21$\times$ \\
632	$yaw$ & 0.03388 & 0.01783 & 1.90$\times$ \\
633	$gripper$ & 0.29072 & 0.14072 & 2.07$\times$ \\
634	\bottomrule
635	\end{tabular}
636	\end{table}
637	
638	\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
639	\label{sec:per_task_r2}
640	
641	Table~\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).
642	
643	\begin{table}[h]
644	\centering
645	\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$), confirming that instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
646	\label{tab:per_task_r2}
647	\small
648	\begin{tabular}{lccc}
649	\toprule
650	Task & Baseline $R^2$ & Ablated $R^2$ & $\Delta R^2$ \\
651	\midrule
652	open middle drawer & 0.197 & 0.221 & $+$0.024 \\
653	open top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\
654	push plate to stove & 0.190 & 0.197 & $+$0.007 \\
655	put bowl on plate & 0.375 & 0.474 & $+$0.099 \\
656	put bowl on stove & 0.235 & 0.395 & $+$0.160 \\
657	put bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\
658	put cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\
659	put wine on rack & 0.189 & 0.424 & $+$0.235 \\
660	put wine on cabinet & 0.279 & 0.353 & $+$0.074 \\
661	turn on stove & 0.385 & 0.421 & $+$0.036 \\
662	\midrule
663	Mean $\pm$ std & $0.256 \pm 0.070$ & $0.363 \pm 0.088$ & $+$0.107 \\
664	\bottomrule
665	\end{tabular}
666	\end{table}
667	
668	\subsection{Specificity Control: Top-24 vs.\ Bottom-24 Head Ablation}
669	\label{sec:specificity_control}
670	
671	To test whether ablation effects are specific to instruction-dominant heads, we compare ablating the top-24 heads (highest instruction attention fraction, i.e., the instruction-dominant group) against the bottom-24 heads (lowest instruction attention fraction).
672	The two groups overlap on 16 heads and differ only on the top-8 vs.\ bottom-8 extremes.
673	
674	\begin{table}[h]
675	\centering
676	\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
677	\label{tab:specificity_control}
678	\small
679	\begin{tabular}{lccc}
680	\toprule
681	Metric & Top-24 & Bottom-24 & Ratio \\
682	\midrule
683	Cohen's $d$ & 0.650 & 0.565 & $1.15\times$ \\
684	KL divergence & 6.50 & 4.17 & $1.56\times$ \\
685	\bottomrule
686	\end{tabular}
687	\end{table}
688	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ec1c75da-111c-4db2-9060-1df5663bffd5"
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Agent · `toolu_01EkV7ERxEvqeZhZqGBGxAd6`</summary>

````json
{
  "description": "Cross-reference integrity check",
  "prompt": "You are checking cross-reference integrity in a LaTeX paper.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\nThe .bib file is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib\n\n## Task\n1. **Labels and refs**: \n   - Extract ALL \\label{...} from all .tex files (note file:line for each)\n   - Extract ALL \\ref{...}, \\eqref{...}, \\autoref{...}, \\cref{...}, \\Cref{...} from all .tex files\n   - Find orphan labels (defined but never referenced)\n   - Find dangling refs (referenced but never defined)\n\n2. **Citations**:\n   - Extract ALL \\cite{...}, \\citep{...}, \\citet{...}, \\citealp{...} etc. from all .tex files\n   - Extract ALL bib entry keys from references.bib\n   - Find missing citations (cited in tex but not in bib)\n   - Find unused bib entries (in bib but never cited) - just count these, don't list all\n\n3. **Other checks**:\n   - Check for duplicate labels\n   - Check for common issues like \\ref without preceding ~ (should be ~\\ref for non-breaking space)\n\n## Output format\nReturn:\n```\n## 交叉引用检查\n\n### 孤立 \\label (defined but never referenced)\n- file:line - \\label{xxx}\n...\n\n### 悬空 \\ref (referenced but never defined)\n- file:line - \\ref{xxx}\n...\n\n### 缺失 \\cite (cited but not in .bib)\n- file:line - \\cite{xxx}\n...\n\n### 未使用 bib 条目\nN entries in .bib are never cited.\n\n### 其他问题\n- duplicate labels, missing ~\\ref, etc.\n```\n\nReturn a summary count."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "72e50fd9-986e-4bab-89c5-5fa6fed3fb8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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


### System

_source line 91_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Cross-reference integrity check",
  "task_type": "local_agent",
  "prompt": "You are checking cross-reference integrity in a LaTeX paper.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\nThe .bib file is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib\n\n## Task\n1. **Labels and refs**: \n   - Extract ALL \\label{...} from all .tex files (note file:line for each)\n   - Extract ALL \\ref{...}, \\eqref{...}, \\autoref{...}, \\cref{...}, \\Cref{...} from all .tex files\n   - Find orphan labels (defined but never referenced)\n   - Find dangling refs (referenced but never defined)\n\n2. **Citations**:\n   - Extract ALL \\cite{...}, \\citep{...}, \\citet{...}, \\citealp{...} etc. from all .tex files\n   - Extract ALL bib entry keys from references.bib\n   - Find missing citations (cited in tex but not in bib)\n   - Find unused bib entries (in bib but never cited) - just count these, don't list all\n\n3. **Other checks**:\n   - Check for duplicate labels\n   - Check for common issues like \\ref without preceding ~ (should be ~\\ref for non-breaking space)\n\n## Output format\nReturn:\n```\n## 交叉引用检查\n\n### 孤立 \\label (defined but never referenced)\n- file:line - \\label{xxx}\n...\n\n### 悬空 \\ref (referenced but never defined)\n- file:line - \\ref{xxx}\n...\n\n### 缺失 \\cite (cited but not in .bib)\n- file:line - \\cite{xxx}\n...\n\n### 未使用 bib 条目\nN entries in .bib are never cited.\n\n### 其他问题\n- duplicate labels, missing ~\\ref, etc.\n```\n\nReturn a summary count.",
  "uuid": "240dbcb7-cff4-4512-be1a-63e0b5112372",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
````

---


## Round 3

## Round 3

34 recorded events


### User

_source line 92 · 2026-05-18T19:28:32.379Z_

You are checking cross-reference integrity in a LaTeX paper.

## Paper files location
All .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
Files: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex

The .bib file is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib

## Task
1. **Labels and refs**: 
   - Extract ALL \label{...} from all .tex files (note file:line for each)
   - Extract ALL \ref{...}, \eqref{...}, \autoref{...}, \cref{...}, \Cref{...} from all .tex files
   - Find orphan labels (defined but never referenced)
   - Find dangling refs (referenced but never defined)

2. **Citations**:
   - Extract ALL \cite{...}, \citep{...}, \citet{...}, \citealp{...} etc. from all .tex files
   - Extract ALL bib entry keys from references.bib
   - Find missing citations (cited in tex but not in bib)
   - Find unused bib entries (in bib but never cited) - just count these, don't list all

3. **Other checks**:
   - Check for duplicate labels
   - Check for common issues like \ref without preceding ~ (should be ~\ref for non-breaking space)

## Output format
Return:
```
## 交叉引用检查

### 孤立 \label (defined but never referenced)
- file:line - \label{xxx}
...

### 悬空 \ref (referenced but never defined)
- file:line - \ref{xxx}
...

### 缺失 \cite (cited but not in .bib)
- file:line - \cite{xxx}
...

### 未使用 bib 条目
N entries in .bib are never cited.

### 其他问题
- duplicate labels, missing ~\ref, etc.
```

Return a summary count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "742b627a-ffcb-43de-b088-660c4c3dd0bd"
}
```

</details>

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Running Extract all experiment metrics and notes from registry",
  "usage": {
    "total_tokens": 52926,
    "tool_uses": 12,
    "duration_ms": 23905
  },
  "last_tool_name": "Bash",
  "uuid": "841868cb-0e05-4736-a03e-fc21e928a570",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Finding *.tex",
  "usage": {
    "total_tokens": 15881,
    "tool_uses": 1,
    "duration_ms": 3578
  },
  "last_tool_name": "Glob",
  "uuid": "1d221c2e-ab22-4f87-a10e-99bab920c598",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for uniquely responsible",
  "usage": {
    "total_tokens": 43272,
    "tool_uses": 10,
    "duration_ms": 13597
  },
  "last_tool_name": "Grep",
  "uuid": "cfd1bccb-cb5d-441d-9b68-85cc250001fb",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for exclusively",
  "usage": {
    "total_tokens": 43273,
    "tool_uses": 11,
    "duration_ms": 14535
  },
  "last_tool_name": "Grep",
  "uuid": "89b5c230-1d3f-490c-8047-580a815cd301",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for solely driven",
  "usage": {
    "total_tokens": 43274,
    "tool_uses": 12,
    "duration_ms": 15022
  },
  "last_tool_name": "Grep",
  "uuid": "57cef249-a0fa-49ab-ba48-89d0d898df30",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 17012,
    "tool_uses": 2,
    "duration_ms": 6294
  },
  "last_tool_name": "Read",
  "uuid": "1be01d92-e265-4462-a4c4-27da92b64b38",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 17083,
    "tool_uses": 3,
    "duration_ms": 6772
  },
  "last_tool_name": "Read",
  "uuid": "807ca252-d266-4ec0-b377-ff4b8d45b44a",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for only instruction heads",
  "usage": {
    "total_tokens": 43275,
    "tool_uses": 13,
    "duration_ms": 15959
  },
  "last_tool_name": "Grep",
  "uuid": "9e3cb8a0-55e0-4e91-9e16-cdda97d3c72e",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 17154,
    "tool_uses": 4,
    "duration_ms": 7243
  },
  "last_tool_name": "Read",
  "uuid": "86a837c2-0dc6-4028-b3cb-3171a914f548",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01CPVCqZ3UHMz8AxLWqoQPEY`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print all experiment names and their metrics/notes\nfor name, exp in result.get('experiments', {}).items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    if metrics or notes:\n        print(f'--- {name} ---')\n        if metrics:\n            print('METRICS:', json.dumps(metrics, indent=2, default=str))\n        if notes:\n            print('NOTES:', notes)\n        print()\n\" 2>&1",
  "description": "Extract all experiment metrics and notes from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b09f2983-5361-427c-bce0-4178b981ef49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvWsBdKJyNTroaWsmdde3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 52462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 360,
        "ephemeral_1h_input_tokens": 0
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

_source line 103 · 2026-05-18T19:28:35.471Z_

<details><summary>↩ Tool result · `toolu_01CPVCqZ3UHMz8AxLWqoQPEY`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "04dd5da8-c9ad-4720-bfb5-cf8f43892cdf"
}
```

</details>

---


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Grep · `toolu_01DpenmyXXHutrsg4VKtek6y`</summary>

```json
{
  "pattern": "uniquely responsible",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "cae68731-9e31-4180-a602-1322ab4c00a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 105 · 2026-05-18T19:28:36.876Z_

<details><summary>↩ Tool result · `toolu_01DpenmyXXHutrsg4VKtek6y`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3efbfa08-03c9-4d84-8344-11f12e786c59"
}
```

</details>

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Grep · `toolu_01TRHHLXcwtzr1QMcaAgBP6R`</summary>

```json
{
  "pattern": "exclusively",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a5f38646-2efe-4b8b-b45d-9d6f550bb54a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-18T19:28:37.804Z_

<details><summary>↩ Tool result · `toolu_01TRHHLXcwtzr1QMcaAgBP6R`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "d835e187-11b5-4491-a130-3136f4e66f83"
}
```

</details>

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Grep · `toolu_01XQs697JpQegzEkNyKncs2A`</summary>

```json
{
  "pattern": "solely driven",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "9d0339fa-8b1f-4863-9c2c-a4e4a52cdb1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 109 · 2026-05-18T19:28:38.299Z_

<details><summary>↩ Tool result · `toolu_01XQs697JpQegzEkNyKncs2A`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "272c11fd-c399-4884-b5ee-373b7bf1badc"
}
```

</details>

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Grep · `toolu_01UNCbAE2urDH1BsqQycFdKX`</summary>

```json
{
  "pattern": "only instruction heads",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "bd853479-fb7c-463e-baf3-fbfd48692f98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 111 · 2026-05-18T19:28:39.234Z_

<details><summary>↩ Tool result · `toolu_01UNCbAE2urDH1BsqQycFdKX`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c6599f35-90dd-498b-ac79-23d0506c2d8f"
}
```

</details>

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Glob · `toolu_01A1MM5dZ415S66mfuNF4xSk`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "785c4113-7e44-4d68-879b-3c9849629563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyHqNtgqTFGQncFKwnBQBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7625,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7625,
        "ephemeral_1h_input_tokens": 0
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

_source line 113 · 2026-05-18T19:28:35.967Z_

<details><summary>↩ Tool result · `toolu_01A1MM5dZ415S66mfuNF4xSk`</summary>

```text
docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "713879da-67a8-49fc-8a2f-22cbf0bbf26c"
}
```

</details>

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_01RztpRmACJdv6Qfy7e32zMy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "767f3a49-c3ed-405f-899d-83755831ea0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 115 · 2026-05-18T19:28:38.678Z_

<details><summary>↩ Tool result · `toolu_01RztpRmACJdv6Qfy7e32zMy`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "99c15ffa-83a7-42a4-b92f-0b5f384ca662"
}
```

</details>

---


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Read · `toolu_012RsBwAn67DqKwqY8ocqWV2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "19b380bb-2f20-4c17-bacf-b9b83490eb86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 117 · 2026-05-18T19:28:39.156Z_

<details><summary>↩ Tool result · `toolu_012RsBwAn67DqKwqY8ocqWV2`</summary>

```text
1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "dd30bccf-0a71-4804-a2a4-ecbc21636f29"
}
```

</details>

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Read · `toolu_01Bbrt4vEZhVMtp4bQonBEFE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a3afd9db-0a25-4963-9639-580d7d1eebd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 17225,
    "tool_uses": 5,
    "duration_ms": 7710
  },
  "last_tool_name": "Read",
  "uuid": "a41fd093-03c0-4e52-865d-cc2913c9781c",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool result

_source line 120 · 2026-05-18T19:28:39.626Z_

<details><summary>↩ Tool result · `toolu_01Bbrt4vEZhVMtp4bQonBEFE`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\cite{alain2017} for functional decodability.
15	
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, our framework validates architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions) due to the causal mask and frozen encoder, while the readout token maintains perfect instruction identity ($100\%$, cross-validated) from L1 onward.
18	\emph{Second}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
19	Convergent causal evidence, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
20	\emph{Third}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
21	Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
22	
23	Our contributions are: (i)~a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, validating architecture-expected specialization as a sanity check; (ii)~convergent causal evidence, from seven independent analyses on OpenVLA-7B/LIBERO, that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub; and (iii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes confirm; CKA diverges), with training primarily enhancing readout-token integration rather than visual geometry.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "bcdb0a49-626d-4ab0-9aaa-f94c5d6df2fb"
}
```

</details>

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_01LJi8DibbWP72qrYRMLhvmN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "30cf04ca-5217-4389-b20b-0e211a2e0d38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 122_

<details open><summary>🔧 Tool call — Agent · `toolu_01J3XcDyN2Ln2q2pdMJDeK2S`</summary>

````json
{
  "description": "LaTeX compilation check",
  "prompt": "You are checking if a LaTeX paper compiles successfully.\n\n## Paper files location\nThe paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nMain file: main.tex\n\n## Task\n1. First, read main.tex to understand the document structure and what packages/files it includes.\n\n2. Check if there's a Makefile in the paper directory.\n\n3. Try to compile the paper locally. Try in this order:\n   a. `latexmk -pdf main.tex` (if latexmk is available)\n   b. `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n   c. If neither works, check what's available with `which latexmk pdflatex xelatex lualatex`\n\n4. If local compilation tools aren't available, check on the remote server:\n   - SSH command: `ssh connect.westd.seetacloud.com`\n   - The paper might also be at /root/vla-ssd/docs/paper/ on the server\n   - Check if LaTeX tools are available there\n\n5. Report ALL warnings and errors from compilation. Focus especially on:\n   - Undefined references\n   - Missing citations\n   - Missing packages\n   - Overfull/underfull hbox warnings (just count, don't list all)\n   - Any other errors\n\n## Output format\nReturn:\n```\n## 编译结果\n\n### 编译环境\n- Tool used: ...\n- Location: local / remote\n\n### Errors (N)\n- ...\n\n### Warnings (N)\n- Undefined references: N\n- Missing citations: N\n- Overfull hbox: N\n- Underfull hbox: N\n- Other: N\n\n### 详细 warning 列表\n(list non-trivial warnings)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "610cd7fb-94c4-439f-9198-85caca0a0736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6G6Scz4QYkvvnEjwh99ZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 754
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


### System

_source line 123_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "LaTeX compilation check",
  "task_type": "local_agent",
  "prompt": "You are checking if a LaTeX paper compiles successfully.\n\n## Paper files location\nThe paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nMain file: main.tex\n\n## Task\n1. First, read main.tex to understand the document structure and what packages/files it includes.\n\n2. Check if there's a Makefile in the paper directory.\n\n3. Try to compile the paper locally. Try in this order:\n   a. `latexmk -pdf main.tex` (if latexmk is available)\n   b. `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n   c. If neither works, check what's available with `which latexmk pdflatex xelatex lualatex`\n\n4. If local compilation tools aren't available, check on the remote server:\n   - SSH command: `ssh connect.westd.seetacloud.com`\n   - The paper might also be at /root/vla-ssd/docs/paper/ on the server\n   - Check if LaTeX tools are available there\n\n5. Report ALL warnings and errors from compilation. Focus especially on:\n   - Undefined references\n   - Missing citations\n   - Missing packages\n   - Overfull/underfull hbox warnings (just count, don't list all)\n   - Any other errors\n\n## Output format\nReturn:\n```\n## 编译结果\n\n### 编译环境\n- Tool used: ...\n- Location: local / remote\n\n### Errors (N)\n- ...\n\n### Warnings (N)\n- Undefined references: N\n- Missing citations: N\n- Overfull hbox: N\n- Underfull hbox: N\n- Other: N\n\n### 详细 warning 列表\n(list non-trivial warnings)\n```",
  "uuid": "0c6ca2f9-1147-4e05-ad1f-16498d5fa9b6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
````

---


### System

_source line 124_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for specific to instruction",
  "usage": {
    "total_tokens": 43276,
    "tool_uses": 14,
    "duration_ms": 16973
  },
  "last_tool_name": "Grep",
  "uuid": "01c331e8-293d-423f-a1d9-edd9a5a7e3f0",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Grep · `toolu_01YXWxa7UEUe9ropP8LNZbzD`</summary>

```json
{
  "pattern": "specific to instruction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7e2739fc-9af1-4a41-aa75-dbb1e3ea4403",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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


## Round 4

## Round 4

222 recorded events


### User

_source line 126 · 2026-05-18T19:28:40.210Z_

You are checking if a LaTeX paper compiles successfully.

## Paper files location
The paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
Main file: main.tex

## Task
1. First, read main.tex to understand the document structure and what packages/files it includes.

2. Check if there's a Makefile in the paper directory.

3. Try to compile the paper locally. Try in this order:
   a. `latexmk -pdf main.tex` (if latexmk is available)
   b. `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
   c. If neither works, check what's available with `which latexmk pdflatex xelatex lualatex`

4. If local compilation tools aren't available, check on the remote server:
   - SSH command: `ssh connect.westd.seetacloud.com`
   - The paper might also be at /root/vla-ssd/docs/paper/ on the server
   - Check if LaTeX tools are available there

5. Report ALL warnings and errors from compilation. Focus especially on:
   - Undefined references
   - Missing citations
   - Missing packages
   - Overfull/underfull hbox warnings (just count, don't list all)
   - Any other errors

## Output format
Return:
```
## 编译结果

### 编译环境
- Tool used: ...
- Location: local / remote

### Errors (N)
- ...

### Warnings (N)
- Undefined references: N
- Missing citations: N
- Overfull hbox: N
- Underfull hbox: N
- Other: N

### 详细 warning 列表
(list non-trivial warnings)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "fa73c8b0-669d-4321-82b4-c0264d26f700"
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-18T19:28:40.095Z_

<details><summary>↩ Tool result · `toolu_01LJi8DibbWP72qrYRMLhvmN`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
17	
18	\paragraph{Behavioral and mechanistic analysis of VLAs.}
19	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
20	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
21	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
22	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
23	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
24	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
25	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
26	
27	\paragraph{Token-level functional specialization in transformers.}
28	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
29	We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
30	
31	\paragraph{Representation similarity and probing methodology.}
32	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
33	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
34	We adopt RSA and MLP probes, with CKA in the appendix.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f42aa9c4-48d7-4f59-a657-47f12c3207a7"
}
```

</details>

---


### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 17296,
    "tool_uses": 6,
    "duration_ms": 8184
  },
  "last_tool_name": "Read",
  "uuid": "ec6ed7f1-5acf-4861-8781-4ed63afa4e03",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — Read · `toolu_018R5xt6obMLDXXLN2tjFQSf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "225275ee-8ab0-4bb0-83c1-a39acf615820",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 130_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Running Inspect registry structure",
  "usage": {
    "total_tokens": 53337,
    "tool_uses": 13,
    "duration_ms": 29373
  },
  "last_tool_name": "Bash",
  "uuid": "4ccbc7dc-4cf1-476e-84e4-25e4a3ff31f2",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 131_

<details open><summary>🔧 Tool call — Bash · `toolu_01K96zV8E7xUicqViHiq4M1t`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\nkeys = list(result.keys())\nprint(\"Top-level keys:\", keys)\nfor k in keys:\n    v = result[k]\n    if isinstance(v, dict):\n        print(f\"\\n{k} has {len(v)} entries: {list(v.keys())[:20]}\")\n    else:\n        print(f\"\\n{k}: {type(v).__name__} = {str(v)[:200]}\")\nPYEOF",
  "description": "Inspect registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7ab058ce-54dd-4e67-8b1e-870c7ee63e71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnB4SJ6mzwzvRHaMTYe932",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 52822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 339,
        "ephemeral_1h_input_tokens": 0
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

_source line 132 · 2026-05-18T19:28:40.251Z_

<details><summary>↩ Tool result · `toolu_01YXWxa7UEUe9ropP8LNZbzD`</summary>

```text
docs/paper/appendix.tex:87:To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
docs/paper/appendix.tex:671:To test whether ablation effects are specific to instruction-dominant heads, we compare ablating the top-24 heads (highest instruction attention fraction, i.e., the instruction-dominant group) against the bottom-24 heads (lowest instruction attention fraction).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "08c073da-fffb-40b3-835f-cb5b54093ca9"
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-18T19:28:40.951Z_

<details><summary>↩ Tool result · `toolu_01K96zV8E7xUicqViHiq4M1t`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']

success: bool = True

data has 4 entries: ['experiments', 'count', 'total', 'baseline']

error: NoneType = None

metadata has 1 entries: ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a1005558-cb23-46d5-bc70-58359b8372ff"
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-18T19:28:40.570Z_

<details><summary>↩ Tool result · `toolu_018R5xt6obMLDXXLN2tjFQSf`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
25	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.
26	Throughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.
27	We cross two factors: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description) in a $2\times 2$ factorial design.
28	
29	%------------------------------------------------------------------
30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to confirm that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}
40	
41	We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42	This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43	
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) confirms neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "316a2174-0737-406c-a511-12d213c9a111"
}
```

</details>

---


### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 17367,
    "tool_uses": 7,
    "duration_ms": 8665
  },
  "last_tool_name": "Read",
  "uuid": "98099311-c96b-4471-b980-60b2f53c98df",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 136_

<details open><summary>🔧 Tool call — Read · `toolu_018sCzMpnWWCxjbvfrjeYffC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "33e84d64-576a-4d5f-954f-e62957257c3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 137 · 2026-05-18T19:28:41.052Z_

<details><summary>↩ Tool result · `toolu_018sCzMpnWWCxjbvfrjeYffC`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confirm this, as does standalone DINOv2 ($10\%$; Appendix~\ref{sec:instruction_invariance_appendix}).
23	
24	\paragraph{Readout token as multimodal hub.}
25	Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
26	The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
27	
28	\begin{table}[t]
29	\centering
30	\caption{Cross-instruction 10-way classification (full in Appendix~\ref{sec:dense_routing}). Image\_mean: chance; readout: $100\%$ from L1 (trained) or decays.}
31	\label{tab:dense_routing_main}
32	\small
33	\begin{tabular}{lccc}
34	\toprule
35	Layer & Trained readout & Untrained readout & Image\_mean \\
36	\midrule
37	L0 & 10.0\% & 10.0\% & 10.0\% \\
38	L1 & 100.0\% & 100.0\% & 10.0\% \\
39	L4 & 100.0\% & 99.1\% & 10.0\% \\
40	L8 & 100.0\% & 95.5\% & 10.0\% \\
41	L16 & 100.0\% & 91.1\% & 10.0\% \\
42	L31 & 100.0\% & 82.0\% & 10.0\% \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	%------------------------------------------------------------------
48	\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}
49	\label{sec:learned_routing}
50	
51	\paragraph{Three-level routing gradient at L1.}
52	L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
53	
54	\paragraph{Redistribution of routing across depth.}
55	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
56	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
57	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\%--70\%; Appendix~\ref{sec:threshold_sensitivity}).
58	
59	\paragraph{Probe robustness confirms the pattern.}
60	Cross-instruction probes (Appendix Figure~\ref{fig:probe_conditions_appendix}) corroborate: VLA-trained achieves $99.6\%$ at L1; Llama-2 base starts at $80.2\%$, saturating by L5; untrained decays from $100\%$ to $82\%$ (L31).
61	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
62	
63	\paragraph{Ablation confirms routing function.}
64	We ablate attention to instruction tokens at the readout position.
65	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
66	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
67	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
68	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
69	
70	\paragraph{Action trajectory validation.}
71	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
72	
73	\paragraph{Dose-response gradient.}
74	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
75	
76	\paragraph{Counterfactual instruction analysis.}
77	To test instruction dependence, we replace the original instruction with four perturbation types.
78	All conditions produce substantial trajectory divergence: empty ($d = 0.968$), wrong task ($d = 0.844$), paraphrased ($d = 0.697$), and shuffled word order ($d = 0.625$; Table~\ref{tab:counterfactual}).
79	The ordering follows semantic distance from the original instruction.
80	L1 ablation ($d = 0.65$) falls between shuffled and paraphrased, consistent with removal of instruction signal rather than injection of noise (Appendix~\ref{sec:action_trajectory}).
81	
82	\begin{table}[t]
83	\centering
84	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
85	\label{tab:routing_gradient}
86	\small
87	\begin{tabular}{lccccc}
88	\toprule
89	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
90	\midrule
91	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
92	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
93	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
101	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
102	\label{fig:attention_profile}
103	\end{figure}
104	
105	%------------------------------------------------------------------
106	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
107	\label{sec:nonmonotonic}
108	
109	\paragraph{Vision encoder provides geometric foundation.}
110	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
111	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
112	
113	\paragraph{Middle-layer peak (metric-dependent).}
114	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
115	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
116	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
117	
118	\paragraph{Training enhances decodability, not geometry.}
119	Best-vs-best RSA gain is non-significant ($\Delta\rho = 0.017$, $3\%$; Appendix Table~\ref{tab:training_effects}); training reshapes \emph{where} geometry peaks rather than \emph{how high}.
120	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
121	The pattern replicates on LIBERO-Spatial ($p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
122	
123	\begin{table}[t]
124	\centering
125	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
126	\label{tab:rsa_overview}
127	\small
128	\begin{tabular}{lcccc}
129	\toprule
130	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
131	\midrule
132	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
133	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
134	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
135	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
136	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
137	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
138	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
139	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
140	\bottomrule
141	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
142	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
143	\end{tabular}
144	\end{table}
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
149	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
150	\label{fig:layer_curves}
151	\end{figure}
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "222f4cd5-b954-4f08-9745-184430cee160"
}
```

</details>

---


### System

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 17438,
    "tool_uses": 8,
    "duration_ms": 9130
  },
  "last_tool_name": "Read",
  "uuid": "19891863-3157-4dfb-a955-4c0468f47f6b",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 139_

<details open><summary>🔧 Tool call — Read · `toolu_01HPLUb3JccJEuYit8XXCQM3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5769f2a3-447c-4d65-8a01-727b54fc01aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for instruction-specific",
  "usage": {
    "total_tokens": 43277,
    "tool_uses": 15,
    "duration_ms": 18360
  },
  "last_tool_name": "Grep",
  "uuid": "5a2e79a6-0554-42c5-92cd-98266a411cf8",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Grep · `toolu_01J4G7FkX4P54puwN3XcUZsP`</summary>

```json
{
  "pattern": "instruction-specific",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3c0645ff-6169-4fa9-ba7a-83616670341c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 142 · 2026-05-18T19:28:41.634Z_

<details><summary>↩ Tool result · `toolu_01J4G7FkX4P54puwN3XcUZsP`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "80306390-6501-44fb-a814-83cee84f310e"
}
```

</details>

---


### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for —",
  "usage": {
    "total_tokens": 43278,
    "tool_uses": 16,
    "duration_ms": 18453
  },
  "last_tool_name": "Grep",
  "uuid": "e2ea8eb4-fd70-4bff-b3df-a0fffda25521",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Grep · `toolu_01VogZtMkDgMVMacSC5w4pSQ`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "652150b7-7311-4ee0-ac12-d8d7384e18c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 145 · 2026-05-18T19:28:41.514Z_

<details><summary>↩ Tool result · `toolu_01HPLUb3JccJEuYit8XXCQM3`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraphrased $>$ shuffled) follows semantic distance, with L1 ablation falling between shuffled and paraphrased, consistent with signal removal rather than noise injection.
20	The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
21	$R^2$ captures linear decodability; action output reflects the full nonlinear pass. The two are complementary.
22	
23	\paragraph{Predictions.}
24	Other decoder-only VLAs (e.g., RT-2) should show similar entry-layer routing given the shared causal-mask constraint; cross-attention architectures (e.g., $\pi_0$) should differ.
25	L1 ablation should produce measurable task degradation on instruction-discriminative tasks.
26	
27	\paragraph{Limitations and scope.}
28	We study OpenVLA-7B on LIBERO; C1 follows from shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0}, but C2 may differ across backbone scales and decoder paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
29	Our analyses are representational and open-loop; closed-loop evaluation is future work.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "83522fca-69e2-434b-afed-00c31c05bdf7"
}
```

</details>

---


### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 17509,
    "tool_uses": 9,
    "duration_ms": 9560
  },
  "last_tool_name": "Read",
  "uuid": "c768cac5-4879-4e39-a2f3-c4b970fe2ab8",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Read · `toolu_016jBfAvPzKVgf14NjurdwnQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "35fc544d-744f-40fe-88b6-0ce20747fe2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 148 · 2026-05-18T19:28:41.944Z_

<details><summary>↩ Tool result · `toolu_016jBfAvPzKVgf14NjurdwnQ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3ebe9106-4b56-4ac2-a32d-36fe00c840ab"
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-18T19:28:41.730Z_

<details><summary>↩ Tool result · `toolu_01VogZtMkDgMVMacSC5w4pSQ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5a1d2701-19cd-4303-8364-dd1d092d2889"
}
```

</details>

---


### System

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for  – ",
  "usage": {
    "total_tokens": 43279,
    "tool_uses": 17,
    "duration_ms": 19328
  },
  "last_tool_name": "Grep",
  "uuid": "81c5fb96-ddfc-456e-b5b3-57f82103adb0",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 151_

<details open><summary>🔧 Tool call — Grep · `toolu_01QwdHtQJ7Ysk4T8mNw4Lw2Q`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b6bf4357-a343-4f6e-be7f-3432af7be0d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 17580,
    "tool_uses": 10,
    "duration_ms": 10537
  },
  "last_tool_name": "Read",
  "uuid": "87924924-5cf6-4290-b2c3-21518bbb4f2c",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Read · `toolu_01FsoGT8L1d8TS13JeqeQ6nQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f34cce84-e9bf-4273-aca2-4097ed8d8b17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 17651,
    "tool_uses": 11,
    "duration_ms": 10703
  },
  "last_tool_name": "Read",
  "uuid": "94191cd8-6bc6-4319-88de-f382cb10a3cd",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 155_

<details open><summary>🔧 Tool call — Read · `toolu_01EfQA47oRxYT5cZQaZytMiq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "803f9799-7479-47c7-95b4-047ae55e3b07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRrP6Q5A7S5fyJtR8n37qR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 15874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 156 · 2026-05-18T19:28:42.599Z_

<details><summary>↩ Tool result · `toolu_01QwdHtQJ7Ysk4T8mNw4Lw2Q`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1798bd97-e652-40db-87d7-e18cfe55cb72"
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-18T19:28:43.087Z_

<details><summary>↩ Tool result · `toolu_01EfQA47oRxYT5cZQaZytMiq`</summary>

```text
1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},
38	  journal   = {Frontiers in Systems Neuroscience},
39	  volume    = {2},
40	  pages     = {4},
41	  year      = {2008},
42	  publisher = {Frontiers},
43	}
44	
45	@inproceedings{kornblith2019,
46	  title     = {Similarity of Neural Network Representations Revisited},
47	  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
48	  booktitle = {International Conference on Machine Learning (ICML)},
49	  year      = {2019},
50	}
51	
52	@inproceedings{alain2017,
53	  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},
54	  author    = {Alain, Guillaume and Bengio, Yoshua},
55	  booktitle = {International Conference on Learning Representations (ICLR), Workshop Track},
56	  year      = {2017},
57	}
58	
59	% === Vision Encoders ===
60	
61	@inproceedings{zhai2023_siglip,
62	  title     = {Sigmoid Loss for Language Image Pre-Training},
63	  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
64	  booktitle = {International Conference on Computer Vision (ICCV)},
65	  year      = {2023},
66	}
67	
68	@article{oquab2024_dinov2,
69	  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},
70	  author    = {Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},
71	  journal   = {Transactions on Machine Learning Research (TMLR)},
72	  year      = {2024},
73	}
74	
75	@inproceedings{radford2021_clip,
76	  title     = {Learning Transferable Visual Models From Natural Language Supervision},
77	  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},
78	  booktitle = {International Conference on Machine Learning (ICML)},
79	  year      = {2021},
80	}
81	
82	% === Domain-Specific ===
83	
84	@article{grant2026,
85	  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},
86	  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},
87	  journal   = {arXiv preprint arXiv:2603.19233},
88	  year      = {2026},
89	}
90	
91	@article{haon2025,
92	  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},
93	  author    = {H{\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},
94	  journal   = {arXiv preprint arXiv:2509.00328},
95	  year      = {2025},
96	}
97	
98	% === Behavioral Analysis of VLAs ===
99	
100	@article{hou2026,
101	  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
102	  author    = {Hou, Yuchen and Zhao, Lin},
103	  journal   = {arXiv preprint arXiv:2603.00592},
104	  year      = {2026},
105	}
106	
107	@article{fei2025,
108	  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},
109	  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},
110	  journal   = {arXiv preprint arXiv:2510.13626},
111	  year      = {2025},
112	}
113	
114	% === Mechanistic Interpretability of VLAs ===
115	
116	@article{swann2026,
117	  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
118	  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},
119	  journal   = {arXiv preprint arXiv:2603.19183},
120	  year      = {2026},
121	}
122	
123	@article{buurmeijer2026,
124	  title     = {Observing and Controlling Features in Vision-Language-Action Models},
125	  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
126	  journal   = {arXiv preprint arXiv:2603.05487},
127	  year      = {2026},
128	}
129	
130	@article{lu2025,
131	  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},
132	  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},
133	  journal   = {arXiv preprint arXiv:2502.04558},
134	  year      = {2025},
135	}
136	
137	@article{molinari2025,
138	  title     = {Emergent World Representations in {OpenVLA}},
139	  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},
140	  journal   = {arXiv preprint arXiv:2509.24559},
141	  year      = {2025},
142	}
143	
144	% === Probing Methods ===
145	
146	@article{belinkov2022,
147	  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},
148	  author    = {Belinkov, Yonatan},
149	  journal   = {Computational Linguistics},
150	  volume    = {48},
151	  number    = {1},
152	  pages     = {207--219},
153	  year      = {2022},
154	}
155	
156	% === Causal Tracing and Per-Layer Analysis ===
157	
158	@inproceedings{meng2022_rome,
159	  title     = {Locating and Editing Factual Associations in {GPT}},
160	  author    = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},
161	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
162	  year      = {2022},
163	}
164	
165	@article{belrose2023_tunedlens,
166	  title     = {Eliciting Latent Predictions from Transformers with the Tuned Lens},
167	  author    = {Belrose, Nora and Furman, Zach and Smith, Logan and Biderman, Stella and Steinhardt, Jacob and Frankle, Jonathan},
168	  journal   = {arXiv preprint arXiv:2303.08112},
169	  year      = {2023},
170	}
171	
172	% === Mechanistic Interpretability in Transformers ===
173	
174	@article{elhage2021,
175	  title     = {A Mathematical Framework for Transformer Circuits},
176	  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
177	  journal   = {Transformer Circuits Thread},
178	  year      = {2021},
179	  url       = {https://transformer-circuits.pub/2021/framework/index.html},
180	}
181	
182	@article{olsson2022,
183	  title     = {In-context Learning and Induction Heads},
184	  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
185	  journal   = {arXiv preprint arXiv:2209.11895},
186	  year      = {2022},
187	}
188	
189	@inproceedings{wang2023_ioi,
190	  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},
191	  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},
192	  booktitle = {International Conference on Learning Representations (ICLR)},
193	  year      = {2023},
194	}
195	
196	@inproceedings{conmy2023,
197	  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},
198	  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\`a}},
199	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
200	  year      = {2023},
201	}
202	
203	% === Attention Analysis ===
204	
205	@inproceedings{clark2019,
206	  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},
207	  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
208	  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},
209	  year      = {2019},
210	}
211	
212	@inproceedings{vig2019,
213	  title     = {Analyzing the Structure of Attention in a Transformer Language Model},
214	  author    = {Vig, Jesse and Belinkov, Yonatan},
215	  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},
216	  year      = {2019},
217	}
218	
219	@inproceedings{voita2019,
220	  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
221	  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
222	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
223	  year      = {2019},
224	}
225	
226	% === Token-Level Functional Specialization ===
227	
228	@inproceedings{dosovitskiy2021,
229	  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
230	  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},
231	  booktitle = {International Conference on Learning Representations (ICLR)},
232	  year      = {2021},
233	}
234	
235	@inproceedings{darcet2024,
236	  title     = {Vision Transformers Need Registers},
237	  author    = {Darcet, Timoth{\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},
238	  booktitle = {International Conference on Learning Representations (ICLR)},
239	  year      = {2024},
240	}
241	
242	@inproceedings{geva2021,
243	  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},
244	  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},
245	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
246	  year      = {2021},
247	}
248	
249	@inproceedings{tenney2019,
250	  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},
251	  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},
252	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
253	  year      = {2019},
254	}
255	
256	% === Representation Similarity Methods ===
257	
258	@inproceedings{raghu2017,
259	  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},
260	  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},
261	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
262	  year      = {2017},
263	}
264	
265	@inproceedings{morcos2018,
266	  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},
267	  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},
268	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
269	  year      = {2018},
270	}
271	
272	@inproceedings{hewitt2019,
273	  title     = {A Structural Probe for Finding Syntax in Word Representations},
274	  author    = {Hewitt, John and Manning, Christopher D.},
275	  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},
276	  year      = {2019},
277	}
278	
279	% === VLM Token-Level Analysis ===
280	
281	@inproceedings{neo2025,
282	  title     = {Towards Understanding Multi-Task Learning (Generalization) of {LLMs} via Detecting and Exploring Task-Specific Neurons},
283	  author    = {Neo, Yifan and Wu, Jingcheng and Hooi, Bryan},
284	  booktitle = {International Conference on Learning Representations (ICLR)},
285	  year      = {2025},
286	}
287	
288	% === Representation Similarity (ViT) ===
289	
290	@inproceedings{raghu2021,
291	  title     = {Do Vision Transformers See Like Convolutional Neural Networks?},
292	  author    = {Raghu, Maithra and Unterthiner, Thomas and Kornblith, Simon and Zhang, Chiyuan and Dosovitskiy, Alexey},
293	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
294	  year      = {2021},
295	}
296	
297	% === Probe Methodology ===
298	
299	@inproceedings{hewitt2019control,
300	  title     = {Designing and Interpreting Probes with Control Tasks},
301	  author    = {Hewitt, John and Liang, Percy},
302	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
303	  pages     = {2733--2743},
304	  year      = {2019},
305	  doi       = {10.18653/v1/D19-1275},
306	}
307	
308	% === RSA Toolbox ===
309	
310	@article{nili2014toolbox,
311	  title     = {A Toolbox for Representational Similarity Analysis},
312	  author    = {Nili, Hamed and Wingfield, Cai and Walther, Alexander and Su, Li and Marslen-Wilson, William and Kriegeskorte, Nikolaus},
313	  journal   = {PLoS Computational Biology},
314	  volume    = {10},
315	  number    = {4},
316	  pages     = {e1003553},
317	  year      = {2014},
318	  doi       = {10.1371/journal.pcbi.1003553},
319	}
320	
321	% === Mechanistic Interpretability ===
322	
323	@misc{bills2023language,
324	  title     = {Language Models Can Explain Neurons in Language Models},
325	  author    = {Bills, Steven and Cammarata, Nick and Mossing, Dan and Tillman, Henk and Gao, Leo and Goh, Gabriel and Sutskever, Ilya and Leike, Jan and Wu, Jeff and Saunders, William},
326	  year      = {2023},
327	  howpublished = {OpenAI Blog},
328	  url       = {https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html},
329	}
330	
331	@article{templeton2024scaling,
332	  title     = {Scaling Monosemanticity: Extracting Interpretable Features from {C}laude 3 {S}onnet},
333	  author    = {Templeton, Adly and Conerly, Tom and Marcus, Jonathan and Lindsey, Jack and Bricken, Trenton and Chen, Brian and Pearce, Adam and Citro, Craig and Ameisen, Emmanuel and Jones, Andy and others},
334	  journal   = {Transformer Circuits Thread},
335	  year      = {2024},
336	  url       = {https://transformer-circuits.pub/2024/scaling-monosemanticity/},
337	}
338	
339	% === LLM Internal Probing ===
340	
341	@misc{nostalgebraist2020,
342	  title     = {interpreting {GPT}: the logit lens},
343	  author    = {nostalgebraist},
344	  year      = {2020},
345	  howpublished = {LessWrong blog post},
346	  url       = {https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens},
347	  note      = {Accessed: 2026-05-18},
348	}
349	
350	% === VLA Fine-tuning and Reasoning ===
351	
352	@article{fang2025,
353	  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},
354	  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},
355	  journal   = {arXiv preprint arXiv:2511.22134},
356	  year      = {2025},
357	}
358	
359	% === LLM Backbone ===
360	
361	@article{touvron2023_llama2,
362	  title     = {{Llama} 2: Open Foundation and Fine-Tuned Chat Models},
363	  author    = {Touvron, Hugo and Martin, Louis and Stone, Kevin and Albert, Peter and Almahairi, Amjad and Babaei, Yasmine and Bashlykov, Nikolay and Batra, Soumya and Bhargava, Prajjwal and Bhosale, Shruti and others},
364	  journal   = {arXiv preprint arXiv:2307.09288},
365	  year      = {2023},
366	}
367	
368	% === Dataset ===
369	
370	@article{padalkar2023_oxe,
371	  title     = {Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
372	  author    = {Padalkar, Abhishek and Poolber, Acorn and Bewley, Ajinkya and others},
373	  journal   = {arXiv preprint arXiv:2310.08864},
374	  year      = {2023},
375	}
376	
377	% === VLA Foundation Models ===
378	
379	@article{black2024_pi0,
380	  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
381	  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},
382	  journal   = {arXiv preprint arXiv:2410.24164},
383	  year      = {2024},
384	}
385	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "10152f9d-7436-415f-868b-9191f1a3a8e3"
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-18T19:28:43.248Z_

<details><summary>↩ Tool result · `toolu_01FsoGT8L1d8TS13JeqeQ6nQ`</summary>

```text
1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures rank-order geometric alignment; CKA captures global linear structure.
27	The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
32	\caption{Three similarity metrics across representation sources. \textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}
33	\label{fig:metric_comparison}
34	\end{figure}
35	
36	\subsection{Branch-Split Detailed Analysis}
37	\label{sec:branch_split_appendix}
38	
39	To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.
40	The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
41	Fusion produces a representation ($\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.
42	The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\rho = 0.615$, a drop of $\Delta = 0.019$ from the fused 2{,}176-D input.
43	
44	\subsection{RSA Across Representation Sources}
45	\label{sec:rsa_bar_appendix}
46	
47	Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
48	
49	\begin{figure}[h]
50	\centering
51	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
52	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 \texttt{cls\_token} ($\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\% bootstrap CIs.}
53	\label{fig:rsa_bar}
54	\end{figure}
55	
56	\subsection{Per-Layer RSA Profiles}
57	\label{sec:rsa_perlayer_appendix}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}
62	\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
63	\label{fig:rsa_perlayer_curve}
64	\end{figure}
65	
66	\subsection{Per-Layer Action Decoding Across Training Stages}
67	\label{sec:action_r2_threecond}
68	
69	Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
70	All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
71	The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
72	Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
73	The untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability confirms that randomly initialized Transformer layers produce destructive interference on action-relevant structure.
74	The three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.
75	The qualitative pattern is consistent across all 3 seeds.
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_action_r2_threecond.pdf}
80	\caption{Per-layer action probe $R^2$ (image\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\pm$ std).}
81	\label{fig:action_r2_threecond}
82	\end{figure}
83	
84	\subsection{Random-Subset Ablation Details}
85	\label{sec:random_subset_ablation}
86	
87	To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
88	Dominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \pm 0.013$.
89	The dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); instruction-dominant heads are thus specialized for routing rather than general-purpose computation.
90	
91	\begin{figure}[h]
92	\centering
93	\includegraphics[width=0.75\columnwidth]{figures/fig_random_subset_ablation.pdf}
94	\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with routing-first specialization of instruction-dominant heads.}
95	\label{fig:random_subset_ablation}
96	\end{figure}
97	
98	\subsection{Action Trajectory Analysis Details}
99	\label{sec:action_trajectory}
100	
101	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
102	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
103	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
104	
105	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
106	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
107	
108	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
109	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.
110	The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
111	
112	\begin{table}[h]
113	\centering
114	\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
115	\label{tab:perhead_bootstrap}
116	\small
117	\begin{tabular}{lccc}
118	\toprule
119	Group & $N$ heads & Collective $d$ & Per-head $d$ [95\% CI] \\
120	\midrule
121	Instruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\
122	Control & 8 & 0.41 & 0.051 [0.048, 0.055] \\
123	\midrule
124	Difference & --- & --- & 0.024, $p = 0.0018$ \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
130	
131	Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
132	Trajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\Delta d / \Delta 4 \approx 0.026$), a plateau at 16--20 heads ($\Delta d = 0.001$), and slow increase at 20--32.
133	
134	\begin{figure}[h]
135	\centering
136	\includegraphics[width=0.75\columnwidth]{figures/fig_dose_response.pdf}
137	\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}
138	\label{fig:dose_response}
139	\end{figure}
140	
141	\begin{table}[h]
142	\centering
143	\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\ original action sequence; 95\% bootstrap CIs ($10{,}000$ resamples).}
144	\label{tab:dose_response}
145	\small
146	\begin{tabular}{rcc}
147	\toprule
148	Heads ablated & Cohen's $d$ & 95\% CI \\
149	\midrule
150	4 & 0.482 & [0.449, 0.511] \\
151	8 & 0.508 & [0.479, 0.541] \\
152	12 & 0.560 & [0.529, 0.593] \\
153	16 & 0.592 & [0.559, 0.625] \\
154	20 & 0.593 & [0.559, 0.627] \\
155	24 & 0.611 & [0.578, 0.645] \\
156	28 & 0.619 & [0.587, 0.654] \\
157	32 & 0.639 & [0.603, 0.671] \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	\begin{table}[h]
163	\centering
164	\caption{Counterfactual instruction analysis. Cohen's $d$ and token divergence (\%) relative to original instruction. L1 ablation ($d = 0.65$) included for comparison. The ordering follows semantic distance from the original instruction.}
165	\label{tab:counterfactual}
166	\small
167	\begin{tabular}{lcc}
168	\toprule
169	Condition & Cohen's $d$ & Token div.\ (\%) \\
170	\midrule
171	Empty (no instruction) & 0.968 & 90.7 \\
172	Wrong (different task) & 0.844 & 89.5 \\
173	Paraphrased & 0.697 & 82.6 \\
174	Shuffled (random order) & 0.625 & 85.7 \\
175	\midrule
176	L1 ablation (24 heads) & 0.650 & 72.3 \\
177	\bottomrule
178	\end{tabular}
179	\end{table}
180	
181	\begin{table}[h]
182	\centering
183	\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}
184	\label{tab:action_shift_perdim}
185	\small
186	\begin{tabular}{lccccccc}
187	\toprule
188	Condition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\
189	\midrule
190	Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
191	Control (8) & --- & --- & --- & --- & --- & --- & 0.141 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\subsection{Pretrained LLM Representation Quality Under Visual Input}
197	\label{sec:ood_diagnostics}
198	
199	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
200	We evaluate three diagnostics to assess representation quality.
201	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
202	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, reflecting gradual differentiation rather than catastrophic out-of-distribution behavior.
203	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
204	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
205	
206	\begin{figure}[h]
207	\centering
208	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
209	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics confirm structured, non-degenerate representations.}
210	\label{fig:ood_diagnostics}
211	\end{figure}
212	
213	\subsection{Probe Architecture Sensitivity}
214	\label{sec:linear_probe}
215	
216	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \to 7$, $N/\text{params} \approx 2.2$).
217	The inverted-U pattern reproduces: trained image\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).
218	The trained--untrained gap is larger under the linear probe (L14: $\Delta = +0.324$) than the MLP probe (L8: $\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.
219	Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
220	For last\_preaction tokens, the linear probe also confirms the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\Delta = 0.103$ ($p < 0.001$).
221	These results confirm that our qualitative findings reflect representational structure rather than probe capacity artifacts.
222	
223	\begin{figure}[h]
224	\centering
225	\includegraphics[width=\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}
226	\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}
227	\label{fig:linear_vs_mlp}
228	\end{figure}
229	
230	\subsection{Functional Probe Comparison}
231	\label{sec:probe_bars_appendix}
232	
233	Figure~\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.
234	
235	\begin{figure}[h]
236	\centering
237	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
238	\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
239	\label{fig:probe_bars}
240	\end{figure}
241	
242	\subsection{Training Effect and Instruction Invariance}
243	\label{sec:instruction_invariance_appendix}
244	
245	Figure~\ref{fig:factorial} shows trained vs.\ untrained RSA profiles and instruction invariance.
246	Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
247	
248	\begin{figure}[h]
249	\centering
250	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
251	\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$, confirming visually grounded action geometry.}
252	\label{fig:factorial}
253	\end{figure}
254	
255	\subsection{Additional RSA Values}
256	\label{sec:additional_rsa}
257	
258	DINOv2 \texttt{patch\_mean} achieves RSA $\rho = 0.631$, between the \texttt{cls\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).
259	VLA untrained readout peaks at L1 ($\rho = 0.626$).
260	
261	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
262	\label{sec:cross_benchmark_appendix}
263	
264	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).
265	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
266	
267	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
268	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero) and confirming that the n.s.\ result on Goal reflects limited statistical power.
269	
270	Two notable differences emerge.
271	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
272	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
273	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
274	
275	\begin{figure}[t]
276	\centering
277	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
278	\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
279	\label{fig:cross_benchmark}
280	\end{figure}
281	
282	\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}
283	\label{sec:spatial_cross_instruction}
284	
285	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
286	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
287	The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
288	
289	\begin{table}[h]
290	\centering
291	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\ Table~\ref{tab:dense_routing_main}).}
292	\label{tab:spatial_cross_instruction}
293	\small
294	\begin{tabular}{llccccc}
295	\toprule
296	Token & Condition & L1 & L4 & L8 & L16 & L31 \\
297	\midrule
298	last\_preaction & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
299	last\_preaction & Untrained & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
300	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
301	image\_mean & Untrained & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
302	\bottomrule
303	\end{tabular}
304	\end{table}
305	
306	\subsection{Robustness Analyses}
307	\label{sec:robustness_appendix}
308	
309	\subsubsection{Distance Metric Invariance}
310	\label{sec:metric_invariance}
311	
312	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
313	
314	\begin{table}[h]
315	\centering
316	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
317	\label{tab:metric_invariance}
318	\small
319	\begin{tabular}{lccc}
320	\toprule
321	Condition & Eucl.\ Peak & Cos.\ Peak & Profile $r$ \\
322	\midrule
323	Trained image\_mean & L12 & L12 & 0.990 \\
324	Trained last\_preaction & L12 & L13 & 0.990 \\
325	Untrained image\_mean & L0 & L0 & 0.995 \\
326	Untrained last\_preaction & L1 & L1 & 0.992 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	\subsubsection{Per-DOF Decomposition}
332	\label{sec:perdof}
333	
334	RSA decomposition by action dimension confirms the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\rho = 0.193$), rotation (peak L12, $\rho = 0.175$), and gripper (peak L13, $\rho = 0.106$) all exhibit non-monotonic profiles.
335	Per-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.
336	
337	\subsubsection{Permutation Test}
338	\label{sec:permutation}
339	
340	Permutation testing (1{,}000 shuffles) confirms all observed RSA values are highly significant: observed $\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).
341	
342	\subsubsection{Probe Seed Sensitivity}
343	\label{sec:seed_sensitivity}
344	
345	Action probe $R^2$ is highly stable across random seeds.
346	Over 5 seeds (trained image\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\%$ ($0.655 \pm 0.002$; Table~\ref{tab:seed_sensitivity}).
347	Peak layer concentrates in the L8--L10 region ($4/5$ seeds), confirming the inverted-U shape is not a seed artifact.
348	Seed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.
349	
350	\begin{table}[h]
351	\centering
352	\caption{Probe $R^2$ peak across 5 random seeds (trained image\_mean).}
353	\label{tab:seed_sensitivity}
354	\small
355	\begin{tabular}{lcc}
356	\toprule
357	Seed & Peak Layer & Peak $R^2$ \\
358	\midrule
359	0 & L9 & 0.654 \\
360	1 & L16 & 0.656 \\
361	2 & L9 & 0.653 \\
362	3 & L10 & 0.655 \\
363	42 & L9 & 0.655 \\
364	\midrule
365	Mean$\pm$std & $10.6\pm2.7$ & $0.655\pm0.002$ \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	\subsubsection{Demonstration Subsample Sensitivity}
371	\label{sec:demo_sensitivity}
372	
373	To verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\ref{tab:demo_sensitivity}).
374	The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions, confirming high stability.
375	The probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$, reflecting greater sensitivity of $R^2$ to training set size.
376	Both metrics show reduced absolute values (RSA $-3.6\%$, $R^2$ $-7.6\%$) as expected from halved data, but the non-monotonic profile shape is preserved.
377	
378	\begin{table}[h]
379	\centering
380	\caption{Inverted-U stability under demonstration subsampling (trained image\_mean).}
381	\label{tab:demo_sensitivity}
382	\small
383	\begin{tabular}{lccc}
384	\toprule
385	Metric & 50 demos & 25 demos & $\Delta$ \\
386	\midrule
387	RSA peak layer & L12 & L12 & 0 \\
388	RSA peak $\rho$ & 0.628 & 0.606 & $-3.6\%$ \\
389	$R^2$ peak layer & L9 & L11 & $+2$ \\
390	$R^2$ peak value & 0.659 & 0.609 & $-7.6\%$ \\
391	RSA profile $r$ & --- & 0.970 & --- \\
392	$R^2$ profile $r$ & --- & 0.819 & --- \\
393	\bottomrule
394	\end{tabular}
395	\end{table}
396	
397	\subsection{Detailed Training Effects}
398	\label{sec:training_effects_appendix}
399	
400	Table~\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.
401	
402	\begin{table}[h]
403	\centering
404	\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\Delta{=}+0.017$, $3\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}
405	\label{tab:training_effects}
406	\small
407	\begin{tabular}{lccc}
408	\toprule
409	Comparison & $\Delta$ & 95\% CI & $p$ \\
410	\midrule
411	\multicolumn{4}{l}{\emph{RSA ($\rho$)}} \\
412	Best-vs-best image\_mean & $+$0.017 & incl.\ 0 & n.s. \\
413	\quad (trained L12 vs.\ untrained L0) & & & \\
414	Same-layer L12 image\_mean & $+$0.079 & excl.\ 0 & $<$0.0001 \\
415	\quad (trained vs.\ untrained) & & & \\
416	Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
417	\midrule
418	\multicolumn{4}{l}{\emph{Probe $R^2$}} \\
419	Best-vs-best image\_mean & $+$0.015 & excl.\ 0 & 0.006 \\
420	\quad (trained L8 vs.\ untrained L0) & & & \\
421	Best-vs-best readout & $+$0.069 & excl.\ 0 & $<$0.0001 \\
422	\quad (trained L13 vs.\ untrained L32) & & & \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	\subsection{Training Effect Size Summary}
428	\label{sec:training_effect_summary}
429	
430	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
431	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on last\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
432	This asymmetry confirms that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
433	
434	\begin{table}[h]
435	\centering
436	\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large, confirming that training targets readout-token information integration.}
437	\label{tab:training_effect_summary}
438	\small
439	\begin{tabular}{lccc}
440	\toprule
441	Metric & Trained & Untrained & $\Delta$ \\
442	\midrule
443	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
444	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
445	$R^2$ peak (last\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
446	Instruction routing L31 & 100\% & 82\% & $+$18pp \\
447	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
448	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	\subsection{Instruction Routing Probes}
454	\label{sec:routing_appendix}
455	
456	\subsubsection{Cross-Instruction Classification: Dense Layer Profile}
457	\label{sec:dense_routing}
458	
459	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
460	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
461	Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
462	
463	\begin{table}[h]
464	\centering
465	\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8.}
466	\label{tab:dense_routing}
467	\small
468	\begin{tabular}{lccc}
469	\toprule
470	Layer & Trained & Untrained & Image\_mean (trained) \\
471	\midrule
472	L0 & 10.0\% & 10.0\% & 10.0\% \\
473	L1 & 100.0\% & 100.0\% & 10.0\% \\
474	L2 & 100.0\% & 99.6\% & 10.0\% \\
475	L3 & 100.0\% & 99.6\% & 10.0\% \\
476	L4 & 100.0\% & 99.1\% & 10.0\% \\
477	L5 & 100.0\% & 98.2\% & 10.0\% \\
478	L6 & 100.0\% & 97.3\% & 10.0\% \\
479	L7 & 100.0\% & 96.4\% & 10.0\% \\
480	L8 & 100.0\% & 95.5\% & 10.0\% \\
481	\bottomrule
482	\end{tabular}
483	\end{table}
484	
485	\subsubsection{Cross-Instruction LOOCV Validation}
486	\label{sec:loocv}
487	
488	Leave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) confirms the cross-instruction probe result is not driven by memorization.
489	Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31, confirming perfect generalization.
490	
491	\subsubsection{QA Probe: Progress and Subtask Classification}
492	\label{sec:qa_probe}
493	
494	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\ref{tab:qa_probe}).
495	
496	\begin{table}[h]
497	\centering
498	\caption{QA probe accuracy (progress + subtask classification, best layer).}
499	\label{tab:qa_probe}
500	\small
501	\begin{tabular}{lcc}
502	\toprule
503	Source & Best Layer & Accuracy \\
504	\midrule
505	Trained last\_preaction & L20 & 86.3\% \\
506	Untrained last\_preaction & L20 & 85.3\% \\
507	DINOv2 cls\_token & --- & 82.7\% \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	\subsubsection{Cross-Instruction Probe Profiles}
513	\label{sec:probe_profiles}
514	
515	\begin{figure}[h]
516	\centering
517	\includegraphics[width=\columnwidth]{figures/fig_probe_conditions.pdf}
518	\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\%$ at L1, saturating to $100\%$. Llama-2 base starts at $80.2\%$, reaching $100\%$ by L5. Untrained starts at $100\%$ but decays to $82\%$ by L31.}
519	\label{fig:probe_conditions_appendix}
520	\end{figure}
521	
522	\subsubsection{L1 Attention Pattern Analysis}
523	\label{sec:attention_pattern}
524	
525	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
526	The three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.
527	
528	\begin{figure}[h]
529	\centering
530	\includegraphics[width=\columnwidth]{figures/fig_l1_stacked_bar.pdf}
531	\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\%$ text attention). Llama-2 base: 9/32 heads ($36.5\%$). Untrained: 0/32 heads ($11.7\%$). See Table~\ref{tab:routing_gradient} for quantitative comparison.}
532	\label{fig:attention_appendix}
533	\end{figure}
534	
535	\subsubsection{Multi-Layer Attention Patterns}
536	\label{sec:multilayer_attention}
537	
538	Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
539	The full profile confirms three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
540	
541	\begin{figure}[h]
542	\centering
543	\includegraphics[width=\columnwidth]{figures/fig_multi_layer_attn.pdf}
544	\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}
545	\label{fig:multilayer_attention}
546	\end{figure}
547	
548	\begin{table}[h]
549	\centering
550	\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
551	\label{tab:multilayer_attention}
552	\small
553	\begin{tabular}{lcccccc}
554	\toprule
555	 & \multicolumn{2}{c}{VLA Trained} & \multicolumn{2}{c}{Llama-2 base} & \multicolumn{2}{c}{Untrained} \\
556	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
557	Layer & Heads & Text\% & Heads & Text\% & Heads & Text\% \\
558	\midrule
559	L1 & \textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\
560	L8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\
561	L16 & 10/32 & 48.4 & \textbf{25/32} & 60.2 & 0/32 & 9.2 \\
562	L31 & \textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\subsubsection{Threshold Sensitivity Analysis}
568	\label{sec:threshold_sensitivity}
569	
570	The main text defines instruction-dominant heads as those allocating $>50\%$ attention to instruction tokens.
571	Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%, confirming that the 50\% threshold is not a boundary-sensitive choice.
572	
573	\begin{table}[h]
574	\centering
575	\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}
576	\label{tab:threshold_sensitivity}
577	\small
578	\begin{tabular}{lccc}
579	\toprule
580	Threshold & VLA Trained & Llama-2 base & Untrained \\
581	\midrule
582	30\% & 32 & 13 & 0 \\
583	40\% & 31 & 10 & 0 \\
584	50\% & 24 & 9 & 0 \\
585	60\% & 9 & 4 & 0 \\
586	70\% & 5 & 3 & 0 \\
587	\bottomrule
588	\end{tabular}
589	\end{table}
590	
591	\subsection{L1 Attention Decomposition by Head Group}
592	\label{sec:attention_decomp}
593	
594	Table~\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.
595	
596	\begin{table}[h]
597	\centering
598	\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}
599	\label{tab:attention_decomp}
600	\small
601	\begin{tabular}{lcccc}
602	\toprule
603	Head Group & $N$ & Instruction & Vision & BOS/Other \\
604	\midrule
605	Instruction-dominant & 24 & 62.4\% & 18.8\% & 18.8\% \\
606	Control & 8 & 44.9\% & 27.1\% & 28.0\% \\
607	\midrule
608	$\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\
609	\bottomrule
610	\end{tabular}
611	\end{table}
612	
613	\subsection{Per-Dimension Action MAE Under Head Ablation}
614	\label{sec:per_dim_mae}
615	
616	Table~\ref{tab:per_dim_mae} extends Table~\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.
617	
618	\begin{table}[h]
619	\centering
620	\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$), indicating instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
621	\label{tab:per_dim_mae}
622	\small
623	\begin{tabular}{lccc}
624	\toprule
625	Dimension & Instr.\ 24h MAE & Control 8h MAE & Ratio \\
626	\midrule
627	$dx$ & 0.00189 & 0.00037 & 5.09$\times$ \\
628	$dy$ & 0.00531 & 0.00125 & 4.26$\times$ \\
629	$dz$ & 0.00762 & 0.00243 & 3.14$\times$ \\
630	$roll$ & 0.02059 & 0.00785 & 2.62$\times$ \\
631	$pitch$ & 0.03071 & 0.01387 & 2.21$\times$ \\
632	$yaw$ & 0.03388 & 0.01783 & 1.90$\times$ \\
633	$gripper$ & 0.29072 & 0.14072 & 2.07$\times$ \\
634	\bottomrule
635	\end{tabular}
636	\end{table}
637	
638	\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
639	\label{sec:per_task_r2}
640	
641	Table~\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).
642	
643	\begin{table}[h]
644	\centering
645	\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$), confirming that instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
646	\label{tab:per_task_r2}
647	\small
648	\begin{tabular}{lccc}
649	\toprule
650	Task & Baseline $R^2$ & Ablated $R^2$ & $\Delta R^2$ \\
651	\midrule
652	open middle drawer & 0.197 & 0.221 & $+$0.024 \\
653	open top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\
654	push plate to stove & 0.190 & 0.197 & $+$0.007 \\
655	put bowl on plate & 0.375 & 0.474 & $+$0.099 \\
656	put bowl on stove & 0.235 & 0.395 & $+$0.160 \\
657	put bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\
658	put cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\
659	put wine on rack & 0.189 & 0.424 & $+$0.235 \\
660	put wine on cabinet & 0.279 & 0.353 & $+$0.074 \\
661	turn on stove & 0.385 & 0.421 & $+$0.036 \\
662	\midrule
663	Mean $\pm$ std & $0.256 \pm 0.070$ & $0.363 \pm 0.088$ & $+$0.107 \\
664	\bottomrule
665	\end{tabular}
666	\end{table}
667	
668	\subsection{Specificity Control: Top-24 vs.\ Bottom-24 Head Ablation}
669	\label{sec:specificity_control}
670	
671	To test whether ablation effects are specific to instruction-dominant heads, we compare ablating the top-24 heads (highest instruction attention fraction, i.e., the instruction-dominant group) against the bottom-24 heads (lowest instruction attention fraction).
672	The two groups overlap on 16 heads and differ only on the top-8 vs.\ bottom-8 extremes.
673	
674	\begin{table}[h]
675	\centering
676	\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
677	\label{tab:specificity_control}
678	\small
679	\begin{tabular}{lccc}
680	\toprule
681	Metric & Top-24 & Bottom-24 & Ratio \\
682	\midrule
683	Cohen's $d$ & 0.650 & 0.565 & $1.15\times$ \\
684	KL divergence & 6.50 & 4.17 & $1.56\times$ \\
685	\bottomrule
686	\end{tabular}
687	\end{table}
688	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "d1100520-b3b4-4227-aa5b-fedacd73c047"
}
```

</details>

---


### System

_source line 159_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for ing,",
  "usage": {
    "total_tokens": 43280,
    "tool_uses": 18,
    "duration_ms": 20308
  },
  "last_tool_name": "Grep",
  "uuid": "a3d42c9f-a9d5-4a61-aeeb-49b5970a2ad0",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 160_

<details open><summary>🔧 Tool call — Grep · `toolu_018V1oKWLBTLGQSHffZjHt9U`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7ef63b29-c64c-4dc0-9266-4bc708ffb9d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 15795,
    "tool_uses": 1,
    "duration_ms": 3403
  },
  "last_tool_name": "Read",
  "uuid": "79b94e9e-cdf2-43cc-b88b-d94d3aa6c424",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Read · `toolu_0181W9ZRHUTfDamv59PzYXAK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1f893037-e4f6-4220-8165-c535e9442e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dyLFPxbo5493AfzR8YVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7539,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7539,
        "ephemeral_1h_input_tokens": 0
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

_source line 163 · 2026-05-18T19:28:43.618Z_

<details><summary>↩ Tool result · `toolu_0181W9ZRHUTfDamv59PzYXAK`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1cca6afa-859f-40aa-b8c5-2f59d544aae2"
}
```

</details>

---


### System

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Finding Makefile",
  "usage": {
    "total_tokens": 15797,
    "tool_uses": 2,
    "duration_ms": 3719
  },
  "last_tool_name": "Glob",
  "uuid": "43c72e1d-12a9-4e62-91ea-43a7798f0531",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — Glob · `toolu_01PEsUzxh4rtNpqaja1xJ8Pc`</summary>

```json
{
  "pattern": "Makefile",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "4cea0d2c-ec12-4eb6-af5a-ea2dd110f800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dyLFPxbo5493AfzR8YVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7539,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7539,
        "ephemeral_1h_input_tokens": 0
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

_source line 166 · 2026-05-18T19:28:43.583Z_

<details><summary>↩ Tool result · `toolu_018V1oKWLBTLGQSHffZjHt9U`</summary>

```text
docs/paper/main.bbl:9:  Choromanski, Ding, Driess, Dubey, Finn, et~al.]{brohan2023_rt2}
docs/paper/main.bbl:11:  T.~Ding, D.~Driess, A.~Dubey, C.~Finn, et~al.
docs/paper/main.bbl:31:\bibitem[H{\"a}on et~al.(2025)H{\"a}on, Stocking, Chuang, and Tomlin]{haon2025}
docs/paper/main.bbl:32:B.~H{\"a}on, K.~C. Stocking, I.~Chuang, and C.~J. Tomlin.
docs/paper/main.bbl:87:  Nair, Pertsch, Shi, Tanner, Vuong, Walling, Wang, and
docs/paper/main.bbl:92:  A.~Walling, H.~Wang, and U.~Zhilinsky.
docs/paper/main.bbl:148:\bibitem[Bills et~al.(2023)Bills, Cammarata, Mossing, Tillman, Gao, Goh,
docs/paper/main.bbl:150:S.~Bills, N.~Cammarata, D.~Mossing, H.~Tillman, L.~Gao, G.~Goh, I.~Sutskever,
docs/paper/main.bbl:181:  lifting, the rest can be pruned.
docs/paper/appendix.tex:199:A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
docs/paper/appendix.tex:204:These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
docs/paper/introduction.tex:6:Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
docs/paper/references.bib:19:  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
docs/paper/references.bib:93:  author    = {H{\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},
docs/paper/references.bib:207:  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
docs/paper/references.bib:220:  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
docs/paper/references.bib:274:  author    = {Hewitt, John and Manning, Christopher D.},
docs/paper/references.bib:325:  author    = {Bills, Steven and Cammarata, Nick and Mossing, Dan and Tillman, Henk and Gao, Leo and Goh, Gabriel and Sutskever, Ilya and Leike, Jan and Wu, Jeff and Saunders, William},
docs/paper/references.bib:331:@article{templeton2024scaling,
docs/paper/references.bib:381:  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},
docs/paper/main.aux:128:\bibcite{brohan2023_rt2}{{1}{2023}{{Brohan et~al.}}{{Brohan, Brown, Carbajal, Chebotar, Chen, Choromanski, Ding, Driess, Dubey, Finn, et~al.}}}
docs/paper/main.aux:131:\bibcite{haon2025}{{4}{2025}{{H{\"a}on et~al.}}{{H{\"a}on, Stocking, Chuang, and Tomlin}}}
docs/paper/main.aux:139:\bibcite{black2024_pi0}{{12}{2024}{{Black et~al.}}{{Black, Brown, Driess, Esmail, Equi, Finn, Fusai, Groom, Hausman, Ichter, Jakubczak, Jones, Ke, Levine, Li-Bell, Mothukuri, Nair, Pertsch, Shi, Tanner, Vuong, Walling, Wang, and Zhilinsky}}}
docs/paper/main.aux:146:\bibcite{bills2023language}{{19}{2023}{{Bills et~al.}}{{Bills, Cammarata, Mossing, Tillman, Gao, Goh, Sutskever, Leike, Wu, and Saunders}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "186ae5ca-a7b4-45b1-91c2-53d7156bd1a8"
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-18T19:28:43.938Z_

<details><summary>↩ Tool result · `toolu_01PEsUzxh4rtNpqaja1xJ8Pc`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c0f70790-5f4c-4eb8-87f8-9df1bef0259e"
}
```

</details>

---


### System

_source line 168_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for Furthermore|Moreover|Additionally",
  "usage": {
    "total_tokens": 43281,
    "tool_uses": 19,
    "duration_ms": 21306
  },
  "last_tool_name": "Grep",
  "uuid": "87557196-e876-4335-a86f-9b72d67974a2",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 169_

<details open><summary>🔧 Tool call — Grep · `toolu_015YXCsyZTST1YxZ6W5EX88G`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7cf1fdc4-b2cf-454f-a4b8-0c362043784f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 15799,
    "tool_uses": 3,
    "duration_ms": 4362
  },
  "last_tool_name": "Glob",
  "uuid": "1701f651-cd0b-43dc-807a-d59230487296",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 171_

<details open><summary>🔧 Tool call — Glob · `toolu_015qjbbgX3mdC9FuKCZsUD86`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "d3a545bb-00b0-4705-8c8b-5300e629c4bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dyLFPxbo5493AfzR8YVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7539,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7539,
        "ephemeral_1h_input_tokens": 0
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

_source line 172 · 2026-05-18T19:28:44.592Z_

<details><summary>↩ Tool result · `toolu_015qjbbgX3mdC9FuKCZsUD86`</summary>

```text
docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f08086a6-b142-487b-827c-54ae2c70a9bc"
}
```

</details>

---


### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Finding **/*.bib",
  "usage": {
    "total_tokens": 15801,
    "tool_uses": 4,
    "duration_ms": 4786
  },
  "last_tool_name": "Glob",
  "uuid": "86c22f38-4e0c-4e66-b5fe-e5bea3a9a179",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — Glob · `toolu_011bx7VPbRDWX85wgPhMUuHA`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1a9ac26c-83e2-49aa-83be-9b52882d6466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157dyLFPxbo5493AfzR8YVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7539,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7539,
        "ephemeral_1h_input_tokens": 0
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

_source line 175 · 2026-05-18T19:28:44.592Z_

<details><summary>↩ Tool result · `toolu_015YXCsyZTST1YxZ6W5EX88G`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "fcb401e9-497f-490a-a089-2db70db54b8f"
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-18T19:28:45.007Z_

<details><summary>↩ Tool result · `toolu_011bx7VPbRDWX85wgPhMUuHA`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "62ae8164-37f3-43f6-b22c-599278a3a036"
}
```

</details>

---


### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for It is worth noting|Notably",
  "usage": {
    "total_tokens": 43282,
    "tool_uses": 20,
    "duration_ms": 21799
  },
  "last_tool_name": "Grep",
  "uuid": "8a8bbd5b-18c1-4f82-ba80-92b8f2b5872a",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 178_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mh23u4NbeBN4nw9BUPtC4E`</summary>

```json
{
  "pattern": "It is worth noting|Notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "902b5248-2dab-4f4c-9103-db83ce9b220a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 179 · 2026-05-18T19:28:45.078Z_

<details><summary>↩ Tool result · `toolu_01Mh23u4NbeBN4nw9BUPtC4E`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "977744a0-6bfd-448f-bb52-f0a983df2182"
}
```

</details>

---


### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Running Extract all experiment data from nested registry JSON",
  "usage": {
    "total_tokens": 53816,
    "tool_uses": 14,
    "duration_ms": 34149
  },
  "last_tool_name": "Bash",
  "uuid": "bbc00a0e-9e74-44aa-9f68-38a1697b4cfa",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 181_

<details open><summary>🔧 Tool call — Bash · `toolu_01HXuqZPuxo7hC7CWpVYfDui`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\nouter = json.loads(raw)\nresult = json.loads(outer['result'])\ndata = result['data']\n\n# Print all experiments with their metrics and notes\nfor name, exp in data['experiments'].items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    print(f'=== {name} ===')\n    if metrics:\n        print('METRICS:', json.dumps(metrics, indent=2, default=str))\n    if notes:\n        print('NOTES:', notes)\n    print()\nPYEOF",
  "description": "Extract all experiment data from nested registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f635ccbb-7ab8-4a81-953a-2611f8d67389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HURdePgjpcJAjUmnF6YgZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 53161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 407,
        "ephemeral_1h_input_tokens": 0
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

_source line 182 · 2026-05-18T19:28:45.751Z_

<details><summary>↩ Tool result · `toolu_01HXuqZPuxo7hC7CWpVYfDui`</summary>

```text
&lt;persisted-output>
Output too large (53.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt

Preview (first 2KB):
=== specificity_control_action ===
METRICS: {
  "cohens_d": 0.565,
  "paired_mse": 0.034,
  "token_divergence": 0.598,
  "kl_divergence": 4.166,
  "top24_d": 0.65,
  "bottom24_d": 0.565,
  "ratio": 1.15,
  "per_task_d": {
    "cabinet": 0.405,
    "bowl": 0.628,
    "plate": 0.659
  }
}
NOTES: Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.

=== counterfactual_instruction ===
NOTES: 4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim.

=== attention_decomposition ===
NOTES: B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json

=== action_metrics_extended ===
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a885004d-8ea9-4398-aa5a-02940735128a"
}
```

</details>

---


### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for delve|leverage|utilize|facilitate",
  "usage": {
    "total_tokens": 43283,
    "tool_uses": 21,
    "duration_ms": 23186
  },
  "last_tool_name": "Grep",
  "uuid": "3f171268-f8ab-45b5-95b1-9e8cccdf4292",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 184_

<details open><summary>🔧 Tool call — Grep · `toolu_01AqsnuQuGbzjuBvuNy6mBhG`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5e4d5d45-1941-49a9-b2f0-8e97b302ea4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 185 · 2026-05-18T19:28:46.481Z_

<details><summary>↩ Tool result · `toolu_01AqsnuQuGbzjuBvuNy6mBhG`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "dcfc7d06-d187-4a8d-87ea-22217ef2b292"
}
```

</details>

---


### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for a myriad of|a plethora of",
  "usage": {
    "total_tokens": 43284,
    "tool_uses": 22,
    "duration_ms": 24191
  },
  "last_tool_name": "Grep",
  "uuid": "8b165f62-9d7a-446c-ba44-5bc95636fb81",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 187_

<details open><summary>🔧 Tool call — Grep · `toolu_019pHQyQPYcc8MQRiVu3KY81`</summary>

```json
{
  "pattern": "a myriad of|a plethora of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "2f162b24-e931-413d-9e72-b4152b90bc91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 188 · 2026-05-18T19:28:47.471Z_

<details><summary>↩ Tool result · `toolu_019pHQyQPYcc8MQRiVu3KY81`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5ffc47d3-a1a1-4081-8a5a-3c30005a2241"
}
```

</details>

---


### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for graded|distributed",
  "usage": {
    "total_tokens": 43285,
    "tool_uses": 23,
    "duration_ms": 25128
  },
  "last_tool_name": "Grep",
  "uuid": "e3cde2fa-a84b-4087-b58b-725ece6c845d",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 190_

<details open><summary>🔧 Tool call — Grep · `toolu_015Qn8edhStYJU1SLScxDVLv`</summary>

```json
{
  "pattern": "graded|distributed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "2160bea0-1277-441d-9887-63fc760c572b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4bd80ae7b5e60fe",
  "tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt",
  "usage": {
    "total_tokens": 54936,
    "tool_uses": 15,
    "duration_ms": 37025
  },
  "last_tool_name": "Read",
  "uuid": "a7973318-3dce-4efd-9d28-7092e109cb58",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 192_

<details open><summary>🔧 Tool call — Read · `toolu_01V5Tn5ETK5kBC4DSDFnKqeJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ec2e7b90-57cb-4e9a-8726-73377d427edd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni3h8QKhSa4xKHUEeYr9Hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 53568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1048,
        "ephemeral_1h_input_tokens": 0
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

_source line 193 · 2026-05-18T19:28:48.851Z_

<details><summary>↩ Tool result · `toolu_01V5Tn5ETK5kBC4DSDFnKqeJ`</summary>

```text
1	=== specificity_control_action ===
2	METRICS: {
3	  "cohens_d": 0.565,
4	  "paired_mse": 0.034,
5	  "token_divergence": 0.598,
6	  "kl_divergence": 4.166,
7	  "top24_d": 0.65,
8	  "bottom24_d": 0.565,
9	  "ratio": 1.15,
10	  "per_task_d": {
11	    "cabinet": 0.405,
12	    "bowl": 0.628,
13	    "plate": 0.659
14	  }
15	}
16	NOTES: Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.
17	
18	=== counterfactual_instruction ===
19	NOTES: 4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim.
20	
21	=== attention_decomposition ===
22	NOTES: B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json
23	
24	=== action_metrics_extended ===
25	NOTES: Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x, dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x. Cosine similarity NOT computable: source JSONs only have aggregated stats, no raw per-sample action vectors.
26	
27	=== cross_layer_L13_ablation ===
28	NOTES: M006/D064: L13 full-layer ablation d=0.668 ≈ L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.
29	
30	=== cross_layer_L8_ablation ===
31	NOTES: M006/D064: L8 full-layer ablation d=0.652 ≈ L1 d=0.65. Cross-layer gradient not confirmed at action trajectory level. Methodological issue: L1 partial (24/32) vs L8/L13 full (32/32) knockout not comparable; d values saturate. Not for paper.
32	
33	=== dose_response_curve ===
34	NOTES: 单调递增 dose-response 曲线，d=0.482(top4)→0.639(top32)，diminishing returns at ~12-16 heads
35	
36	=== permutation_test_I2 ===
37	METRICS: {
38	  "cv_exact_paired_p": 0.0156,
39	  "cv_mc_unpaired_p": 0.0048,
40	  "cv_7d_p": 0.0078,
41	  "I2_exact_paired_p": 0.1562,
42	  "I2_mc_unpaired_p": 0.1434,
43	  "cv_null_mean": 0,
44	  "cv_null_std": 0.6756,
45	  "I2_null_mean": 0,
46	  "I2_null_std": 0.2468
47	}
48	
49	=== action_trajectory_cpu_analysis ===
50	METRICS: {
51	  "bootstrap_per_head_d": {
52	    "instruction_24h": {
53	      "mean": 0.0271,
54	      "ci_95": [
55	        0.0258,
56	        0.0285
57	      ]
58	    },
59	    "control_8h": {
60	      "mean": 0.0514,
61	      "ci_95": [
62	        0.0478,
63	        0.0551
64	      ]
65	    },
66	    "difference_ctrl_minus_inst": {
67	      "mean": 0.0244,
68	      "ci_95": [
69	        0.0203,
70	        0.0281
71	      ]
72	    },
73	    "task_paired_t": {
74	      "t": 7.356,
75	      "p": 0.0018
76	    },
77	    "all_5_tasks_ctrl_gt_inst": true,
78	    "interpretation": "Control heads ~1.9x per-head effect; instruction heads achieve larger total via 24-head collective coordination"
79	  },
80	  "temporal_coherence_proxy": {
81	    "per_dim_cv_instruction": 1.3,
82	    "per_dim_cv_control": 2.74,
83	    "cross_task_I2_instruction": 0.87,
84	    "cross_task_I2_control": 0.78,
85	    "interpretation": "Instruction ablation produces more consistent (low CV) and more task-dependent (high I\u00b2) perturbation, consistent with structured language-dependent computation"
86	  },
87	  "result_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json"
88	}
89	NOTES: Per-head effect formally confirmed: control heads ~1.9x stronger per-head (d=0.051 vs 0.027, p=0.0018). But instruction heads show qualitatively different perturbation: more consistent across dimensions (CV 1.30 vs 2.74) and more task-dependent (I²=0.87 vs 0.78). Instruction heads mediate structured, coordinated computation rather than individual strong effects.
90	
91	=== action_trajectory_control ===
92	METRICS: {
93	  "paired_action_mse": {
94	    "mean": 0.0201,
95	    "std": 0.0489,
96	    "t_stat": 20.54,
97	    "p_value": 9e-87,
98	    "cohens_d": 0.41
99	  },
100	  "token_divergence_rate": 0.293,
101	  "per_dim_action_shift": {
102	    "dx": 0.00037,
103	    "dy": 0.00125,
104	    "dz": 0.00243,
105	    "rx": 0.00785,
106	    "ry": 0.01387,
107	    "rz": 0.01783,
108	    "gripper": 0.1407
109	  },
110	  "kl_divergence": {
111	    "mean": 1.69,
112	    "std": 3.7
113	  },
114	  "wilcoxon_p": 8e-235,
115	  "config": {
116	    "n_tasks": 5,
117	    "n_demos_per_task": 10,
118	    "n_timesteps_per_demo": 50,
119	    "total_forward_passes": 5000,
120	    "ablated_heads": [
121	      3,
122	      5,
123	      6,
124	      9,
125	      13,
126	      21,
127	      24,
128	      28
129	    ]
130	  },
131	  "per_task": {
132	    "open_middle_drawer": {
133	      "mse": 0.0071,
134	      "cohens_d": 0.24,
135	      "token_div": 0.24
136	    },
137	    "open_top_drawer_put_bowl": {
138	      "mse": 0.0258,
139	      "cohens_d": 0.48,
140	      "token_div": 0.304
141	    },
142	    "push_plate_to_stove": {
143	      "mse": 0.0213,
144	      "cohens_d": 0.42,
145	      "token_div": 0.306
146	    },
147	    "put_bowl_on_plate": {
148	      "mse": 0.0227,
149	      "cohens_d": 0.44,
150	      "token_div": 0.299
151	    },
152	    "put_bowl_on_stove": {
153	      "mse": 0.0236,
154	      "cohens_d": 0.45,
155	      "token_div": 0.313
156	    }
157	  },
158	  "comparison_vs_instruction_ablation": {
159	    "instruction_24heads_mse": 0.0416,
160	    "control_8heads_mse": 0.0201,
161	    "mse_ratio": 2.07,
162	    "instruction_token_div": 0.723,
163	    "control_token_div": 0.293,
164	    "div_ratio": 2.47,
165	    "instruction_kl": 5.079,
166	    "control_kl": 1.69,
167	    "kl_ratio": 3,
168	    "instruction_gripper": 0.291,
169	    "control_gripper": 0.141,
170	    "gripper_ratio": 2.07,
171	    "head_count_ratio": 3,
172	    "note": "Ratios (2.0-3.0x) are at or below head count ratio (3:1), meaning per-head effect of control heads is comparable to instruction heads"
173	  }
174	}
175	NOTES: Control ablation (8 non-instruction heads) also produces significant action divergence (d=0.41, 29.3% token divergence). Per-head effect comparable to instruction heads (0.00250 vs 0.00175). Specificity hypothesis not confirmed. Effect distributed across L1.
176	
177	=== behavioral_pilot_v2 ===
178	NOTES: Director 确认放弃 behavioral rollout（mujoco 版本不匹配）。Phase 1 SR=0/3，fine-tuned checkpoint 加载成功但 action[0] 锁定在 0.236，Blackwell GPU 需要 device_map 绕过 segfault，可能影响 inference。不再投入。
179	
180	=== action_trajectory_analysis ===
181	METRICS: {
182	  "paired_action_mse": {
183	    "mean": 0.0416,
184	    "std": 0.0639,
185	    "t_stat": 32.56,
186	    "p_value": 3.99e-194,
187	    "cohens_d": 0.651
188	  },
189	  "token_divergence_rate": 0.723,
190	  "per_dim_action_shift_means": [
191	    0.0019,
192	    0.0053,
193	    0.0076,
194	    0.0206,
195	    0.0307,
196	    0.0339,
197	    0.2907
198	  ],
199	  "per_dim_names": [
200	    "dx",
201	    "dy",
202	    "dz",
203	    "rx",
204	    "ry",
205	    "rz",
206	    "gripper"
207	  ],
208	  "kl_divergence": {
209	    "mean": 5.079,
210	    "std": 4.961
211	  },
212	  "mse_vs_gt_baseline": 0.432,
213	  "mse_vs_gt_ablated": 0.436,
214	  "wilcoxon_p": 0,
215	  "n_tasks": 5,
216	  "n_samples": 2500,
217	  "all_tasks_significant": true,
218	  "per_task_cohens_d_range": [
219	    0.433,
220	    0.729
221	  ],
222	  "result_path": "/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json"
223	}
224	
225	=== behavioral_pilot_w4 ===
226	NOTES: OpenVLA bridge_orig unnorm_key 与 LIBERO action space 不兼容，baseline SR=0/6，实验前提不成立。两个进程被 SIGHUP 终止。Checkpoint 是 base pretrained（OXE 970K），未在 LIBERO fine-tune，无 LoRA adapter，norm_stats 无 LIBERO key。
227	
228	=== behavioral_pilot ===
229	
230	=== threecond_multiseed_r2_v2 ===
231	METRICS: {
232	  "conditions": [
233	    "untrained",
234	    "llama2base",
235	    "trained"
236	  ],
237	  "seeds": [
238	    42,
239	    123,
240	    456
241	  ],
242	  "trained_peak": {
243	    "layer": 9,
244	    "mean_R2": 0.643,
245	    "std": 0.014
246	  },
247	  "L0_baseline": {
248	    "mean_R2": 0.645,
249	    "std": 0.008,
250	    "note": "three conditions consistent at L0"
251	  },
252	  "pattern_L1_L15": "U&lt;L&lt;T",
253	  "pattern_L16_L25": "L\u2248T>>U",
254	  "pattern_L32": "reversal",
255	  "split": "sequential (demo_0-39 train, demo_40-49 val)",
256	  "r2_space": "original (denormalized)",
257	  "result_path": "/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.json"
258	}
259	NOTES: v2 修正版（顺序 split + 反归一化 R²）。trained peak L9 0.643±0.014, llama2base peak L12 0.634±0.013, untrained peak L1 0.547±0.008 (排除 L32 异常 0.589±0.007)。L0=0.645 三条件一致（共享 vision encoder）。trained-llama2base gap small (0.009 at peak, n=3), direction consistent。llama2base v2=0.634 vs llama2base_action_probe registry peak L4=0.6447，差距 0.010 在 seed 方差内，一致。untrained 中间层崩溃（负 R² + 高方差）是最强信号。
260	
261	=== threecond_multiseed_r2 ===
262	METRICS: {
263	  "conditions": [
264	    "untrained",
265	    "llama2base",
266	    "trained"
267	  ],
268	  "seeds": [
269	    42,
270	    123,
271	    456
272	  ],
273	  "trained_peak": {
274	    "layer": 10,
275	    "mean_R2": 0.548,
276	    "std": 0.012
277	  },
278	  "llama2base_peak": {
279	    "layer": 0,
280	    "mean_R2": 0.538,
281	    "std": 0.015
282	  },
283	  "untrained_peak": {
284	    "layer": 0,
285	    "mean_R2": 0.538,
286	    "std": 0.015
287	  },
288	  "L0_shared_baseline": 0.538,
289	  "pattern_trained": "mild inverted-U, peak L10",
290	  "pattern_llama2base": "stable monotonic decline",
291	  "pattern_untrained": "high variance, deep layer collapse",
292	  "result_path": "/root/autodl-tmp/vla-ssd/results/threecond_multiseed.json"
293	}
294	NOTES: ⚠️ SUPERSEDED by threecond_multiseed_r2_v2 — R² 偏低因 train/val split 用了 random shuffle 而非顺序切分。原实验用顺序切分（demo_0-39 train, demo_40-49 val），multi-seed 脚本误用了 rng.shuffle，导致 R² 系统性偏低（peak 0.548 vs 0.655）。
295	
296	=== random_subset_ablation ===
297	METRICS: {
298	  "baseline_r2": 0.517,
299	  "dominant_24_delta": 0.042,
300	  "random_24_mean_delta": 0.077,
301	  "random_24_std_delta": 0.013,
302	  "z_score": -2.73,
303	  "p_value": 0.003,
304	  "n_random_seeds": 10,
305	  "interpretation": "dominant-24 heads NOT special - any 24/32 heads ablation produces similar or larger R\u00b2 increase",
306	  "result_path": "/root/autodl-tmp/vla-ssd/results/random_subset_ablation.json",
307	  "figure_path": "/root/autodl-tmp/vla-ssd/results/figures/fig_random_subset_ablation.pdf"
308	}
309	NOTES: Plan C (D061) 核心证据。Dominant-24 heads 不具有特异性——10 组随机 24-head 子集的 R² 增量均高于 dominant-24（z=-2.73, p=0.003）。支持 dual routing-encoding function 解释。
310	
311	=== linear_probe_last_preaction ===
312	METRICS: {
313	  "readout": "last_preaction",
314	  "probe_type": "linear",
315	  "trained_peak_layer": 13,
316	  "trained_peak_R2": 0.596,
317	  "untrained_peak_layer": 1,
318	  "untrained_peak_R2": 0.492,
319	  "inverted_U_trained": true,
320	  "trained_gt_untrained_at_peak": true,
321	  "bootstrap_best_vs_best": {
322	    "delta": 0.103,
323	    "ci": [
324	      0.056,
325	      0.167
326	    ],
327	    "p": 0
328	  },
329	  "bootstrap_same_layer_trained_peak": {
330	    "delta": 0.513,
331	    "ci": [
332	      0.314,
333	      0.789
334	    ],
335	    "p": 0
336	  },
337	  "mlp_trained_peak_R2_L13": 0.678,
338	  "linear_vs_mlp_gap_at_peak": -0.082,
339	  "result_path": "/root/autodl-tmp/vla-ssd/results/linear_probe_last_preaction.json"
340	}
341	
342	=== fulllayer_action_probe ===
343	NOTES: superseded — fulllayer_action_probe.json already exists in results/functional_validation/
344	
345	=== l1_head_ablation_control8 ===
346	NOTES: superseded by ablation_50demos_control8 (DONE, success)
347	
348	=== l1_head_ablation_50demos ===
349	NOTES: superseded by ablation_50demos_main (DONE, success)
350	
351	=== llama2base_action_probe ===
352	METRICS: {
353	  "L1_untrained_R2": 0.5546,
354	  "L1_llama2base_R2": 0.6366,
355	  "L1_trained_R2": 0.6331,
356	  "peak_untrained": {
357	    "layer": "L0",
358	    "R2": 0.6403
359	  },
360	  "peak_llama2base": {
361	    "layer": "L4",
362	    "R2": 0.6447
363	  },
364	  "peak_trained": {
365	    "layer": "L8",
366	    "R2": 0.6553
367	  },
368	  "mean_all_untrained": 0.4491,
369	  "mean_all_llama2base": 0.6014,
370	  "mean_all_trained": 0.5849,
371	  "mean_L2_L9_untrained": 0.5294,
372	  "mean_L2_L9_llama2base": 0.6347,
373	  "mean_L2_L9_trained": 0.6463,
374	  "pattern_L2_L9": "U&lt;L&lt;T (19/21 layers)",
375	  "pattern_L1": "U&lt;L\u2248T (pretraining near ceiling)",
376	  "pattern_late": "L>T (VLA repurposes late layers)",
377	  "result_path": "/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json"
378	}
379	
380	=== ablation_50demos_main ===
381	METRICS: {
382	  "baseline_L1": 0.5567,
383	  "baseline_L8": 0.6199,
384	  "baseline_L13": 0.6763,
385	  "all24_L1": 0.6153,
386	  "all24_L8": 0.6377,
387	  "all24_L13": 0.6762,
388	  "all32_L1": 0.5823,
389	  "all32_L8": 0.6311,
390	  "all32_L13": 0.6636,
391	  "all24_vs_baseline_L1_delta": 0.0585,
392	  "all24_vs_baseline_L1_p": 0,
393	  "all24_vs_baseline_L1_CI": [
394	    0.042,
395	    0.0752
396	  ],
397	  "all24_vs_control8_L1_delta": 0.0421,
398	  "all24_vs_control8_L1_p": 0,
399	  "all24_vs_control8_L1_CI": [
400	    0.0286,
401	    0.0563
402	  ]
403	}
404	
405	=== ablation_p2_demo_sensitivity ===
406	METRICS: {
407	  "rsa_peak_layer": "L12",
408	  "rsa_peak_rho": 0.6059,
409	  "rsa_peak_rho_50demo": 0.6282,
410	  "r2_peak_layer": "L11",
411	  "r2_peak": 0.6088,
412	  "r2_peak_50demo": 0.6587,
413	  "rsa_profile_corr": 0.9696,
414	  "r2_profile_corr": 0.8189,
415	  "pattern": "inverted-U preserved"
416	}
417	NOTES: v1 killed — RSA used wrong method (demo-mean-then-distance). Replaced by ablation_p2_demo_sensitivity_v2 with correct Method B (timestep-wise pdist). Probe was correct, only RSA fixed.
418	
419	=== ablation_50demos_control8 ===
420	METRICS: {
421	  "ablate_control8_L1_R2": 0.5732,
422	  "ablate_control8_L1_CI": [
423	    0.5149,
424	    0.6321
425	  ],
426	  "ablate_control8_L8_R2": 0.6311,
427	  "ablate_control8_L8_CI": [
428	    0.5773,
429	    0.6834
430	  ],
431	  "ablate_control8_L13_R2": 0.6787,
432	  "ablate_control8_L13_CI": [
433	    0.6322,
434	    0.7255
435	  ]
436	}
437	
438	=== l1_head_ablation ===
439	METRICS: {
440	  "classification_v2": {
441	    "baseline": {
442	      "L1": 1,
443	      "L8": 1,
444	      "L16": 1,
445	      "L31": 1
446	    },
447	    "ablate_all24": {
448	      "L1": 1,
449	      "L8": 1,
450	      "L16": 1,
451	      "L31": 1
452	    },
453	    "ablate_all32": {
454	      "L1": 1,
455	      "L8": 1,
456	      "L16": 1,
457	      "L31": 1
458	    },
459	    "ablate_top5": {
460	      "L1": 1,
461	      "L8": 1,
462	      "L16": 1,
463	      "L31": 1
464	    },
465	    "ablate_control8": {
466	      "L1": 1,
467	      "L8": 1,
468	      "L16": 1,
469	      "L31": 1
470	    }
471	  },
472	  "action_probe_R2": {
473	    "baseline": {
474	      "L1": 0.2558,
475	      "L8": 0.4401,
476	      "L13": 0.524
477	    },
478	    "ablate_all24": {
479	      "L1": 0.3627,
480	      "L8": 0.4496,
481	      "L13": 0.5194
482	    },
483	    "ablate_all32": {
484	      "L1": 0.3747,
485	      "L8": 0.4449,
486	      "L13": 0.5184
487	    }
488	  },
489	  "diagnostic": {
490	    "monkey_patch": "verified_working",
491	    "ablated_inst_attn": 0,
492	    "baseline_inst_attn": 0.029,
493	    "hidden_cosine_sim": 0.973
494	  }
495	}
496	NOTES: D057. Results: Classification 1.0 all conditions (instruction identity via residual stream). Action probe R²: L1 baseline=0.256 → ablate_all24=0.363 (Δ=+0.107, p<0.0001, CI [0.063,0.153]) → ablate_all32=0.375 (Δ=+0.119, p<0.0001, CI [0.065,0.167]). L8/L13 ns. Interpretation: L1 instruction-attending heads trade capacity between instruction routing and action encoding. Ablation frees capacity → L1 action R² increases. Deep layers unaffected. Monkey-patch verified working (diagnostic: inst attn → 0, cosine sim = 0.973).
497	
498	=== cross_inst_spatial_trained ===
499	METRICS: {
500	  "trained_image_mean": {
501	    "L0": 0.1,
502	    "L1": 0.1,
503	    "L4": 0.1,
504	    "L8": 0.1,
505	    "L12": 0.1,
506	    "L16": 0.1,
507	    "L20": 0.1,
508	    "L24": 0.1,
509	    "L28": 0.1,
510	    "L31": 0.101
511	  },
512	  "trained_last_preaction": {
513	    "L0": 0.1,
514	    "L1": 0.989,
515	    "L4": 1,
516	    "L8": 1,
517	    "L12": 1,
518	    "L16": 1,
519	    "L20": 1,
520	    "L24": 1,
521	    "L28": 1,
522	    "L31": 1
523	  },
524	  "untrained_image_mean": {
525	    "L0": 0.1,
526	    "L1": 0.1,
527	    "L4": 0.1,
528	    "L8": 0.101,
529	    "L12": 0.099,
530	    "L16": 0.1,
531	    "L20": 0.099,
532	    "L24": 0.1,
533	    "L28": 0.1,
534	    "L31": 0.1
535	  },
536	  "untrained_last_preaction": {
537	    "L0": 0.1,
538	    "L1": 0.995,
539	    "L4": 0.862,
540	    "L8": 0.683,
541	    "L12": 0.795,
542	    "L16": 0.765,
543	    "L20": 0.689,
544	    "L24": 0.777,
545	    "L28": 0.76,
546	    "L31": 0.754
547	  }
548	}
549	
550	=== plan010_rsa_spatial ===
551	METRICS: {
552	  "trained_image_mean": {
553	    "best_layer": "L14",
554	    "RSA": 0.6911
555	  },
556	  "trained_last_preaction": {
557	    "best_layer": "L15",
558	    "RSA": 0.6945
559	  },
560	  "untrained_image_mean": {
561	    "best_layer": "L0",
562	    "RSA": 0.6523
563	  },
564	  "untrained_last_preaction": {
565	    "best_layer": "L1",
566	    "RSA": 0.6659
567	  }
568	}
569	
570	=== plan010_action_probe_spatial ===
571	METRICS: {
572	  "trained_image_mean": {
573	    "best_layer": "L13",
574	    "R2": 0.6963
575	  },
576	  "trained_last_preaction": {
577	    "best_layer": "L21",
578	    "R2": 0.6748
579	  },
580	  "untrained_image_mean": {
581	    "best_layer": "L0",
582	    "R2": 0.6732
583	  },
584	  "untrained_last_preaction": {
585	    "best_layer": "L1",
586	    "R2": 0.6348
587	  },
588	  "bootstrap_significance": "p < 0.001 for all trained vs untrained comparisons"
589	}
590	
591	=== llama2_base_control ===
592	METRICS: {
593	  "l1_heads_gt50pct": {
594	    "trained": 25,
595	    "untrained": 0,
596	    "llama2base": 9
597	  },
598	  "l1_mean_text_attn": {
599	    "trained": 0.577,
600	    "untrained": 0.117,
601	    "llama2base": 0.365
602	  },
603	  "l1_mean_image_attn": {
604	    "trained": 0.213,
605	    "untrained": 0.878,
606	    "llama2base": 0.617
607	  },
608	  "dense_probe_L1_acc": {
609	    "trained": 0.996,
610	    "untrained": 1,
611	    "llama2base": 0.802
612	  },
613	  "dense_probe_L2_acc": {
614	    "trained": 1,
615	    "untrained": 1,
616	    "llama2base": 0.987
617	  },
618	  "dense_probe_L8_acc": {
619	    "trained": 1,
620	    "untrained": 0.986,
621	    "llama2base": 0.999
622	  },
623	  "dense_probe_L16_acc": {
624	    "trained": 1,
625	    "untrained": 0.92,
626	    "llama2base": 1
627	  },
628	  "dense_probe_L31_acc": {
629	    "trained": 1,
630	    "untrained": 0.82,
631	    "llama2base": 1
632	  },
633	  "llama2base_instruction_heads": [
634	    0,
635	    15,
636	    16,
637	    17,
638	    18,
639	    23,
640	    25,
641	    26,
642	    27
643	  ],
644	  "full_profile": "llama2base saturates at L5 (99.8-100%), NO deep-layer degradation unlike untrained (82% at L31)"
645	}
646	
647	=== rsa_cosine_ablation ===
648	
649	=== rsa_permutation_test ===
650	
651	=== ablation_p1_seed_robustness ===
652	METRICS: {
653	  "seeds": [
654	    0,
655	    1,
656	    2,
657	    3,
658	    42
659	  ],
660	  "peak_layer_per_seed": [
661	    9,
662	    16,
663	    9,
664	    10,
665	    9
666	  ],
667	  "peak_r2_per_seed": [
668	    0.6534,
669	    0.6549,
670	    0.6529,
671	    0.6531,
672	    0.6587
673	  ],
674	  "peak_layer_mean": 10.6,
675	  "peak_layer_std": 2.73,
676	  "peak_r2_mean": 0.6546,
677	  "peak_r2_std": 0.0022,
678	  "per_layer_std_range": [
679	    0.0022,
680	    0.0086
681	  ],
682	  "runtime_seconds": 845.7,
683	  "condition": "trained_image_mean"
684	}
685	
686	=== ablation_p2_demo_sensitivity_v2 ===
687	METRICS: {
688	  "rsa_profile_correlation": 0.9696,
689	  "probe_profile_correlation": 0.8189,
690	  "rsa_peak_50demos": {
691	    "layer": 12,
692	    "rsa": 0.6282
693	  },
694	  "rsa_peak_25demos": {
695	    "layer": 12,
696	    "rsa": 0.6059
697	  },
698	  "probe_peak_50demos": {
699	    "layer": 9,
700	    "r2": 0.6587
701	  },
702	  "probe_peak_25demos": {
703	    "layer": 11,
704	    "r2": 0.6088
705	  },
706	  "n_layers": 33,
707	  "elapsed_seconds": 1583.8,
708	  "conclusion_summary": "Inverted-U highly stable under halved data. RSA profile r=0.97, peak L12 unchanged. Probe profile r=0.82, peak shifts L9\u2192L11 but shape preserved."
709	}
710	
711	=== p0_functional_action_delta_probe ===
712	METRICS: {
713	  "projector": {
714	    "mean_R2": 0.1181,
715	    "overall_R2": 0.1053
716	  },
717	  "trained_image_mean_L14": {
718	    "mean_R2": 0.1215,
719	    "overall_R2": 0.1091
720	  },
721	  "untrained_best_L0": {
722	    "mean_R2": 0.1174,
723	    "overall_R2": 0.107
724	  },
725	  "bootstrap_proj_vs_trained": {
726	    "delta": -0.0034,
727	    "ci_95": [
728	      -0.0066,
729	      0.0005
730	    ],
731	    "p_value": 0.04
732	  },
733	  "note": "image_mean R\u00b2 (~0.12) substantially higher than last_preaction (~0.06). Per-dim: dz=0.46, dx=0.29, dy=0.25 most predictable.",
734	  "gate": "Projector (0.118) \u2248 LLM (0.122), gap tiny (\u0394=0.003). Consistent with redistribution narrative.",
735	  "result_path": "/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json"
736	}
737	NOTES: Delta probe: projector (0.118) BELOW LLM (0.122), CI=[-0.007, +0.001] 含 0, p=0.04. 差异不显著。论文需如实汇报：raw action PASS (projector > image_mean), delta BELOW (差异不显著)。双维度呈现。
738	
739	=== p0_functional_probe_v2 ===
740	METRICS: {
741	  "bootstrap_proj_vs_image_mean_L19": {
742	    "proj_mean_R2": 0.7063,
743	    "image_mean_L19_mean_R2": 0.6832,
744	    "delta": 0.0231,
745	    "ci_95": [
746	      0.0105,
747	      0.0367
748	    ],
749	    "p_value": 0.001,
750	    "gate": "PASS \u2014 CI lower bound > 0"
751	  },
752	  "dino_action": {
753	    "mean_R2": 0.7116,
754	    "feature_key": "cls_token"
755	  },
756	  "dino_action_delta": {
757	    "mean_R2": 0.1
758	  },
759	  "bootstrap_dino_vs_proj": {
760	    "delta": 0.005,
761	    "ci_95": [
762	      -0.008,
763	      0.019
764	    ],
765	    "p_value": 0.22,
766	    "significant": false
767	  },
768	  "three_way_ordering": "DINO (0.712) \u2248 Projector (0.706) > LLM image_mean (0.683)",
769	  "untrained_L10_L11_diagnosis": {
770	    "verdict": "pathological_random_init",
771	    "detail": "Feature stats normal (no NaN/Inf/zeros, std~5), but probe R\u00b2 drops L9=0.632\u2192L10=0.029. Random LLM weights create non-decodable representations at these layers."
772	  },
773	  "result_path": "/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_v2.json"
774	}
775	
776	=== d027_trained_no_inst_rsa ===
777	METRICS: {
778	  "trained_no_inst_peak_rsa": 0.489,
779	  "trained_no_inst_peak_layer": 30,
780	  "full_2x2_matrix": {
781	    "trained_with_inst": 0.4876,
782	    "trained_no_inst": 0.489,
783	    "untrained_with_inst": 0.4846,
784	    "untrained_no_inst": 0.4802,
785	    "dino": 0.388
786	  },
787	  "training_effect_with_inst": 0.003,
788	  "training_effect_no_inst": 0.0088,
789	  "instruction_effect_trained": -0.0014,
790	  "instruction_effect_untrained": 0.0044,
791	  "bootstrap_delta_ci": "[-0.058, 0.072] includes 0",
792	  "conclusion_summary": "All 4 conditions converge in 0.48-0.49 band. Neither training nor instruction has meaningful effect on RSA."
793	}
794	
795	=== d021_output_head_analysis ===
796	METRICS: {
797	  "group_summary": {
798	    "vision": {
799	      "count": 685,
800	      "mean_rel_change": 0,
801	      "cos_sim": 1,
802	      "verdict": "IDENTICAL"
803	    },
804	    "projector": {
805	      "count": 6,
806	      "mean_rel_change": 0,
807	      "cos_sim": 1.001,
808	      "verdict": "IDENTICAL"
809	    },
810	    "embedding": {
811	      "count": 1,
812	      "rel_change": 1.3287,
813	      "cos_sim": -0.0001
814	    },
815	    "llm": {
816	      "count": 288,
817	      "mean_rel_change": 1.3156,
818	      "std": 0.3759,
819	      "cos_sim": 0.2178,
820	      "range": [
821	        1.22,
822	        1.37
823	      ]
824	    },
825	    "llm_final_norm": {
826	      "count": 1,
827	      "rel_change": 0.8628,
828	      "cos_sim": 0.998
829	    },
830	    "head_lm_head": {
831	      "count": 1,
832	      "rel_change": 1.4754,
833	      "cos_sim": 0.0002
834	    }
835	  },
836	  "head_vs_llm_ratio": 1.12,
837	  "shallow_adaptation_gate": "FAIL (ratio 1.12x, threshold 3x)",
838	  "key_finding_1": "Vision backbone + Projector IDENTICAL between trained and untrained (rel_change=0, cos_sim=1.0)",
839	  "key_finding_2": "LLM weight diffs uniformly distributed across all 32 layers (rel_change 1.22-1.37), head not special",
840	  "key_finding_3": "Shared frozen components (SigLIP + projector) explain WHY trained \u2248 untrained in representation structure \u2014 regardless of LLM weights",
841	  "caveat": "Comparison is pretrained Llama + fine-tune vs random init, not fine-tuned vs pre-fine-tuning. Differences dominated by pretrained vs random."
842	}
843	
844	=== d021_instruction_ablation ===
845	METRICS: {
846	  "no_inst_untrained_peak_rsa": 0.4802,
847	  "with_inst_untrained_peak_rsa": 0.4846,
848	  "with_inst_trained_peak_rsa": 0.4876,
849	  "dino_rsa": 0.388,
850	  "delta_with_minus_no_inst": 0.0044,
851	  "gate_threshold_delta": 0.1,
852	  "gate_threshold_no_inst_max": 0.438,
853	  "gate_judgment": "FAIL \u2014 \u0394=0.0044 << 0.10; no_inst=0.4802 >> DINO+0.05=0.438",
854	  "interpretation": "Removing instruction text does NOT collapse RSA. Untrained VLA action-relevant structure is vision-driven, not instruction-driven. Option B framing falsified."
855	}
856	
857	=== lg_pca1024_linear_pertimestep ===
858	METRICS: {
859	  "bin_0_trained": 0.9992,
860	  "bin_0_untrained": 1,
861	  "bin_0_dino": 0.354,
862	  "bin_0_delta_TU": -0.0008,
863	  "overall_trained": 0.9999,
864	  "overall_untrained": 1,
865	  "overall_dino": 0.8397,
866	  "per_bin": {
867	    "0": {
868	      "trained": 0.9992,
869	      "untrained": 1,
870	      "dino": 0.354
871	    },
872	    "1": {
873	      "trained": 1,
874	      "untrained": 1,
875	      "dino": 0.7662
876	    },
877	    "2": {
878	      "trained": 1,
879	      "untrained": 1,
880	      "dino": 0.8244
881	    },
882	    "3": {
883	      "trained": 1,
884	      "untrained": 1,
885	      "dino": 0.8676
886	    },
887	    "4": {
888	      "trained": 1,
889	      "untrained": 1,
890	      "dino": 0.8575
891	    },
892	    "5": {
893	      "trained": 1,
894	      "untrained": 1,
895	      "dino": 0.8903
896	    },
897	    "6": {
898	      "trained": 1,
899	      "untrained": 1,
900	      "dino": 0.9618
901	    },
902	    "7": {
903	      "trained": 1,
904	      "untrained": 1,
905	      "dino": 0.9574
906	    },
907	    "8": {
908	      "trained": 1,
909	      "untrained": 1,
910	      "dino": 0.969
911	    },
912	    "9": {
913	      "trained": 1,
914	      "untrained": 1,
915	      "dino": 0.9676
916	    }
917	  },
918	  "gate_exp2": "FAIL",
919	  "gate_exp2_delta": -0.0008,
920	  "gate_exp2_threshold": 0.15
921	}
922	
923	=== lg_rsa_analysis ===
924	METRICS: {
925	  "trained_peak_rsa": 0.4876,
926	  "trained_peak_layer": 9,
927	  "untrained_peak_rsa": 0.4846,
928	  "untrained_peak_layer": 12,
929	  "dino_rsa": 0.388,
930	  "delta_TU_at_trained_peak": 0.003,
931	  "delta_TU_range": [
932	    -0.0722,
933	    0.0109
934	  ],
935	  "layers_trained_gt_untrained": 4,
936	  "layers_total": 33,
937	  "per_phase": {
938	    "early": {
939	      "trained": 0.3197,
940	      "untrained": 0.4148,
941	      "dino": 0.4909
942	    },
943	    "mid": {
944	      "trained": 0.5231,
945	      "untrained": 0.5248,
946	      "dino": 0.4132
947	    },
948	    "late": {
949	      "trained": 0.4758,
950	      "untrained": 0.4592,
951	      "dino": 0.2601
952	    }
953	  },
954	  "cka_range": [
955	    0.687,
956	    0.86
957	  ],
958	  "gate_G1_D020": "PASS (0.4876 > 0.15)",
959	  "gate_G2_D020": "FAIL (\u0394\u03c1=0.003, threshold 0.08)",
960	  "gate_G3_D020": "PASS (0.4876 > 0.388, margin +0.0996)",
961	  "interpretation": "Architecture matters (VLA >> DINO), training doesn't (trained \u2248 untrained). Instruction input adds action-relevant structure, but LLM training does not improve it."
962	}
963	
964	=== lg_gc_trained_frame0 ===
965	METRICS: {
966	  "trained_best_layer": 3,
967	  "trained_best_acc": 1,
968	  "trained_best_f1": 1,
969	  "untrained_best_layer": 2,
970	  "untrained_best_acc": 1,
971	  "untrained_best_f1": 1,
972	  "dino_best_acc": 0.15,
973	  "dino_best_f1": 0.0911,
974	  "n_classes": 10,
975	  "n_train": 400,
976	  "n_val": 100,
977	  "trained_layer_curve": {
978	    "L0": 0.1,
979	    "L1": 0.39,
980	    "L2": 0.58,
981	    "L3": 1,
982	    "L4_to_L18": 1,
983	    "L19": 1,
984	    "L28": 1,
985	    "L31": 1,
986	    "L32": 1
987	  },
988	  "untrained_layer_curve": {
989	    "L0": 0.1,
990	    "L1": 0.95,
991	    "L2": 1,
992	    "L3": 0.99,
993	    "L19": 0.91,
994	    "L28": 0.9,
995	    "L31": 0.88,
996	    "L32": 0.98
997	  },
998	  "sanity_gc_frame0": "PASS (DINO 15% <= 25%)",
999	  "g3_gc_frame0": "FAIL (\u0394=0pp, both 100%)",
1000	  "key_finding": "DINO 15% at t=0 confirms visual ambiguity. But MLP+4096 probe capacity still saturates both VLA models. Trained VLA more stable across layers (100% L3+) vs untrained (88-100% oscillation in deep layers). Needs PCA+linear verification."
1001	}
1002	
1003	=== lg_gc_dino ===
1004	METRICS: {
1005	  "best_accuracy": 0.8626,
1006	  "best_traj_accuracy": 1,
1007	  "best_macro_f1": 0.8412,
1008	  "n_classes": 10,
1009	  "num_layers": 1,
1010	  "feature_dim": 1024,
1011	  "gate_Sanity_GC": "FAIL",
1012	  "note": "DINO acc 86.26% >> 25% threshold. Goals are visually distinguishable. Sanity-GC gate FAILED."
1013	}
1014	
1015	=== lg_gc_untrained ===
1016	METRICS: {
1017	  "best_layer": 1,
1018	  "best_accuracy": 1,
1019	  "best_traj_accuracy": 1,
1020	  "best_macro_f1": 1,
1021	  "worst_layer": 31,
1022	  "worst_accuracy": 0.9971,
1023	  "n_classes": 10,
1024	  "n_train": 50880,
1025	  "n_val": 12848,
1026	  "per_layer_accuracies": {
1027	    "0": 0.1582,
1028	    "1": 1,
1029	    "2": 1,
1030	    "3": 1,
1031	    "4": 1,
1032	    "5": 1,
1033	    "6": 1,
1034	    "7": 1,
1035	    "8": 1,
1036	    "9": 1,
1037	    "10": 0.9998,
1038	    "11": 0.9998,
1039	    "12": 0.9999,
1040	    "13": 0.9999,
1041	    "14": 0.9996,
1042	    "15": 0.9996,
1043	    "16": 0.9998,
1044	    "17": 0.9994,
1045	    "18": 0.9989,
1046	    "19": 0.9992,
1047	    "20": 0.9995,
1048	    "21": 0.9993,
1049	    "22": 0.9996,
1050	    "23": 0.9991,
1051	    "24": 0.9994,
1052	    "25": 0.9988,
1053	    "26": 0.9993,
1054	    "27": 0.9993,
1055	    "28": 0.9986,
1056	    "29": 0.9984,
1057	    "30": 0.9977,
1058	    "31": 0.9971,
1059	    "32": 0.9991
1060	  },
1061	  "gate_G2_GC": "FAIL",
1062	  "gate_G2_GC_delta": 0,
1063	  "gate_G2_GC_threshold": 0.25,
1064	  "layer0_detail": "predicts_only_class1_acc_0.158_random_level",
1065	  "comparison": {
1066	    "trained_best_acc": 1,
1067	    "untrained_best_acc": 1,
1068	    "dino_best_acc": 0.8626,
1069	    "delta_trained_untrained": 0,
1070	    "delta_trained_dino": 0.1374
1071	  },
1072	  "interpretation": "Untrained VLA (random LLM) achieves identical 100% goal classification from layer 1+. G2-GC FAIL: \u0394=0pp (threshold 25pp). Goal classification is NOT a valid discriminator between trained and untrained VLA \u2014 the MLP probe on 4096-dim features trivially separates 10 classes even from random projections."
1073	}
1074	
1075	=== lg_gc_trained ===
1076	METRICS: {
1077	  "best_layer": 1,
1078	  "best_accuracy": 1,
1079	  "best_traj_accuracy": 1,
1080	  "best_macro_f1": 1,
1081	  "n_classes": 10,
1082	  "n_train": 50880,
1083	  "n_val": 12848,
1084	  "per_layer_accuracies": {
1085	    "0": 0.1582,
1086	    "1": 1,
1087	    "2": 1,
1088	    "3": 1,
1089	    "4": 1,
1090	    "5": 1,
1091	    "6": 1,
1092	    "7": 1,
1093	    "8": 1,
1094	    "9": 1,
1095	    "10": 1,
1096	    "11": 1,
1097	    "12": 1,
1098	    "13": 1,
1099	    "14": 1,
1100	    "15": 1,
1101	    "16": 1,
1102	    "17": 1,
1103	    "18": 1,
1104	    "19": 1,
1105	    "20": 1,
1106	    "21": 1,
1107	    "22": 1,
1108	    "23": 1,
1109	    "24": 1,
1110	    "25": 1,
1111	    "26": 1,
1112	    "27": 1,
1113	    "28": 1,
1114	    "29": 1,
1115	    "30": 1,
1116	    "31": 1,
1117	    "32": 1
1118	  },
1119	  "layer0_detail": "predicts_only_class1_acc_0.158",
1120	  "layer1_epochs": 13,
1121	  "layers_2_32_epochs": 6,
1122	  "gate_G1_GC": "PASS"
1123	}
1124	
1125	=== cross_inst_extract_untrained ===
1126	
1127	=== cross_inst_extract_trained ===
1128	
1129	=== openvla-untrained-extract ===
1130	METRICS: {
1131	  "tasks_completed": "10/10",
1132	  "total_size_gb": 52,
1133	  "feature_dim": 4096,
1134	  "num_layers": 33,
1135	  "dtype": "float16",
1136	  "demos_per_task": 50,
1137	  "feature_keys": [
1138	    "image_mean",
1139	    "last_preaction"
1140	  ],
1141	  "io_fix_speedup": "52x (0.8\u219242 step/s)",
1142	  "reextracted_tasks": [
1143	    "LIVING_ROOM_SCENE6",
1144	    "STUDY_SCENE1"
1145	  ],
1146	  "reextraction_time_min": 18.5
1147	}
1148	NOTES: 1. 当前 untrained checkpoint 未使用固定 seed（init_untrained.py 缺 torch.manual_seed），但 checkpoint 已持久化到 /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/，可复现。脚本已补 seed=42 供将来使用。2. 日志中 mode=trained 为 extract_features.py 默认值，实际使用的是 openvla-7b-untrained checkpoint。3. EXIT_CODE=130 是 Worker(fix-extraction-restart) 主动 kill 以修复 I/O 瓶颈（264次 .cpu() → 2次/batch，52x 加速）。4. fix-extraction-restart Worker 补完 LIVING_ROOM_SCENE6 + STUDY_SCENE1（18.5 min），最终 10/10 tasks 全部完成。features/untrained/ 现有 10 个 .h5 文件，每个 50 demos。
1149	
1150	=== openvla-trained-extract ===
1151	METRICS: {
1152	  "tasks_completed": "10/10",
1153	  "total_size_gb": 53,
1154	  "feature_dim": 4096,
1155	  "num_layers": 33,
1156	  "dtype": "float16",
1157	  "demos_per_task": 50,
1158	  "feature_keys": [
1159	    "image_mean",
1160	    "last_preaction"
1161	  ],
1162	  "extraction_time_min": 185.3,
1163	  "exit_code": 0
1164	}
1165	
1166	=== lg_extract_untrained ===
1167	METRICS: {
1168	  "tasks_completed": "10/10",
1169	  "feature_dim": 4096,
1170	  "num_layers": 33,
1171	  "dtype": "float16",
1172	  "demos_per_task": 50,
1173	  "exit_code": 0,
1174	  "feature_keys": [
1175	    "image_mean",
1176	    "last_preaction"
1177	  ],
1178	  "note": "Retry after local_files_only fix. 2/10 from first run + 8/10 from retry."
1179	}
1180	NOTES: 失败原因: 同 lg_extract_trained — AutoProcessor.from_pretrained() 网络不可达。提取进度到 22%。诊断 Worker: worker_diagnose_lg_extract_failed_20260515T165835
1181	
1182	=== lg_extract_trained ===
1183	METRICS: {
1184	  "tasks_completed": "10/10",
1185	  "extraction_time_min": 53.4,
1186	  "feature_dim": 4096,
1187	  "num_layers": 33,
1188	  "dtype": "float16",
1189	  "demos_per_task": 50,
1190	  "exit_code": 0,
1191	  "feature_keys": [
1192	    "image_mean",
1193	    "last_preaction"
1194	  ],
1195	  "note": "Retry after local_files_only fix. 3/10 from first run + 7/10 from retry."
1196	}
1197	NOTES: Retry #1 after local_files_only fix. PID 627256 restarted ~17:00 UTC. Script skips completed h5 files (3/10 done from first run).
1198	
1199	=== dinov2_baseline ===
1200	METRICS: {
1201	  "temporal_distance_rho": 0.833,
1202	  "temporal_distance_rho_pooled": 0.833,
1203	  "per_task_rho_mean": 0.9008,
1204	  "per_task_rho_range": [
1205	    0.41,
1206	    0.68
1207	  ],
1208	  "per_task_n_pairs": 500,
1209	  "R2": 0.687,
1210	  "MAE": 0.127,
1211	  "feature_dim": 1024,
1212	  "num_layers": 1,
1213	  "probe_type": "mlp_adam_early_stopping",
1214	  "training_time_seconds": 7.5,
1215	  "note": "pooled \u03c1=0.833 inflated by cross-task variance; per-task mean \u03c1=0.9008 is correct comparison baseline (updated per D005/D006)",
1216	  "subtask_macro_auc": 0.9717,
1217	  "subtask_auc_per_predicate": {
1218	    "subtask_0": 0.9694,
1219	    "subtask_1": 0.9739
1220	  },
1221	  "subtask_labels": "auto-extracted from MuJoCo state transitions (2 subtasks per task)",
1222	  "subtask_probe_type": "sklearn_logistic_regression_lbfgs",
1223	  "control_b_label_permutation_rho": 0.039,
1224	  "control_b_label_permutation_per_task_mean": 0.039,
1225	  "control_b_label_permutation_R2": -0.052,
1226	  "cross_traj_rho": 0.65,
1227	  "cross_traj_note": "supplementary analysis, not control; visual progress transfers across trajectories"
1228	}
1229	
1230	=== plan_012_clip_vit_control ===
1231	METRICS: {
1232	  "unified_probe_hyperparams": "epochs=50,patience=5,lr=1e-3,batch=256,hidden=256,seed=42",
1233	  "projector_mean_R2": 0.6298,
1234	  "dino_cls_mean_R2": 0.6343,
1235	  "clip_cls_mean_R2": 0.5866,
1236	  "vla_image_mean_L19_mean_R2": 0.5986,
1237	  "vla_last_preaction_L19_mean_R2": 0.6711,
1238	  "ordering": "vla_last_preaction_L19 > dino_cls \u2248 projector > vla_image_mean_L19 > clip_cls",
1239	  "projector_vs_dino_p": 0.557,
1240	  "projector_vs_clip_p": 0,
1241	  "clip_vs_dino_p": 0,
1242	  "projector_vs_vla_imL19_p": 0,
1243	  "projector_vs_vla_lpL19_p": 0.002
1244	}
1245	
1246	=== qa_probe_classification ===
1247	METRICS: {
1248	  "progress_best_acc": 0.8632,
1249	  "progress_best_layer": "L20_trained",
1250	  "subtask_best_acc": 0.9367,
1251	  "subtask_best_layer": "L16/L20_trained",
1252	  "dino_progress": 0.8272,
1253	  "dino_subtask": 0.9209
1254	}
1255	
1256	=== rsa_per_dof_ablation ===
1257	
1258	=== plan_010_extract_trained ===
1259	METRICS: {
1260	  "tasks_completed": "10/10",
1261	  "output_size_gb": 24,
1262	  "output_dir": "/root/autodl-tmp/vla-ssd/features/trained_libero_spatial/",
1263	  "feature_keys": [
1264	    "image_mean",
1265	    "last_preaction"
1266	  ],
1267	  "num_layers": 33,
1268	  "demos_per_task": 50
1269	}
1270	
1271	=== plan_010_extract_untrained ===
1272	METRICS: {
1273	  "tasks_completed": "10/10",
1274	  "output_size_gb": 25,
1275	  "output_dir": "/root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/",
1276	  "feature_keys": [
1277	    "image_mean",
1278	    "last_preaction"
1279	  ],
1280	  "num_layers": 33,
1281	  "demos_per_task": 50
1282	}
1283	
1284	=== plan_010_libero_spatial ===
1285	METRICS: {
1286	  "rsa": {
1287	    "trained_image_mean_peak": {
1288	      "layer": 14,
1289	      "rsa": 0.6911
1290	    },
1291	    "trained_last_preaction_peak": {
1292	      "layer": 15,
1293	      "rsa": 0.6945
1294	    },
1295	    "untrained_image_mean_peak": {
1296	      "layer": 0,
1297	      "rsa": 0.6523
1298	    },
1299	    "untrained_last_preaction_peak": {
1300	      "layer": 1,
1301	      "rsa": 0.6659
1302	    },
1303	    "pattern": "trained inverted-U confirmed, untrained flat/declining"
1304	  },
1305	  "action_probe": {
1306	    "trained_image_mean_peak": {
1307	      "layer": 13,
1308	      "R2": 0.6963
1309	    },
1310	    "trained_last_preaction_peak": {
1311	      "layer": 21,
1312	      "R2": 0.6748
1313	    },
1314	    "untrained_image_mean_peak": {
1315	      "layer": 0,
1316	      "R2": 0.6732
1317	    },
1318	    "untrained_last_preaction_peak": {
1319	      "layer": 1,
1320	      "R2": 0.6348
1321	    },
1322	    "untrained_lastpre_collapse": "L5-L31 R2 approx -0.015, only L32 recovers to 0.621"
1323	  },
1324	  "bootstrap": {
1325	    "best_vs_best_imgmean": {
1326	      "delta": 0.023,
1327	      "ci_95": [
1328	        0.012,
1329	        0.036
1330	      ],
1331	      "p": 0.001
1332	    },
1333	    "best_vs_best_lastpre": {
1334	      "delta": 0.04,
1335	      "ci_95": [
1336	        0.019,
1337	        0.057
1338	      ],
1339	      "p": 0.0004
1340	    },
1341	    "same_layer_L13_imgmean": {
1342	      "delta": 0.711,
1343	      "ci_95": [
1344	        0.685,
1345	        0.74
1346	      ],
1347	      "p": 0.001
1348	    },
1349	    "same_layer_L21_lastpre": {
1350	      "delta": 0.37,
1351	      "ci_95": [
1352	        0.317,
1353	        0.427
1354	      ],
1355	      "p": 0.001
1356	    }
1357	  },
1358	  "cross_benchmark": {
1359	    "rsa_peak_goal": "L12",
1360	    "rsa_peak_spatial": "L14-15",
1361	    "probe_peak_goal": "L8-13",
1362	    "probe_peak_spatial": "L13-21",
1363	    "consistency": "high \u2014 peak layers within 2-layer range"
1364	  },
1365	  "result_files": [
1366	    "/root/autodl-tmp/vla-ssd/results/rsa/rsa_libero_spatial.json",
1367	    "/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json"
1368	  ]
1369	}
1370	NOTES: LIBERO-Spatial cross-benchmark validation complete. All three Core Claims replicate. Inverted-U (C2) confirmed on both RSA and R². Training redistribution (C3) confirmed — peaks shift from L0 to L13-15. Key: Spatial best-vs-best RSA Δ=+0.023, CI=[0.012, 0.036], p<0.001 (SIGNIFICANT) — contrasts with Goal's n.s. result (Δ=+0.017, CI=[-0.0002, 0.035]). Goal was underpowered; Spatial detects significance. Training effect is real but small.
1371	
1372	=== plan_013_branch_split ===
1373	METRICS: {
1374	  "dinov2_branch_rsa": 0.619,
1375	  "siglip_branch_rsa": 0.621,
1376	  "fused_2176d_rsa": 0.634,
1377	  "post_projector_4096d_rsa": 0.615,
1378	  "standalone_dino_cls_rsa": 0.692,
1379	  "standalone_dino_patch_mean_rsa": 0.631,
1380	  "key_findings": [
1381	    "DINOv2 \u2248 SigLIP in fused backbone (delta < 0.002)",
1382	    "Fused > either branch (complementary benefit)",
1383	    "Projector compresses 0.634\u21920.615",
1384	    "Standalone DINO cls > in-backbone DINOv2 (different extraction layer)"
1385	  ],
1386	  "result_file": "/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json"
1387	}
1388	
1389	=== d041_method_b_rsa ===
1390	METRICS: {
1391	  "trained_image_mean_peak": {
1392	    "layer": 12,
1393	    "rsa": 0.6282
1394	  },
1395	  "trained_last_preaction_peak": {
1396	    "layer": 12,
1397	    "rsa": 0.6425
1398	  },
1399	  "untrained_image_mean_peak": {
1400	    "layer": 0,
1401	    "rsa": 0.6117
1402	  },
1403	  "untrained_last_preaction_peak": {
1404	    "layer": 1,
1405	    "rsa": 0.6262
1406	  },
1407	  "baselines": {
1408	    "dino_cls": 0.6915,
1409	    "dino_patch_mean": 0.6307,
1410	    "siglip_projector": 0.615,
1411	    "clip_cls": 0.557
1412	  },
1413	  "bootstrap_best_vs_best_imgmean": {
1414	    "delta": 0.017,
1415	    "ci_95": [
1416	      -0.0002,
1417	      0.035
1418	    ],
1419	    "significant": false
1420	  },
1421	  "bootstrap_best_vs_best_lastpre": {
1422	    "delta": 0.016,
1423	    "ci_95": [
1424	      0.0001,
1425	      0.031
1426	    ],
1427	    "significant": "marginal"
1428	  },
1429	  "bootstrap_same_layer_L12_imgmean": {
1430	    "delta": 0.079,
1431	    "p": 0.0001
1432	  },
1433	  "bootstrap_same_layer_L12_lastpre": {
1434	    "delta": 0.047,
1435	    "p": 0.0001
1436	  },
1437	  "result_files": [
1438	    "/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json",
1439	    "/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json"
1440	  ]
1441	}
1442	
1443	=== plan_011_fulllayer_r2 ===
1444	METRICS: {
1445	  "trained_image_mean_peak": {
1446	    "layer": 8,
1447	    "mean_R2": 0.6553
1448	  },
1449	  "trained_last_preaction_peak": {
1450	    "layer": 13,
1451	    "mean_R2": 0.6779
1452	  },
1453	  "untrained_image_mean_peak": {
1454	    "layer": 0,
1455	    "mean_R2": 0.6403
1456	  },
1457	  "untrained_last_preaction_peak": {
1458	    "layer": 32,
1459	    "mean_R2": 0.6093
1460	  },
1461	  "bootstrap_best_vs_best": {
1462	    "image_mean": {
1463	      "delta": 0.0149,
1464	      "p": 0.006
1465	    },
1466	    "last_preaction": {
1467	      "delta": 0.0686,
1468	      "p": 0.0001
1469	    }
1470	  },
1471	  "bootstrap_same_layer": {
1472	    "image_mean_L8": {
1473	      "delta": 0.1229,
1474	      "p": 0.0001
1475	    },
1476	    "last_preaction_L13": {
1477	      "delta": 1.0071,
1478	      "p": 0.0001,
1479	      "note": "large delta suggests untrained L13 R2 near -0.33 (collapsed layer)"
1480	    }
1481	  },
1482	  "rsa_vs_r2_peak_comparison": {
1483	    "trained_imgmean": "RSA peak L12, R2 peak L8 \u2014 4-layer offset",
1484	    "trained_lastpre": "RSA peak L12, R2 peak L13 \u2014 near-aligned",
1485	    "untrained_imgmean": "RSA peak L0, R2 peak L0 \u2014 aligned",
1486	    "untrained_lastpre": "RSA peak L1, R2 peak L32 \u2014 maximally divergent"
1487	  },
1488	  "runtime_minutes": 19.5,
1489	  "result_path": "/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json"
1490	}
1491	NOTES: checkpoint_path: N/A (probe experiment, no persistent model)
1492	
1493	=== unified_action_probe ===
1494	METRICS: {
1495	  "hyperparams": {
1496	    "epochs": 50,
1497	    "patience": 5,
1498	    "lr": 0.001,
1499	    "hidden": 256,
1500	    "seed": 42,
1501	    "target": "a_{t+1}",
1502	    "target_verified": true,
1503	    "note": "All probes (original + unified) use same target feat[t]\u2192act[t+1]. Confirmed by code audit."
1504	  },
1505	  "results": {
1506	    "vla_last_preaction_L19": {
1507	      "mean_R2": 0.6711,
1508	      "overall_R2": 0.7234
1509	    },
1510	    "dino_cls": {
1511	      "mean_R2": 0.6343,
1512	      "overall_R2": 0.7012
1513	    },
1514	    "projector": {
1515	      "mean_R2": 0.6298,
1516	      "overall_R2": 0.6992
1517	    },
1518	    "vla_image_mean_L19": {
1519	      "mean_R2": 0.5986,
1520	      "overall_R2": 0.677
1521	    },
1522	    "clip_cls": {
1523	      "mean_R2": 0.5866,
1524	      "overall_R2": 0.6602
1525	    }
1526	  },
1527	  "bootstrap_pairwise": {
1528	    "projector_vs_dino": {
1529	      "delta": -0.0045,
1530	      "p": 0.557,
1531	      "significant": false
1532	    },
1533	    "projector_vs_clip": {
1534	      "delta": 0.043,
1535	      "p": 0.001,
1536	      "significant": true
1537	    },
1538	    "dino_vs_clip": {
1539	      "delta": 0.048,
1540	      "p": 0.001,
1541	      "significant": true
1542	    },
1543	    "projector_vs_vla_image_mean": {
1544	      "delta": 0.031,
1545	      "p": 0.001,
1546	      "significant": true
1547	    },
1548	    "last_preaction_vs_projector": {
1549	      "delta": 0.041,
1550	      "p": 0.002,
1551	      "significant": true
1552	    }
1553	  }
1554	}
1555	NOTES: D041 confirmed: unified_rsa_results.json uses 50 demos/task (Method B), consistent with all standalone baselines. n_demos verified from server-side h5 files. Key results: trained image_mean peak L12=0.6282, last_preaction peak L12=0.6425. D040 (L9-only 10-demo "readout RSA training degradation") superseded — L9 is not peak, trained peak is L12. Bootstrap CI (best-vs-best): image_mean Δ=+0.017 CI=[-0.0002,+0.035] n.s.; last_preaction Δ=+0.016 CI=[+0.0001,+0.031] marginal. Same-layer L12: image_mean Δ=+0.079 p<0.0001; last_preaction Δ=+0.047 p<0.0001. Training redistributes peak from L0→L12, does not create new information.
1556	
1557	=== lg_instruction_ablation ===
1558	NOTES: Duplicate of d021_instruction_ablation. Superseded by Director-specified ID. Cleaned up per D028.
1559	
1560	=== lg_output_head_analysis ===
1561	NOTES: Duplicate of d021_output_head_analysis. Superseded by Director-specified ID. Cleaned up per D028.
1562	
1563	=== plan_008_random_inst_control ===
1564	METRICS: {
1565	  "normal_peak_rsa": 0.4888,
1566	  "normal_peak_layer": 16,
1567	  "empty_peak_rsa": 0.4723,
1568	  "empty_peak_layer": 16,
1569	  "random_s0_peak_rsa": 0.4835,
1570	  "random_s0_peak_layer": 16,
1571	  "shuffled_peak_rsa": 0.4832,
1572	  "shuffled_peak_layer": 16,
1573	  "delta_empty_vs_normal": -0.0165,
1574	  "delta_random_s0_vs_normal": -0.0053,
1575	  "delta_shuffled_vs_normal": -0.0056,
1576	  "max_absolute_delta": 0.0165,
1577	  "instruction_invariant": true
1578	}
1579	NOTES: RSA instruction control completed. All 4 conditions peak at L16. Deltas vs normal: empty=-0.0165, random_s0=-0.0053, shuffled=-0.0056. Max |Δ|=0.0165 (well within 0.02 threshold). Instruction content is irrelevant to representation-action alignment structure. Result file: /root/autodl-tmp/vla-ssd/results/rsa/rsa_instruction_control_last_preaction.json
1580	
1581	=== untrained_last_preaction_probe ===
1582	METRICS: {
1583	  "untrained_last_preaction_L19_mean_R2": 0.325,
1584	  "trained_last_preaction_L19_mean_R2": 0.7309,
1585	  "projector_mean_R2": 0.706,
1586	  "delta_trained_vs_untrained_L19": 0.406,
1587	  "untrained_best_layer": "L32",
1588	  "untrained_best_R2": 0.6858,
1589	  "delta_best_vs_best": 0.0452,
1590	  "bootstrap_ci_trained_vs_untrained": {
1591	    "trained_L19_mean_R2": 0.7309,
1592	    "untrained_L32_mean_R2": 0.6858,
1593	    "observed_delta": 0.0452,
1594	    "ci_95": [
1595	      0.0321,
1596	      0.0585
1597	    ],
1598	    "p_value": 0.0001,
1599	    "ci_excludes_0": true,
1600	    "all_10_tasks_positive": true,
1601	    "per_task_delta_range": [
1602	      0.02,
1603	      0.083
1604	    ],
1605	    "n_bootstrap": 10000
1606	  },
1607	  "conclusion_summary": "Untrained best last_preaction R\u00b2=0.686 < trained 0.731 (\u0394=0.045, CI=[0.032,0.059], p<0.0001). Redistribution is training-dependent."
1608	}
1609	
1610	=== plan_009_cka_verification ===
1611	METRICS: {
1612	  "linear_cka": {
1613	    "untrained_img_mean_L23": 0.0894,
1614	    "trained_img_mean_L23": 0.0834,
1615	    "projector": 0.0809,
1616	    "dino": 0.0664,
1617	    "trained_last_preaction_L32": 0.127
1618	  },
1619	  "rdm_cka": {
1620	    "trained_img_mean_L23": 0.2599,
1621	    "projector": 0.2568,
1622	    "untrained_img_mean_L23": 0.2464,
1623	    "dino": 0.2408,
1624	    "trained_last_preaction_L32": 0.2898
1625	  },
1626	  "findings": "DINO lowest across all metrics (robust). last_preaction >> image_mean (redistribution confirmed). Projector vs trained gap compressed in CKA vs RSA (metric-dependent)."
1627	}
1628	
1629	=== p0_functional_action_probe ===
1630	METRICS: {
1631	  "projector": {
1632	    "mean_R2": 0.7063,
1633	    "overall_R2": 0.7169,
1634	    "grip_acc": 0.9221
1635	  },
1636	  "image_mean_trained_L19": {
1637	    "mean_R2": 0.6832,
1638	    "overall_R2": 0.6961,
1639	    "grip_acc": 0.9182
1640	  },
1641	  "image_mean_trained_L23": {
1642	    "mean_R2": 0.5736,
1643	    "overall_R2": 0.59,
1644	    "grip_acc": 0.8924
1645	  },
1646	  "llm_last_preaction_L19": {
1647	    "mean_R2": 0.7309,
1648	    "overall_R2": 0.7397,
1649	    "grip_acc": 0.9184
1650	  },
1651	  "untrained_image_mean_L0": {
1652	    "mean_R2": 0.7136,
1653	    "overall_R2": 0.7234,
1654	    "grip_acc": 0.9218
1655	  },
1656	  "bootstrap_ci_proj_vs_llm_last_preaction": {
1657	    "delta": -0.0246,
1658	    "ci_95": [
1659	      -0.04,
1660	      -0.009
1661	    ],
1662	    "p_value": 0.0014
1663	  },
1664	  "gate_judgment": "PASS \u2014 projector 0.706 \u2265 0.683 threshold. But LLM last_preaction (0.731) > projector (0.706), p=0.001.",
1665	  "result_path": "/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json"
1666	}
1667	NOTES: V1 完成但缺统计检验：(1) 缺 projector vs image_mean_L19 bootstrap CI (主比较 0.706 vs 0.683), (2) 缺 DINO probe, (3) untrained L10/L11 异常需排查。V2 修正版见 p0_functional_probe_v2。
1668	
1669	=== p0_bootstrap_ci_training_effect ===
1670	METRICS: {
1671	  "image_mean": {
1672	    "delta": 0.0206,
1673	    "ci_95": [
1674	      -0.0314,
1675	      0.0638
1676	    ],
1677	    "p_value": 0.2,
1678	    "significant": false
1679	  },
1680	  "last_preaction": {
1681	    "delta": 0.0076,
1682	    "ci_95": [
1683	      -0.0395,
1684	      0.0558
1685	    ],
1686	    "p_value": 0.37,
1687	    "significant": false
1688	  },
1689	  "n_bootstrap": 10000,
1690	  "n_tasks": 10,
1691	  "conclusion": "Both CIs include 0. Training effect not significant under task-level bootstrap. Claim 3 invariance holds.",
1692	  "result_path": "/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json"
1693	}
1694	
1695	=== p0_image_mean_rsa_verify ===
1696	METRICS: {
1697	  "trained_image_mean_rsa": 0.5014,
1698	  "trained_image_mean_peak_layer": 23,
1699	  "trained_last_preaction_rsa": 0.4876,
1700	  "untrained_image_mean_rsa": 0.4847,
1701	  "untrained_image_mean_peak_layer": 23,
1702	  "untrained_last_preaction_rsa": 0.4846,
1703	  "siglip_projector_rsa": 0.6153,
1704	  "gap_siglip_vs_image_mean": 0.1139,
1705	  "verdict": "Claim 2 HOLDS \u2014 image_mean RSA (0.5014) \u2248 last_preaction (0.4876), both far below SigLIP (0.6153). Aggregation artifact hypothesis rejected.",
1706	  "result_path": "/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json"
1707	}
1708	NOTES: 额外发现 (SSH worker): image_mean 聚合下 trained-untrained delta = +0.017 (L23)，比 last_preaction 的 +0.003 明显更大。Training 增强了 image token 表征的 action 相关性，但信号在 last_preaction (序列末位 token) 中被稀释。Trained 呈 inverted-U 曲线 (L0=0.45→L23=0.50→L32=0.44)，untrained 近乎平坦 (0.47-0.48)。Layer 0 trained=untrained=0.4509 (LLM 处理前一致)。
1709	
1710	=== plan_003_perlayer_degradation ===
1711	METRICS: {
1712	  "siglip_projector_rsa": 0.6153,
1713	  "perlayer_summary": {
1714	    "with_inst_trained": {
1715	      "peak_rsa": 0.4876,
1716	      "peak_layer": 9,
1717	      "proj_to_l1_drop": 0.2036,
1718	      "pattern": "non_monotonic"
1719	    },
1720	    "with_inst_untrained": {
1721	      "peak_rsa": 0.4846,
1722	      "peak_layer": 12,
1723	      "proj_to_l1_drop": 0.1512,
1724	      "pattern": "non_monotonic"
1725	    },
1726	    "no_inst_trained": {
1727	      "peak_rsa": 0.489,
1728	      "peak_layer": 30,
1729	      "proj_to_l1_drop": 0.2526,
1730	      "pattern": "predominantly_increasing"
1731	    },
1732	    "no_inst_untrained": {
1733	      "peak_rsa": 0.4802,
1734	      "peak_layer": 6,
1735	      "proj_to_l1_drop": 0.1374,
1736	      "pattern": "non_monotonic"
1737	    }
1738	  },
1739	  "total_degradation_range": [
1740	    0.126,
1741	    0.135
1742	  ],
1743	  "key_findings": [
1744	    "Proj\u2192L1 is the biggest RSA drop (0.13-0.25, ~20-40%)",
1745	    "L0 (embedding) is anomaly (RSA\u22480 for trained), structure recovers at L1",
1746	    "No-inst trained is unique: predominantly increasing L1\u2192L30",
1747	    "All LLM layers RSA >> DINO (0.388)",
1748	    "Total degradation ~0.13: best LLM layer still 0.13 below projector output"
1749	  ],
1750	  "result_path": "/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json"
1751	}
1752	
1753	=== d027_siglip_only_rsa ===
1754	METRICS: {
1755	  "siglip_projector_rsa": 0.6153,
1756	  "bootstrap_95_ci": [
1757	    0.5257,
1758	    0.6954
1759	  ],
1760	  "comparison": {
1761	    "siglip_projector": 0.6153,
1762	    "trained_with_inst": 0.4876,
1763	    "untrained_with_inst": 0.4846,
1764	    "untrained_no_inst": 0.4802,
1765	    "trained_no_inst": 0.489,
1766	    "dino": 0.388
1767	  },
1768	  "llm_degradation": "LLM reduces RSA from 0.615 (projector output) to ~0.488 (LLM hidden states)",
1769	  "gate_judgment": "PASS \u2014 SigLIP+projector RSA=0.6153 >> 0.45-0.50 threshold. Vision encoder is the source of action-relevant structure. LLM is not passthrough but actually degrades action alignment."
1770	}
1771	
1772	=== lg_shuffled_token_control ===
1773	NOTES: 实验从未实际启动：GPU 0%，输出目录不存在。Worker 可能在 Agent OOM kill 前未完成提交。加之 prompt format 不一致（bare task name vs formatted prompt），参考价值有限。标记 CANCELLED per D019 Reviewer 审查。
1774	
1775	=== lg_dino_extract ===
1776	METRICS: {
1777	  "tasks_completed": 10,
1778	  "tasks_total": 10,
1779	  "demos_per_task": 50,
1780	  "total_frames": 63728,
1781	  "feature_dim": 1024,
1782	  "dtype": "float16",
1783	  "feature_keys": [
1784	    "cls_token",
1785	    "patch_mean"
1786	  ],
1787	  "file_count": 10,
1788	  "total_size_mb": 234,
1789	  "extraction_fps": 183,
1790	  "extraction_time_s": 347.3
1791	}
1792	
1793	=== mvp2_action_probe ===
1794	METRICS: {
1795	  "copy_baseline_R2": 0.975,
1796	  "copy_baseline_per_task_mean_R2": 0.972,
1797	  "random_frame_baseline_R2": -0.91,
1798	  "random_frame_per_task_mean_R2": -0.977,
1799	  "copy_baseline_per_dim_R2": {
1800	    "dx": 0.979,
1801	    "dy": 0.988,
1802	    "dz": 0.982,
1803	    "drx": 0.971,
1804	    "dry": 0.966,
1805	    "drz": 0.991,
1806	    "grip": 0.949
1807	  },
1808	  "note": "LIBERO action autocorrelation very high \u2014 copy a_t predicts a_{t+1} at R\u00b2=0.975. Action probe R\u00b2 must be interpreted relative to this ceiling. Key comparison remains trained-vs-untrained \u0394, not absolute R\u00b2."
1809	}
1810	NOTES: Superseded by LIBERO-Goal pivot (D015). Sub-experiments (mvp2_action_trained/untrained/dino, mvp2_delta_trained/untrained/dino) all completed as DONE. Parent umbrella experiment killed per Director instruction.
1811	
1812	=== lg_extract_untrained_r2 ===
1813	NOTES: Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.
1814	
1815	=== lg_extract_trained_r2 ===
1816	NOTES: Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.
1817	
1818	=== lg_extract_untrained_r1 ===
1819	NOTES: Duplicate of original experiment lg_extract_untrained. Cleaned up per Director instruction.
1820	
1821	=== lg_extract_trained_r1 ===
1822	NOTES: Duplicate of original experiment lg_extract_trained. Cleaned up per Director instruction.
1823	
1824	=== mvp2_delta_dino ===
1825	METRICS: {
1826	  "overall_R2": 0.0604,
1827	  "per_task_mean_R2": 0.0609,
1828	  "gripper_accuracy": 0.57,
1829	  "per_dim_R2": {
1830	    "dx": 0.1744,
1831	    "dy": 0.2588,
1832	    "dz": 0.3745,
1833	    "drx": 0.084,
1834	    "dry": 0.0563,
1835	    "drz": 0.1765,
1836	    "gripper": 0.0365
1837	  },
1838	  "num_layers": 1,
1839	  "feature_dim": 1024
1840	}
1841	
1842	=== mvp2_delta_untrained ===
1843	METRICS: {
1844	  "best_layer": 32,
1845	  "per_task_mean_R2": 0.0485,
1846	  "overall_R2": 0.0485,
1847	  "per_dim_R2_at_best": {
1848	    "note": "L32 only layer with signal; L5-L28 all \u2248 0"
1849	  },
1850	  "layer_stability": "catastrophic \u2014 layers 5-28 all R\u00b2\u22480, only L1-L4 and L32 have signal",
1851	  "collapsed_layers": "5,6,7,8,9,10,11,12,13,14,15,17,18,26,28"
1852	}
1853	
1854	=== mvp2_delta_trained ===
1855	METRICS: {
1856	  "best_layer": 14,
1857	  "per_task_mean_R2": 0.0594,
1858	  "overall_R2": 0.0594,
1859	  "per_dim_R2_at_best": {
1860	    "dx": 0.1783,
1861	    "dy": 0.2665,
1862	    "dz": 0.3576,
1863	    "drx": 0.0942,
1864	    "dry": 0.0511,
1865	    "drz": 0.1735,
1866	    "gripper": 0.0357
1867	  },
1868	  "layer_stability": "stable plateau 0.04-0.06 across layers 5-30, smooth curve"
1869	}
1870	
1871	=== mvp2_action_dino ===
1872	METRICS: {
1873	  "overall_R2": 0.6689,
1874	  "per_task_mean_R2": 0.6759,
1875	  "gripper_accuracy": 0.9001,
1876	  "epochs": 17,
1877	  "training_time_seconds": 7.3,
1878	  "num_layers": 1,
1879	  "feature_dim": 1024,
1880	  "feature_key": "cls_token",
1881	  "probe_type": "MLP action probe (1024->256->7)"
1882	}
1883	
1884	=== mvp2_action_untrained ===
1885	METRICS: {
1886	  "best_layer": 32,
1887	  "per_task_mean_R2": 0.6164,
1888	  "overall_R2": 0.6067,
1889	  "gripper_accuracy": 0.8726,
1890	  "per_dim_R2_at_best": {
1891	    "dx": 0.5345,
1892	    "dy": 0.7067,
1893	    "dz": 0.5102,
1894	    "drx": 0.3658,
1895	    "dry": 0.2037,
1896	    "drz": 0.6361,
1897	    "gripper": 0.6066
1898	  },
1899	  "layers_unstable_range": "0.05-0.62 (many layers R\u00b2<0.25, probe likely not converging)",
1900	  "layer_stability": "very low \u2014 wildly oscillating, multiple collapsed layers"
1901	}
1902	
1903	=== mvp2_action_trained ===
1904	METRICS: {
1905	  "best_layer": 19,
1906	  "per_task_mean_R2": 0.6831,
1907	  "overall_R2": 0.677,
1908	  "gripper_accuracy": 0.8989,
1909	  "per_dim_R2_at_best": {
1910	    "dx": 0.5885,
1911	    "dy": 0.7629,
1912	    "dz": 0.5854,
1913	    "drx": 0.3712,
1914	    "dry": 0.1649,
1915	    "drz": 0.6654,
1916	    "gripper": 0.6815
1917	  },
1918	  "layers_stable_range": "0.45-0.68 (31/33 layers > untrained)",
1919	  "layer_stability": "high \u2014 smooth R\u00b2 curve across all 33 layers"
1920	}
1921	
1922	=== mvp_controlb_untrained ===
1923	METRICS: {
1924	  "mean_rho_across_layers": 0.0003,
1925	  "mean_task_rho_across_layers": 0.0003,
1926	  "best_layer_rho": 0.0085,
1927	  "best_layer": 1,
1928	  "mean_R2": -0.0092,
1929	  "mean_MAE": 0.2482,
1930	  "rho_std": 0.0034,
1931	  "constant_prediction_layers": 21,
1932	  "normal_experiment_rho": 0.933,
1933	  "rho_ratio_normal_vs_shuffled": 3110
1934	}
1935	
1936	=== mvp_controlb_trained ===
1937	METRICS: {
1938	  "mean_rho_across_layers": 0.0012,
1939	  "mean_task_rho_across_layers": 0.0011,
1940	  "best_layer_rho": 0.0123,
1941	  "best_layer": 8,
1942	  "mean_R2": -0.0041,
1943	  "mean_MAE": 0.2478,
1944	  "rho_std": 0.0051,
1945	  "all_layers_abs_rho_below_0.013": true,
1946	  "normal_experiment_rho": 0.955,
1947	  "rho_ratio_normal_vs_shuffled": 783
1948	}
1949	
1950	=== mvp_001 ===
1951	METRICS: {
1952	  "overall_verdict": "FAIL",
1953	  "gate1_rho_pass": true,
1954	  "gate2_delta_pass": false,
1955	  "gate3_dino_pass": true,
1956	  "best_layer": 4,
1957	  "best_per_task_mean_rho": 0.955,
1958	  "delta_rho_at_best": 0.0427,
1959	  "dino_per_task_mean_rho": 0.9008,
1960	  "collapsed_layers": 16,
1961	  "healthy_layers": 17,
1962	  "subtask_predicate_pivot_viable": false,
1963	  "subtask_predicate_reason": "all LIBERO predicates visually observable, DINO AUC=0.9717"
1964	}
1965	
1966	=== mvp_probe_untrained ===
1967	METRICS: {
1968	  "best_layer": 1,
1969	  "best_per_task_mean_rho": 0.9334,
1970	  "note": "Control C baseline \u2014 untrained model (random LLM + preserved SigLIP vision encoder) already achieves \u03c1=0.933, confirming temporal distance signal is vision-dominated"
1971	}
1972	
1973	=== mvp_probe_trained ===
1974	METRICS: {
1975	  "best_layer": 4,
1976	  "best_per_task_mean_rho": 0.955,
1977	  "best_pooled_rho": 0.9556,
1978	  "delta_rho_at_best": 0.0427,
1979	  "delta_rho_ci_95": [
1980	    0.0359,
1981	    0.0502
1982	  ],
1983	  "delta_rho_perm_p": 0,
1984	  "gate1_rho_pass": true,
1985	  "gate2_delta_pass": false,
1986	  "gate3_dino_pass": true,
1987	  "overall_verdict": "FAIL",
1988	  "collapsed_layers": 16,
1989	  "healthy_layers": 17,
1990	  "dino_threshold": 0.901,
1991	  "dino_per_task_mean_rho": 0.9008
1992	}
1993	
1994	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UCXM3HddsVF29jR77cHjoQ",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "08a1fb0e-cf3f-4184-8c53-17e9beeb906f"
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-18T19:28:48.406Z_

<details><summary>↩ Tool result · `toolu_015Qn8edhStYJU1SLScxDVLv`</summary>

```text
docs/paper/appendix.tex:219:Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
docs/paper/appendix.tex:676:\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
docs/paper/main.aux:310:\@writefile{lot}{\contentsline {table}{\numberline {21}{\ignorespaces Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times $, KL ratio $1.56\times $), consistent with graded, attention-ordered contribution to routing.}}{26}{table.21}\protected@file@percent }
docs/paper/main.aux:311:\newlabel{tab:specificity_control}{{21}{26}{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times $, KL ratio $1.56\times $), consistent with graded, attention-ordered contribution to routing}{table.21}{}}
docs/paper/corlabbrvnat.bst:17:%% This program can be redistributed and/or modified under the terms
docs/paper/method.tex:4:We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "898030a0-11ce-43c8-98bf-5c5d279ff8af"
}
```

</details>

---


### System

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Finding **/*.sty",
  "usage": {
    "total_tokens": 17544,
    "tool_uses": 5,
    "duration_ms": 8759
  },
  "last_tool_name": "Glob",
  "uuid": "e70d2373-e3a9-4a23-a65f-268884df2436",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 196_

<details open><summary>🔧 Tool call — Glob · `toolu_016LWxVktGUgNNGAxDnFSzXg`</summary>

```json
{
  "pattern": "**/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "13f87844-f050-4255-89ea-176466a94e3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MrptmQvPwzYSyR3aXrqZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1743,
      "cache_read_input_tokens": 15788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1743,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 197_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for primarily|preferentially|predominantly",
  "usage": {
    "total_tokens": 43286,
    "tool_uses": 24,
    "duration_ms": 25760
  },
  "last_tool_name": "Grep",
  "uuid": "3cfdeea5-1d56-4153-9310-cd293733cf18",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 198_

<details open><summary>🔧 Tool call — Grep · `toolu_017wRFdQXtxMT5XgNVvD1uSr`</summary>

```json
{
  "pattern": "primarily|preferentially|predominantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "f962d19c-f669-40d0-b3ea-76c6cb8dd870",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zZaXxMsSCa3xT7N7M6UDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 15933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27316,
        "ephemeral_1h_input_tokens": 0
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

_source line 199 · 2026-05-18T19:28:49.045Z_

<details><summary>↩ Tool result · `toolu_017wRFdQXtxMT5XgNVvD1uSr`</summary>

```text
docs/paper/conclusion.tex:4:We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
docs/paper/appendix.tex:432:This asymmetry confirms that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
docs/paper/introduction.tex:23:[Omitted long matching line]
docs/paper/discussion.tex:5:VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1aaa1898-e45e-4217-9af6-852a8bad2b7d"
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-18T19:28:48.986Z_

<details><summary>↩ Tool result · `toolu_016LWxVktGUgNNGAxDnFSzXg`</summary>

```text
docs/paper/corl_2026.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ee19059c-bc5a-4a51-97db-0fa67a695541"
}
```

</details>

---


### System

_source line 201_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Check available LaTeX tools",
  "usage": {
    "total_tokens": 17545,
    "tool_uses": 6,
    "duration_ms": 9112
  },
  "last_tool_name": "Bash",
  "uuid": "ede28aed-9192-4d26-96ec-5a60eea02203",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 202_

<details open><summary>🔧 Tool call — Bash · `toolu_01JEVqfE2rsi59fTEp3pgmKt`</summary>

```json
{
  "command": "which latexmk pdflatex xelatex lualatex bibtex 2>&1",
  "description": "Check available LaTeX tools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a5b41952-654a-4799-9478-ab81c98306fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MrptmQvPwzYSyR3aXrqZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1743,
      "cache_read_input_tokens": 15788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1743,
        "ephemeral_1h_input_tokens": 0
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

_source line 203 · 2026-05-18T19:28:49.377Z_

<details><summary>↩ Tool result · reported error · `toolu_01JEVqfE2rsi59fTEp3pgmKt`</summary>

```text
Exit code 1
/usr/bin/latexmk
/usr/bin/pdflatex
/usr/bin/lualatex
/usr/bin/bibtex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b4204acd-fd6e-49fa-bf76-432fdc0000ac",
  "tool_use_result": "Error: Exit code 1\n/usr/bin/latexmk\n/usr/bin/pdflatex\n/usr/bin/lualatex\n/usr/bin/bibtex"
}
```

</details>

---


### System

_source line 204_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Reading docs/paper/corl_example.tex",
  "usage": {
    "total_tokens": 51204,
    "tool_uses": 12,
    "duration_ms": 18536
  },
  "last_tool_name": "Read",
  "uuid": "c3adb0b7-48e4-4817-a48d-25907dfa99ca",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 205_

<details open><summary>🔧 Tool call — Read · `toolu_014boCwyBbbpkMHNxPssaszu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7c73ed26-8809-42b6-9456-572959cf96b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmkAsoovhrhMGn1irMkKPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7030,
      "cache_creation_input_tokens": 26522,
      "cache_read_input_tokens": 16936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26522,
        "ephemeral_1h_input_tokens": 0
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

_source line 206 · 2026-05-18T19:28:50.927Z_

<details><summary>↩ Tool result · `toolu_014boCwyBbbpkMHNxPssaszu`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Use this for the initial submission.
4	% \usepackage[final]{corl_2026} % Uncomment for the camera-ready ``final'' version.
5	% \usepackage[preprint]{corl_2026} % Uncomment for pre-prints (e.g., arxiv); This is like ``final'', but will remove the CORL footnote.
6	
7	\title{Formatting Instructions for CoRL 2026 Camera-Ready}
8	
9	% The \author macro works with any number of authors. There are two
10	% commands used to separate the names and addresses of multiple
11	% authors: \And and \AND.
12	%
13	% Using \And between authors leaves it to LaTeX to determine where to
14	% break the lines. Using \AND forces a line break at that point. So,
15	% if LaTeX puts 3 of 4 authors names on the first line, and the last
16	% on the second line, try using \AND instead of \And before the third
17	% author name.
18	
19	% NOTE: authors will be visible only in the camera-ready and preprint versions (i.e., when using the option 'final' or 'preprint'). 
20	% 	For the initial submission the authors will be anonymized.
21	
22	\author{
23	  Jane E.~Doe\\
24	  Department of Electrical Engineering and Computer Sciences\\
25	  University of California Berkeley 
26	  United States\\
27	  \texttt{janedoe@berkeley.edu} \\
28	  %% examples of more authors
29	  %% \And
30	  %% Coauthor \\
31	  %% Affiliation \\
32	  %% Address \\
33	  %% \texttt{email} \\
34	  %% \AND
35	  %% Coauthor \\
36	  %% Affiliation \\
37	  %% Address \\
38	  %% \texttt{email} \\
39	  %% \And
40	  %% Coauthor \\
41	  %% Affiliation \\
42	  %% Address \\
43	  %% \texttt{email} \\
44	  %% \And
45	  %% Coauthor \\
46	  %% Affiliation \\
47	  %% Address \\
48	  %% \texttt{email} \\
49	}
50	
51	
52	\begin{document}
53	\maketitle
54	
55	%===============================================================================
56	
57	\begin{abstract}
58	    The purpose of this document is to provide both the basic paper template and submission guidelines. Abstracts should be a single paragraph, between 4--6 sentences long, ideally. Gross violations will trigger corrections at the camera-ready phase.
59	\end{abstract}
60	
61	% Two or three meaningful keywords should be added here
62	\keywords{CoRL, Robots, Learning} 
63	
64	%===============================================================================
65	
66	\section{Introduction}
67		
68	    Submission to CoRL 2026 will be entirely electronic, via a web site (not email). Information about the submission process and \LaTeX{} templates are available on the conference web site at \url{https://corl.org/}. For camera ready submission, use the \texttt{final} option for the \texttt{\textbackslash usepackage} command. 
69	
70	%===============================================================================
71	
72	\section{Citations}
73	\label{sec:citations}
74	
75		Citations can be made using either \textbackslash citep\{\} or \textbackslash citet\{\}, depending from the appropriateness. To avoid the citation moving to the next line, it is often a good practice to replace the space before with a tilde (\~{}) character.
76		Example 1: ``CoRL is the best conference ever~\citep{Gauss1857}.''
77		Example 2: ``\citet{Lagrange1788} proved, both theoretically and numerically, that CoRL is the best conference ever.''
78		
79	%===============================================================================
80	
81	\section{Experimental Results}
82	\label{sec:result}
83	
84		Nam dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi auctor lorem non justo.
85		Nam lacus libero, pretium at, lobortis vitae, ultricies et, tellus. Donec aliquet, tortor sed accumsan
86		bibendum, erat ligula aliquet magna, vitae ornare odio metus a mi. Morbi ac orci et nisl hendrerit
87		mollis. 
88	
89		Suspendisse ut massa. Cras nec ante. Pellentesque a nulla. Cum sociis natoque penatibus
90		et magnis dis parturient montes, nascetur ridiculus mus. Aliquam tincidunt urna. Nulla ullamcorper
91		vestibulum turpis. Pellentesque cursus luctus mauris.
92		
93		Nulla malesuada porttitor diam. Donec felis erat, congue non, volutpat at, tincidunt tristique, libero.
94		Vivamus viverra fermentum felis. Donec nonummy pellentesque ante. Phasellus adipiscing semper 	elit. 
95		Proin fermentum massa ac quam. Sed diam turpis, molestie vitae, placerat a, molestie nec, leo.
96		Maecenas lacinia. Nam ipsum ligula, eleifend at, accumsan nec, suscipit a, ipsum. Morbi blandit
97		ligula feugiat magna. Nunc eleifend consequat lorem. Sed lacinia nulla vitae enim. Pellentesque tin-
98		cidunt purus vel magna. Integer non enim. Praesent euismod nunc eu purus. Donec bibendum quam
99		in tellus. Nullam cursus pulvinar lectus. Donec et mi. Nam vulputate metus eu enim. Vestibulum
100		pellentesque felis eu massa.
101		Quisque ullamcorper placerat ipsum. Cras nibh. Morbi vel justo vitae lacus tincidunt ultrices. 
102		
103		Lorem
104		ipsum dolor sit amet, consectetuer adipiscing elit. In hac habitasse platea dictumst. Integer tempus
105		convallis augue. Etiam facilisis. Nunc elementum fermentum wisi. Aenean placerat. Ut imperdiet,
106		enim sed gravida sollicitudin, felis odio placerat quam, ac pulvinar elit purus eget enim. Nunc vitae
107		tortor. Proin tempus nibh sit amet nisl. Vivamus quis tortor vitae risus porta vehicula.
108	
109	%===============================================================================
110	
111	\section{Conclusion}
112	\label{sec:conclusion}
113	
114		Nam dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi auctor lorem non justo.
115		Nam lacus libero, pretium at, lobortis vitae, ultricies et, tellus. Donec aliquet, tortor sed accumsan
116		bibendum, erat ligula aliquet magna, vitae ornare odio metus a mi. Morbi ac orci et nisl hendrerit
117		mollis. Suspendisse ut massa. Cras nec ante. Pellentesque a nulla. Cum sociis natoque penatibus
118		et magnis dis parturient montes, nascetur ridiculus mus. Aliquam tincidunt urna. Nulla ullamcorper
119		vestibulum turpis. Pellentesque cursus luctus mauris.
120		Nulla malesuada porttitor diam. Donec felis erat, congue non, volutpat at, tincidunt tristique, libero.
121		Vivamus viverra fermentum felis. Donec nonummy pellentesque ante. Phasellus adipiscing semper
122		elit. Proin fermentum massa ac quam. Sed diam turpis, molestie vitae, placerat a, molestie nec, leo.
123		Maecenas lacinia. Nam ipsum ligula, eleifend at, accumsan nec, suscipit a, ipsum. Morbi blandit
124		ligula feugiat magna. Nunc eleifend consequat lorem. Sed lacinia nulla vitae enim. Pellentesque tin-
125		cidunt purus vel magna. Integer non enim. Praesent euismod nunc eu purus. Donec bibendum quam
126		in tellus. Nullam cursus pulvinar lectus. Donec et mi. Nam vulputate metus eu enim. Vestibulum
127		pellentesque felis eu massa.
128		Quisque ullamcorper placerat ipsum. Cras nibh. Morbi vel justo vitae lacus tincidunt ultrices. Lorem
129		ipsum dolor sit amet, consectetuer adipiscing elit. In hac habitasse platea dictumst. Integer tempus
130		convallis augue. Etiam facilisis. Nunc elementum fermentum wisi. Aenean placerat. Ut imperdiet,
131		enim sed gravida sollicitudin, felis odio placerat quam, ac pulvinar elit purus eget enim. Nunc vitae
132		tortor. Proin tempus nibh sit amet nisl. Vivamus quis tortor vitae risus porta vehicula.
133	
134	%===============================================================================
135	
136	\clearpage
137	% The acknowledgments are automatically included only in the final and preprint versions of the paper.
138	\acknowledgments{If a paper is accepted, the final camera-ready version will (and probably should) include acknowledgments. All acknowledgments go at the end of the paper, including thanks to reviewers who gave useful comments, to colleagues who contributed to the ideas, and to funding agencies and corporate sponsors that provided financial support.}
139	
140	%===============================================================================
141	
142	% no \bibliographystyle is required, since the corl style is automatically used.
143	\bibliography{example}  % .bib
144	
145	\end{document}
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "17177e25-9ae3-4b8b-b930-8d08cab4b571"
}
```

</details>

---


### System

_source line 207_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Compile LaTeX paper with latexmk",
  "usage": {
    "total_tokens": 17858,
    "tool_uses": 7,
    "duration_ms": 12396
  },
  "last_tool_name": "Bash",
  "uuid": "c7c945ab-2219-4f0d-a126-20eb7ca3cac4",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 208_

<details open><summary>🔧 Tool call — Bash · `toolu_01GQn14zkZBwBAXPuLF8R4sH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1",
  "description": "Compile LaTeX paper with latexmk",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5d2a3396-5b0e-4556-a409-1eba31d5949f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xdX9gNkpLqrM6HGXn2nqr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 17531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 311,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 209_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for exclusive",
  "usage": {
    "total_tokens": 47516,
    "tool_uses": 25,
    "duration_ms": 30043
  },
  "last_tool_name": "Grep",
  "uuid": "feebe441-cc8b-4702-9844-942731c52c4d",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 210_

<details open><summary>🔧 Tool call — Grep · `toolu_017TaPb2nXKmc4TmScur1ZDh`</summary>

```json
{
  "pattern": "exclusive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "dad695b9-1994-4adc-91af-59f4a2154977",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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

_source line 211 · 2026-05-18T19:28:53.327Z_

<details><summary>↩ Tool result · `toolu_017TaPb2nXKmc4TmScur1ZDh`</summary>

```text
docs/paper/related_work.tex:29:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "49c705c2-ba4d-4cc6-879a-05a67a71a504"
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-18T19:28:53.859Z_

<details><summary>↩ Tool result · `toolu_01GQn14zkZBwBAXPuLF8R4sH`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  introduction.tex
Category 'changed_user':
  introduction.tex

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo)) (./corl_2026.sty
(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/color.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty))
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/units/nicefrac.sty
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./main.aux) (/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii

[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* verbose mode - [ newgeometry ] result:
* driver: 
* paper: letterpaper
* layout: &lt;same size as paper>
* layoutoffset:(h,v)=(0.0pt,0.0pt)
* modes: 
* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)
* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)
* \paperwidth=614.295pt
* \paperheight=794.96999pt
* \textwidth=397.48499pt
* \textheight=650.43pt
* \oddsidemargin=36.13501pt
* \evensidemargin=36.13501pt
* \topmargin=-37.0pt
* \headheight=12.0pt
* \headsep=25.0pt
* \topskip=10.0pt
* \footskip=30.0pt
* \marginparwidth=65.0pt
* \marginparsep=11.0pt
* \columnsep=10.0pt
* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
* \hoffset=0.0pt
* \voffset=0.0pt
* \mag=1000
* \@twocolumnfalse
* \@twosidefalse
* \@mparswitchfalse
* \@reversemarginfalse
* (1in=72.27pt=25.4mm, 1cm=28.453pt)

(./main.out) (./main.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
*geometry* verbose mode - [ preamble ] result:
* driver: pdftex
* paper: letterpaper
* layout: &lt;same size as paper>
* layoutoffset:(h,v)=(0.0pt,0.0pt)
* modes: 
* h-part:(L,W,R)=(108.405pt, 397.48499pt, 108.40501pt)
* v-part:(T,H,B)=(72.26999pt, 650.43pt, 72.27pt)
* \paperwidth=614.295pt
* \paperheight=794.96999pt
* \textwidth=397.48499pt
* \textheight=650.43pt
* \oddsidemargin=36.13501pt
* \evensidemargin=36.13501pt
* \topmargin=-37.0pt
* \headheight=12.0pt
* \headsep=25.0pt
* \topskip=10.0pt
* \footskip=30.0pt
* \marginparwidth=65.0pt
* \marginparsep=11.0pt
* \columnsep=10.0pt
* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
* \hoffset=0.0pt
* \voffset=0.0pt
* \mag=1000
* \@twocolumnfalse
* \@twosidefalse
* \@mparswitchfalse
* \@reversemarginfalse
* (1in=72.27pt=25.4mm, 1cm=28.453pt)

(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) (./abstract.tex)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1phv.fd) (./introduction.tex
Underfull \vbox (badness 3396) has occurred while \output is active [1{/var/lib
/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/
enc/dvips/base/8r.enc}]) (./related_work.tex [2]) (./method.tex [3])
(./experiments.tex [4]
Underfull \vbox (badness 1960) has occurred while \output is active [5]
[6 <./figures/fig_32layer_attention.pdf>]) (./discussion.tex [7])
(./conclusion.tex) (./main.bbl [8 <./figures/fig3.pdf>] [9]
Underfull \hbox (badness 1173) in paragraph at lines 159--166
\T1/ptm/m/n/10 tures from Claude 3 Son-net.  \T1/ptm/m/it/10 Trans-former Cir-c
uits Thread\T1/ptm/m/n/10 , 2024.  URL [][]$\T1/cmtt/m/n/10 https : / /
[10]
Underfull \hbox (badness 10000) in paragraph at lines 262--268
[]\T1/ptm/m/n/10 nostalgebraist.  in-ter-pret-ing GPT: the logit lens.  Less-Wr
ong blog post,

Underfull \hbox (badness 10000) in paragraph at lines 262--268
\T1/ptm/m/n/10 2020.  URL [][]$\T1/cmtt/m/n/10 https : / / www . lesswrong . co
m / posts / AcKRB8wDpdaN6v6ru /
) (./appendix.tex [11] [12 <./figures/fig6.pdf>]
Underfull \vbox (badness 2042) has occurred while \output is active [13 <./figu
res/fig2.pdf> <./figures/fig_rsa_perlayer_curve.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.

[14 <./figures/fig_action_r2_threecond.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[15 <./figures/fig_random_subset_ablation.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \vbox (badness 6063) has occurred while \output is active [16 <./figu
res/fig_dose_response.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \vbox (badness 4254) has occurred while \output is active [17]
[18 <./figures/fig_ood_diagnostics.pdf> <./figures/fig_linear_vs_mlp_probe.pdf>
] [19 <./figures/fig4.pdf> <./figures/fig5.pdf>] [20 <./figures/fig7.pdf>]
[21]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[22]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \vbox (badness 1917) has occurred while \output is active [23 <./figu
res/fig_probe_conditions.pdf> <./figures/fig_l1_stacked_bar.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \vbox (badness 10000) has occurred while \output is active [24 <./fig
ures/fig_multi_layer_attn.pdf>]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 638.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 638.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 638.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

) [25] [26] (./main.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (26 pages, 554950 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "567b216b-79ab-4b94-a8e8-a512501e6d01"
}
```

</details>

---


### System

_source line 213_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for sole ",
  "usage": {
    "total_tokens": 47517,
    "tool_uses": 26,
    "duration_ms": 30997
  },
  "last_tool_name": "Grep",
  "uuid": "6e20e8e3-acc2-4112-9ffa-33de4ba0b292",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — Grep · `toolu_01RruivNbebWuqgqYPUwMJ4z`</summary>

```json
{
  "pattern": "sole ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "22243d35-12f5-4d71-8d75-aa490182c42f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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

_source line 215 · 2026-05-18T19:28:54.291Z_

<details><summary>↩ Tool result · `toolu_01RruivNbebWuqgqYPUwMJ4z`</summary>

```text
docs/paper/related_work.tex:25:Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
docs/paper/experiments.tex:26:The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
docs/paper/abstract.tex:4:First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c19c19ee-620c-4aab-941d-caa30009080a"
}
```

</details>

---


### System

_source line 216_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for only.*responsible|responsible.*only",
  "usage": {
    "total_tokens": 47518,
    "tool_uses": 27,
    "duration_ms": 31930
  },
  "last_tool_name": "Grep",
  "uuid": "4d605f3d-4e90-4da7-ab95-7a8497753649",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 217_

<details open><summary>🔧 Tool call — Grep · `toolu_01TyZ6LazjrhdWsYAEBSp357`</summary>

```json
{
  "pattern": "only.*responsible|responsible.*only",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "97e817cb-58e6-4f71-bdaa-9799413fd47b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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

_source line 218 · 2026-05-18T19:28:55.208Z_

<details><summary>↩ Tool result · `toolu_01TyZ6LazjrhdWsYAEBSp357`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0ff5b737-1aa3-47c0-9066-69ffb4ba019f"
}
```

</details>

---


### System

_source line 219_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for trajectory.level specificity|trajectory specifici…",
  "usage": {
    "total_tokens": 47519,
    "tool_uses": 28,
    "duration_ms": 32851
  },
  "last_tool_name": "Grep",
  "uuid": "0ee7f201-28ab-40b4-b83f-b59b371f315e",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 220_

<details open><summary>🔧 Tool call — Grep · `toolu_01CdohypF73uQXjKuD9NMDS1`</summary>

```json
{
  "pattern": "trajectory.level specificity|trajectory specificity",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0e70bfd2-c615-4bd8-8e79-ca5773e202a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 221_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all \\label definitions from tex files with line numbers",
  "usage": {
    "total_tokens": 53985,
    "tool_uses": 13,
    "duration_ms": 24151
  },
  "last_tool_name": "Bash",
  "uuid": "e412afd0-784c-4aee-894e-f864c2539a36",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 222_

<details open><summary>🔧 Tool call — Bash · `toolu_01AL9XKJpTuqmXLbJT8ewXzB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n '\\\\label{' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\label definitions from tex files with line numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ca0b8510-b390-4c5b-9cea-06925c038c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5d9Dp9k2JLtcCj4zc3qbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9808,
      "cache_read_input_tokens": 43458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9808,
        "ephemeral_1h_input_tokens": 0
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

_source line 223 · 2026-05-18T19:28:56.128Z_

<details><summary>↩ Tool result · `toolu_01CdohypF73uQXjKuD9NMDS1`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a7dc2af0-5c8f-4938-8e31-e11682eed53a"
}
```

</details>

---


### System

_source line 224_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for ing\\.",
  "usage": {
    "total_tokens": 47520,
    "tool_uses": 29,
    "duration_ms": 33816
  },
  "last_tool_name": "Grep",
  "uuid": "94cc29ae-3c3e-41b1-8590-45b46f543801",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 225_

<details open><summary>🔧 Tool call — Grep · `toolu_018qe6bMXoNPRVwLUjwKD7vm`</summary>

```json
{
  "pattern": "ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "00b0d260-8809-4095-a7ec-bff38c37d0d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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

_source line 226 · 2026-05-18T19:28:56.625Z_

<details><summary>↩ Tool result · `toolu_01AL9XKJpTuqmXLbJT8ewXzB`</summary>

```text
=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
2:\label{sec:introduction}
=== related_work.tex ===
1:\section{Related Work}\label{sec:related_work}
=== method.tex ===
2:\label{sec:method}
8:\label{sec:model_data}
17:\label{sec:repr_extraction}
31:\label{sec:cross_instruction_probes}
39:\label{sec:attention_analysis}
46:\label{sec:rsa}
55:\label{sec:probes}
=== experiments.tex ===
2:\label{sec:experiments}
5:\label{sec:setup}
16:\label{sec:token_specialization}
31:\label{tab:dense_routing_main}
49:\label{sec:learned_routing}
85:\label{tab:routing_gradient}
102:\label{fig:attention_profile}
107:\label{sec:nonmonotonic}
126:\label{tab:rsa_overview}
150:\label{fig:layer_curves}
=== discussion.tex ===
2:\label{sec:discussion}
=== conclusion.tex ===
2:\label{sec:conclusion}
=== appendix.tex ===
4:\label{sec:appendix}
7:\label{sec:cka_appendix}
19:\label{sec:metric_sensitivity_appendix}
33:\label{fig:metric_comparison}
37:\label{sec:branch_split_appendix}
45:\label{sec:rsa_bar_appendix}
53:\label{fig:rsa_bar}
57:\label{sec:rsa_perlayer_appendix}
63:\label{fig:rsa_perlayer_curve}
67:\label{sec:action_r2_threecond}
81:\label{fig:action_r2_threecond}
85:\label{sec:random_subset_ablation}
95:\label{fig:random_subset_ablation}
99:\label{sec:action_trajectory}
115:\label{tab:perhead_bootstrap}
138:\label{fig:dose_response}
144:\label{tab:dose_response}
165:\label{tab:counterfactual}
184:\label{tab:action_shift_perdim}
197:\label{sec:ood_diagnostics}
210:\label{fig:ood_diagnostics}
214:\label{sec:linear_probe}
227:\label{fig:linear_vs_mlp}
231:\label{sec:probe_bars_appendix}
239:\label{fig:probe_bars}
243:\label{sec:instruction_invariance_appendix}
252:\label{fig:factorial}
256:\label{sec:additional_rsa}
262:\label{sec:cross_benchmark_appendix}
279:\label{fig:cross_benchmark}
283:\label{sec:spatial_cross_instruction}
292:\label{tab:spatial_cross_instruction}
307:\label{sec:robustness_appendix}
310:\label{sec:metric_invariance}
317:\label{tab:metric_invariance}
332:\label{sec:perdof}
338:\label{sec:permutation}
343:\label{sec:seed_sensitivity}
353:\label{tab:seed_sensitivity}
371:\label{sec:demo_sensitivity}
381:\label{tab:demo_sensitivity}
398:\label{sec:training_effects_appendix}
405:\label{tab:training_effects}
428:\label{sec:training_effect_summary}
437:\label{tab:training_effect_summary}
454:\label{sec:routing_appendix}
457:\label{sec:dense_routing}
466:\label{tab:dense_routing}
486:\label{sec:loocv}
492:\label{sec:qa_probe}
499:\label{tab:qa_probe}
513:\label{sec:probe_profiles}
519:\label{fig:probe_conditions_appendix}
523:\label{sec:attention_pattern}
532:\label{fig:attention_appendix}
536:\label{sec:multilayer_attention}
545:\label{fig:multilayer_attention}
551:\label{tab:multilayer_attention}
568:\label{sec:threshold_sensitivity}
576:\label{tab:threshold_sensitivity}
592:\label{sec:attention_decomp}
599:\label{tab:attention_decomp}
614:\label{sec:per_dim_mae}
621:\label{tab:per_dim_mae}
639:\label{sec:per_task_r2}
646:\label{tab:per_task_r2}
669:\label{sec:specificity_control}
677:\label{tab:specificity_control}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "a9f25631-4e75-416d-8ac1-ac8a5880d573"
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-18T19:28:57.092Z_

<details><summary>↩ Tool result · `toolu_018qe6bMXoNPRVwLUjwKD7vm`</summary>

```text
docs/paper/related_work.tex:16:Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:114:\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
docs/paper/appendix.tex:267:The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
docs/paper/appendix.tex:273:This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
docs/paper/appendix.tex:550:\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
docs/paper/appendix.tex:676:\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "2045580a-6f15-44b4-99e2-76fe617db416"
}
```

</details>

---


### System

_source line 228_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all \\ref, \\eqref, \\autoref, \\cref, \\Cref from tex files",
  "usage": {
    "total_tokens": 53986,
    "tool_uses": 14,
    "duration_ms": 26171
  },
  "last_tool_name": "Bash",
  "uuid": "db818abb-7a27-4b9b-a6d3-3e2c29835ced",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 229_

<details open><summary>🔧 Tool call — Bash · `toolu_018Y35xvmH4vYTiqAsphuTX9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\ref, \\eqref, \\autoref, \\cref, \\Cref from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ffa85ffb-b528-48c6-8b51-5d3479748b00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5d9Dp9k2JLtcCj4zc3qbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9808,
      "cache_read_input_tokens": 43458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9808,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 230_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for , (demonstrating|highlighting|showcasing|indicati…",
  "usage": {
    "total_tokens": 47521,
    "tool_uses": 30,
    "duration_ms": 35757
  },
  "last_tool_name": "Grep",
  "uuid": "6afb2821-ae72-45ce-b78f-429df1e25c07",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 231_

<details open><summary>🔧 Tool call — Grep · `toolu_01MEtUZtP86XU43QLgyUWgz3`</summary>

```json
{
  "pattern": ", (demonstrating|highlighting|showcasing|indicating|suggesting|confirming|showing|revealing|establishing|underscoring)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e83ff35c-75c6-4f40-aa73-52776f31afb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 232_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count errors in log",
  "usage": {
    "total_tokens": 23207,
    "tool_uses": 8,
    "duration_ms": 19018
  },
  "last_tool_name": "Bash",
  "uuid": "1b8f3aff-524e-4e29-ab3d-b07a3a5d32a4",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 233_

<details open><summary>🔧 Tool call — Bash · `toolu_0126C912YqS8kYknGbRL6RQt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"^!\" main.log",
  "description": "Count errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "85a2bd4f-9b29-4069-8e86-d63911d290a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 234 · 2026-05-18T19:28:59.028Z_

<details><summary>↩ Tool result · `toolu_01MEtUZtP86XU43QLgyUWgz3`</summary>

```text
docs/paper/related_work.tex:29:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
docs/paper/conclusion.tex:4:We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
docs/paper/discussion.tex:20:The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
docs/paper/appendix.tex:25:At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
docs/paper/appendix.tex:47:Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:110:The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
docs/paper/appendix.tex:238:\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
docs/paper/appendix.tex:246:Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
docs/paper/appendix.tex:251:\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$, confirming visually grounded action geometry.}
docs/paper/appendix.tex:347:Peak layer concentrates in the L8--L10 region ($4/5$ seeds), confirming the inverted-U shape is not a seed artifact.
docs/paper/appendix.tex:374:The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions, confirming high stability.
docs/paper/appendix.tex:436:\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large, confirming that training targets readout-token information integration.}
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
docs/paper/appendix.tex:489:Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31, confirming perfect generalization.
docs/paper/appendix.tex:571:Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%, confirming that the 50\% threshold is not a boundary-sensitive choice.
docs/paper/appendix.tex:620:\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$), indicating instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
docs/paper/appendix.tex:645:\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$), confirming that instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "86f944b6-8b13-4d1b-8bd9-61ddfee7dc87"
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-18T19:28:59.277Z_

<details><summary>↩ Tool result · `toolu_0126C912YqS8kYknGbRL6RQt`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e0faa38a-2230-49ca-9575-0e2a788a6739"
}
```

</details>

---


### System

_source line 236_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for the primary",
  "usage": {
    "total_tokens": 47522,
    "tool_uses": 31,
    "duration_ms": 36470
  },
  "last_tool_name": "Grep",
  "uuid": "9d9f3b40-886c-45be-8da6-8610a5a98f5c",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 237_

<details open><summary>🔧 Tool call — Grep · `toolu_01L4YcAA7u4WWwXSXA4YmxL1`</summary>

```json
{
  "pattern": "the primary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3ef902d9-28a9-4f62-b04e-fac9e8dadd52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyF9ZXiwXDy6Y7N1V5Npkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39228,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39228,
        "ephemeral_1h_input_tokens": 0
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

_source line 238 · 2026-05-18T19:28:58.624Z_

<details><summary>↩ Tool result · `toolu_018Y35xvmH4vYTiqAsphuTX9`</summary>

```text
=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
20:\ref{sec:cka_appendix}
=== related_work.tex ===
=== method.tex ===
64:\ref{sec:cka_appendix}
64:\ref{sec:nonmonotonic}
=== experiments.tex ===
8:\ref{sec:repr_extraction}
9:\ref{sec:model_data}
10:\ref{sec:rsa}
11:\ref{sec:probes}
12:\ref{sec:linear_probe}
18:\ref{sec:cross_instruction_probes}
21:\ref{tab:dense_routing_main}
22:\ref{sec:instruction_invariance_appendix}
25:\ref{sec:loocv}
26:\ref{sec:qa_probe}
26:\ref{sec:cross_benchmark_appendix}
30:\ref{sec:dense_routing}
52:\ref{tab:routing_gradient}
52:\ref{fig:attention_profile}
55:\ref{fig:attention_profile}
57:\ref{sec:threshold_sensitivity}
60:\ref{fig:probe_conditions_appendix}
61:\ref{sec:training_effect_summary}
61:\ref{sec:action_r2_threecond}
65:\ref{tab:rsa_overview}
66:\ref{sec:random_subset_ablation}
68:\ref{sec:repr_extraction}
68:\ref{tab:per_task_r2}
71:\ref{tab:attention_decomp}
71:\ref{tab:per_dim_mae}
71:\ref{sec:action_trajectory}
74:\ref{fig:dose_response}
74:\ref{sec:action_trajectory}
78:\ref{tab:counterfactual}
80:\ref{sec:action_trajectory}
84:\ref{tab:dense_routing_main}
101:\ref{fig:probe_conditions_appendix}
110:\ref{tab:rsa_overview}
111:\ref{sec:cka_appendix}
114:\ref{fig:layer_curves}
114:\ref{sec:seed_sensitivity}
115:\ref{tab:rsa_overview}
116:\ref{sec:cka_appendix}
119:\ref{tab:training_effects}
121:\ref{sec:cross_benchmark_appendix}
125:\ref{sec:cka_appendix}
141:\ref{sec:seed_sensitivity}
=== discussion.tex ===
11:\ref{fig:dose_response}
12:\ref{tab:counterfactual}
18:\ref{tab:specificity_control}
28:\ref{sec:ood_diagnostics}
28:\ref{sec:cka_appendix}
=== conclusion.tex ===
=== appendix.tex ===
21:\ref{fig:metric_comparison}
47:\ref{fig:rsa_bar}
47:\ref{tab:rsa_overview}
69:\ref{fig:action_r2_threecond}
87:\ref{sec:learned_routing}
101:\ref{tab:action_shift_perdim}
108:\ref{tab:perhead_bootstrap}
131:\ref{tab:dose_response}
131:\ref{fig:dose_response}
199:\ref{sec:model_data}
233:\ref{fig:probe_bars}
245:\ref{fig:factorial}
265:\ref{fig:cross_benchmark}
285:\ref{tab:spatial_cross_instruction}
291:\ref{tab:dense_routing_main}
312:\ref{tab:metric_invariance}
346:\ref{tab:seed_sensitivity}
373:\ref{tab:demo_sensitivity}
400:\ref{tab:training_effects}
430:\ref{tab:training_effect_summary}
459:\ref{tab:dense_routing}
494:\ref{tab:qa_probe}
525:\ref{fig:attention_appendix}
531:\ref{tab:routing_gradient}
538:\ref{tab:multilayer_attention}
538:\ref{fig:attention_profile}
550:\ref{fig:attention_profile}
550:\ref{tab:routing_gradient}
571:\ref{tab:threshold_sensitivity}
594:\ref{tab:attention_decomp}
616:\ref{tab:per_dim_mae}
616:\ref{tab:action_shift_perdim}
641:\ref{tab:per_task_r2}
645:\ref{sec:learned_routing}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "39024434-d8e6-4589-82bb-497724dba8af"
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-18T19:28:59.745Z_

<details><summary>↩ Tool result · `toolu_01L4YcAA7u4WWwXSXA4YmxL1`</summary>

```text
docs/paper/conclusion.tex:5:Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
docs/paper/abstract.tex:8:Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
docs/paper/introduction.tex:21:Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
docs/paper/introduction.tex:23:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "eed33542-9754-454a-91c9-638ad214c1b7"
}
```

</details>

---


### System

_source line 240_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Check undefined references",
  "usage": {
    "total_tokens": 23209,
    "tool_uses": 9,
    "duration_ms": 19928
  },
  "last_tool_name": "Bash",
  "uuid": "e0a3bcc5-d216-4226-a1fd-117ad000b7d1",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 241_

<details open><summary>🔧 Tool call — Bash · `toolu_01NFEALTsLfmZ4mhwTB8wBZn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"undefined\" main.log 2>&1",
  "description": "Check undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0eeaf478-b425-402b-b1c7-1e8c5871a0aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 242_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all \\cite variants from tex files",
  "usage": {
    "total_tokens": 53987,
    "tool_uses": 15,
    "duration_ms": 27986
  },
  "last_tool_name": "Bash",
  "uuid": "c81c9505-78ed-4d89-9978-bcd490104744",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 243_

<details open><summary>🔧 Tool call — Bash · `toolu_01GWdSssNkqYTLvGXHZo1Ng3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\cite variants from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0230259c-6650-4fcf-95e3-8b7807160550",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5d9Dp9k2JLtcCj4zc3qbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9808,
      "cache_read_input_tokens": 43458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9808,
        "ephemeral_1h_input_tokens": 0
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

_source line 244 · 2026-05-18T19:29:00.207Z_

<details><summary>↩ Tool result · `toolu_01NFEALTsLfmZ4mhwTB8wBZn`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0f40940a-134c-4f01-bf48-a743a69c65cc"
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-18T19:29:00.433Z_

<details><summary>↩ Tool result · `toolu_01GWdSssNkqYTLvGXHZo1Ng3`</summary>

```text
=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
5:\cite{brohan2023_rt2,kim2024_openvla}
8:\cite{grant2026}
8:\cite{haon2025}
12:\cite{kim2024_openvla,karamcheti2024}
12:\cite{zhai2023_siglip,oquab2024_dinov2}
12:\cite{touvron2023_llama2}
13:\cite{oquab2024_dinov2}
13:\cite{radford2021_clip}
14:\cite{kriegeskorte2008}
14:\cite{alain2017}
=== related_work.tex ===
4:\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}
11:\cite{elhage2021}
12:\cite{olsson2022}
13:\cite{wang2023_ioi}
13:\cite{conmy2023}
14:\cite{meng2022_rome}
14:\cite{belrose2023_tunedlens}
14:\cite{bills2023language,templeton2024scaling}
15:\cite{clark2019}
15:\cite{vig2019}
15:\cite{voita2019}
19:\cite{grant2026,hou2026,fei2025}
20:\cite{haon2025}
21:\cite{swann2026,buurmeijer2026}
21:\cite{lu2025,molinari2025}
22:\cite{fang2025}
24:\cite{grant2026}
28:\cite{dosovitskiy2021}
28:\cite{darcet2024}
28:\cite{geva2021}
28:\cite{tenney2019}
28:\cite{nostalgebraist2020}
28:\cite{neo2025}
32:\cite{kriegeskorte2008}
32:\cite{raghu2017}
32:\cite{morcos2018}
32:\cite{kornblith2019}
32:\cite{raghu2021}
33:\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022}
=== method.tex ===
10:\cite{kim2024_openvla,karamcheti2024}
10:\cite{zhai2023_siglip,oquab2024_dinov2}
10:\cite{touvron2023_llama2}
11:\cite{padalkar2023_oxe}
11:\cite{liu2023_libero}
23:\cite{oquab2024_dinov2}
24:\cite{radford2021_clip}
48:\cite{kriegeskorte2008}
51:\cite{nili2014toolbox}
58:\cite{alain2017}
63:\cite{kornblith2019}
=== experiments.tex ===
7:\cite{kim2024_openvla,karamcheti2024}
7:\cite{liu2023_libero}
8:\cite{oquab2024_dinov2}
8:\cite{radford2021_clip}
=== discussion.tex ===
6:\cite{grant2026}
28:\cite{brohan2023_rt2,black2024_pi0}
=== conclusion.tex ===
=== appendix.tex ===
9:\cite{kornblith2019}
21:\cite{kornblith2019}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e6f441a4-9314-42d5-b1cf-aa6cbb70ed16"
}
```

</details>

---


### System

_source line 246_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Check missing citations/files",
  "usage": {
    "total_tokens": 23211,
    "tool_uses": 10,
    "duration_ms": 20869
  },
  "last_tool_name": "Bash",
  "uuid": "fab02c47-5d0c-4a65-80bf-320aa958ff2d",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 247_

<details open><summary>🔧 Tool call — Bash · `toolu_01N2WBteAtaseXQdGdH4aR6Y`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"missing\" main.log 2>&1",
  "description": "Check missing citations/files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1b32ba51-a47d-4709-ab1f-a20a0eb55ede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 248 · 2026-05-18T19:29:01.136Z_

<details><summary>↩ Tool result · `toolu_01N2WBteAtaseXQdGdH4aR6Y`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "20546214-657d-41bd-b64d-e8c9311332f4"
}
```

</details>

---


### System

_source line 249_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count overfull warnings",
  "usage": {
    "total_tokens": 23213,
    "tool_uses": 11,
    "duration_ms": 21849
  },
  "last_tool_name": "Bash",
  "uuid": "c04ab866-498d-4efa-a610-c7ec0435d79e",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 250_

<details open><summary>🔧 Tool call — Bash · `toolu_01VxErHgHstv4NdsEc7PJX5p`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Overfull\" main.log",
  "description": "Count overfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "40775981-0f70-4701-bae9-4e57b5623204",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 251 · 2026-05-18T19:29:02.132Z_

<details><summary>↩ Tool result · `toolu_01VxErHgHstv4NdsEc7PJX5p`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "97f2bdfa-e015-4210-9fa7-9022bb3d13c7"
}
```

</details>

---


### System

_source line 252_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count underfull warnings",
  "usage": {
    "total_tokens": 23215,
    "tool_uses": 12,
    "duration_ms": 22382
  },
  "last_tool_name": "Bash",
  "uuid": "c9d6b490-4a11-4c63-a842-da482b9a11df",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 253_

<details open><summary>🔧 Tool call — Bash · `toolu_01KzQ6cDWbpBJbugryTZXKTA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull\" main.log",
  "description": "Count underfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "cce72d16-e672-4ad2-a869-9d4baf2ab086",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 254 · 2026-05-18T19:29:02.641Z_

<details><summary>↩ Tool result · `toolu_01KzQ6cDWbpBJbugryTZXKTA`</summary>

```text
10
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "72326f25-9fc5-4938-b1e6-0a64d26ffe72"
}
```

</details>

---


### System

_source line 255_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count all warnings",
  "usage": {
    "total_tokens": 23217,
    "tool_uses": 13,
    "duration_ms": 23230
  },
  "last_tool_name": "Bash",
  "uuid": "610f2d42-4462-4956-82e1-be8d780490c0",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 256_

<details open><summary>🔧 Tool call — Bash · `toolu_01XN56X2cr4kfR7h2TQDi5au`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Warning\" main.log",
  "description": "Count all warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "30ff1cfa-3d66-443d-ab3e-99b7c743b0c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 257 · 2026-05-18T19:29:03.487Z_

<details><summary>↩ Tool result · `toolu_01XN56X2cr4kfR7h2TQDi5au`</summary>

```text
20
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7261299d-f71a-49da-9a39-9d874838c6a1"
}
```

</details>

---


### System

_source line 258_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for , (confirming|indicating|suggesting|consistent wi…",
  "usage": {
    "total_tokens": 50937,
    "tool_uses": 32,
    "duration_ms": 40955
  },
  "last_tool_name": "Grep",
  "uuid": "6a8b5892-5a88-418e-ad81-acba06efd237",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 259_

<details open><summary>🔧 Tool call — Grep · `toolu_01ErRT1mThLEVQo2yKF3Ut4j`</summary>

```json
{
  "pattern": ", (confirming|indicating|suggesting|consistent with) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "cec7579b-e1ae-4297-997f-1b7f458ef135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014v8KRvThuHXEwy9G9Kvm2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3407,
      "cache_read_input_tokens": 47477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 260_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Categorize warnings",
  "usage": {
    "total_tokens": 23219,
    "tool_uses": 14,
    "duration_ms": 24209
  },
  "last_tool_name": "Bash",
  "uuid": "5532a00e-4067-4142-b85f-9157a804c086",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 261_

<details open><summary>🔧 Tool call — Bash · `toolu_01RyQjfgkKJ8XcfKsQ77XPKD`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Warning\" main.log | sort | uniq -c | sort -rn",
  "description": "Categorize warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "31e513b1-bccb-47c3-af0a-2d13929e33e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 262 · 2026-05-18T19:29:04.227Z_

<details><summary>↩ Tool result · `toolu_01ErRT1mThLEVQo2yKF3Ut4j`</summary>

```text
docs/paper/experiments.tex:80:L1 ablation ($d = 0.65$) falls between shuffled and paraphrased, consistent with removal of instruction signal rather than injection of noise (Appendix~\ref{sec:action_trajectory}).
docs/paper/discussion.tex:19:The counterfactual ordering (empty $>$ wrong $>$ paraphrased $>$ shuffled) follows semantic distance, with L1 ablation falling between shuffled and paraphrased, consistent with signal removal rather than noise injection.
docs/paper/discussion.tex:20:The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
docs/paper/appendix.tex:47:Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
docs/paper/appendix.tex:62:\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
docs/paper/appendix.tex:71:The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:94:\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with routing-first specialization of instruction-dominant heads.}
docs/paper/appendix.tex:103:The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
docs/paper/appendix.tex:110:The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
docs/paper/appendix.tex:114:\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
docs/paper/appendix.tex:129:Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
docs/paper/appendix.tex:238:\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
docs/paper/appendix.tex:246:Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
docs/paper/appendix.tex:251:\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$, confirming visually grounded action geometry.}
docs/paper/appendix.tex:267:The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
docs/paper/appendix.tex:287:The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
docs/paper/appendix.tex:347:Peak layer concentrates in the L8--L10 region ($4/5$ seeds), confirming the inverted-U shape is not a seed artifact.
docs/paper/appendix.tex:374:The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions, confirming high stability.
docs/paper/appendix.tex:436:\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large, confirming that training targets readout-token information integration.}
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
docs/paper/appendix.tex:489:Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31, confirming perfect generalization.
docs/paper/appendix.tex:539:The full profile confirms three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
docs/paper/appendix.tex:571:Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%, confirming that the 50\% threshold is not a boundary-sensitive choice.
docs/paper/appendix.tex:620:\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$), indicating instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
docs/paper/appendix.tex:645:\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$), confirming that instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
docs/paper/appendix.tex:676:\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
docs/paper/introduction.tex:21:Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "4180b035-446c-4eb8-9887-142bcd151524"
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-18T19:29:04.493Z_

<details><summary>↩ Tool result · `toolu_01RyQjfgkKJ8XcfKsQ77XPKD`</summary>

```text
     17 LaTeX Warning: `h' float specifier changed to `ht'.
      3 Package hyperref Warning: Token not allowed in a PDF string (Unicode):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "8a81edf6-065d-4232-ac23-9061bdb7255d"
}
```

</details>

---


### System

_source line 264_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running List overfull details",
  "usage": {
    "total_tokens": 23221,
    "tool_uses": 15,
    "duration_ms": 24802
  },
  "last_tool_name": "Bash",
  "uuid": "a930c0bd-8fce-43ac-8a26-86fa27d5ce70",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 265_

<details open><summary>🔧 Tool call — Bash · `toolu_01RQ6o7xSHLsoNkDpCsxHe9m`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Overfull\" main.log",
  "description": "List overfull details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3909cf75-4716-4869-a597-a4f89050a13e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDwj81eAvKu6efqCKSpGPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5345,
      "cache_read_input_tokens": 17842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5345,
        "ephemeral_1h_input_tokens": 0
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

_source line 266 · 2026-05-18T19:29:05.063Z_

<details><summary>↩ Tool result · `toolu_01RQ6o7xSHLsoNkDpCsxHe9m`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "ca51568c-f67f-4186-89f3-6cf968e19223"
}
```

</details>

---


### System

_source line 267_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for ing\\.\\s*$",
  "usage": {
    "total_tokens": 50941,
    "tool_uses": 33,
    "duration_ms": 42338
  },
  "last_tool_name": "Grep",
  "uuid": "e324a233-18a5-4fc7-8185-e6bd60d07b04",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 268_

<details open><summary>🔧 Tool call — Grep · `toolu_014ktMS6uo3wGFo78uS2yNN7`</summary>

```json
{
  "pattern": "ing\\.\\s*$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0da6f41b-2093-4abe-bad1-ffe2d9b68bd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014v8KRvThuHXEwy9G9Kvm2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3407,
      "cache_read_input_tokens": 47477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 269 · 2026-05-18T19:29:05.610Z_

<details><summary>↩ Tool result · `toolu_014ktMS6uo3wGFo78uS2yNN7`</summary>

```text
docs/paper/related_work.tex:16:Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:267:The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
docs/paper/appendix.tex:273:This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "1d10eada-9a6e-45d1-acd3-ffede91e638e"
}
```

</details>

---


### System

_source line 270_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all unique label keys",
  "usage": {
    "total_tokens": 57737,
    "tool_uses": 16,
    "duration_ms": 33855
  },
  "last_tool_name": "Bash",
  "uuid": "3f9a747f-84ad-41d9-9569-daaa2520c459",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 271_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xc9W73gR2w27zcCHA8i2m7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL LABELS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed \"s/\\\\\\\\label{//;s/}//\" | while read lbl; do echo \"$lbl\"; done; done | sort -u",
  "description": "Extract all unique label keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "e2769a96-34a5-4ccc-818b-e8046c1d9f8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2cRKSWvKpoEBVDa79rULn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 53266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3746,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 272_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af3daf08d49231099",
  "tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "description": "Searching for the sole|the only",
  "usage": {
    "total_tokens": 50945,
    "tool_uses": 34,
    "duration_ms": 43277
  },
  "last_tool_name": "Grep",
  "uuid": "707e8010-a725-419c-91e5-5efe72925179",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 273_

<details open><summary>🔧 Tool call — Grep · `toolu_011BakL2p8aFvjCh5iNmQic1`</summary>

```json
{
  "pattern": "the sole|the only",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
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
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0198692e-1854-4861-86f7-e278d57a59fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014v8KRvThuHXEwy9G9Kvm2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3407,
      "cache_read_input_tokens": 47477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 274 · 2026-05-18T19:29:06.547Z_

<details><summary>↩ Tool result · `toolu_011BakL2p8aFvjCh5iNmQic1`</summary>

```text
docs/paper/related_work.tex:25:Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
docs/paper/experiments.tex:26:The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
docs/paper/abstract.tex:4:First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JZAJ6mbk1oJw53X3udJY3y",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "7520918d-e359-4eb4-bd50-ecf658193d3b"
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T19:29:06.322Z_

<details><summary>↩ Tool result · `toolu_01Xc9W73gR2w27zcCHA8i2m7`</summary>

```text
=== ALL LABELS ===
fig:action_r2_threecond
fig:attention_appendix
fig:attention_profile
fig:cross_benchmark
fig:dose_response
fig:factorial
fig:layer_curves
fig:linear_vs_mlp
fig:metric_comparison
fig:multilayer_attention
fig:ood_diagnostics
fig:probe_bars
fig:probe_conditions_appendix
fig:random_subset_ablation
fig:rsa_bar
fig:rsa_perlayer_curve
sec:action_r2_threecond
sec:action_trajectory
sec:additional_rsa
sec:appendix
sec:attention_analysis
sec:attention_decomp
sec:attention_pattern
sec:branch_split_appendix
sec:cka_appendix
sec:conclusion
sec:cross_benchmark_appendix
sec:cross_instruction_probes
sec:demo_sensitivity
sec:dense_routing
sec:discussion
sec:experiments
sec:instruction_invariance_appendix
sec:introduction
sec:learned_routing
sec:linear_probe
sec:loocv
sec:method
sec:metric_invariance
sec:metric_sensitivity_appendix
sec:model_data
sec:multilayer_attention
sec:nonmonotonic
sec:ood_diagnostics
sec:per_dim_mae
sec:per_task_r2
sec:perdof
sec:permutation
sec:probe_bars_appendix
sec:probe_profiles
sec:probes
sec:qa_probe
sec:random_subset_ablation
sec:related_work
sec:repr_extraction
sec:robustness_appendix
sec:routing_appendix
sec:rsa
sec:rsa_bar_appendix
sec:rsa_perlayer_appendix
sec:seed_sensitivity
sec:setup
sec:spatial_cross_instruction
sec:specificity_control
sec:threshold_sensitivity
sec:token_specialization
sec:training_effect_summary
sec:training_effects_appendix
tab:action_shift_perdim
tab:attention_decomp
tab:counterfactual
tab:demo_sensitivity
tab:dense_routing
tab:dense_routing_main
tab:dose_response
tab:metric_invariance
tab:multilayer_attention
tab:per_dim_mae
tab:per_task_r2
tab:perhead_bootstrap
tab:qa_probe
tab:routing_gradient
tab:rsa_overview
tab:seed_sensitivity
tab:spatial_cross_instruction
tab:specificity_control
tab:threshold_sensitivity
tab:training_effect_summary
tab:training_effects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "39732c1a-82a0-4b76-8b11-264661b2cf86"
}
```

</details>

---


### System

_source line 276_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all unique ref keys",
  "usage": {
    "total_tokens": 57739,
    "tool_uses": 17,
    "duration_ms": 35722
  },
  "last_tool_name": "Bash",
  "uuid": "6ade1daa-e6dd-4f4e-aadf-07a876e808a1",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 277_

<details open><summary>🔧 Tool call — Bash · `toolu_011839aBGJkCcWWujHeS9AkG`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL REFS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//' ; done | sort -u",
  "description": "Extract all unique ref keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "dd93e5a2-cc26-4ad7-b225-7c6f657fcf28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2cRKSWvKpoEBVDa79rULn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 53266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3746,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 278_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running List underfull details",
  "usage": {
    "total_tokens": 24326,
    "tool_uses": 16,
    "duration_ms": 28324
  },
  "last_tool_name": "Bash",
  "uuid": "13e0e5aa-e02f-446d-9204-d432d723117d",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 279_

<details open><summary>🔧 Tool call — Bash · `toolu_01XF41vMjohPWdUrQ5n37KyS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Underfull\" main.log",
  "description": "List underfull details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "bba75aa3-1eeb-432b-b7bf-f3eaf2ccc157",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8HQFLhMSZzNtgYm4Ris4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 280 · 2026-05-18T19:29:08.593Z_

<details><summary>↩ Tool result · `toolu_01XF41vMjohPWdUrQ5n37KyS`</summary>

```text
Underfull \vbox (badness 3396) has occurred while \output is active []
Underfull \vbox (badness 1960) has occurred while \output is active []
Underfull \hbox (badness 1173) in paragraph at lines 159--166
Underfull \hbox (badness 10000) in paragraph at lines 262--268
Underfull \hbox (badness 10000) in paragraph at lines 262--268
Underfull \vbox (badness 2042) has occurred while \output is active []
Underfull \vbox (badness 6063) has occurred while \output is active []
Underfull \vbox (badness 4254) has occurred while \output is active []
Underfull \vbox (badness 1917) has occurred while \output is active []
Underfull \vbox (badness 10000) has occurred while \output is active []
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "9b29fecb-5510-4ece-ac81-30c0f54c7cca"
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-18T19:29:08.173Z_

<details><summary>↩ Tool result · `toolu_011839aBGJkCcWWujHeS9AkG`</summary>

```text
=== ALL REFS ===
fig:action_r2_threecond
fig:attention_appendix
fig:attention_profile
fig:cross_benchmark
fig:dose_response
fig:factorial
fig:layer_curves
fig:metric_comparison
fig:probe_bars
fig:probe_conditions_appendix
fig:rsa_bar
sec:action_r2_threecond
sec:action_trajectory
sec:cka_appendix
sec:cross_benchmark_appendix
sec:cross_instruction_probes
sec:dense_routing
sec:instruction_invariance_appendix
sec:learned_routing
sec:linear_probe
sec:loocv
sec:model_data
sec:nonmonotonic
sec:ood_diagnostics
sec:probes
sec:qa_probe
sec:random_subset_ablation
sec:repr_extraction
sec:rsa
sec:seed_sensitivity
sec:threshold_sensitivity
sec:training_effect_summary
tab:action_shift_perdim
tab:attention_decomp
tab:counterfactual
tab:demo_sensitivity
tab:dense_routing
tab:dense_routing_main
tab:dose_response
tab:metric_invariance
tab:multilayer_attention
tab:per_dim_mae
tab:per_task_r2
tab:perhead_bootstrap
tab:qa_probe
tab:routing_gradient
tab:rsa_overview
tab:seed_sensitivity
tab:spatial_cross_instruction
tab:specificity_control
tab:threshold_sensitivity
tab:training_effect_summary
tab:training_effects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b30c5061-358f-4e8f-b57f-29d4801e0dbe"
}
```

</details>

---


### System

_source line 282_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count underfull hbox vs vbox",
  "usage": {
    "total_tokens": 24329,
    "tool_uses": 17,
    "duration_ms": 29339
  },
  "last_tool_name": "Bash",
  "uuid": "cf521dbb-3ead-4ab2-9678-9adccdbfe9a7",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 283_

<details open><summary>🔧 Tool call — Bash · `toolu_01XNijEkw2h3wmKqMkQAPvd6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull \\\\\\\\hbox\" main.log && grep -c \"Underfull \\\\\\\\vbox\" main.log",
  "description": "Count underfull hbox vs vbox"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "3840a6d9-f5ea-455f-9d6a-657065cfa3cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8HQFLhMSZzNtgYm4Ris4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 284 · 2026-05-18T19:29:09.625Z_

<details><summary>↩ Tool result · `toolu_01XNijEkw2h3wmKqMkQAPvd6`</summary>

```text
3
7
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "9134ccf1-f184-4ace-b175-f556b56aaf1d"
}
```

</details>

---


### System

_source line 285_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all unique citation keys from tex files",
  "usage": {
    "total_tokens": 57741,
    "tool_uses": 18,
    "duration_ms": 37663
  },
  "last_tool_name": "Bash",
  "uuid": "65253d3c-6756-402a-bbe7-f7783e50b9bb",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 286_

<details open><summary>🔧 Tool call — Bash · `toolu_01TWE7vAqwDgSWHMayvjnPUA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL CITE KEYS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "5b4e475d-cfde-4b61-8a61-4089b481bb8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2cRKSWvKpoEBVDa79rULn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 53266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3746,
        "ephemeral_1h_input_tokens": 0
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

_source line 287 · 2026-05-18T19:29:10.148Z_

<details><summary>↩ Tool result · `toolu_01TWE7vAqwDgSWHMayvjnPUA`</summary>

```text
=== ALL CITE KEYS ===
alain2017
belinkov2022
belrose2023_tunedlens
bills2023language
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hewitt2019control
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
liu2023_libero
lu2025
meng2022_rome
molinari2025
morcos2018
neo2025
nili2014toolbox
nostalgebraist2020
olsson2022
oquab2024_dinov2
padalkar2023_oxe
radford2021_clip
raghu2017
raghu2021
swann2026
templeton2024scaling
tenney2019
touvron2023_llama2
vig2019
voita2019
wang2023_ioi
zhai2023_siglip
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "0c42b0c8-a319-4112-ac90-899810258847"
}
```

</details>

---


### System

_source line 288_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1296edc6c84f3e83",
  "tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "description": "Running Extract all bib entry keys from references.bib",
  "usage": {
    "total_tokens": 57743,
    "tool_uses": 19,
    "duration_ms": 39504
  },
  "last_tool_name": "Bash",
  "uuid": "267ac150-415f-4111-963e-d36990948e1b",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---


### Tool call

_source line 289_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vb4uqCtLzWc1VzGZgXCj1F`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL BIB KEYS ===\" && grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
  "description": "Extract all bib entry keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "b5a227c0-af61-474f-81d8-eca359ca5d9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2cRKSWvKpoEBVDa79rULn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 53266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3746,
        "ephemeral_1h_input_tokens": 0
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

_source line 290 · 2026-05-18T19:29:11.954Z_

<details><summary>↩ Tool result · `toolu_01Vb4uqCtLzWc1VzGZgXCj1F`</summary>

```text
=== ALL BIB KEYS ===
alain2017
belinkov2022
belrose2023_tunedlens
bills2023language
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hewitt2019control
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
liu2023_libero
lu2025
meng2022_rome
molinari2025
morcos2018
neo2025
nili2014toolbox
nostalgebraist2020
olsson2022
oquab2024_dinov2
padalkar2023_oxe
radford2021_clip
raghu2017
raghu2021
swann2026
templeton2024scaling
tenney2019
touvron2023_llama2
vig2019
voita2019
wang2023_ioi
zhai2023_siglip
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EkV7ERxEvqeZhZqGBGxAd6",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739",
  "uuid": "c6d5f761-a4f3-4b74-af6b-a3317ca2e833"
}
```

</details>

---


### System

_source line 291_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5857206b887a1a30",
  "tool_use_id": "toolu_01J3XcDyN2Ln2q2pdMJDeK2S",
  "description": "Running Count hyperref warnings",
  "usage": {
    "total_tokens": 24944,
    "tool_uses": 18,
    "duration_ms": 33058
  },
  "last_tool_name": "Bash",
  "uuid": "bd582245-c26c-4f1b-8382-75970d3a2d3b",
  "session_id": "2e136dbf-061a-4249-b788-cde9bf2a0739"
}
```

---

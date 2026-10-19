# research protest dataset search

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 276
- **Recorded user turns:** 3
- **Tool calls:** 85
- **Original source:** `logs/workers/worker_research_protest-dataset-search_20260520T092905.log`
- **Structured JSON:** [`d44dd4d0bbe037e9529e.json`](../../sessions/d4/d44dd4d0bbe037e9529e.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
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
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "23a60f4d-402d-4382-a930-0854def23d9a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779281400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c5bf88d8-13a1-44a8-a610-804d5318968b",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Assistant

_source line 4_

I'll search for publicly available protest/political event multi-class annotation datasets in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c7b8cfbb-7f8c-4d0d-84d1-99dd68ec2f7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11812
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

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01Cgb3VqR4Wn9RangSRTpyE5`</summary>

````json
{
  "description": "Search POLDEM dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9ab89efb-c2f6-4f2d-9842-4b914e3b58bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11812
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

### System

_source line 6_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Search POLDEM dataset",
  "task_type": "local_agent",
  "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
  "uuid": "8e9b2922-372e-4312-8ed2-43ed3173d7b3",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
````

---

## Round 1

6 recorded events

### User

_source line 7 · 2026-05-20T09:29:20.136Z_

Search the web for the "POLDEM Protest Event Dataset" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.

Specifically search for:
1. "POLDEM protest event dataset" — what it is, where to download
2. Whether it's freely downloadable without application/approval
3. Number of event type categories (K≥3?)
4. Sample size
5. License
6. Citation paper

Use WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.

Report in this format:
```
数据集名称: xxx
类别数 K: x
类别列表: [...]
样本量: xxx
License: xxx
下载方式: xxx (具体 URL 或命令)
Gold-standard human labels: 是/否 (标注方式说明)
引用论文: xxx
备注: xxx
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ca09697e-6ea1-4f58-b842-f6a1d677892b"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Search POLDEM dataset",
  "usage": {
    "total_tokens": 14813,
    "tool_uses": 1,
    "duration_ms": 2353
  },
  "last_tool_name": "ToolSearch",
  "uuid": "2c8d2588-f4bb-42e2-945b-6053112011dc",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0131jdcakhEVDmqCFJYTQibg`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "1fd130f1-14ec-47c9-9435-ae16c3eb0010",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQYXjh3741JEY1aosT1eRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14743,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14743,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-20T09:29:22.494Z_

<details><summary>↩ Tool result · `toolu_0131jdcakhEVDmqCFJYTQibg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9ffb0e7f-580e-4eeb-98a7-7753cffd49cb"
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Agent · `toolu_01RKjDE1P2EHBH2piAJtV2ws`</summary>

````json
{
  "description": "Search MMD dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b5f66ded-cf40-4533-a59f-cbea94c2fbc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11812
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

### System

_source line 12_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Search MMD dataset",
  "task_type": "local_agent",
  "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
  "uuid": "aa87d1cd-f87b-4b4e-ab6d-e3fa232297f3",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
````

---

## Round 2

14 recorded events

### User

_source line 13 · 2026-05-20T09:29:23.431Z_

Search the web for the "Mass Mobilization Project" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.

Specifically search for:
1. "Mass Mobilization Project dataset" — what it is, where to download
2. Whether it's freely downloadable without application/approval
3. Number of event type categories — does it have K≥3 classification categories?
4. Sample size
5. License and terms of use — is it allowed for ML/NLP research?
6. Citation paper

Use WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.

Report in this format:
```
数据集名称: xxx
类别数 K: x
类别列表: [...]
样本量: xxx
License: xxx
下载方式: xxx (具体 URL 或命令)
Gold-standard human labels: 是/否 (标注方式说明)
引用论文: xxx
备注: xxx
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5b6b2031-1528-4051-afce-d5fb3fa7d8a5"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for POLDEM Protest Event Dataset download categories",
  "usage": {
    "total_tokens": 16324,
    "tool_uses": 2,
    "duration_ms": 4904
  },
  "last_tool_name": "WebSearch",
  "uuid": "4dc6a226-e259-4f8b-a3a5-f84f0b1bd7e3",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for POLDEM protest event dataset citation paper sampl…",
  "usage": {
    "total_tokens": 16396,
    "tool_uses": 3,
    "duration_ms": 5186
  },
  "last_tool_name": "WebSearch",
  "uuid": "e116c173-e242-4cbb-82c6-c64329275383",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Search MMD dataset",
  "usage": {
    "total_tokens": 14771,
    "tool_uses": 1,
    "duration_ms": 2784
  },
  "last_tool_name": "ToolSearch",
  "uuid": "193f26a5-cb56-4885-9621-1161ba1f9e9b",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Mass Mobilization Project dataset download MMP pr…",
  "usage": {
    "total_tokens": 16274,
    "tool_uses": 2,
    "duration_ms": 5507
  },
  "last_tool_name": "WebSearch",
  "uuid": "a8a6ad59-7b5b-4512-9913-16fdd3759609",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization Data\" MMD dataset categories e…",
  "usage": {
    "total_tokens": 16321,
    "tool_uses": 3,
    "duration_ms": 5742
  },
  "last_tool_name": "WebSearch",
  "uuid": "0b914d5e-e362-49c9-a417-082cd05fbb04",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016kw5DHaVAqWG4eaELc4od2`</summary>

```json
{
  "query": "POLDEM Protest Event Dataset download categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "be208c73-90b7-4496-a64f-f46d50224afd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ucTEzbN6EZyykZTcYeTbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AsqAegxYjHHMUT1kAGaePw`</summary>

```json
{
  "query": "POLDEM protest event dataset citation paper sample size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "440220c2-605f-46e6-a103-16846d44e873",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ucTEzbN6EZyykZTcYeTbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019KbZJUrwMGE69uYmvc3R2D`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "706ea8b7-fc24-4438-b532-d37855964635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rVMJqNwUUR12SZWK593pW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6514,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6514,
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

_source line 22 · 2026-05-20T09:29:26.219Z_

<details><summary>↩ Tool result · `toolu_019KbZJUrwMGE69uYmvc3R2D`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "cb6c5573-3f77-4ddc-8b68-10377dd37dc3"
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vks53KuVi87fop8bGQgAGk`</summary>

```json
{
  "query": "Mass Mobilization Project dataset download MMP protest data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "67e2ec48-e360-403b-b807-763a431481be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoNnH86c3aZfkf7QPBxx82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 14764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
        "ephemeral_1h_input_tokens": 0
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019xUbSsBk3ncaPbaw2bPoHh`</summary>

```json
{
  "query": "\"Mass Mobilization Data\" MMD dataset categories event types NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "f1fd73ef-1c3b-446b-be1e-d00d72f9574e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoNnH86c3aZfkf7QPBxx82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 14764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
        "ephemeral_1h_input_tokens": 0
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

_source line 25_

<details open><summary>🔧 Tool call — Agent · `toolu_0192Rf5hZwdGc442eWRxtvrU`</summary>

````json
{
  "description": "Search protest NLP datasets",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "a1fdcd79-ca93-47d1-9a78-1693517c2624",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11812
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

### System

_source line 26_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Search protest NLP datasets",
  "task_type": "local_agent",
  "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found.",
  "uuid": "e3734a50-89c5-4a6c-aafd-26e7fb072937",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
````

---

## Round 3

250 recorded events

### User

_source line 27 · 2026-05-20T09:29:30.647Z_

Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.

Use WebSearch with these queries (try at least 3-4 of them):
1. "protest event dataset NLP" OR "political event classification dataset"
2. "contentious politics dataset annotation NLP"
3. "event type classification benchmark" protest
4. Search Papers with Code for protest event or political event benchmarks
5. "protest news classification dataset" github
6. "political event coding dataset" public download

For each dataset found, report:
```
数据集名称: xxx
类别数 K: x
类别列表: [...]
样本量: xxx
License: xxx
下载方式: xxx (具体 URL 或命令)
Gold-standard human labels: 是/否 (标注方式说明)
引用论文: xxx
备注: xxx
```

If you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:
- Indian Protest Event datasets
- SPEED (Social, Political and Economic Event Database)
- Any HuggingFace datasets related to protest classification
- ProtestNews shared task datasets (CLEF)

Be thorough — search multiple queries and report ALL candidates found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "938b35dd-59e8-4dd3-87bb-9dfd0696a22a"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T09:29:32.323Z_

<details><summary>↩ Tool result · `toolu_016kw5DHaVAqWG4eaELc4od2`</summary>

```text
Web search results for query: "POLDEM Protest Event Dataset download categories"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Data Overview - PolDem - European University Institute","url":"https://poldem.eui.eu/data-overview/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"}]

Based on the search results, I found information about the POLDEM Protest Event Dataset:

The Observatory for Political Conflict and Democracy (PolDem) provides interactive data exploration and analysis tools, as well as the methodology and codebooks used for data generation and analysis, with a short overview of the main datasets provided.

PolDem includes data on protest events in 30 European countries obtained by coding media coverage. The data collection relies on semi-automated coding of newswire reports and covers 30 European countries and the time period from 2000 until 2015.

Regarding the download and categories, the website provides online interactive downloading tools and R tools to aid the analysis of the different datasets. The dataset includes various categorical variables for protest events, such as categories indicating whether an event is linked to other protest events that take place in the same country, in Europe (i.e., current member states of the European Union as well as Norway and Switzerland).

Both the dataset and the codebook, as well as additional information, are available as a free download from the official Observatory for Political Conflict and Democracy in Europe website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "89d2301d-4c4b-46b7-9daa-d531914f7690"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Search protest NLP datasets",
  "usage": {
    "total_tokens": 14888,
    "tool_uses": 1,
    "duration_ms": 2698
  },
  "last_tool_name": "ToolSearch",
  "uuid": "102daba1-6d17-4850-bb33-8e1d32784b28",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K8LnvAaqJWjR8D88HF9P5p`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3c86cbe9-b9fa-4bc6-be43-8130138348c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EBX94usTx3FKmYYdoT2Nx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6623,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6623,
        "ephemeral_1h_input_tokens": 0
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

_source line 31 · 2026-05-20T09:29:33.351Z_

<details><summary>↩ Tool result · `toolu_01K8LnvAaqJWjR8D88HF9P5p`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "76c28e5d-4046-40a1-89ad-2f2f3cdc16ed"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T09:29:34.314Z_

<details><summary>↩ Tool result · `toolu_01AsqAegxYjHHMUT1kAGaePw`</summary>

```text
Web search results for query: "POLDEM protest event dataset citation paper sample size"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"PolDem – Protest Dataset 30 European countries - Research output - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries/publications/"}]

Based on the search results, I found relevant information about the POLDEM protest event dataset:

## Citation Information

The main citation for the PolDem-Protest Dataset on EU issues is Maag, Simon 2020. PolDem-Protest Dataset on EU issues, Version 1. For the broader European dataset, the PolDem-Protest Dataset 30 European Countries, Version 1 is cited.

## Dataset Scope

The data collection relies on a semi-automated coding of newswire reports and covers 30 European countries and the time period from 2000 until 2015.

## Sample Size Information

Regarding sampling methodology, for medium-sized countries (Estonia, Greece, Norway, Portugal and Slovakia), 50 percent of reports were sampled, and for very small countries with only a few hundred news reports, all the reports were manually annotated. Additionally, events found for Germany, the UK, Hungary, Poland and Spain were multiplied by four to adjust for their sampling strategy.

The PolDem-30 dataset contains thousands of events—3491 events were recorded in PolDem-30 for Germany 2000–2020 as one example of coverage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "52daa3ac-cd8e-4d3c-91fd-1234fd46a80e"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"protest event dataset NLP\" OR \"political event c…",
  "usage": {
    "total_tokens": 16347,
    "tool_uses": 2,
    "duration_ms": 5420
  },
  "last_tool_name": "WebSearch",
  "uuid": "fc489250-d1b7-485d-9b23-564402ed6966",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xn1TKfvxxdDHZtWmtqmGZn`</summary>

```json
{
  "query": "\"protest event dataset NLP\" OR \"political event classification dataset\" multi-class"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "a5b2d23b-2ada-4268-874c-d844390cd834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FswRucUmPZ5pakh2UJPhw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 14873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
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

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"contentious politics dataset annotation NLP\" tex…",
  "usage": {
    "total_tokens": 16349,
    "tool_uses": 3,
    "duration_ms": 5895
  },
  "last_tool_name": "WebSearch",
  "uuid": "008e8c2c-e6d5-4a86-8ff8-223adf9f2722",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0198tHj11JrPpYqoaWuSiH3j`</summary>

```json
{
  "query": "\"contentious politics dataset annotation NLP\" text classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b3873cb4-d7fb-44bf-b3b2-59150ae09d41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FswRucUmPZ5pakh2UJPhw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 14873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
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

_source line 37 · 2026-05-20T09:29:36.795Z_

<details><summary>↩ Tool result · `toolu_019xUbSsBk3ncaPbaw2bPoHh`</summary>

```text
Web search results for query: ""Mass Mobilization Data" MMD dataset categories event types NLP"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data/activity"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Creating Custom Event Data Without Dictionaries: A Bag-of-Tricks","url":"https://arxiv.org/pdf/2304.01331"},{"title":"Visualization Techniques to Enhance Automated Event Extraction","url":"https://arxiv.org/pdf/2106.06588"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"}]

Based on the search results, here's what I found about the Mass Mobilization Data (MMD) dataset:

## Overview
The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018. These data contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events.

## Demand Categories
For each event, the MM data itemize what protesters demand across as many as seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

## Government Response Types
The dataset also records up to seven types of government responses, including accommodation, arrests, beatings, crowd dispersal, ignore, killings, and shootings.

## Event Data Recorded
Each event records location, protest size, protester demands, and government responses.

The search results did not provide extensive detail about NLP-specific applications with the MMD dataset, though there are related projects in the broader research community using NLP techniques for automated event data extraction from news sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2ad1a807-412e-4a94-bbd3-dba13feab597"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T09:29:36.885Z_

<details><summary>↩ Tool result · `toolu_01Vks53KuVi87fop8bGQgAGk`</summary>

```text
Web search results for query: "Mass Mobilization Project dataset download MMP protest data"

Links: [{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"}]

Based on the search results, here's what I found about the Mass Mobilization Project dataset and how to download it:

## Dataset Overview

The Mass Mobilization Project codes protests against governments, covering 162 countries between 1990 and March 2020, and for each protest event records protester demands, government responses, protest location, and protester identities.

## Download Locations

The main sources for downloading the MMP protest data are:

1. **Harvard Dataverse** - The Mass Mobilization dataset can be found at https://dataverse.harvard.edu/dataverse/MMdata.

2. **Official Project Website** - The official project website can be found at http://www.binghamton.edu/massmobilization/.

3. **Project GitHub** - You can also visit the project page at https://massmobilization.github.io

## Dataset Details

The data contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events, with each event recording location, protest size, protester demands, and government responses.

These resources should provide you with access to download the Mass Mobilization Project protest dataset in various formats.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c3cae42b-93d0-41ce-ba93-aae5aa3ae375"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for POLDEM protest event dataset \"event type\" categor…",
  "usage": {
    "total_tokens": 18055,
    "tool_uses": 4,
    "duration_ms": 16756
  },
  "last_tool_name": "WebSearch",
  "uuid": "fa0685b7-09ab-4240-b921-f1d153f3d1b7",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AoaMcQwwd9HfAWJ1PgDwVp`</summary>

```json
{
  "query": "POLDEM protest event dataset \"event type\" categories codebook issue type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "8464814b-453b-4c33-b016-97abe234ab49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPskT8EAbV7KZ1WRF6QjaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1617,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1617,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"event type classification benchmark\" protest NLP…",
  "usage": {
    "total_tokens": 16351,
    "tool_uses": 4,
    "duration_ms": 6362
  },
  "last_tool_name": "WebSearch",
  "uuid": "9d0ad374-f35d-41cb-b54a-8fade96717d6",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011SiY7tSZAzX5GxcKtWhV4B`</summary>

```json
{
  "query": "\"event type classification benchmark\" protest NLP dataset public"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "cd77af6e-dc5e-4229-8aef-a22a380eda15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FswRucUmPZ5pakh2UJPhw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 14873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
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

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for poldem.eui.eu protest dataset license download re…",
  "usage": {
    "total_tokens": 18099,
    "tool_uses": 5,
    "duration_ms": 17141
  },
  "last_tool_name": "WebSearch",
  "uuid": "96a849f4-549a-446a-8432-4ac5a740f500",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LR2QoFc7QPqkhvJ8mWSuo9`</summary>

```json
{
  "query": "poldem.eui.eu protest dataset license download registration required"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "7c285e36-e2f4-4c70-9b35-de1f29a2e8ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPskT8EAbV7KZ1WRF6QjaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1617,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1617,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for site:paperswithcode.com protest event OR politica…",
  "usage": {
    "total_tokens": 16353,
    "tool_uses": 5,
    "duration_ms": 6706
  },
  "last_tool_name": "WebSearch",
  "uuid": "5580c804-e809-4ab0-8c54-8906678ad89f",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XgMiBGYWHYjmD4U1r5J2FB`</summary>

```json
{
  "query": "site:paperswithcode.com protest event OR political event classification benchmark dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3b054c39-aef0-41a3-ac38-ace8661a5dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FswRucUmPZ5pakh2UJPhw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 14873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
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

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Mass Mobilization Project codebook protest demand…",
  "usage": {
    "total_tokens": 17954,
    "tool_uses": 4,
    "duration_ms": 16083
  },
  "last_tool_name": "WebSearch",
  "uuid": "eebc2c2d-87bd-469c-86da-d4ef646bcffb",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TReZXKyxa2134eYTQCFarV`</summary>

```json
{
  "query": "Mass Mobilization Project codebook protest demand categories full list Clark Regan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2b92b506-f46e-4980-bde0-8adf8eaeb9fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTu5vD7FQYUrFJTv7ivhyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 16220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Mass Mobilization Project citation paper Clark Re…",
  "usage": {
    "total_tokens": 17996,
    "tool_uses": 5,
    "duration_ms": 16434
  },
  "last_tool_name": "WebSearch",
  "uuid": "19d34794-dc3b-4b1d-a653-b987d4839d7a",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lu39xephPK2HBWKLgtpSDo`</summary>

```json
{
  "query": "Mass Mobilization Project citation paper Clark Regan license terms of use Harvard Dataverse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "f3b282e3-e183-4092-bab8-2782f1d459cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTu5vD7FQYUrFJTv7ivhyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 16220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 51 · 2026-05-20T09:29:43.833Z_

<details><summary>↩ Tool result · `toolu_01LR2QoFc7QPqkhvJ8mWSuo9`</summary>

```text
Web search results for query: "poldem.eui.eu protest dataset license download registration required"

Links: [{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"National Election Campaign Dataset on EU issues","url":"https://poldem.eui.eu/downloads/cosa/poldem-election_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Eui","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu.dta"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Platform for Protest and Conflict in Europe | WZB","url":"https://www.wzb.eu/en/news/platform-for-protest-and-conflict-in-europe"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"}]

Based on the search results, I found information about the PolDem protest dataset from the European University Institute. Here's what I found:

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large time-span.

The core of PolDem is data on election campaigns in 15 European countries and on protest events in 30 European countries obtained by coding media coverage.

PolDem aims to update and disseminate data within the scientific community and wider public, and to provide users with the relevant documentation, codebooks, and tools to interpret the data.

The search results indicate that the platform hosts downloadable datasets (including codebooks and data files), but the specific information about license terms and whether registration is required to download the datasets was not clearly detailed in these search results. The results show links to various documentation files and datasets available through the poldem.eui.eu website, but don't explicitly confirm the registration and licensing requirements. For those specific details, you may need to visit the main PolDem website directly or check the terms of use section.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "af8e996e-e9b3-4f7b-87d4-3617822fa323"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T09:29:44.127Z_

<details><summary>↩ Tool result · `toolu_01Xn1TKfvxxdDHZtWmtqmGZn`</summary>

```text
Web search results for query: ""protest event dataset NLP" OR "political event classification dataset" multi-class"

Links: [{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://www.ovid.com/journals/absc/fulltext/10.1177/00027642211021650~protest-event-analysis-developing-a-semiautomated-nlp"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Emerging Markets Welfare – Work Package 2: Protest Events Database using NLP and Machine Learning","url":"https://emw.ku.edu.tr/project/work-packages/work-package-2-protest-events-database/"},{"title":"Collecting protest event data using natural language processing models: Post-Soviet Affairs: Vol 42 , No 1 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/1060586X.2025.2600874"},{"title":"[2102.00917] Counting Protests in News Articles: A Dataset and Semi-Automated Data Collection Pipeline","url":"https://ar5iv.labs.arxiv.org/html/2102.00917"}]

Based on the search results, I found several relevant datasets and resources for protest event classification using NLP:

## Key Datasets and Research

**PolDem – Protest Event Dataset**: This dataset reports about protest events with probability scores above 0.90, and includes multi-class classification for different action forms.

**Russian Contentious Events Dataset (RCED)**: This is a comprehensive dataset of contentious events in Russia from 2010 to 2023, with a methodological workflow that includes event classification, named entity recognition, duplicate removal, and post-processing.

**US Protest Events Dataset**: A manually labeled dataset corresponding to 42,347 reported protest events in the United States between January 2017 and January 2021, including news article URLs, dates, locations, crowd size estimates, and 494 discrete descriptive tags.

## Multi-class Classification Approaches

Research has used 518 documents annotated at the word level for protest event mentions, marking word spans such as "take to the streets," "violent demonstration," "signed a petition," and "carried banners" to classify different types of protest events.

Protest databases classify events such as strikes, rallies, boycotts, protests, riots, and demonstrations, referred to as the "repertoire of contention".

These resources provide multi-class datasets suitable for NLP-based political event classification tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b405c2e7-e3e0-4792-85cf-af9910b8e9ce"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T09:29:45.034Z_

<details><summary>↩ Tool result · `toolu_01AoaMcQwwd9HfAWJ1PgDwVp`</summary>

```text
Web search results for query: "POLDEM protest event dataset "event type" categories codebook issue type"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"Full article: Protest in unlikely times: dynamics of collective mobilization in Europe during the COVID-19 crisis","url":"https://www.tandfonline.com/doi/full/10.1080/13501763.2022.2140819"}]

I found relevant information about the POLDEM protest event dataset. Here are the key findings:

## POLDEM Dataset Overview

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large time-span.

## Event Type and Issue Categories

The dataset includes issue categories labeled as 'issue_econ_private', 'issue_econ_public', 'issue_cult_lib', 'issue_environment', 'issue_political', 'issue_regional', 'issue_cult_cons', 'issue_xeno', 'issue_other', and 'issue_dontkno' (with the last one likely representing "don't know" responses).

The dataset includes violent protests and strikes, but demonstrations make up a larger share of events. An action form indicator called 'action_form' is used in the dataset.

## Codebook Resources

The official Observatory for Political Conflict and Democracy in Europe website provides both the dataset and the codebook as free downloads. The codebooks are available in PDF format from the PolDem website, including versions for the 30-country dataset and EU-specific protest data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "1d2f6fcc-836e-465b-972c-ffeb9bf1551c"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T09:29:45.370Z_

<details><summary>↩ Tool result · `toolu_0198tHj11JrPpYqoaWuSiH3j`</summary>

```text
Web search results for query: ""contentious politics dataset annotation NLP" text classification"

Links: [{"title":"Large language models as a substitute for human experts in annotating political text - Michael Heseltine, Bernhard Clemm von Hohenberg, 2024","url":"https://journals.sagepub.com/doi/10.1177/20531680241236239"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://arxiv.org/pdf/2206.10299"},{"title":"Enhancing LLM-Based Text Classification in Political Science: Automatic Prompt Optimization and Dynamic Exemplar Selection for Few-Shot Learning","url":"https://arxiv.org/html/2409.01466v2"},{"title":"AgoraSpeech: A multi-annotated comprehensive dataset of political discourse through the lens of humans and AI","url":"https://arxiv.org/html/2501.06265v1"},{"title":"Benchmarking LLMs in Political Content Text-Annotation: Proof-of-Concept   with Toxicity and Incivility Data","url":"https://arxiv.org/pdf/2409.09741"},{"title":"Political Leaning and Politicalness Classification of Texts","url":"https://arxiv.org/html/2507.13913v1"}]

I found several relevant results on contentious politics, dataset annotation, and NLP text classification. Here are the key findings:

**Major Datasets and Projects:**

The Global Contentious Politics Database (GLOCON) is an annotation project developed by researchers at Koç University, funded by the European Research Council Starting Grant, which focuses on annotating contentious political events.

The AgoraSpeech dataset is a comprehensive annotated dataset of political discourse with annotations for six NLP tasks including text classification, topic identification, sentiment analysis, named entity recognition, and polarization and populism detection, using a two-step annotation process with ChatGPT-generated annotations followed by human-in-the-loop validation.

**Annotation Challenges:**

When dealing with contentious classifications, human-coded data can be problematic particularly due to the subjective nature of tone interpretation and nuanced distinctions between categories, which often involve overlapping criteria that lead to disagreements among coders.

Recent research has benchmarked LLMs' ability to perform annotation tasks on political content, using protest event datasets comprising millions of digital interactions with human-coded labels for toxicity and incivility.

These resources represent current approaches to handling the complexities of annotating contentious political text through a combination of human expertise and AI-assisted methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "7e7d12ca-6a27-4331-99b1-20dc9526adc2"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T09:29:45.669Z_

<details><summary>↩ Tool result · `toolu_01XgMiBGYWHYjmD4U1r5J2FB`</summary>

```text
Web search results for query: "site:paperswithcode.com protest event OR political event classification benchmark dataset"

Links: [{"title":"Zachary C. Steinert-Threlkeld | Papers With Code","url":"https://paperswithcode.com/search?q=author:Zachary+C.+Steinert-Threlkeld"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Benchmarking LLMs in Political Content Text-Annotation: Proof-of-Concept   with Toxicity and Incivility Data","url":"https://arxiv.org/pdf/2409.09741"},{"title":"Papers with Code - Joanna Szwoch","url":"https://paperswithcode.com/search?q=author:Joanna+Szwoch"},{"title":"Papers with Code - Event-Stream Dataset Dataset","url":"https://paperswithcode.com/dataset/event-stream-dataset"},{"title":"Protest Activity Detection and Perceived Violence Estimation from Social   Media Images","url":"https://arxiv.org/pdf/1709.06204"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"}]

Based on the search results, here are some relevant protest event and political event classification benchmark datasets found on Papers with Code:

1. **UCLA Protest Image Dataset**: A novel dataset of 40,764 images (11,659 protest images and hard negatives) with various annotations of visual attributes and sentiments. This was used to train a multi-task convolutional neural network to automatically classify the presence of protesters in an image and predict its visual attributes, perceived violence and exhibited emotions.

2. **Cross-context News Corpus for Protest Events**: A gold standard corpus of protest events from various local and international sources across countries in English with document, sentence, and token level annotations. This corpus facilitates creating machine learning models that automatically classify news articles and extract protest event-related information.

3. **CLEF 2019 ProtestNews Lab**: This lab tasks participants to identify text relating to political protests within larger corpora of news data, with three tasks including article classification, sentence detection, and event extraction.

4. **Protest Event Dataset for Text Annotation**: A novel protest event dataset comprising more than three million digital interactions with gold standard labels annotated by human coders about toxicity and incivility on social media.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2d1b07b3-f286-4754-a79f-baf3b8cd6e1f"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T09:29:46.149Z_

<details><summary>↩ Tool result · `toolu_011SiY7tSZAzX5GxcKtWhV4B`</summary>

```text
Web search results for query: ""event type classification benchmark" protest NLP dataset public"

Links: [{"title":"Collecting protest event data using natural language processing models: Post-Soviet Affairs: Vol 42 , No 1 - Get Access","url":"https://doi.org/10.1080/1060586X.2025.2600874"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"New Benchmark Corpus and Models for Fine-grained ...","url":"https://aclanthology.org/2020.coling-main.584.pdf"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"(PDF) NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models","url":"https://www.academia.edu/110108255/NSUT_NLP_at_CASE_2022_Task_1_Multilingual_Protest_Event_Detection_using_Transformer_based_Models"},{"title":"[2102.00917] Counting Protests in News Articles: A Dataset and Semi-Automated Data Collection Pipeline","url":"https://ar5iv.labs.arxiv.org/html/2102.00917"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"}]

Based on the search results, here are several event type classification benchmarks and NLP datasets related to protests that are publicly available:

## Key Public Datasets

The Russian Contentious Events Dataset (RCED) is a comprehensive dataset of contentious events in Russia from 2010 to 2023, with the dataset, codebook, and samples available publicly on Zenodo. The dataset includes a methodological workflow for event classification, named entity recognition, duplicate removal, and post-processing, demonstrating how modern machine learning and language models can automate and scale protest event analysis.

CEHA is a benchmark dataset containing event descriptions of violent conflicts in the Horn of Africa region, annotated with fine-grained event-types by subject matter experts.

A protest event dataset from news articles includes manually labeled data of 42,347 reported protest events in the United States between January 2017 and January 2021, with 494 discrete descriptive tags and a semi-automated data collection pipeline comprising 138,826 English articles.

## Shared Task Benchmarks

The CASE shared task (Socio-political and Crisis Events Detection) benchmarks state-of-the-art text classification systems in multilingual settings, with Task 1 focusing on multilingual protest news detection including document classification, sentence classification, event sentence coreference identification, and event extraction.

One benchmark dataset covers circa 600K short event descriptions for the evaluation of fine-grained event classification, covering 25 event types related to political violence events, crisis situations, and protest and unrest events.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "132e1d7b-502e-490a-82bb-e478e5032871"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T09:29:46.459Z_

<details><summary>↩ Tool result · `toolu_01TReZXKyxa2134eYTQCFarV`</summary>

```text
Web search results for query: "Mass Mobilization Project codebook protest demand categories full list Clark Regan"

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Data Is Plural — 2020.08.26 edition","url":"https://www.data-is-plural.com/archive/2020-08-26-edition/"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Project - Political Science | Binghamton University","url":"https://www.binghamton.edu/political-science/massmobilization.html"}]

Based on the search results, I found information about the Mass Mobilization Project protest demand categories. The MM data itemize what protesters demand across as many as seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

The search results reference the Principle Investigators for the Mass Mobilization project are David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame).

The complete codebook is available in the Mass Mobilization Data Project Codebook and User's Manual, which can be accessed through the Harvard Dataverse or the official Mass Mobilization Project website. The codebook PDF was referenced in the search results but the full detailed list of all demand categories with their complete definitions would be found in that official document.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9efc1e9f-3a8f-460a-9f66-4bd2d6e508c9"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for PolDem protest dataset 30 codebook \"action form\" …",
  "usage": {
    "total_tokens": 19841,
    "tool_uses": 6,
    "duration_ms": 27981
  },
  "last_tool_name": "WebSearch",
  "uuid": "6aabc548-e31e-4f27-ab47-88cae53e8313",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K3k3MQ2otqMLgLbUuURnBq`</summary>

```json
{
  "query": "PolDem protest dataset 30 codebook \"action form\" categories list \"protest form\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "57cdd6a2-eb43-4056-a816-eb82a4560ae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcMpQkbpNhuUsqLn8bc8CD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 17799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 878,
        "ephemeral_1h_input_tokens": 0
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

_source line 60 · 2026-05-20T09:29:48.344Z_

<details><summary>↩ Tool result · `toolu_01Lu39xephPK2HBWKLgtpSDo`</summary>

```text
Web search results for query: "Mass Mobilization Project citation paper Clark Regan license terms of use Harvard Dataverse"

Links: [{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Data innovations on protests in the United States - Cassy Dorff, Grace Adcox, Amanda Konet, 2023","url":"https://journals.sagepub.com/doi/abs/10.1177/00223433221143808"},{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse.xhtml?alias=MMdata"}]

Based on the search results, I found information about the Mass Mobilization Project:

The Mass Mobilization Data Project is authored by David Clark and Patrick Regan and was published in 2016 via Harvard Dataverse. The Principal Investigators for the Mass Mobilization project are David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame).

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The project codes protests against governments and the data cover 162 countries between 1990 and March 2017, with each protest event recording protester demands, government responses, protest location, and protester identities.

However, the search results do not contain specific information about the citation format for the paper or the detailed terms of use/license from Harvard Dataverse. The DOI for the dataset is provided as 10.7910/DVN/HTTWYL, which can be used to access the full citation information and license terms directly on the Harvard Dataverse website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "278b97e6-5454-49f4-a916-5cad13156cd6"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for PolDem protest event dataset total number events …",
  "usage": {
    "total_tokens": 19886,
    "tool_uses": 7,
    "duration_ms": 28919
  },
  "last_tool_name": "WebSearch",
  "uuid": "3f680840-2962-4223-be78-0fced3a04749",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWMEy7KuWxce5nCV7XTyAW`</summary>

```json
{
  "query": "PolDem protest event dataset total number events observations sample size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0240cc80-0a19-4dce-b90e-b593d1968e9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcMpQkbpNhuUsqLn8bc8CD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 17799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 878,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"protest news classification dataset\" github hugg…",
  "usage": {
    "total_tokens": 19563,
    "tool_uses": 6,
    "duration_ms": 18679
  },
  "last_tool_name": "WebSearch",
  "uuid": "545e8542-696e-4383-8400-77a7292040cf",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMj3mHDd5LeTt7XFYa5iDk`</summary>

```json
{
  "query": "\"protest news classification dataset\" github huggingface download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "cffdd7a1-9bc6-4f39-90f0-84feeaf93b5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzZfvqmULJcw12Qkophiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 2580,
      "cache_read_input_tokens": 16328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2580,
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

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CLEF ProtestNews shared task dataset download \"ev…",
  "usage": {
    "total_tokens": 19564,
    "tool_uses": 7,
    "duration_ms": 19149
  },
  "last_tool_name": "WebSearch",
  "uuid": "b7d5cb30-d748-44be-87c8-beb43556adb9",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uFcemakzgNYJQJuvkiH8v`</summary>

```json
{
  "query": "CLEF ProtestNews shared task dataset download \"event type\" classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2cd183b1-a8c6-4bf8-bccc-d9ba58a70735",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzZfvqmULJcw12Qkophiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 2580,
      "cache_read_input_tokens": 16328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2580,
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

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for PolDem protest dataset \"creative commons\" OR \"CC …",
  "usage": {
    "total_tokens": 19931,
    "tool_uses": 8,
    "duration_ms": 29823
  },
  "last_tool_name": "WebSearch",
  "uuid": "c1cde999-e880-4a2c-b74f-c5fe30eb5e8a",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PX5GJDBTbPm3NKbJ58Wmd`</summary>

```json
{
  "query": "PolDem protest dataset \"creative commons\" OR \"CC BY\" OR license OR \"terms of use\" cite Kriesi Hutter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2c89eced-e862-45a4-add2-ace8be31fe17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcMpQkbpNhuUsqLn8bc8CD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 17799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 878,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CASE shared task 2021 2022 \"socio-political event…",
  "usage": {
    "total_tokens": 19565,
    "tool_uses": 8,
    "duration_ms": 20150
  },
  "last_tool_name": "WebSearch",
  "uuid": "acf74990-200a-4fb0-bca8-f131a4426264",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkRgHB4fMrN4Tdjwxd7QxB`</summary>

```json
{
  "query": "CASE shared task 2021 2022 \"socio-political event\" dataset download github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2d225b81-ff20-4b69-a8d8-0cd38a4bc404",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzZfvqmULJcw12Qkophiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 2580,
      "cache_read_input_tokens": 16328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2580,
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

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for site:dataverse.harvard.edu \"Mass Mobilization\" li…",
  "usage": {
    "total_tokens": 19551,
    "tool_uses": 6,
    "duration_ms": 27471
  },
  "last_tool_name": "WebSearch",
  "uuid": "5e66812f-10e3-450a-9afa-ed639ddf5bfd",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLN9b8M5ZUJ5zgGX6VnP1X`</summary>

```json
{
  "query": "site:dataverse.harvard.edu \"Mass Mobilization\" license CC0 terms download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "032f98cc-125e-44a8-b64c-747620086de1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KupheDJTqodsbNEcGsMFQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 17073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2246,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" protest data sample size numb…",
  "usage": {
    "total_tokens": 19600,
    "tool_uses": 7,
    "duration_ms": 28032
  },
  "last_tool_name": "WebSearch",
  "uuid": "2f4eb528-096f-4592-86b7-ae1dca3fc2ff",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMNPYH2Jbsec83VAt32NgQ`</summary>

```json
{
  "query": "\"Mass Mobilization\" protest data sample size number of events rows 10000 17000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "6a86e8d4-f0fa-4f07-8ee7-50c8479b405d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KupheDJTqodsbNEcGsMFQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 17073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2246,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for SPEED \"Social Political Economic Event Database\" …",
  "usage": {
    "total_tokens": 19566,
    "tool_uses": 9,
    "duration_ms": 20951
  },
  "last_tool_name": "WebSearch",
  "uuid": "df77e8b0-89df-47a8-a3a9-ded4be086a09",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011z74o5Sewr3YpWHrsYLhtD`</summary>

```json
{
  "query": "SPEED \"Social Political Economic Event Database\" dataset download NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "d9139bf7-d1fa-4c38-88f2-f5a88de69541",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzZfvqmULJcw12Qkophiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 631,
      "cache_creation_input_tokens": 2580,
      "cache_read_input_tokens": 16328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2580,
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

_source line 77 · 2026-05-20T09:29:55.564Z_

<details><summary>↩ Tool result · `toolu_01NWMEy7KuWxce5nCV7XTyAW`</summary>

```text
Web search results for query: "PolDem protest event dataset total number events observations sample size"

Links: [{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"How to Capture Global Protest Trends: Using Survey Data Recycling Data to Construct Cross-National Trends in Protest - J. Craig Jenkins, Joonghyun Kwak, 2022","url":"https://journals.sagepub.com/doi/full/10.1177/00027642211021627"}]

Based on the search results, I found information about the PolDem protest event dataset. However, the search results don't contain a specific total number of events or sample size. The documents reference the dataset covering protest events in 30 European countries obtained by coding media coverage, and the data covers the years 2000–2020.

One specific reference mentions that in a comparison study, PolDem recorded 294 events in four cities in a given time period, but this is just a subset of the larger dataset.

The search results primarily contain methodological information about the dataset (such as how events are coded and weighted for sampling probability) rather than the overall dataset statistics you're looking for. To get the specific total number of observations in the full PolDem protest dataset, you may need to consult the dataset documentation directly from the PolDem website (poldem.eui.eu) or contact the dataset creators at the European University Institute.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "67ddd363-52b9-420c-9716-f20fc5d2e96c"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T09:29:55.998Z_

<details><summary>↩ Tool result · `toolu_01K3k3MQ2otqMLgLbUuURnBq`</summary>

```text
Web search results for query: "PolDem protest dataset 30 codebook "action form" categories list "protest form""

Links: [{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"PolDem – Protest Dataset 30 European countries - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"}]

I found relevant resources for the PolDem Protest Dataset 30. The search results include links to the official codebook PDF (https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf) and documentation that contain information about the dataset structure.

Based on the search results, the dataset includes various protest-related activities such as petitions, campaigns, protests, demonstrations, marches, parades, rallies, pickets, human chains, riots, festivals, ceremonies, street theatre, vigils, strikes, boycotts, blockades, sit-ins, squats, and violent actions including bombs, firebombs, molotov cocktails, graffiti, assaults, attacks, and arson.

To get the complete list of "action form" categories with their specific coding structure, you would need to consult the full codebook PDF directly, as the search results contain excerpts but not the complete categorized list. The official codebook at https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf should contain the detailed variable definitions and the complete "action form" categories list you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "a125d1a2-0937-4e4b-ba28-f81bd8a003f7"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-20T09:29:56.860Z_

<details><summary>↩ Tool result · `toolu_01XLN9b8M5ZUJ5zgGX6VnP1X`</summary>

```text
Web search results for query: "site:dataverse.harvard.edu "Mass Mobilization" license CC0 terms download"

Links: [{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Replication Data for: Unpopular Protest: Mass Mobilization and Attitudes to Democracy in Post-Mubarak Egypt - The Journal of Politics Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml;jsessionid=05dd6f02a13e27718e597bbbabd5?persistentId=doi:10.7910/DVN/NDHKSG&fileSortField=date&fileSortOrder=desc"},{"title":"Replication Data for: Regime Transformation From Below: Mobilization for Democracy and Autocracy From 1900 to 2021 - Comparative Political Studies Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQPN8D"},{"title":"Measuring and Predicting Speed of Social Mobilization","url":"https://arxiv.org/pdf/1303.3805"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired   and Ascribed Traits","url":"https://arxiv.org/pdf/1404.6935"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired and Ascribed Traits","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3989266/"}]

I found the search results for the Mass Mobilization dataset on Harvard Dataverse. Here's what I found:

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The Mass Mobilization Data project covers protests against governments across all countries from 1990-2020.

The main dataset appears to be hosted at:
- **Harvard Dataverse**: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
- **Project page**: https://massmobilization.github.io

However, the search results don't include specific details about the CC0 license terms or download information you were looking for. To access the specific licensing terms and download options, you would need to visit the dataset page directly on Harvard Dataverse, where such information is typically displayed prominently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "405467b6-2aba-4b40-849d-ef500694a4a9"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T09:29:57.165Z_

<details><summary>↩ Tool result · `toolu_01JMj3mHDd5LeTt7XFYa5iDk`</summary>

```text
Web search results for query: ""protest news classification dataset" github huggingface download"

Links: [{"title":"[Dataset requests] New datasets for Text Classification · Issue #353 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/353"},{"title":"elnazrezaee/News-Classification-Dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/elnazrezaee/News-Classification-Dataset"},{"title":"valurank/PoliticalBias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/valurank/PoliticalBias"},{"title":"huggingface-datasets · GitHub Topics · GitHub","url":"https://github.com/topics/huggingface-datasets"},{"title":"okite97/news-data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/okite97/news-data"},{"title":"Hate-speech-CNERG/hatexplain · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Hate-speech-CNERG/hatexplain"},{"title":"AiresPucrs/News-Category-Dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AiresPucrs/News-Category-Dataset"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"Build software better, together","url":"https://github.com/topics/hate-speech-detection"},{"title":"mteb/NewsClassification · Datasets at Hugging Face","url":"https://huggingface.co/datasets/mteb/NewsClassification"}]

Based on the search results, I found several news classification datasets available on Hugging Face, though I didn't find a specific "protest news classification dataset." Here are the relevant resources:

## News Classification Datasets on Hugging Face:

1. **News-Classification-Dataset** - Available at elnazrezaee/News-Classification-Dataset on Hugging Face

2. **News-Category-Dataset** - The AiresPucrs/News-Category-Dataset can be loaded using: `from datasets import load_dataset` and `dataset = load_dataset("AiresPucrs/News-Category-Dataset", split = 'train')`

3. **News-Data** - The okite97/news-data dataset supports news article classification into different categories and was created and scraped at arise but later hosted on Hugging Face

4. **mteb/NewsClassification** - This is a Large News Classification Dataset with 120,000 training samples and 7,600 test samples, containing 4 unique labels

## To Download:

You can download these datasets directly from Hugging Face using the `datasets` library:
- Visit the Hugging Face Datasets page at huggingface.co/datasets
- Search for the specific dataset name
- Use the provided Python code snippets to load the data programmatically

If you're looking for a specific protest-related news classification dataset, you may need to search with different keywords or check GitHub repositories directly for academic datasets focused on protest detection or political content classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "695b786a-d4ac-41dc-83fc-c5fc9737aee5"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-20T09:29:57.352Z_

<details><summary>↩ Tool result · `toolu_01JMNPYH2Jbsec83VAt32NgQ`</summary>

```text
Web search results for query: ""Mass Mobilization" protest data sample size number of events rows 10000 17000"

Links: [{"title":"Mass Mobilization Project tracks protests around the world - Binghamton News","url":"https://www.binghamton.edu/news/story/3282/hit-the-streets-mass-mobilization-project-tracks-protests-around-the-world"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization and Regime Change. Evidence From a New Measure of","url":"https://v-dem.net/media/publications/Working_Paper_128_final.pdf"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Full article: Episodes of sustained protest: temporal patterns of online mobilization on X","url":"https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2585094"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Data - PLSC 410: Political Protests - Yale University Library Research Guides at Yale University","url":"https://guides.library.yale.edu/c.php?g=956915&p=6961578"},{"title":"Few-Shot Upsampling for Protest Size Detection","url":"https://arxiv.org/pdf/2105.11260"}]

Based on the search results, I found information about the Mass Mobilization Project protest dataset:

The Mass Mobilization data contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events. More specifically, the data covers more than 15,000 events since 1990.

The MM data cover 162 countries between 1990 and 2018. Each event records location, protest size, protester demands, and government responses.

So the sample size falls within the range you mentioned (10,000-17,000 events), with sources indicating over 10,000 events and more than 15,000 events across the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "e17ead27-5ae5-4f03-9361-884d1592174d"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T09:29:57.998Z_

<details><summary>↩ Tool result · `toolu_015uFcemakzgNYJQJuvkiH8v`</summary>

```text
Web search results for query: "CLEF ProtestNews shared task dataset download "event type" classification"

Links: [{"title":"(PDF) Overview of CLEF 2019 Lab ProtestNews: Extracting Protests from News in a Cross-Context Setting","url":"https://www.researchgate.net/publication/335551147_Overview_of_CLEF_2019_Lab_ProtestNews_Extracting_Protests_from_News_in_a_Cross-Context_Setting"},{"title":"(PDF) Extraction of political event data from news articles in a cross-context setting","url":"https://www.academia.edu/40865598/Extraction_of_political_event_data_from_news_articles_in_a_cross_context_setting"},{"title":"(PDF) Automated Extraction of Socio-political Events from News (AESPEN): Workshop and Shared Task Report","url":"https://www.researchgate.net/publication/341369381_Automated_Extraction_of_Socio-political_Events_from_News_AESPEN_Workshop_and_Shared_Task_Report"},{"title":"(PDF) Multilingual Protest News Detection - Shared Task 1, CASE 2021","url":"https://www.academia.edu/64931265/Multilingual_Protest_News_Detection_Shared_Task_1_CASE_2021"},{"title":"IIITT at CASE 2021 Task 1: Leveraging Pretrained ...","url":"https://aclanthology.org/2021.case-1.13.pdf"},{"title":"Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction | Data Intelligence | MIT Press","url":"https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"},{"title":"Event Coreference Resolution for Contentious Politics Events","url":"https://arxiv.org/pdf/2203.10123"}]

Based on the search results, I found information about the CLEF ProtestNews shared task dataset:

## Overview

The CLEF 2019 Lab ProtestNews presented an overview on Extracting Protests from News in the context of generalizable natural language processing. The lab consisted of document, sentence, and token level information classification and extraction tasks.

## Task Structure

Task 1 on multilingual protest news detection comprises four subtasks that are document classification (subtask 1), sentence classification (subtask 2), event sentence coreference identification (subtask 3), and event extraction (subtask 4).

## Dataset Composition

The training and development data were collected from India and test data was collected from India and China. For sentence classification, the dataset comprises 26,208 sentences in three languages (English, Spanish, and Portuguese), with two classes: Event (the sentence indicates an event of the past) and Not-event (the sentence does not talk about any event).

## Participation

The lab attracted 58 teams to participate.

However, the search results do not contain direct download links or information about event type classification specifically. For actual dataset downloads, you may need to visit the official CLEF website or CodaLab platform where the shared task was hosted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "99857fa6-dbdd-4d46-bb81-77ebca82135f"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-20T09:29:58.571Z_

<details><summary>↩ Tool result · `toolu_01DkRgHB4fMrN4Tdjwxd7QxB`</summary>

```text
Web search results for query: "CASE shared task 2021 2022 "socio-political event" dataset download github"

Links: [{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text","url":"https://groups.google.com/g/ml-news/c/24ZK--jfhV8"},{"title":"Final Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/final-call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"},{"title":"GitHub - furkan-celik/CASE21-SuNLP-Models: Models developed for task 1 of CASE21 by SuNLP Team · GitHub","url":"https://github.com/furkan-celik/CASE21-SuNLP-Models"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2022): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2211.11359"}]

Based on the search results, here's what I found about the CASE shared task datasets for 2021-2022:

## CASE Shared Task Overview

The CASE workshop organized a Socio-political and Crisis Events Detection shared task at ACL-IJCNLP 2021, followed by a multilingual protest news detection shared task at CASE 2022.

## Dataset Access

The main GitHub repositories for accessing the datasets are:

- For CASE 2021 shared task data: https://github.com/emerging-welfare/case-2021-shared-task

- For CASE 2022 multilingual event tasks: https://github.com/emerging-welfare/case-2022-multilingual-event

- For the Causal News Corpus (Task 3): https://github.com/tanfiona/CausalNewsCorpus

## Key Dataset Information

The Causal News Corpus consists of 3,559 event sentences extracted from protest event news, annotated with sequence labels for causal relations, as well as Cause, Effect, and Signal spans.

You can access these repositories directly on GitHub to download the datasets needed for the socio-political event extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "f6aabbe0-50b1-469c-bb56-b8afab9e0293"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T09:29:59.569Z_

<details><summary>↩ Tool result · `toolu_011z74o5Sewr3YpWHrsYLhtD`</summary>

```text
Web search results for query: "SPEED "Social Political Economic Event Database" dataset download NLP"

Links: [{"title":"Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008). Cline Center for Advanced Social Research. V1.0.0. August 29 - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/social-political-economic-event-dataset-speed-liberia-philippines-2/"},{"title":"The Social, Political and Economic Event Database Project ...","url":"https://discuss-data.net/dataset/a47d51a9-6c5f-4bc4-827b-b310b083481e/"},{"title":"Social Political Economic Event Dataset (SPEED): Liberia ...","url":"https://databank.illinois.edu/datasets/IDB-7407320"},{"title":"Social, Political and Economic Event Database (SPEED) Project Data.","url":"https://staffblogs.le.ac.uk/socscilibrarians/2014/05/12/social-political-and-economic-event-database-speed-project-data/"},{"title":"(PDF) Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008) Codebook (v.1.0.0) About the Cline Center for Advanced Social Research | Dan Shalmon - Academia.edu","url":"https://www.academia.edu/40213536/Social_Political_Economic_Event_Dataset_SPEED_Liberia_Philippines_and_Sierra_Leone_1979_2008_Codebook_v_1_0_0_About_the_Cline_Center_for_Advanced_Social_Research"},{"title":"The Social, Political and Economic Event Database Project (SPEED) | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED"},{"title":"Data Download • Data on Armed Conflict and Security","url":"https://www.conflict-data.org/edacs/downloads/index.html"},{"title":"Distributions of Recorded Pain in Mental Health Records: A Natural Language Processing Based Study","url":"https://www.medrxiv.org/content/10.1101/2023.09.15.23295064.full.pdf"},{"title":"Automated Extraction of Mortality Information from Publicly Available Sources Using Language Models","url":"https://www.medrxiv.org/content/10.1101/2024.10.28.24316027.full.pdf"}]

Based on the search results, here's information about the SPEED dataset:

## Overview

The Social, Political and Economic Event Database Project (SPEED) is a technology-intensive dataset developed by the University of Illinois that offers worldwide social, political and economic event data from a global archive of news reports covering from January 1st 1946 to 2008 in the form of datasets available as downloadable material from their website.

## Dataset Access

The dataset and codebook, as well as additional information are available as a free download from the official SPEED website. The SPEED project includes observations representing events involving civil unrest, repression, or political violence in Sierra Leone, Liberia, and the Philippines (1979-2009).

## NLP Techniques Used

NLP techniques are used with lexicons of social group names (religious, ethnic, racial, tribal, nationality, insurgent, etc.) to capture the identity of event participants (initiators, targets, victims, etc.) and external facilitators/collaborators (other nations, NGOs, etc.).

The official SPEED project website hosted by the Cline Center for Advanced Social Research at the University of Illinois is the primary source for accessing the dataset and its documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2164d4d6-daf5-4245-b6e5-59fa3b09d93f"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Mass Mobilization Project codebook protester dema…",
  "usage": {
    "total_tokens": 21178,
    "tool_uses": 8,
    "duration_ms": 36921
  },
  "last_tool_name": "WebSearch",
  "uuid": "e0c66ae2-3615-4291-a65b-c051429101d9",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HfZ3G667obp6se6TQKhuPT`</summary>

```json
{
  "query": "Mass Mobilization Project codebook protester demand categories \"labor\" \"land\" \"police brutality\" \"political\" \"prices\" \"removal\" \"social\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ac30d648-4ee2-4a40-8e65-138df3d195e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqGZAimU3Y2rbwMYyLiCVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 19319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1529,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Clark Regan \"Mass Mobilization\" journal paper cit…",
  "usage": {
    "total_tokens": 21227,
    "tool_uses": 9,
    "duration_ms": 37722
  },
  "last_tool_name": "WebSearch",
  "uuid": "9ba21424-8c3a-4550-9885-45eeec4cdc6a",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016iz5oKAPXJdKsEckrjhiNS`</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization\" journal paper citation 2016 2018 \"International Interactions\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5c2d78d7-4be5-4e10-b8fd-5e456469060e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqGZAimU3Y2rbwMYyLiCVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 19319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1529,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for Indian protest event dataset NLP annotation \"even…",
  "usage": {
    "total_tokens": 23312,
    "tool_uses": 10,
    "duration_ms": 32466
  },
  "last_tool_name": "WebSearch",
  "uuid": "f7ce7e3a-e598-4c17-8198-02fc1113fc03",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHN3NSH31hC8irTF4WBKg4`</summary>

```json
{
  "query": "Indian protest event dataset NLP annotation \"event type\" classification download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "eb447b55-dc17-4511-ad22-c7314b268435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154ciRVgDUzRppyQV3JqXkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 18908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4374,
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

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for GLOCON \"Global Contentious Politics\" dataset down…",
  "usage": {
    "total_tokens": 23313,
    "tool_uses": 11,
    "duration_ms": 33363
  },
  "last_tool_name": "WebSearch",
  "uuid": "37fc0a6d-757e-42d8-bb0c-2d7ca9512f80",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YH4xKLgMjLshDQzmcLUabE`</summary>

```json
{
  "query": "GLOCON \"Global Contentious Politics\" dataset download categories event types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c2d17534-1f5c-4a39-9008-1f00dfd61582",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154ciRVgDUzRppyQV3JqXkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 18908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4374,
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

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for huggingface dataset protest event classification …",
  "usage": {
    "total_tokens": 23314,
    "tool_uses": 12,
    "duration_ms": 34055
  },
  "last_tool_name": "WebSearch",
  "uuid": "06dbf955-375f-4c63-a802-ab498a8204f1",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S2KAmr8gbreLgGwknZ3meM`</summary>

```json
{
  "query": "huggingface dataset protest event classification \"event type\" categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "362a61ce-c343-4c80-bc34-5fe123c2704e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154ciRVgDUzRppyQV3JqXkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 18908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4374,
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

_source line 95 · 2026-05-20T09:30:05.879Z_

<details><summary>↩ Tool result · `toolu_018PX5GJDBTbPm3NKbJ58Wmd`</summary>

```text
Web search results for query: "PolDem protest dataset "creative commons" OR "CC BY" OR license OR "terms of use" cite Kriesi Hutter"

Links: [{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem – Protest Dataset 30 European countries - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"Databases | WZB","url":"https://www.wzb.eu/en/publications/databases"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Platform for Protest and Conflict in Europe | WZB","url":"https://www.wzb.eu/en/news/platform-for-protest-and-conflict-in-europe"}]

Let me search more specifically for the licensing and terms of use information for the PolDem dataset.

Links: [{"title":"Data - Creative Commons","url":"https://wiki.creativecommons.org/wiki/data"},{"title":"Common license types for datasets and what they mean - Get Help","url":"https://libanswers.ucalgary.ca/faq/200582"},{"title":"Common license types for datasets - Documentation","url":"https://docs.data.world/en/214274-common-license-types-for-datasets.html"},{"title":"Choosing a licence for your data","url":"https://www.graindb.info/dataset/choose_a_licence"},{"title":"The POLUSA Dataset: 0.9M Political News Articles Balanced by Time and   Outlet Popularity","url":"https://arxiv.org/pdf/2005.14024"}]

Let me search more directly on the PolDem website for licensing information.

Links: [{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Terms and conditions of use for licensed electronic resources • European University Institute","url":"https://www.eui.eu/Research/Library/Collections/TermsAndConditions"},{"title":"Open Access: Copyright and licensing - EUI Library guides","url":"https://eui.libguides.com/OpenAccess/copyright"},{"title":"European Union Public License 1.2 | Choose a License","url":"https://choosealicense.com/licenses/eupl-1.2/"},{"title":"The Observatory - PolDem - European University Institute","url":"https://poldem.eui.eu/the-observatory/"},{"title":"Specific Terms and Conditions of Use • European University Institute","url":"https://www.eui.eu/AboutTheWebsite/TermsandConditionsofUse"},{"title":"European Union Public Licence - European Commission","url":"https://commission.europa.eu/about/departments-and-executive-agencies/digital-services/open-source-strategy-history/european-union-public-licence_en"},{"title":"Library Copyright Policy • European University Institute","url":"https://www.eui.eu/Research/Library/AboutTheLibrary/Copyright"},{"title":"European Union Public License 1.2 | Software Package Data Exchange (SPDX)","url":"https://spdx.org/licenses/EUPL-1.2.html"},{"title":"Copyright and terms of use - Research Data Guide - LibGuides at European University Institute","url":"https://eui.libguides.com/research-data-guide/protection-ethics-copyright/copyright"}]

Let me try a more specific search for PolDem data access and terms.

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem – Protest Dataset 30 European countries - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"The Observatory - PolDem - European University Institute","url":"https://poldem.eui.eu/the-observatory/"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"}]

Based on my search results, I was unable to find specific information about Creative Commons licensing, CC BY, or detailed "terms of use" stipulations for the PolDem protest dataset in the available search results. 

What I did find is that the PolDem – Protest Event Dataset 30 includes authors Kriesi, Hanspeter, Wüest, Bruno, Lorenzini, Jasmine, Makarov, Peter, Enggist, Matthias, Rothenhäusler, Klaus, Kurer, Thomas, Häusermann, Silja, Patrice Wangen, Altiparmakis, Argyrios, Borbáth, Endre, Bremer, Björn, Gessler, Theresa, Hunger, Sophia, Hutter, Swen, Schulte-Cloos, Julia, and Wang, Chendi (2019). The documentation indicates that PolDem aims to update and disseminate data within the scientific community and wider public, and to provide users with the relevant documentation, codebooks, and tools to interpret the data.

However, the specific licensing terms (whether Creative Commons, CC BY, or other license types) for the PolDem protest dataset are not clearly documented in the search results I retrieved. The actual terms of use may be available directly on the PolDem website or in supplementary documentation that wasn't captured in my search. I recommend checking the main PolDem portal (poldem.eui.eu) directly or contacting the dataset creators for the most current licensing information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "bd02d3fe-ad12-4c61-a482-b94e4fabe9e6"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T09:30:07.355Z_

<details><summary>↩ Tool result · `toolu_016iz5oKAPXJdKsEckrjhiNS`</summary>

```text
Web search results for query: "Clark Regan "Mass Mobilization" journal paper citation 2016 2018 "International Interactions""

Links: [{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Project - Political Science | Binghamton University","url":"https://www.binghamton.edu/massmobilization/about.html"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired   and Ascribed Traits","url":"https://arxiv.org/pdf/1404.6935"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Measuring and Predicting Speed of Social Mobilization","url":"https://arxiv.org/pdf/1303.3805"}]

Based on the search results, I found information about the Clark and Regan Mass Mobilization project:

Clark and Regan published Mass Mobilization Data in 2016. The MM data cover 162 countries between 1990 and 2018 and contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events, with each event recording location, protest size, protester demands, and government responses.

The dataset was published in 2016 via Harvard Dataverse. However, the search results do not contain a specific journal article published in "International Interactions" with this data. The references I found cite the Mass Mobilization Data as a 2016 dataset project rather than a journal article publication. If you're looking for a specific journal article in International Interactions that uses or cites this data, you may need to search more specifically for that journal publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "1034c440-9ec1-4862-bcde-96bcc12c9033"
}
```

</details>

---

### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for poldem protest dataset discuss-data.net license a…",
  "usage": {
    "total_tokens": 23769,
    "tool_uses": 9,
    "duration_ms": 48573
  },
  "last_tool_name": "WebSearch",
  "uuid": "1211aa0e-8610-4968-83a7-3bdbb6d879be",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 98_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjDfzMxwkfx6AEGc77QvmE`</summary>

```json
{
  "query": "poldem protest dataset discuss-data.net license access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "89fb31f6-5449-409a-940c-14c3d2bf2b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8SHyukGmnARy7oFmzDeNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 18677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for ACLED \"Armed Conflict Location Event Data\" text c…",
  "usage": {
    "total_tokens": 23315,
    "tool_uses": 13,
    "duration_ms": 38174
  },
  "last_tool_name": "WebSearch",
  "uuid": "8970e0fa-5ca4-48a9-a55a-9825854465ea",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YB8gtPpNLEKQm3KR6Aj1GP`</summary>

```json
{
  "query": "ACLED \"Armed Conflict Location Event Data\" text classification NLP dataset public download categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "46144147-4289-4e7d-aba3-6bf295c549df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154ciRVgDUzRppyQV3JqXkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 18908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4374,
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

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for PolDem protest 30 dataset \"issue\" categories \"act…",
  "usage": {
    "total_tokens": 23809,
    "tool_uses": 10,
    "duration_ms": 49214
  },
  "last_tool_name": "WebSearch",
  "uuid": "2cd81398-755f-40df-a4cd-421d2542a747",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UPMPdnjQapZzF7i7ZyUtuN`</summary>

```json
{
  "query": "PolDem protest 30 dataset \"issue\" categories \"action_form\" number of events N= observations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2fa58a6c-c653-4596-a4f2-414766c2a8f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8SHyukGmnARy7oFmzDeNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 18677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
        "ephemeral_1h_input_tokens": 0
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

_source line 103 · 2026-05-20T09:30:10.638Z_

<details><summary>↩ Tool result · `toolu_01HfZ3G667obp6se6TQKhuPT`</summary>

```text
Web search results for query: "Mass Mobilization Project codebook protester demand categories "labor" "land" "police brutality" "political" "prices" "removal" "social""

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization in the Modern Era: Introducing the Opposition Movements and Groups (OMG) Dataset, 1789–2019 - Marianne Dahl, Sirianne Dahlum, Hanne Fjelde, Haakon Gjerløw, Carl Henrik Knutsen, Carina Strøm-Sedgwick, Tore Wig, 2025","url":"https://journals.sagepub.com/doi/10.1177/00104140251369330"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Full article: Episodes of sustained protest: temporal patterns of online mobilization on X","url":"https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2585094"}]

I found information about the Mass Mobilization Project codebook and its protester demand categories. Here's what the search revealed:

The Mass Mobilization Project identifies seven categories of protester demands that describe the types of issues that motivate protest behavior. For each event, the MM data itemize what protesters demand across these seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

The demand categories you mentioned align with the official codebook structure:
- **Labor** - Protests against state policy that influence labor conditions or wage rates, including state-set labor policy, minimum wages, and state-owned or controlled industries
- **Land** - Access to or restrictions imposed on the use of land
- **Police brutality** - Listed as a distinct category
- **Political** - The political process category
- **Prices** - Prices/taxes category
- **Removal** - Removal of a politician
- **Social** - Social restrictions

Any protest event can have multiple demands.

The official codebook document appears to be available through Harvard Dataverse, where you can access the complete Mass Mobilization Data Project Codebook and User's Manual for more detailed descriptions of each demand category.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "898155df-f552-4c2c-ac89-f6d828708abf"
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-20T09:30:11.573Z_

<details><summary>↩ Tool result · `toolu_01YH4xKLgMjLshDQzmcLUabE`</summary>

```text
Web search results for query: "GLOCON "Global Contentious Politics" dataset download categories event types"

Links: [{"title":"New Dataset Collects Instances of 'Contentious Politics ...","url":"https://www.socialsciencespace.com/2023/12/new-dataset-collects-instances-of-contentious-politics-around-the-world/"},{"title":"Global Contentious Politics Dataset (GLOCON)","url":"https://glocon.ku.edu.tr/"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://zenodo.org/records/6540579"},{"title":"[PDF] Global Contentious Politics Database (GLOCON ...","url":"https://www.semanticscholar.org/paper/Global-Contentious-Politics-Database-(GLOCON)-Duru%C5%9Fan-Hurriyetoglu/dd035f2dc20a8aa29d33b31a293d7d3eebd0852c"},{"title":"(PDF) Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://www.academia.edu/79307023/Global_Contentious_Politics_Database_GLOCON_Annotation_Manuals"},{"title":"Global Contentious Politics Dataset (GLOCON) - YouTube","url":"https://www.youtube.com/watch?v=NLHUjYXUSu0"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://explore.openaire.eu/search/other?pid=10.5281/zenodo.6540579"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals | Zenodo","url":"https://zenodo.org/record/6540579/export/hx"},{"title":"[2206.10299] Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://arxiv.org/abs/2206.10299"},{"title":"Emerging Markets Welfare – Data","url":"https://emw.ku.edu.tr/data/"}]

Based on the search results, here's information about the GLOCON dataset:

## Overview
GLOCON is the first multi-country protest event database for the Global South that uses local sources for automated data collection. The database features event data for India, Brazil, South Africa, Turkey, and Argentina.

## Event Types
GLOCON records diverse types of events, including but not limited to demonstrations, rallies, strikes, clashes, and political violence.

## Dataset Categories
The database records contentious politics events with information available in the source about the events' time and place, actor, type, demands raised, and violence level. The database provides an interactive dashboard, distinguishing between violent vs. non-violent and rural vs. urban events.

## Data Access
The tool offers data visualizations drawn from categorical, geolocational, and temporal filters, and users can gain access to raw data through the download feature. The GLOCON Dashboard features instant access to the visualized event information geolocated and presented in time series.

The main GLOCON database can be accessed at https://glocon.ku.edu.tr/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "44c220ad-9529-4b53-ae95-9aeb5578d986"
}
```

</details>

---

### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Harvard Dataverse doi:10.7910/DVN/HTTWYL license …",
  "usage": {
    "total_tokens": 23045,
    "tool_uses": 10,
    "duration_ms": 49863
  },
  "last_tool_name": "WebSearch",
  "uuid": "804f7992-b838-4f05-8ae8-8d823612047d",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 106_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UEMM5zTmgsLGtrRFfLNPVm`</summary>

```json
{
  "query": "Harvard Dataverse doi:10.7910/DVN/HTTWYL license \"CC0\" OR \"public domain\" OR \"terms of use\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ce1d074a-65c9-4771-b3a1-33602e6348b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxDdQxG58UJM8iL5BmGsrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 20848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1057,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-20T09:30:13.522Z_

<details><summary>↩ Tool result · `toolu_01S2KAmr8gbreLgGwknZ3meM`</summary>

```text
Web search results for query: "huggingface dataset protest event classification "event type" categories"

Links: [{"title":"Introductory Guide to using HuggingFace for your Modelling Needs | by Louis D'hulst | Medium","url":"https://medium.com/@louisdhulst/introductory-guide-to-using-huggingface-for-your-modelling-needs-e4e9907cf6b4"},{"title":"Methodology of the dataset of detentions at protests from 2012 to 2023 | OVD-Info","url":"https://ovd.info/en/methodology-dataset-detentions-protests-2012-2023"},{"title":"QCRI/HumAID-event-type · Datasets at Hugging Face","url":"https://huggingface.co/datasets/QCRI/HumAID-event-type"},{"title":"Deep Learning based Multi-Label Image Classification of Protest   Activities","url":"https://arxiv.org/pdf/2301.04212"},{"title":"Protest Activity Detection and Perceived Violence Estimation from Social   Media Images","url":"https://arxiv.org/pdf/1709.06204"},{"title":"Ontology-driven Event Type Classification in Images","url":"https://arxiv.org/pdf/2011.04714"}]

Based on the search results, I found relevant information about HuggingFace datasets and protest event classification:

## HuggingFace Event Classification Datasets

The search results reveal several relevant datasets available on HuggingFace for event classification:

1. **HumAID-event-type Dataset**: The HumAID Twitter dataset consists of several thousands of manually annotated tweets collected during 19 major natural disaster events including earthquakes, hurricanes, wildfires, and floods from 2016 to 2019. The resulting annotated dataset consists of 11 labels.

2. **Protest Activity Detection**: The UCLA Protest Image Dataset consists of 40,764 images (11,659 protest images and hard negatives) with various annotations of visual attributes and sentiments.

## Event Type Categories for Protest Events

For protest event classification specifically, research has identified several categorization approaches:

- **Event Organizer Types**: Institutional protest is a category of events conducted by organisations or movements with a formalised structure.

- **Protest Format Categories**: Solitary protest is a form of protest carried out by an individual with or without a placard.

- **Visual Attributes in Protest Images**: Annotated images consist of 327 fire, 1,943 flag, 7,347 large crowd, 248 other, 2,159 police, 4,462 sign, and 1,233 student images.

These datasets provide comprehensive frameworks for classifying different types of protest events and related activities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9a2091b2-5ca3-48e0-b6d3-70c95446f8e7"
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-20T09:30:13.718Z_

<details><summary>↩ Tool result · `toolu_01YHN3NSH31hC8irTF4WBKg4`</summary>

```text
Web search results for query: "Indian protest event dataset NLP annotation "event type" classification download"

Links: [{"title":"arXiv:2008.00351v1 [cs.CL] 1 Aug 2020","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Cross-context News Corpus for Protest Events related ...","url":"https://openreview.net/pdf?id=7NZkNhLCjp"},{"title":"Enhancing Event Extraction from Short Stories through Contextualized Prompts","url":"https://arxiv.org/html/2412.10745"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Fine-grained Narrative Classification in Biased News Articles","url":"https://www.arxiv.org/pdf/2512.03582"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"(PDF) NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models","url":"https://www.academia.edu/110108255/NSUT_NLP_at_CASE_2022_Task_1_Multilingual_Protest_Event_Detection_using_Transformer_based_Models"}]

Based on the search results, here are the relevant findings about Indian protest event datasets with NLP annotation for event type classification:

## Key Datasets Found

Content from Indian Express (IEX), New Indian Express (NIEX), The Hindu (TH), Times of India (ToI) and other sources has been downloaded for labelling and annotation for protest event analysis.

Terms like "bandh" and "idol immersion" are event types that are specific to India and not covered by any general-purpose protest key terms list, highlighting the importance of India-specific datasets for protest event classification.

## Related NLP Approaches

The INDI-PROP dataset comprises 1,266 articles focusing on two polarizing socio-political events: CAA and the Farmers' protest, with annotation at two hierarchical levels: ideological article-bias and event-specific fine-grained narrative frames.

There is a gold standard corpus of protest events from various local and international sources containing document, sentence, and token level annotations.

## General NLP Methods

Some studies use 518 documents annotated at the word level for protest event mentions, where political scientists mark word spans which most directly denote protest events.

However, the search results do not provide specific download links for a single comprehensive Indian protest event dataset with event type classification. For specific access to these datasets, you may need to check academic repositories like arXiv, OpenReview, or reach out to the research groups directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9c03cba3-9ade-4fc7-acee-5f9571ceec45"
}
```

</details>

---

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Clark Regan \"Mass Mobilization in Civil War\" OR \"…",
  "usage": {
    "total_tokens": 23100,
    "tool_uses": 11,
    "duration_ms": 50589
  },
  "last_tool_name": "WebSearch",
  "uuid": "b839bdf4-5ab0-411c-8c3f-3f7f6f92574f",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A2aktLD8FZ3iZnsQ5wAidV`</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization in Civil War\" OR \"Mass Mobilization\" protest dataset journal article published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0ef0b435-2c39-4597-a471-ebe0f019c69c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxDdQxG58UJM8iL5BmGsrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 20848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1057,
        "ephemeral_1h_input_tokens": 0
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

_source line 111 · 2026-05-20T09:30:17.113Z_

<details><summary>↩ Tool result · `toolu_01UPMPdnjQapZzF7i7ZyUtuN`</summary>

```text
Web search results for query: "PolDem protest 30 dataset "issue" categories "action_form" number of events N= observations"

Links: [{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"}]

Based on the search results, I found information about the PolDem Protest 30 dataset and its variables. Here's what the search results reveal:

Peaceful demonstrations are most prevalent among the different action forms (indicator: 'action_form'), and violent protests and strikes are rather frequent as well, but nevertheless, their share is less than half than the share of demonstrations.

The dataset includes variables for action forms, issues and actors. The codebook and documentation files reference tables that describe the issue categories and action_form distributions across events.

However, the search results don't provide the specific numerical summary statistics you're asking about (the exact N= number of observations broken down by issue categories and action_form combinations). To access these detailed tables with the precise event counts by issue and action form, you would need to consult the full PolDem-Protest 30 codebook PDF or the actual dataset documentation directly from https://poldem.eui.eu/downloads/pea/, where these tables are typically presented with complete frequency distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "63774309-a105-4b3a-90c5-4c42c4a40985"
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-20T09:30:17.679Z_

<details><summary>↩ Tool result · `toolu_01RjDfzMxwkfx6AEGc77QvmE`</summary>

```text
Web search results for query: "poldem protest dataset discuss-data.net license access"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Discuss-data","url":"https://discuss-data.net/dataset/2cb6c216-7d34-4b94-9992-2748c5c6a110/"},{"title":"Review of the World Protests dataset","url":"https://zenodo.org/records/18484516"},{"title":"PolDem – Protest Dataset 30 European countries - Research output - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries/publications/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"}]

Based on the search results, here's what I found about the PolDem protest dataset:

## Overview

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large time-span.

## Dataset Details

The core of PolDem includes data on protest events in 30 European countries obtained by coding media coverage. The PolDem-Protest Dataset covers Protest Event Data on 30 European Countries from 2000-2015, produced by the European University Institute and University of Zurich.

## Access

The data and documentation can be downloaded at https://poldem.eui.eu/

## License and discuss-data.net

While the search results show that PolDem maintains its own data portal at poldem.eui.eu, the search results do not contain specific information about the PolDem protest dataset being hosted on discuss-data.net or details about the license terms for accessing this dataset. The search results do show that discuss-data.net hosts other protest-related datasets, but not specifically the PolDem dataset. For specific information about licensing and access terms on discuss-data.net, you may need to visit the platform directly or check the PolDem official website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0204b1b0-f062-422c-9c8f-837d84fdfd3a"
}
```

</details>

---

### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Search POLDEM dataset",
  "usage": {
    "total_tokens": 25590,
    "tool_uses": 11,
    "duration_ms": 60292
  },
  "last_tool_name": "ToolSearch",
  "uuid": "18076bf0-f320-40b1-8d8e-6d21a63fa670",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018M7QsByyfbbCWwooW54WWb`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "be71101a-a9fd-47fd-9b0c-f702025fbdd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVtjRQ6fanDQgoF36Wexe4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 742,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 23294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1038,
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

_source line 115 · 2026-05-20T09:30:20.432Z_

<details><summary>↩ Tool result · `toolu_018M7QsByyfbbCWwooW54WWb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3b8d897d-2bc3-46ab-b644-a5f048dee8b2"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-20T09:30:21.008Z_

<details><summary>↩ Tool result · `toolu_01UEMM5zTmgsLGtrRFfLNPVm`</summary>

```text
Web search results for query: "Harvard Dataverse doi:10.7910/DVN/HTTWYL license "CC0" OR "public domain" OR "terms of use""

Links: [{"title":"Harvard Dataverse | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories/harvard-dataverse"},{"title":"Harvard Dataverse General Terms of Use — Dataverse.org","url":"http://best-practices.dataverse.org/harvard-policies/harvard-terms-of-use.html"},{"title":"Data Repositories | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories"},{"title":"General Terms of Use - Harvard Dataverse Support","url":"https://support.dataverse.harvard.edu/harvard-dataverse-general-terms-use"},{"title":"Dataverse Community Norms | The Dataverse Project","url":"https://dataverse.org/best-practices/dataverse-community-norms"},{"title":"Establishment of an open data policy for Journal of Educational Evaluation for Health Professions, appreciation for invited reviewers, and acknowledgement of volunteers who made audio recordings","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5801429/"},{"title":"A large-scale study on research code quality and execution","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8861064/"},{"title":"Multiple license update turned the terms of some datasets with only CC0 licenses into \"custom licenses\" · Issue #9081 · IQSS/dataverse","url":"https://github.com/IQSS/dataverse/issues/9081"}]

Based on the search results, I can provide you with information about Harvard Dataverse's licensing practices:

Harvard Dataverse's default data usage license agreement for all uploaded materials is a Creative Commons Zero ("CC0") Public Domain Dedication Waiver. Harvard Dataverse strongly encourages use of a Creative Commons Zero (CC0) waiver for all public datasets, but dataset owners can specify other terms of use and restrict access to data.

By default, all datasets added in a Dataverse repository are granted the CC0 Public Domain Dedication, as the Dataverse software uses the CC0 waiver by default for all datasets because of its name recognition in the scientific community. However, data depositors can opt-out of using the CC0 waiver for their datasets, if needed.

The search results provide general information about Harvard Dataverse's licensing policies, but do not contain specific details about the particular dataset with DOI 10.7910/DVN/HTTWYL. To find the specific license information for that dataset, you would need to visit the dataset directly at https://doi.org/10.7910/DVN/HTTWYL on the Harvard Dataverse website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ca03a9cd-b6ab-43ec-8fd4-fb68024369a9"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-20T09:30:21.314Z_

<details><summary>↩ Tool result · `toolu_01A2aktLD8FZ3iZnsQ5wAidV`</summary>

```text
Web search results for query: "Clark Regan "Mass Mobilization in Civil War" OR "Mass Mobilization" protest dataset journal article published"

Links: [{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Data Is Plural — 2020.08.26 edition","url":"https://www.data-is-plural.com/archive/2020-08-26-edition/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"}]

Based on the search results, I found information about Clark and Regan's Mass Mobilization Project:

The Mass Mobilization project is led by David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame). The project's dataset covers more than 14,000 protests in more than 160 countries between 1990 and early 2017.

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. For each protest event, the project records protester demands, government responses, protest location, and protester identities.

The project aims to include any protest event that targets a country's own government with at least 50 participants, while excluding inter-communal demonstrations, rebel attacks or other armed protests, and political rallies.

Clark and Regan published Mass Mobilization Data in 2016, and the dataset is available through various repositories including Harvard Dataverse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "71b78f22-b130-49bd-b2f1-28233a611aca"
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-20T09:30:22.940Z_

<details><summary>↩ Tool result · `toolu_01YB8gtPpNLEKQm3KR6Aj1GP`</summary>

```text
Web search results for query: "ACLED "Armed Conflict Location Event Data" text classification NLP dataset public download categories"

Links: [{"title":"Introducing ACLED: An Armed Conflict Location and Events Dataset – Peace Research Institute Oslo (PRIO)","url":"https://www.prio.org/publications/3236"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset: Special Data Feature – Peace Research Institute Oslo (PRIO)","url":"https://www.prio.org/publications/4772"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset - Clionadh Raleigh, rew Linke, Håvard Hegre, Joakim Karlsen, 2010","url":"https://journals.sagepub.com/doi/10.1177/0022343310378914"},{"title":"Armed Conflict Location and Event Data - Wikipedia","url":"https://en.wikipedia.org/wiki/Armed_Conflict_Location_and_Event_Data"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset: Special Data Feature | Request PDF","url":"https://www.researchgate.net/publication/227574688_Introducing_ACLED_An_Armed_Conflict_Location_and_Event_Dataset_Special_Data_Feature"},{"title":"Armed Conflict Location and Event Data Project (ACLED) |","url":"https://terrorismresearch.uark.edu/acled/"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 2015","url":"https://www.strausscenter.org/wp-content/uploads/ACLED_Codebook_2015.pdf"}]

Now let me search specifically for information about the public download and event categories:

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"},{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/acled-introduces-new-event-types-and-sub-event-types/"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"Download data | ACLED","url":"https://acleddata.com/conflict-data/download-data"},{"title":"Conflict categories | ACLED","url":"https://acleddata.com/methodology/conflict-categories"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"Conflict data | ACLED","url":"https://acleddata.com/conflict-data"},{"title":"Armed Conflict Location & Event Data Project (ACLED) Humanitarian Data | 246 Datasets | HDX","url":"https://data.humdata.org/organization/acled"},{"title":"1 ACLED Definitions of Political Violence and Protest","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/2021/11/ACLED_Event-Definitions_v1_April-2019.pdf"}]

Based on my web search results, here is comprehensive information about ACLED (Armed Conflict Location and Event Data):

## Overview

ACLED is a non-profit organization registered in the United States that specializes in the real-time collection, analysis, and mapping of data on political violence and protest events around the world. It was founded in 2005 as a research initiative by political scientist Clionadh Raleigh. As of 2022, the dataset includes more than 1.3 million recorded events and offers updates through a global team of researchers and local partners.

## Event Types and Categories

The organization codes information on events such as armed clashes, demonstrations, riots, and strategic developments, including the date, location, actors, fatalities, and event type. More specifically, ACLED currently records six event types and 25 sub-event types, both violent and non-violent, categorized by three overarching disorder types: "Political violence," "Demonstrations," and "Strategic developments."

The main event types include: Violence against civilians (violent events where an organized armed group deliberately inflicts violence upon unarmed non-combatants); Protests (public demonstrations in which the participants are not violent); Riots (violent events where demonstrators or mobs engage in destructive acts against property and/or disorganized acts of violence against people); and Strategic developments (strategically important instances of non-violent activity by conflict actors).

## Conflict Categories

ACLED has created conflict categories that capture broad conflict dynamics — state repression, rebel insurgency, atrocities against civilians, terrorist activity, or foreign military engagement — using consistent and transparent criteria grounded in event type, actor behavior, and other key attributes in the dataset. These categories are available for event data from 2020 onward, including new data added on a weekly basis.

## Public Data Download

ACLED data can be downloaded using their export tool, by accessing curated data files, or via their API with filters for location, event type, date, etc. The full disaggregated event-based dataset is available for download through ACLED's Data Export Tool and API with an open access account. ACLED makes both data and analysis open for free use by the public.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b896fe1c-772b-4a98-8306-f3a77e7c657b"
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
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for massmobilization.github.io about protest demand c…",
  "usage": {
    "total_tokens": 24757,
    "tool_uses": 12,
    "duration_ms": 60667
  },
  "last_tool_name": "WebSearch",
  "uuid": "d88a2f4e-682d-461a-81b4-0bb15ad9500e",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 120_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X1M4WetRyyyAHLJyFcwQDp`</summary>

```json
{
  "query": "massmobilization.github.io about protest demand categories government response categories complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "542a4f80-4efc-4a8c-90e3-69435c7c5628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MkmMQXhGJ5tcH4gRw2cDt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 21905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2319,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" Clark Regan 2021 \"Internation…",
  "usage": {
    "total_tokens": 24801,
    "tool_uses": 13,
    "duration_ms": 61285
  },
  "last_tool_name": "WebSearch",
  "uuid": "728a0ed9-2661-4932-8240-45d4eace1537",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016K195C6PU5XjB5Zh1GbpJN`</summary>

```json
{
  "query": "\"Mass Mobilization\" Clark Regan 2021 \"International Studies Quarterly\" OR \"Journal of Conflict Resolution\" OR \"International Interactions\" cite paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "4fe0ef92-1a69-41c7-a1f8-27b40d93d7c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MkmMQXhGJ5tcH4gRw2cDt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 21905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2319,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/downloads/pea/poldem-protes…",
  "usage": {
    "total_tokens": 26264,
    "tool_uses": 12,
    "duration_ms": 65141
  },
  "last_tool_name": "WebFetch",
  "uuid": "bdd5c1ec-6d3c-4e19-8519-17b286d17ad4",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013MiWMFRq9y1EoXtFXgd2gS`</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf",
  "prompt": "Extract ALL information about: 1) The list of issue categories (issue_econ_private, issue_econ_public, etc.) and their descriptions. 2) The list of action_form categories and their descriptions. 3) Total number of observations/events in the dataset. 4) License or terms of use. 5) Citation information. 6) Any mention of human annotation / gold standard labels / intercoder reliability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b8c2d0a4-7a58-430f-b6f3-850d496a66a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoVmrRi46xDFFp9Qn29j3e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 24332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1356,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for github \"emerging-welfare\" case-2021-shared-task d…",
  "usage": {
    "total_tokens": 27388,
    "tool_uses": 14,
    "duration_ms": 55817
  },
  "last_tool_name": "WebSearch",
  "uuid": "d4c99c2e-8dac-406f-b348-4924140bc613",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GP3SxYTgtcNkWfopBtoN4y`</summary>

```json
{
  "query": "github \"emerging-welfare\" case-2021-shared-task data subtask event type categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "e0f82193-638b-4eaa-b706-73cf304a09b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcgsvsfAtQAeT6GQ7zz4vB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4038,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4038,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CEHA \"Conflict Events Horn of Africa\" dataset dow…",
  "usage": {
    "total_tokens": 27423,
    "tool_uses": 15,
    "duration_ms": 56758
  },
  "last_tool_name": "WebSearch",
  "uuid": "0143cef9-0b0e-4d46-a527-f1ef3158c48c",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 128_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X1ANs2xtKB6U4MWSvYcWbf`</summary>

```json
{
  "query": "CEHA \"Conflict Events Horn of Africa\" dataset download event types categories github zenodo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "6404964d-4977-4499-833a-b496f3319c0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcgsvsfAtQAeT6GQ7zz4vB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4038,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4038,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/downloads/pea/PEA_documenta…",
  "usage": {
    "total_tokens": 26321,
    "tool_uses": 13,
    "duration_ms": 67424
  },
  "last_tool_name": "WebFetch",
  "uuid": "cdaacb95-e1b8-4f82-9355-728e2e6cbbb4",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015izWVaVdJ2nyW1RqF5gVh7`</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf",
  "prompt": "Extract ALL information about: 1) Total number of events/observations in the dataset. 2) Issue categories and their full list. 3) Action form categories and their full list. 4) Human annotation methodology - was manual coding used? Intercoder reliability? Gold standard labels? 5) License or terms of use. 6) Full citation. 7) Sample size per country or total."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "03acdca7-6184-45ad-8f6a-b603bc0a3767",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoVmrRi46xDFFp9Qn29j3e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 24332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1356,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"political event coding\" dataset public download …",
  "usage": {
    "total_tokens": 27458,
    "tool_uses": 16,
    "duration_ms": 57857
  },
  "last_tool_name": "WebSearch",
  "uuid": "71d83099-f920-49b3-a49d-71d562ab0c2e",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVBYT73pQEMSHZBnjVGmZe`</summary>

```json
{
  "query": "\"political event coding\" dataset public download \"event type\" multi-class classification NLP benchmark 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "24eedecc-fd63-44f8-83e8-4aa662140159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcgsvsfAtQAeT6GQ7zz4vB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4038,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4038,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/data-overview/",
  "usage": {
    "total_tokens": 26378,
    "tool_uses": 14,
    "duration_ms": 68650
  },
  "last_tool_name": "WebFetch",
  "uuid": "876e1b0f-30e1-4afe-861b-60f5d3c0e0b2",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 134_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014J58EggwVHfVsgj63STfxW`</summary>

```json
{
  "url": "https://poldem.eui.eu/data-overview/",
  "prompt": "Extract all information about: 1) How to download the PolDem protest event dataset. 2) Whether registration or approval is needed. 3) License information. 4) List of available datasets and their sizes. 5) Any download links or instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "74ab9c11-a067-4368-b8c7-567ba2c2fdea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoVmrRi46xDFFp9Qn29j3e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 24332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1356,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for MPEDS \"Machine-learning Protest Event Data System…",
  "usage": {
    "total_tokens": 27493,
    "tool_uses": 17,
    "duration_ms": 58369
  },
  "last_tool_name": "WebSearch",
  "uuid": "2694dcd1-445c-42dc-982a-7aa84db08696",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 136_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BkhFFy43tnRzbqp1qiLhsd`</summary>

```json
{
  "query": "MPEDS \"Machine-learning Protest Event Data System\" dataset download github categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "82a0c3ca-5a5d-4699-849b-40292aab8702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcgsvsfAtQAeT6GQ7zz4vB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4038,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4038,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 137 · 2026-05-20T09:30:29.540Z_

<details><summary>↩ Tool result · `toolu_01X1M4WetRyyyAHLJyFcwQDp`</summary>

```text
Web search results for query: "massmobilization.github.io about protest demand categories government response categories complete list"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"GitHub - EmFib/Mass-Protests","url":"https://github.com/EmFib/Mass-Protests"},{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Analysis of Changepoints in Mass Mobilization Data","url":"https://massmobilization.github.io/mmChangepoint.html"},{"title":"The Mass Mobilization Project","url":"https://wt.social/post/1a7so955328518710844/history"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"MassMobilization (Mass Mobilization Data Project) · GitHub","url":"https://github.com/MassMobilization"}]

Based on the search results from massmobilization.github.io, here are the complete lists of protest demand and government response categories:

## Protest Demand Categories

The Mass Mobilization data itemize what protesters demand across seven categories: labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

## Government Response Categories

The dataset records up to seven types of government responses: accommodation, arrests, beatings, crowd dispersal, ignore, killings, and shootings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "81fd09e5-c604-44ec-b8ca-6cf46a386871"
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-20T09:30:32.805Z_

<details><summary>↩ Tool result · `toolu_013MiWMFRq9y1EoXtFXgd2gS`</summary>

```text
I cannot extract the requested information from this PDF document. The content provided is a binary/compressed PDF file structure (indicated by the "%PDF-1.3" header and encoded stream data), not readable plain text.

To help you, I would need:

1. **A text-extracted version** of the PDF document, or
2. **The original document file** that can be properly processed

The current format shows only PDF metadata, font references, and compressed image/content streams that cannot be meaningfully parsed for substantive information about:
- Issue categories
- Action form classifications
- Dataset size
- Licensing terms
- Citation details
- Annotation methodology

**Recommendation:** Please provide either a `.txt` file extracted from this PDF or share the document through an OCR service to convert it to readable text format.

[Binary content (application/pdf, 1.8MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269428379-yy4ryl.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "dca7f861-f9a3-4b15-9af9-402495372460"
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-20T09:30:33.682Z_

<details><summary>↩ Tool result · `toolu_014J58EggwVHfVsgj63STfxW`</summary>

```text
# PolDem Protest Event Dataset Information

Based on the provided content, here's what I found:

## 1) How to Download
The page mentions a **"Download"** section exists at poldem.eui.eu/download/, but specific download instructions aren't detailed in this overview page.

## 2) Registration or Approval Requirements
No information about registration or approval processes appears in this content.

## 3) License Information
No license details are provided in the material shown.

## 4) Available Protest Datasets
Three protest event datasets are listed:

- **poldem-protest_30**: "Protest events in 30 countries" (2000-2015)
- **poldem-protest_6**: "Protest events in 6 countries" (1975-2011)
- **poldem-protest_eu**: "Protest events in 6 countries, EU issues only" (1995-2010)

No file sizes are specified in this overview.

## 5) Download Links or Instructions
The content references online tools exist but provides no direct download links or detailed procedural steps. The page directs users to explore.poldem.eui.eu and mentions "R tools" for analysis support.

**Contact:** poldem@eui.eu or poldem@wzb.eu for additional details about access and download procedures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2e48539a-1e2e-4cb2-8bf3-5447fed84515"
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-20T09:30:34.387Z_

<details><summary>↩ Tool result · `toolu_01GP3SxYTgtcNkWfopBtoN4y`</summary>

```text
Web search results for query: "github "emerging-welfare" case-2021-shared-task data subtask event type categories labels"

Links: [{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"GitHub - emerging-welfare/case-2022-multilingual-event: The repository for the shared tasks Task 1 and Task 3 at CASE 2022 (to be held at EMNLP)","url":"https://github.com/emerging-welfare/case-2022-multilingual-event"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.researchgate.net/publication/353485828_Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"case-2021-shared-task/task2/test_dataset/test_set_final_release_with_labels.tsv at main · emerging-welfare/case-2021-shared-task","url":"https://github.com/emerging-welfare/case-2021-shared-task/blob/main/task2/test_dataset/test_set_final_release_with_labels.tsv"},{"title":"emerging-welfare · GitHub","url":"https://github.com/emerging-welfare"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"}]

Based on the search results, I found information about the GitHub repository for the CASE 2021 shared task related to event detection. Here's what I found:

The CASE 2021 shared task includes Task 1 on Multilingual protest news detection with Subtask 1 (Document classification), Subtask 2 (Sentence classification), Subtask 3 (Event sentence coreference identification), and Subtask 4 (Event extraction), as well as Task 2 on Fine-grained classification of Socio-political events and Task 3 on Discovering Black Lives Matter events in the United States.

Each line of the corpus file consists of three tab-delimited elements: (a) text snippet reporting an event, (b) event main type, and (c) event subtype. For the event classification subtask, the focus is on classification of events using one of 25 subtypes.

The search results show examples from the data including event type categories such as MAN_MADE_DISASTER, AGREEMENT, VIOL_DEMONSTR, and MOB_VIOL.

The code and data samples and submission formats can be found in the task1, task2, and task3 folders of the repository at https://github.com/emerging-welfare/case-2021-shared-task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "af2d16c4-90e6-415a-9ca8-69e9f5489c60"
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-20T09:30:34.954Z_

<details><summary>↩ Tool result · `toolu_015izWVaVdJ2nyW1RqF5gVh7`</summary>

```text
# PDF Content Extraction Issues

I cannot extract the requested information from the provided content. The file appears to be a **corrupted or improperly formatted PDF** containing:

- Binary image data (JPEG streams) rather than readable text
- Flate-compressed streams that don't decompress to meaningful content
- PDF structural elements without legible extracted text

## What I Can Observe:
- The document includes **3 image objects** (Im1, Im2, Im3) with dimensions suggesting charts/tables
- References to fonts and color spaces indicate this was originally a formatted document
- The file structure suggests it may be a research paper or dataset documentation

## Required Actions:

To help you extract this information, please provide:

1. **A text-based PDF** or converted document (DOCX, TXT)
2. **A readable image** of the relevant pages
3. **The original source document** if this is published research

Once you provide readable source material, I can extract:
- Dataset event counts
- Issue/action category taxonomies
- Annotation methodologies
- Licensing information
- Complete citations
- Sample sizes by region

Would you like to provide an alternative version of this document?

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269429750-rcfwgc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c3d4124e-678f-4962-8151-211033ebcfaf"
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-20T09:30:36.417Z_

<details><summary>↩ Tool result · `toolu_01BkhFFy43tnRzbqp1qiLhsd`</summary>

```text
Web search results for query: "MPEDS "Machine-learning Protest Event Data System" dataset download github categories"

Links: [{"title":"GitHub - MPEDS/mpeds: Machine-learning Protest Event Data System · GitHub","url":"https://github.com/MPEDS/mpeds"},{"title":"mpeds/README.md at master · MPEDS/mpeds","url":"https://github.com/MPEDS/mpeds/blob/master/README.md"},{"title":"Coding Protest Event Data & Studying Black Protest | Pamela E. Oliver","url":"https://www.ssc.wisc.edu/~oliver/protest-research/mpeds/"},{"title":"MPEDS · GitHub","url":"https://github.com/MPEDS"},{"title":"MPEDS - Automated Coding of Protest Event Data by MPEDS","url":"https://mpeds.github.io/"},{"title":"mpeds/cliff/Dockerfile at master · MPEDS/mpeds","url":"https://github.com/MPEDS/mpeds/blob/master/cliff/Dockerfile"},{"title":"MPEDS: Machine-Learning Protest Event Data System","url":"https://zenodo.org/records/886459"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"Coding Protest Event Data & Studying Black Protest","url":"https://users.ssc.wisc.edu/~oliver/protest-research/mpeds/"},{"title":"GitHub - MPEDS/mpeds-coder: MPEDS Annotation Interface","url":"https://github.com/MPEDS/mpeds-coder"}]

Based on the search results, here's what I found about MPEDS:

## Overview

MPEDS is a tool for facilitating the creation of protest event data using recent innovations from machine learning and natural language processing to generate protest event data with little to no human intervention.

## GitHub Repository

The main repository is located at **https://github.com/MPEDS/mpeds**. You will need to install Git LFS to properly download the large classifier and vectorizer files from this repository.

## Related Tools

The MPEDS system includes the MPEDS Annotation Interface (MAI), a browser-based coding interface that is available on GitHub as mpeds/mpeds-coder. The MPEDS Annotation Interface helps facilitate the creation of protest event datasets and could be used for the development of other types of event datasets or text annotation tasks.

## Dataset Access

The initial release was documented on Zenodo with DOI: 10.5281/zenodo.886459.

The search results provided information about the system's purpose and GitHub repositories, but did not contain specific details about event categories within the dataset. For more detailed information about the specific event categories used in MPEDS, you may want to consult the academic papers referenced or visit the GitHub repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "a3425756-9f10-43f6-a2f6-083e525bf5d6"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/downloads/pea/PEA_codebook_…",
  "usage": {
    "total_tokens": 27942,
    "tool_uses": 15,
    "duration_ms": 78544
  },
  "last_tool_name": "WebFetch",
  "uuid": "625faf12-73a6-47e0-99cc-e24b31b5d39b",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 144_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T9T7uPZtL9uyqjFhW9aknp`</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf",
  "prompt": "Extract ALL information: 1) Full list of issue categories with descriptions. 2) Full list of action_form categories with descriptions. 3) Total number of events. 4) Human annotation / coding methodology. 5) License. 6) Citation. Report everything you can read from this document."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "19777ce1-e59d-4fbe-bdd9-b36f21f5b718",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EnAFRUgYV7Wm6jJg1cZU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 331,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 25688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1174,
        "ephemeral_1h_input_tokens": 0
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

_source line 145 · 2026-05-20T09:30:41.528Z_

<details><summary>↩ Tool result · `toolu_016K195C6PU5XjB5Zh1GbpJN`</summary>

```text
Web search results for query: ""Mass Mobilization" Clark Regan 2021 "International Studies Quarterly" OR "Journal of Conflict Resolution" OR "International Interactions" cite paper"

Links: [{"title":"Mobilization: An International Quarterly","url":"https://mobilization.kglmeridian.com/"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"About this Journal - Mobilization: An International Quarterly","url":"https://mobilization.kglmeridian.com/page/about"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Opportunities to Fight - David H. Clark, Patrick M. Regan, 2003","url":"https://journals.sagepub.com/doi/10.1177/0022002702239513"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"}]

The search results show references to the Mass Mobilization Database created by Clark and Regan, but I haven't found a specific 2021 publication in one of the three journals you mentioned. Let me search more specifically for a 2021 paper by Clark and Regan in these journals.

Links: [{"title":"International Studies Quarterly","url":"https://www.scimagojr.com/journalsearch.php?q=25848&tip=sid&clean=0"},{"title":"Issues | International Studies Quarterly | Oxford Academic","url":"https://academic.oup.com/isq/issue"},{"title":"International Studies Quarterly | JSTOR","url":"https://www.jstor.org/journal/intestudquar"},{"title":"Presence of Ecuador in the Web of Science from open access in post-pandemic period 2019-2021: A multivariate analysis","url":"https://www.biorxiv.org/content/10.1101/2024.03.18.585617.full.pdf"},{"title":"International Studies Quarterly Latest Journal's Impact IF 2021-2022 | Trend, Prediction, Ranking & Key Factor Analysis","url":"https://academic-accelerator.com/Impact-of-Journal/International-Studies-Quarterly"}]

Links: [{"title":"Opportunities to Fight - David H. Clark, Patrick M. Regan, 2003","url":"https://journals.sagepub.com/doi/10.1177/0022002702239513"},{"title":"Building a Science of World Politics - Stuart A. Bremer, Patrick M. Regan, David H. Clark, 2003","url":"https://journals.sagepub.com/doi/10.1177/0022002702239508"},{"title":"Patrick REGAN | Research profile","url":"https://www.researchgate.net/profile/Patrick-Regan-2"},{"title":"David H. Clark Professor and Chair Department of Political Science","url":"https://www.binghamton.edu/political-science/docs/cv/dclark.cv.pdf"},{"title":"Substituting Policies during U.S. Interventions in Internal Conflicts - Patrick M. Regan, 2000","url":"https://journals.sagepub.com/doi/10.1177/0022002700044001005"}]

Let me search more specifically for their 2021 publication on mass mobilization.

Links: [{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"Thin-skinned leaders: regime legitimation, protest issues, and repression in autocracies | Political Science Research and Methods | Cambridge Core","url":"https://www.cambridge.org/core/journals/political-science-research-and-methods/article/thinskinned-leaders-regime-legitimation-protest-issues-and-repression-in-autocracies/146ADA79CAFEB3C31743472215AA15F7"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization and Regime Change. Evidence From a New Measure of","url":"https://v-dem.net/media/publications/Working_Paper_128_final.pdf"},{"title":"Regime Transformation From Below: Mobilization for Democracy and Autocracy From 1900 to 2021 - Sebastian Hellmeier, Michael Bernhard, 2023","url":"https://journals.sagepub.com/doi/10.1177/00104140231152793"},{"title":"ORIGINAL ARTICLE Thin-skinned leaders: regime legitimation, protest issues,","url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/146ADA79CAFEB3C31743472215AA15F7/S2049847021000194a.pdf/thin-skinned-leaders-regime-legitimation-protest-issues-and-repression-in-autocracies.pdf"}]

Let me try one more search to find a specific 2021 Clark and Regan paper with one of those journals.

Links: [{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"59th Annual International Affairs Symposium Searches for Clarity in Controversy • Newsroom • Lewis & Clark","url":"https://www.lclark.edu/_ingredients/templates/details/newsroom.php?id=45589"},{"title":"David H. Clark Professor and Chair Department of Political Science","url":"https://www.binghamton.edu/political-science/docs/cv/dclark.cv.pdf"},{"title":"Dynamics of Political Protests","url":"https://ideas.repec.org/a/cup/intorg/v72y2018i02p485-521_00.html"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Thin-skinned leaders: regime legitimation, protest issues, and repression in autocracies | Political Science Research and Methods | Cambridge Core","url":"https://www.cambridge.org/core/journals/political-science-research-and-methods/article/thinskinned-leaders-regime-legitimation-protest-issues-and-repression-in-autocracies/146ADA79CAFEB3C31743472215AA15F7"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Dynamics of political protests Klein, G.R.; Regan, P.M. Citation","url":"https://scholarlypublications.universiteitleiden.nl/access/item:3217462/view"},{"title":"Teamster Power, 2021 ESD 141 | 2020–2021 Election Supervisor Protest Decisions | Office of the Election Supervisor for the IBT","url":"https://www.ibtvote.org/Protest-Decisions/esd2020/2021esd141"}]

Based on my search results, I was unable to locate a specific 2021 publication by Clark and Regan in *International Studies Quarterly*, *Journal of Conflict Resolution*, or *International Interactions*. 

However, my searches did reveal that:

Klein and Regan published "Dynamics of Political Protests" in International Organization in 2018, which examined government responses to protest dynamics. While this isn't the exact paper you're searching for, it appears to be an important recent work from Regan on mass mobilization topics.

Additionally, David H. Clark and Patrick M. Regan are the Principal Investigators for the Mass Mobilization project, which is a well-established dataset that has been widely cited in the literature on protest and government responses.

If you're looking for a specific 2021 publication, you may want to:
- Check their institutional websites at Binghamton University and University of Notre Dame
- Search academic databases like Google Scholar or JSTOR directly
- Verify the exact year and journal name, as the publication may be in a different year or venue than expected


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0c6a4f30-80dd-4f97-bb2c-5ac7235c7381"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://discuss-data.net/dataset/c7e7af8f-fa6f-46…",
  "usage": {
    "total_tokens": 28004,
    "tool_uses": 16,
    "duration_ms": 81520
  },
  "last_tool_name": "WebFetch",
  "uuid": "b336d136-433a-4253-ab25-4dd2ec268168",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hxsw8aMQpZSUDapWsDqhJW`</summary>

```json
{
  "url": "https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/",
  "prompt": "Extract all information about: 1) License of the PolDem dataset. 2) Number of observations. 3) Download method and whether registration is required. 4) Citation. 5) Any metadata about categories or variables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "7b755298-d01b-4cba-8bd8-cc64f76dd6c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EnAFRUgYV7Wm6jJg1cZU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 331,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 25688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1174,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://research.vu.nl/en/datasets/poldem-protest…",
  "usage": {
    "total_tokens": 28066,
    "tool_uses": 17,
    "duration_ms": 82547
  },
  "last_tool_name": "WebFetch",
  "uuid": "b4658203-4d55-47fa-9d39-3af2ac7c109f",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NBwHPbTq3QinbzuP39nPfn`</summary>

```json
{
  "url": "https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries",
  "prompt": "Extract all information: 1) License or access rights. 2) Citation. 3) Dataset description, size, number of events. 4) Authors. 5) Any DOI. 6) Keywords or categories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "933aec31-cc46-42d1-b1c2-f2194377b850",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EnAFRUgYV7Wm6jJg1cZU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 331,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 25688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1174,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" dataset freely downloadable n…",
  "usage": {
    "total_tokens": 27886,
    "tool_uses": 14,
    "duration_ms": 80749
  },
  "last_tool_name": "WebSearch",
  "uuid": "b79c0c00-d153-447e-8b85-9feafbf50ebb",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 151_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kv7omqyCMxzRCvbs7B9uYS`</summary>

```json
{
  "query": "\"Mass Mobilization\" dataset freely downloadable no registration Harvard Dataverse CSV format rows columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "03c3ab59-ddaf-4d66-b2ae-7e7a38173c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUrBXCkdJAZUCprFYeQ3kg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 24224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3044,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Clark Regan \"Mass Mobilization\" \"how to cite\" OR …",
  "usage": {
    "total_tokens": 27927,
    "tool_uses": 15,
    "duration_ms": 81578
  },
  "last_tool_name": "WebSearch",
  "uuid": "59efaccb-ced0-4b90-9c56-86934e6732a5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 153_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHhADyNGHrit2d2EjtxKdD`</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization\" \"how to cite\" OR citation recommended 2016 dataset Dataverse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b8df0612-8bb0-435b-9bf8-9f68ff0323e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUrBXCkdJAZUCprFYeQ3kg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 24224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3044,
        "ephemeral_1h_input_tokens": 0
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

_source line 154 · 2026-05-20T09:30:46.184Z_

<details><summary>↩ Tool result · `toolu_01T9T7uPZtL9uyqjFhW9aknp`</summary>

```text
# Document Analysis: Event Data Codebook

I cannot reliably extract the requested information from this PDF document. The content appears to be heavily compressed and encoded (PDF binary format with FlateDecode compression), making direct text extraction impossible through my current processing capabilities.

## What I Can Determine:

**Document Structure:** This is a multi-page PDF containing what appears to be a codebook or reference guide, with embedded images and formatted text content spanning approximately 8 pages.

**Limitations:**
- The compressed stream data prevents accurate parsing of issue categories, action form categories, methodology details, license information, and citation format
- Text content is fragmented across encoded sections that require proper PDF decompression and rendering
- Image-based content (potentially containing tables or charts) cannot be analyzed

## Recommendation:

To extract the specific information you need, please:
1. Provide the document in plain text format
2. Supply an OCR-processed version
3. Share a text export from the PDF
4. Describe the document title/source so I can help you locate it in another format

If you have access to the original source document in text or structured format, I can provide comprehensive extraction of all requested categories, methodologies, and citations.

[Binary content (application/pdf, 422.4KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269440361-0b2vz1.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "adea3674-e90e-47a9-9d18-e5c51e3d2e38"
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-20T09:30:50.849Z_

<details><summary>↩ Tool result · `toolu_01NBwHPbTq3QinbzuP39nPfn`</summary>

```text
# PolDem – Protest Dataset 30 European Countries

## 1) License or Access Rights
No specific license details provided. Access available at: https://poldem.eui.eu/data-overview/

## 2) Citation
Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European countries. Cambridge University Press.

## 3) Dataset Description
Comprehensive protest event data spanning "1 Jan 2000 - 31 Dec 2015" across 30 European countries. Specific counts of events or dataset size not disclosed in provided material.

## 4) Authors
17 creators listed, including Hanspeter Kriesi (lead), Bruno Wüest, Jasmine Lorenzini, and Chendi Wang among others affiliated with Vrije Universiteit Amsterdam.

## 5) DOI
Not provided in the available content.

## 6) Keywords/Categories
- Economic grievances and political grievances
- Protest analysis
- European political systems
- Economic recession impacts
- Political contention
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c56462ef-09bb-4c7e-956e-4c4601f2c7d1"
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-20T09:30:52.047Z_

<details><summary>↩ Tool result · `toolu_01X1ANs2xtKB6U4MWSvYcWbf`</summary>

```text
Web search results for query: "CEHA "Conflict Events Horn of Africa" dataset download event types categories github zenodo"

Links: [{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/pdf/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.99/"},{"title":"[2412.13511] CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/abs/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://aclanthology.org/2025.coling-main.99.pdf"}]

Let me search more specifically for where the dataset can be accessed on GitHub or Zenodo:

Links: [{"title":"Zenodo - A universal repository for all your research outcomes","url":"https://www.openaire.eu/zenodo-guide"},{"title":"Zenodo - Wikipedia","url":"https://en.wikipedia.org/wiki/Zenodo"},{"title":"GitHub - ICAERUS-EU/Zenodo_Datasets: This repository includes the links and information for Zenodo datasets of each ICAERUS Use Case. · GitHub","url":"https://github.com/ICAERUS-EU/Zenodo_Datasets"},{"title":"GitHub - zenodo/zenodo: Research. Shared. · GitHub","url":"https://github.com/zenodo/zenodo"},{"title":"GitHub - rokibulroni/zenodo-datasets-index: API URL · GitHub","url":"https://github.com/rokibulroni/zenodo-datasets-index"},{"title":"GitHub - zenodo/zenodo-classifier","url":"https://github.com/zenodo/zenodo-classifier"},{"title":"Zenodo | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories/zenodo"},{"title":"osbm/zenodo · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osbm/zenodo"},{"title":"Zenodo","url":"https://zenodo.org/"}]

Let me search more specifically for the CEHA dataset with event types and categories:

Links: [{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.99/"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/pdf/2412.13511"},{"title":"[2412.13511] CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/abs/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://aclanthology.org/2025.coling-main.99.pdf"}]

Let me search for where the actual dataset can be accessed or downloaded:

Links: [{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/pdf/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.99/"},{"title":"[2412.13511] CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/abs/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://aclanthology.org/2025.coling-main.99.pdf"}]

Let me search for the paper's availability on HuggingFace or Dataminr resources:

Links: [{"title":"GitHub - dataminr-ai/CEHA","url":"https://github.com/dataminr-ai/CEHA"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/pdf/2412.13511"},{"title":"dataminr-ai · GitHub","url":"https://github.com/dataminr-ai"},{"title":"GitHub - huggingface/datasets: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools","url":"https://github.com/huggingface/datasets"},{"title":"Releases · huggingface/datasets","url":"https://github.com/huggingface/datasets/releases"},{"title":"Navigating Dataset Documentations in AI: A Large-Scale Analysis of   Dataset Cards on Hugging Face","url":"https://arxiv.org/pdf/2401.13822"},{"title":"huggingface-datasets · GitHub Topics · GitHub","url":"https://github.com/topics/huggingface-datasets"}]

Perfect! I found the information. Based on my search results, here's what I found about the CEHA dataset:

## CEHA: A Dataset of Conflict Events in the Horn of Africa

### Dataset Overview
CEHA is a dataset of 500 English event descriptions of conflict events in the Horn of Africa. The dataset consists of 500 English event descriptions regarding conflict events in the Horn of Africa region with fine-grained event-type definitions that emphasize the cause of the conflict.

### Event Type Categories
The four event-types are Tribal/Communal/Ethnic Conflict, Religious Conflict, Socio-political Violence Against Women, and Climate-Related Security Risks.

### Data Source and Composition
CEHA is a dataset containing 500 events sourced from ACLED and GDELT, with 250 events from each source.

### Tasks Supported
The dataset supports two tasks: Event-relevance Classification and Event-type Classification. Each event description is annotated with a binary Event-relevance label to indicate if it is associated with a specific violent conflict event.

### Where to Access the Dataset
The CEHA dataset and the code for the model training and evaluation are available at https://github.com/dataminr-ai/CEHA.

The dataset was published as part of a COLING 2025 paper by researchers at Dataminr Inc., and is designed to support conflict event detection in a region with limited NLP resources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "4d9b58be-3783-4856-8eb6-67183b563dfc"
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-20T09:30:52.340Z_

<details><summary>↩ Tool result · `toolu_01Kv7omqyCMxzRCvbs7B9uYS`</summary>

```text
Web search results for query: ""Mass Mobilization" dataset freely downloadable no registration Harvard Dataverse CSV format rows columns"

Links: [{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Replication Data for: Regime Transformation From Below: Mobilization for Democracy and Autocracy From 1900 to 2021 - Comparative Political Studies Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQPN8D"},{"title":"Replication Data for: Unpopular Protest: Mass Mobilization and Attitudes to Democracy in Post-Mubarak Egypt - The Journal of Politics Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml;jsessionid=05dd6f02a13e27718e597bbbabd5?persistentId=doi:10.7910/DVN/NDHKSG&fileSortField=date&fileSortOrder=desc"},{"title":"Exploring Economic Sectoral Dynamics Through High-resolution Mobility Data","url":"https://arxiv.org/pdf/2506.13985"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse.xhtml?alias=MMdata"}]

Based on my search results, here's what I found about the Mass Mobilization dataset:

## Dataset Overview

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The data cover 162 countries between 1990 and March 2017, and for each protest event, the project records protester demands, government responses, protest location, and protester identities.

## Access Location

The Mass Mobilization dataset can be found at https://dataverse.harvard.edu/dataverse/MMdata, which is hosted on Harvard Dataverse. The dataset appears to be publicly available for download in the Harvard Dataverse repository.

## Data Format & Structure

According to the search results, the dataset is available in CSV format, though the search results don't provide specific details about the exact number of rows and columns in the dataset structure.

For more detailed information about the specific columns, data structure, and exact row counts, I recommend visiting the Harvard Dataverse page directly at the URL provided above, where you should be able to see the complete file specifications and download options.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "116dcd49-c882-4177-aed0-783503cec49b"
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-20T09:30:52.433Z_

<details><summary>↩ Tool result · `toolu_01YHhADyNGHrit2d2EjtxKdD`</summary>

```text
Web search results for query: "Clark Regan "Mass Mobilization" "how to cite" OR citation recommended 2016 dataset Dataverse"

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"How do I cite a dataset in Dataverse? - Ask Us!","url":"https://askalibrarian.library.txstate.edu/faq/199438"},{"title":"Data Citation — Dataverse.org","url":"http://best-practices.dataverse.org/data-citation/"},{"title":"Data Citation | The Dataverse Project","url":"https://dataverse.org/best-practices/data-citation"},{"title":"Academic Credit | The Dataverse Project","url":"https://dataverse.org/best-practices/academic-credit"},{"title":"14- Data Citation in the Dataverse Network | For Attribution: Developing Data Attribution and Citation Practices and Standards: Summary of an International Workshop | The National Academies Press","url":"https://nap.nationalacademies.org/read/13564/chapter/15"},{"title":"Data Citation - Essential Resources for Locating and Using Numeric Data - Research Guides at Harvard Library","url":"https://guides.library.harvard.edu/c.php?g=310097&p=9720164"},{"title":"Cite Dataset - Queen's Dataverse Collection Data Deposit Guidelines - Research Guides at Queen's University Library","url":"https://guides.library.queensu.ca/dv-deposit-guidelines/steps-for-deposit/cite"}]

Based on the search results, I found information about the Mass Mobilization dataset:

The Mass Mobilization Data project was published in 2016 via Harvard Dataverse by David Clark & Patrick Regan and covers protests against governments across all countries from 1990-2020.

The DOI for the dataset is https://doi.org/10.7910/DVN/HTTWYL.

The standard citation for the dataset is: "Mass Mobilization Protest Data." Harvard Dataverse 2 (2016).

The Mass Mobilization data document citizen movements against governments, covering 162 countries between 1990 and March 2017, and for each protest event, the project records protester demands, government responses, protest location, and protester identities.

For instructions on how to cite this dataset, the citation is listed on the public page directly under the title near the top of the screen in a shaded area, and Dataverse has the built-in ability to send a citation to EndNote and BibTeX.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "e72c4b30-0e68-4e51-a530-ca661b47b2b6"
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-20T09:30:52.442Z_

<details><summary>↩ Tool result · `toolu_01Hxsw8aMQpZSUDapWsDqhJW`</summary>

```text
# PolDem Dataset Information

**1) License**
Not specified in the provided content.

**2) Number of Observations**
The dataset contains "30.000+ total entries" overall, with "1.655 events listed" for Estonia, Latvia, and Lithuania specifically.

**3) Download Method & Registration**
The content indicates the dataset is "available as a free download" from the "official Observatory for Political Conflict and Democracy in Europe website." Registration requirements are not mentioned.

**4) Citation**
"Nathalie Rathkamp (2025): Review of European University Institute/Center for Civil Society Research and WZB Berlin Social Science Center (2020): Observatory for Political Conflict and Democracy in Europe (published on Discuss Data), v. 1.0, Discuss Data, https://doi.org/10.48320/C7E7AF8F-FA6F-46D3-8AE5-41A4AAD6E4B9"

**5) Metadata - Categories & Variables**
The dataset covers protest events, election campaigns, public debates, and contentious episodes across 30 European countries (2000-2015). Keywords include: protests, strikes, demonstrations, environment, political issues, violent protests, confrontations, blockades, petitions, symbolic actions, and organizational actors (parties, unions, social groups).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "94868ac4-75ea-4cb0-934d-162c4f203c8c"
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-20T09:30:53.198Z_

<details><summary>↩ Tool result · `toolu_01FVBYT73pQEMSHZBnjVGmZe`</summary>

```text
Web search results for query: ""political event coding" dataset public download "event type" multi-class classification NLP benchmark 2023 2024 2025"

Links: [{"title":"Tracking the 2024 US Presidential Election Chatter on TikTok: A Public   Multimodal Dataset","url":"https://arxiv.org/pdf/2412.15583"},{"title":"A Public Dataset Tracking Social Media Discourse about the 2024 U.S.   Presidential Election on Twitter/X","url":"https://arxiv.org/pdf/2411.00376"},{"title":"Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential   Election: Development of a Public Dataset","url":"https://arxiv.org/pdf/2410.23638"},{"title":"Comparative Agendas","url":"https://www.comparativeagendas.net/project/us/datasets"},{"title":"Indonesian presidential election sentiment: Dataset of response public before 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10788203/"}]

Let me search more specifically for NLP benchmark datasets focused on event classification:

Links: [{"title":"Generative Approaches to Event Extraction: Survey and ...","url":"https://aclanthology.org/2024.futured-1.7.pdf"},{"title":"15 Must-Know NLP Benchmark Datasets to Master in 2025 🚀 - ChatBench","url":"https://www.chatbench.org/nlp-benchmark-datasets/"},{"title":"Ontology-driven Event Type Classification in Images","url":"https://arxiv.org/pdf/2011.04714"},{"title":"Multi-Label Classification Model From Scratch: Step-by-Step Tutorial","url":"https://huggingface.co/blog/Valerii-Knowledgator/multi-label-classification"},{"title":"Ensemble Detection of Single & Multiple Events at Sentence-Level","url":"https://arxiv.org/pdf/1403.6023"},{"title":"Multimodal Classification of Events in Social Media","url":"https://arxiv.org/pdf/1601.00599"}]

Let me search specifically for ACLED or other political event coding datasets:

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 2015","url":"https://www.strausscenter.org/wp-content/uploads/ACLED_Codebook_2015.pdf"},{"title":"Armed Conflict Location and Event Data - Wikipedia","url":"https://en.wikipedia.org/wiki/Armed_Conflict_Location_and_Event_Data"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"Conflict categories | ACLED","url":"https://acleddata.com/methodology/conflict-categories"},{"title":"Armed Conflict Location & Event Data Project (ACLED) Humanitarian Data | 246 Datasets | HDX","url":"https://data.humdata.org/organization/acled"},{"title":"Conflict data | ACLED","url":"https://acleddata.com/conflict-data"}]

Now let me search for NLP datasets specifically for event extraction and classification benchmarks:

Links: [{"title":"EABERT: An Event Annotation Enhanced BERT Framework for Event Extraction | Mobile Networks and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11036-023-02203-w"},{"title":"TextEE: A Standardized, Fair, and Reproducible Benchmark for Event Extraction","url":"https://khhuang.me/TextEE/"},{"title":"Generative Approaches to Event Extraction: Survey and ...","url":"https://aclanthology.org/2024.futured-1.7.pdf"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset | Request PDF","url":"https://www.researchgate.net/publication/347236490_MAVEN_A_Massive_General_Domain_Event_Detection_Dataset"},{"title":"Is a Large Language Model a Good Annotator for Event Extraction?","url":"https://ojs.aaai.org/index.php/AAAI/article/download/29730/31254"},{"title":"Document-Level Event Argument Extraction by Conditional Generation","url":"https://arxiv.org/pdf/2104.05919"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/pdf/2004.13590"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://bakser.github.io/files/EMNLP20-MAVEN/MAVEN.pdf"}]

Based on my web search results, I can provide you with a comprehensive overview of publicly available political event coding datasets and NLP benchmarks for event type classification:

## Key Findings:

### Major Political Event Datasets

ACLED (Armed Conflict Location & Event Data) is a non-profit organization that specializes in real-time collection, analysis, and mapping of data on political violence and protest events around the world. It codes information on events such as armed clashes, demonstrations, riots, and strategic developments, including the date, location, actors, fatalities, and event type. As of 2022, the dataset includes more than 1.3 million recorded events.

Data from ACLED are updated in real time and can be downloaded from the website's Data Export Tool, the website's Curated Data Files, or directly from the ACLED API. ACLED provides a codebook intended for all users of the dataset as well as additional FAQs and guides.

ACLED uses a hierarchical type structure, starting with three broad disorder types: political violence, demonstrations, and strategic developments. Each contains more specific event types — such as "Battles," "Riots," and "Violence against civilians" — and sub-event types that further break down the types of violence and disorder recorded.

### Event Extraction Benchmarks for NLP (2023-2024)

For NLP-focused event classification tasks, several standard benchmarks are commonly used:

ACE 2005 and MAVEN are event extraction benchmark datasets used to evaluate event extraction frameworks.

ACE 2005 is a widely used sentence-level event extraction dataset that provides annotations for 33 distinct event types, though it has an alarmingly low number of labeled samples for some event types like "Justice.Pardon", with fewer than five in certain cases.

The MAVEN dataset was introduced to address the shortage of samples, though it does not include argument labeling, and the long-tail distribution of events persists.

TextEE is a standardized, fair, and reproducible benchmark for event extraction that supports multiple datasets including MAVEN, ACE05, and others.

### Additional Political Datasets (2024)

The TikTok 2024 U.S. Presidential Election Dataset comprises 3.14 million videos published on TikTok between November 1, 2023, and October 16, 2024, and is publicly available.

A dataset capturing discourse on X (a.k.a., Twitter) related to the 2024 U.S. Presidential Election comprises 22 million publicly available posts collected from May 1, 2024, to July 31, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "15731e2d-5a6e-4cfa-8320-2ff9b5ca824a"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for Kriesi protest event analysis Europe \"issue categ…",
  "usage": {
    "total_tokens": 29633,
    "tool_uses": 18,
    "duration_ms": 95351
  },
  "last_tool_name": "WebSearch",
  "uuid": "a4399f82-dbd8-41c2-b880-4410ce76c611",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01138iQXzhGo3bD3yK7fbR3z`</summary>

```json
{
  "query": "Kriesi protest event analysis Europe \"issue categories\" \"economic\" \"cultural\" coding scheme semi-automated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "56936e09-ae4b-4840-bcdd-36420e0c7bec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyuMkJbYVDp1isd6D2BHMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 384,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 26862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1479,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for Mass Mobilization data.world download protest dat…",
  "usage": {
    "total_tokens": 29589,
    "tool_uses": 16,
    "duration_ms": 92062
  },
  "last_tool_name": "WebSearch",
  "uuid": "d206f264-7b74-4962-a848-909c83284ce5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 164_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0122YFg8Zjt1AzmLEBLYhxxd`</summary>

```json
{
  "query": "Mass Mobilization data.world download protest data 17000 events protester_demand government_response columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "a723f56a-d352-43b5-ab38-03273bb4dd56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dYhcKsfU1PG18cuEvJDD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 27268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 165_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" protest data NLP text classif…",
  "usage": {
    "total_tokens": 29627,
    "tool_uses": 17,
    "duration_ms": 92608
  },
  "last_tool_name": "WebSearch",
  "uuid": "91963250-7571-4bf5-9498-e6a0a7c88f5b",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 166_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CM7Z3HN9ebHJ5Pn38VhBT7`</summary>

```json
{
  "query": "\"Mass Mobilization\" protest data NLP text classification annotation label news article source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "514429fb-b941-457e-9c2f-71450573dbb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dYhcKsfU1PG18cuEvJDD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 27268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CASE 2021 task 2 \"fine-grained classification\" so…",
  "usage": {
    "total_tokens": 33129,
    "tool_uses": 18,
    "duration_ms": 85632
  },
  "last_tool_name": "WebSearch",
  "uuid": "27ed5e53-efa2-4835-9a3b-1c707e76f24e",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 168_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011o5jZG9xM4Wxq9Nd23suti`</summary>

```json
{
  "query": "CASE 2021 task 2 \"fine-grained classification\" socio-political event types 25 subtypes dataset download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "962e1d10-cfd6-4bbf-acb4-da45ea5591cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjKeE1UGJ25ZReMyNfEkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 4849,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4849,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 169_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for \"poldem\" OR \"protest event\" dataset Kriesi Hutter…",
  "usage": {
    "total_tokens": 29668,
    "tool_uses": 19,
    "duration_ms": 96207
  },
  "last_tool_name": "WebSearch",
  "uuid": "ebcdc317-0bd0-4fcb-8ee6-822cafb1307e",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 170_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DwfrB8khWyMBCrwH3eLxDx`</summary>

```json
{
  "query": "\"poldem\" OR \"protest event\" dataset Kriesi Hutter \"30,000\" OR \"30000\" OR \"number of events\" coding reliability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "6536f2e4-f287-451c-9cd1-61223d4a4fb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyuMkJbYVDp1isd6D2BHMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 384,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 26862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1479,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 171_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for MAVEN event detection dataset 168 event types dow…",
  "usage": {
    "total_tokens": 33166,
    "tool_uses": 19,
    "duration_ms": 86573
  },
  "last_tool_name": "WebSearch",
  "uuid": "93519f98-aedf-42b5-8d7a-f643ffe6e733",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 172_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hkdGiXhXijYekLLT1FU75`</summary>

```json
{
  "query": "MAVEN event detection dataset 168 event types download huggingface github protest political"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "10d0e552-d498-49c1-9c35-ace2dd21a8fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjKeE1UGJ25ZReMyNfEkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 4849,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4849,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"CrisisNLP\" OR \"CrisisLex\" OR \"HumAID\" event type…",
  "usage": {
    "total_tokens": 33203,
    "tool_uses": 20,
    "duration_ms": 88141
  },
  "last_tool_name": "WebSearch",
  "uuid": "bf803476-da11-49c0-9719-d398aa7f96a0",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 174_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018DMBqnGsbXgo16fzuiqWkR`</summary>

```json
{
  "query": "\"CrisisNLP\" OR \"CrisisLex\" OR \"HumAID\" event type classification dataset download categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9a866330-1606-4220-a17d-8175f5b6a592",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjKeE1UGJ25ZReMyNfEkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 4849,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4849,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 175_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"Crowd Counting Consortium\" OR \"ACLED\" protest cl…",
  "usage": {
    "total_tokens": 33240,
    "tool_uses": 21,
    "duration_ms": 88495
  },
  "last_tool_name": "WebSearch",
  "uuid": "de0f6428-ab1a-4892-81e4-1c7726b8b48d",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 176_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W8vXmkfbCXjEVE3jAVkzfG`</summary>

```json
{
  "query": "\"Crowd Counting Consortium\" OR \"ACLED\" protest classification dataset NLP text multi-class"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "83c36b91-09e7-4f58-b9ee-8da34d8ac342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjKeE1UGJ25ZReMyNfEkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 4849,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4849,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 177 · 2026-05-20T09:31:02.197Z_

<details><summary>↩ Tool result · `toolu_0122YFg8Zjt1AzmLEBLYhxxd`</summary>

```text
Web search results for query: "Mass Mobilization data.world download protest data 17000 events protester_demand government_response columns"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Project tracks protests around the world - Binghamton News","url":"https://www.binghamton.edu/news/story/3282/hit-the-streets-mass-mobilization-project-tracks-protests-around-the-world"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Data - PLSC 410: Political Protests - Yale University Library Research Guides at Yale University","url":"https://guides.library.yale.edu/c.php?g=956915&p=6961578"}]

Based on the search results, I found information about the Mass Mobilization protest data:

The Mass Mobilization dataset contains over 17,000 total entries, and provides information on protester demands and government responses. 

The data cover 162 countries between 1990 and 2018, and include events where 50 or more protesters publicly demonstrate against government, with each event recording location, protest size, protester demands, and government responses.

The dataset is available through multiple platforms:
- The official project page at https://massmobilization.github.io
- Harvard Dataverse, which hosts the Mass Mobilization Data project covering protests against governments from 1990-2020
- data.world also hosts a Mass Mobilization Protest Data dataset

The project is led by Principal Investigators David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame), and is sponsored by the Political Instability Task Force.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9714e5e9-1e2b-4e39-bc47-68e974f20cb6"
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-20T09:31:03.718Z_

<details><summary>↩ Tool result · `toolu_011o5jZG9xM4Wxq9Nd23suti`</summary>

```text
Web search results for query: "CASE 2021 task 2 "fine-grained classification" socio-political event types 25 subtypes dataset download"

Links: [{"title":"CASE 2021 Task 2 Socio-political Fine-grained Event Classification using Fine-tuned RoBERTa Document Embeddings - ACL Anthology","url":"https://aclanthology.org/2021.case-1.26/"},{"title":"CASE 2021 Task 2: Zero-Shot Classification of Fine-Grained Sociopolitical Events with Transformer Models - ACL Anthology","url":"https://aclanthology.org/2021.case-1.25/"},{"title":"CASE 2021 Task 2 – Benjamin J. Radford","url":"https://www.benradford.com/publications/2021-06-20/case-task-2.html"},{"title":"CASE 2021 Task 2 Socio-political Fine-grained Event ...","url":"https://aclanthology.org/2021.case-1.26.pdf"},{"title":"CASE 2021 Task 2: Zero-Shot Classiﬁcation of Fine-Grained","url":"https://aclanthology.org/2021.case-1.25.pdf"},{"title":"Proceedings of the 4th Workshop on Challenges and Applications of Automated Extraction of Socio-political Events from Text (CASE 2021) - ACL Anthology","url":"https://aclanthology.org/volumes/2021.case-1/"},{"title":"Fine-grained Event Classification in News-like Text Snippets - Shared Task 2, CASE 2021 - ACL Anthology","url":"https://aclanthology.org/2021.case-1.23/"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"}]

Based on the search results, I found information about CASE 2021 Task 2 on fine-grained classification of socio-political events:

## Task Overview

CASE 2021 Task 2 is a shared task on fine-grained event classification in news-like text snippets, divided into three sub-tasks: classification of text snippets reporting socio-political events (25 classes), a zero-shot learning problem with 3 additional event types without training data, and further extension introducing 2 additional event types announced shortly before evaluation.

## Dataset

The task uses the Armed Conflict Location & Event Data Project (ACLED) event taxonomy, which consists of 25 event subtypes pertaining to political violence, demonstrations (rioting and protesting) and selected non-violent, politically important events. The corpus consisted of a balanced selection of sub-events extracted from the ACLED event dataset.

## Finding the Dataset

The search results reference papers from the shared task proceedings at ACL Anthology (https://aclanthology.org/volumes/2021.case-1/), but they don't provide a direct download link for the dataset itself. To access the actual dataset, you would likely need to:

1. Check the official CASE 2021 workshop website
2. Contact the task organizers (the papers mention Jacek Haneczok, Guillaume Jacquet, and Jakub Piskorski as organizers)
3. Visit the ACLED project website for the original event taxonomy and data


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "c8335b02-d3b5-4475-96d0-f65b30d81bbe"
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-20T09:31:04.114Z_

<details><summary>↩ Tool result · `toolu_018hkdGiXhXijYekLLT1FU75`</summary>

```text
Web search results for query: "MAVEN event detection dataset 168 event types download huggingface github protest political"

Links: [{"title":"MAVEN","url":"https://thukeg.gitee.io/maven/"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset | Request PDF","url":"https://www.researchgate.net/publication/347236490_MAVEN_A_Massive_General_Domain_Event_Detection_Dataset"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.129/"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://papertalk.org/papertalks/11458"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publication/2020-11-17-MAVEN"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/pdf/2004.13590"},{"title":"[2004.13590] MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/abs/2004.13590"},{"title":"KG-NLP-Papers/EMNLP/2020/EE/8. MAVEN_A Massive General Domain Event Detection Dataset.md at main · Clearailhc/KG-NLP-Papers","url":"https://github.com/Clearailhc/KG-NLP-Papers/blob/main/EMNLP/2020/EE/8.%20MAVEN_A%20Massive%20General%20Domain%20Event%20Detection%20Dataset.md"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://bakser.github.io/files/EMNLP20-MAVEN/MAVEN.pdf"}]

Based on the search results, here's information about the MAVEN event detection dataset:

## Overview
MAVEN is an event detection dataset with massive general domain human annotated data containing 4,480 documents, 118,732 event mentions and 168 event types. It was collected by researchers at Tsinghua University and WeChat AI.

## Download Locations
The source code and dataset can be obtained from https://github.com/THU-KEG/MAVEN-dataset.

## Dataset Details
The dataset contains 4,480 Wikipedia documents, 118,732 event mention instances, and 168 event types. The dataset covers general domain events and includes 168 event types mapped to corresponding frames in FrameNet.

## Publication
The dataset was introduced in an EMNLP paper and addresses the limitations of existing event detection datasets by providing both larger scale data and broader coverage of event types compared to previous benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "67c3c236-1d63-4abb-b768-8d21c8a75800"
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-20T09:31:04.375Z_

<details><summary>↩ Tool result · `toolu_01138iQXzhGo3bD3yK7fbR3z`</summary>

```text
Web search results for query: "Kriesi protest event analysis Europe "issue categories" "economic" "cultural" coding scheme semi-automated"

Links: [{"title":"(PDF) Restructuring protest politics: the terrain of cultural winners","url":"https://www.researchgate.net/publication/307937428_Restructuring_protest_politics_the_terrain_of_cultural_winners"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Dynamics of protest mobilisation in the European poly-crisis","url":"https://cadmus.eui.eu/server/api/core/bitstreams/03312d5a-4f6e-5fdc-b0a8-cfdb82f0cd97/content"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"Political Conflict in Western Europe - Hanspeter Kriesi - Google Books","url":"https://books.google.com/books/about/Political_Conflict_in_Western_Europe.html?id=6_zivrfDd3AC"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"Full article: Dynamics of protest mobilisation in the European poly-crisis","url":"https://www.tandfonline.com/doi/full/10.1080/13501763.2024.2366388"}]

Based on the search results, I found relevant information about Kriesi's protest event analysis methodology and coding schemes in Europe:

Protest event analysis aims at retrieving and describing protest events so as to allow for cross-sectional and longitudinal analyses. A simplified version of the PEA approach established by Kriesi et al. (1995) and further elaborated by Hutter (2014, 2014a) has been used in various research projects.

Regarding issue categories, economic issues and especially economic claims addressed to public institutions are prevalent in the corpus, with indicators including 'issue_econ_private', 'issue_econ_public', 'issue_cult_lib', 'issue_environment', 'issue_political', 'issue_regional', 'issue_cult_cons', 'issue_xeno', and 'issue_other'. The framework distinguishes between three types of issues: economic issues, cultural issues (including political, culturally liberal, peace, ecological, immigration and culturally conservative, European integration, and Covid pro and anti-containment events).

Regarding semi-automated approaches, protest event analysis is a key method to study social movements, though manual coding of protest events is time-consuming and resource intensive, but recently advances in automated approaches offer opportunities to code multiple sources and create large data sets that span many countries and years.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "d0b21dc1-23aa-4fa7-945c-05f1c83f0d70"
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-20T09:31:04.894Z_

<details><summary>↩ Tool result · `toolu_01CM7Z3HN9ebHJ5Pn38VhBT7`</summary>

```text
Web search results for query: ""Mass Mobilization" protest data NLP text classification annotation label news article source"

Links: [{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://www.ovid.com/journals/absc/fulltext/10.1177/00027642211021650~protest-event-analysis-developing-a-semiautomated-nlp"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"When a Nation Speaks: Machine Learning and NLP in People's Sentiment Analysis During Bangladesh's 2024 Mass Uprising","url":"https://arxiv.org/pdf/2512.15547"}]

Based on the search results, here's what I found about Mass Mobilization protest data and NLP text classification:

## Mass Mobilization Project Overview

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018 and contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events. Each event records location, protest size, protester demands, and government responses.

## NLP and Text Classification Approaches

Research has developed semi-automated NLP approaches for protest event analysis. As training data, researchers use 518 documents that political scientists annotated at the word level for protest event mentions, instructing them to mark word spans which, according to their judgment, most directly denote protest events.

Annotation efforts have involved batches of samples annotated by two social and political scientists, adjudicated by an annotation supervisor, and improved by identifying annotation errors semi-automatically. These corpora have been found to have the variety and quality to develop and benchmark text classification and event extraction systems in a cross-context setting.

With growing computing power and the development of advanced natural language processing (NLP) methods, several attempts have been made to automate the creation of protest event data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5844cc9b-7f8f-4a23-a86c-074689ead21d"
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-20T09:31:05.483Z_

<details><summary>↩ Tool result · `toolu_01DwfrB8khWyMBCrwH3eLxDx`</summary>

```text
Web search results for query: ""poldem" OR "protest event" dataset Kriesi Hutter "30,000" OR "30000" OR "number of events" coding reliability"

Links: [{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"}]

Based on the search results, I found relevant information about the PolDem dataset and protest event analysis. Here's what I found:

## PolDem Dataset Overview

PolDem (Kriesi et al. 2020) provides 3 datasets with different countries and time ranges covered, based on newspaper articles obtained from NexisLexis. The core of PolDem is data on election campaigns in 15 European countries and on protest events in 30 European countries obtained by coding media coverage.

## Dataset Scale

The data collection relies on a semi-automated coding of newswire reports and covers 30 European countries and the time period from 2000 until 2015. For specific country analysis, the PolDem-30 dataset recorded 3491 events for Germany 2000–2020.

## Coding Reliability and Methodology

Regarding coding reliability, in order to assess coding quality, researchers manually coded 1,000 documents that were randomly drawn from all documents classified as irrelevant for three countries (Hungary, Spain, and the UK), with two years considered for each country—one pre-crisis (2004) and one post-crisis (2012) year.

The methodology description notes that protest event data has usually relied on newspaper coverage as data source, and mostly on manual coding, though manual coding of protest events across time and space is intensely time consuming. Since the corpus of relevant documents proved to be too large to manage for manual coding, a random sampling procedure was used, with 25% of documents sampled for countries with large document samples, 50% for average countries, and all documents for very small countries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "839b3e0f-d7c1-45dc-b0ad-1b1445211dea"
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
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" dataset human coded annotated…",
  "usage": {
    "total_tokens": 31289,
    "tool_uses": 18,
    "duration_ms": 104179
  },
  "last_tool_name": "WebSearch",
  "uuid": "1f7f4f9c-49c5-430a-9fdc-fa3a0d079502",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 184_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012pztqaVxoGAZQYnByLZDNR`</summary>

```json
{
  "query": "\"Mass Mobilization\" dataset human coded annotated news sources codebook \"hand-coded\" OR \"human-coded\" OR \"manually coded\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "4dba46aa-220e-4554-9088-abe755421246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdNsvrdSWUguTpEX3KbftD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1620,
      "cache_read_input_tokens": 28892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1620,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 185 · 2026-05-20T09:31:07.669Z_

<details><summary>↩ Tool result · `toolu_01W8vXmkfbCXjEVE3jAVkzfG`</summary>

```text
Web search results for query: ""Crowd Counting Consortium" OR "ACLED" protest classification dataset NLP text multi-class"

Links: [{"title":"CONSTRUCTING RELATIONAL AND VERIFIABLE PROTEST EVENT DATA:","url":"https://par.nsf.gov/servlets/purl/10417072"},{"title":"Protest and Conflict - Datasets - Washington and Lee University Research Guides at Washington and Lee University","url":"https://libguides.wlu.edu/c.php?g=99391&p=10563637"},{"title":"Few-Shot Upsampling for Protest Size Detection","url":"https://arxiv.org/pdf/2105.11260"},{"title":"GitHub - rexdouglass/crowd-counting-consortium: Data for the Crowd Counting Consortium Data Dashboard · GitHub","url":"https://github.com/rexdouglass/crowd-counting-consortium"},{"title":"About – Counting Crowds","url":"https://countingcrowds.org/about/"},{"title":"Crowd Counting Consortium U.S. Protest Event Data, 2017 ...","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F6OPP7H"},{"title":"Counting Protests in News Articles: A Dataset and Semi-Automated Data   Collection Pipeline","url":"https://arxiv.org/pdf/2102.00917"},{"title":"Crowd Counting Consortium - Ash Center - Harvard University","url":"https://ash.harvard.edu/programs/crowd-counting-consortium/"}]

I found relevant search results about the Crowd Counting Consortium and ACLED datasets. Here's what the search reveals:

**Crowd Counting Consortium (CCC):**
The Crowd Counting Consortium is a joint project of Harvard Kennedy School and the University of Connecticut that collects publicly available data on political protest events reported in the United States, including rallies, marches, demonstrations, and acts of civil disobedience. The data covers political crowds in the United States, including marches, protests, demonstrations, strikes, riots, and similar actions.

The dataset includes manually labeled news article URLs, dates, locations, crowd size estimates, and 494 discrete descriptive tags corresponding to 42,347 reported protest events in the United States between January 2017 and January 2021.

**ACLED:**
ACLED (Armed Conflict Location and Event Data) is an independent, impartial, international non-profit organization collecting data on violent conflict and protest in all countries and territories in the world.

**NLP Classification Work:**
The search results include a research paper on using NLP techniques with the CCC dataset. A study introduces a new task and dataset for improving information extraction systems' performance using documents annotated with coarse labels and small numbers of documents with fine-grained annotations, drawing on the Crowd Counting Consortium's dataset on dissent and collective action in the United States. The task of extracting events from news articles presents challenges to the NLP community in the fields of domain detection, slot filling, and coreference resolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "08e54e04-4b1c-43f8-a759-cd5dd539dcb9"
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-20T09:31:08.313Z_

<details><summary>↩ Tool result · `toolu_018DMBqnGsbXgo16fzuiqWkR`</summary>

```text
Web search results for query: ""CrisisNLP" OR "CrisisLex" OR "HumAID" event type classification dataset download categories labels"

Links: [{"title":"HumAID: Human-Annotated Disaster Incidents Data from Twitter with Deep Learning Benchmarks | Request PDF","url":"https://www.researchgate.net/publication/365035740_HumAID_Human-Annotated_Disaster_Incidents_Data_from_Twitter_with_Deep_Learning_Benchmarks"},{"title":"(PDF) HumAID: Human-Annotated Disaster Incidents Data from Twitter","url":"https://www.researchgate.net/publication/350720422_HumAID_Human-Annotated_Disaster_Incidents_Data_from_Twitter"},{"title":"README.md · QCRI/HumAID-all at 1843be7","url":"https://huggingface.co/datasets/QCRI/HumAID-all/commit/1843be77b41a2913a7919c780a0a7d8b463b827a"},{"title":"HumAID: Human-Annotated Disaster Incidents Data from ...","url":"https://ojs.aaai.org/index.php/ICWSM/article/download/18116/17919/21611"},{"title":"HumAID: Human-Annotated Disaster Incidents Data from Twitter with Deep Learning Benchmarks - Mendeley Data","url":"https://data.mendeley.com/datasets/zppcyk2fdt/1"},{"title":"CrisisNLP","url":"https://crisisnlp.qcri.org/"},{"title":"GitHub - firojalam/crisis_datasets_benchmarks: Crisis Dataset for Benchmarks Experiments · GitHub","url":"https://github.com/firojalam/crisis_datasets_benchmarks"},{"title":"Natural Disaster Tweets Classification Using Multimodal Data","url":"https://aclanthology.org/2023.emnlp-main.471.pdf"},{"title":"Information Type Classification with Contrastive Task-Specialized   Sentence Encoders","url":"https://arxiv.org/pdf/2312.11020"},{"title":"A Lightweight LLM Framework for Disaster Humanitarian Information Classification","url":"https://arxiv.org/pdf/2602.12284"}]

Based on the search results, here's information about these crisis-related event classification datasets:

## HumAID Dataset

The HumAID Twitter dataset consists of several thousands of manually annotated tweets collected during 19 major natural disaster events including earthquakes, hurricanes, wildfires, and floods from 2016 to 2019. 

**Categories/Labels:** HumAID categorizes posts into 11 classes, spanning from Not Humanitarian to Injured or Dead People. More specifically, the categories range from NOT HUMANITARIAN to INJURED OR DEAD PEOPLE which captures fine-grained information about disasters.

**Download:** The dataset and associated resources are publicly available at https://crisisnlp.qcri.org/humaid_dataset.html

## CrisisLex Dataset

CrisisLex comprises two datasets: CrisisLexT26 consisting of approximately 28,000 labeled tweets from 26 different disaster events that took place in 2012 and 2013. CrisisLexT6 contains approximately 60,000 labeled tweets from six disaster events that occurred between October 2012 and July 2013.

**Labels:** It includes disaster type and sub-type, and coarse- and fine-grained humanitarian class labels. Additionally, the T26 variant includes labeled tweets annotated with seven information types including the category NOT RELATED.

## CrisisNLP

CrisisNLP is among notable sites offering text material for crisis-related classification, and the resources are available at the CrisisNLP website at https://crisisnlp.qcri.org/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "10b2d225-76d8-4c14-ac42-295821a1ae58"
}
```

</details>

---

### System

_source line 187_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://journals.sagepub.com/doi/10.1177/00027642…",
  "usage": {
    "total_tokens": 31829,
    "tool_uses": 20,
    "duration_ms": 109661
  },
  "last_tool_name": "WebFetch",
  "uuid": "9e145ef2-274d-4ac7-9d72-95d402f90e8a",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 188_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017hxKeyLrbHKxVdSBH9JzxU`</summary>

```json
{
  "url": "https://journals.sagepub.com/doi/10.1177/00027642211021650",
  "prompt": "Extract all information about: 1) The semi-automated NLP approach for protest event analysis. 2) Issue categories used and their full list. 3) Action form categories. 4) Total number of events in the dataset. 5) Human annotation methodology and intercoder reliability. 6) Whether annotations are gold-standard human labels. 7) Dataset size. 8) Citation information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "7cd22316-1315-4ca2-b234-a8286ffb4975",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iz9BhTRwD22bAX3ohyydr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 28341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for Lorenzini Kriesi Makarov Wüest 2022 \"Protest Even…",
  "usage": {
    "total_tokens": 31894,
    "tool_uses": 21,
    "duration_ms": 110373
  },
  "last_tool_name": "WebSearch",
  "uuid": "145d0093-6b8d-424d-be88-02b6ce1ada0c",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MGM8TJ9FFZmCFvm7wsBrQW`</summary>

```json
{
  "query": "Lorenzini Kriesi Makarov Wüest 2022 \"Protest Event Analysis\" \"semiautomated\" NLP issue categories action form intercoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "fd7c5819-4009-490a-a38a-bff68ebb9dd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iz9BhTRwD22bAX3ohyydr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 28341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for github emerging-welfare case-2021-shared-task tas…",
  "usage": {
    "total_tokens": 37052,
    "tool_uses": 22,
    "duration_ms": 100738
  },
  "last_tool_name": "WebSearch",
  "uuid": "e55a1ecd-8a0b-4319-a9fd-0a41fa88cb33",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 192_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ntx5FFJkyg3kdUQCA2gJir`</summary>

```json
{
  "query": "github emerging-welfare case-2021-shared-task task2 event subtypes list data format download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "af5bfd20-d347-40d6-9e8e-858e411af3bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeokHNan4rtJkKYZqVCkFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3757,
      "cache_read_input_tokens": 32169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 193_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"cross-context news corpus\" protest event \"gold s…",
  "usage": {
    "total_tokens": 37089,
    "tool_uses": 23,
    "duration_ms": 101741
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2c3f29f-6fb1-451d-a425-31b6a877e956",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 194_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWXEMqFfng95ZLMfNcyrEh`</summary>

```json
{
  "query": "\"cross-context news corpus\" protest event \"gold standard\" download zenodo github categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "11355199-d64b-46f2-960d-cbc83bb3c60e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeokHNan4rtJkKYZqVCkFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3757,
      "cache_read_input_tokens": 32169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for POLDEM protest event dataset 30 download categori…",
  "usage": {
    "total_tokens": 37126,
    "tool_uses": 24,
    "duration_ms": 102704
  },
  "last_tool_name": "WebSearch",
  "uuid": "f975e57d-9a28-45d5-b7cb-beaf5bb8f73f",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 196_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Mtz3A8F8A2k9M6HjDvJdd`</summary>

```json
{
  "query": "POLDEM protest event dataset 30 download categories action forms license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "75bae519-d440-40a7-a323-d272578075dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeokHNan4rtJkKYZqVCkFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3757,
      "cache_read_input_tokens": 32169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for \"INDI-PROP\" dataset protest India NLP classificat…",
  "usage": {
    "total_tokens": 37163,
    "tool_uses": 25,
    "duration_ms": 103137
  },
  "last_tool_name": "WebSearch",
  "uuid": "1fb145b7-b365-49cf-88fb-7ca8fed772f6",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 198_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Maq8roQ33hULPTeDC1RrEb`</summary>

```json
{
  "query": "\"INDI-PROP\" dataset protest India NLP classification download categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3149c2d4-acf0-4c06-b535-d42fc8727cc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeokHNan4rtJkKYZqVCkFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3757,
      "cache_read_input_tokens": 32169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 199 · 2026-05-20T09:31:15.210Z_

<details><summary>↩ Tool result · `toolu_012pztqaVxoGAZQYnByLZDNR`</summary>

```text
Web search results for query: ""Mass Mobilization" dataset human coded annotated news sources codebook "hand-coded" OR "human-coded" OR "manually coded""

Links: [{"title":"Documentation – Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/about/documentation/"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Download the MMAD – Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/get/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"}]

Based on the search results, I found information about the Mass Mobilization datasets and their coding methodology:

## Mass Mobilization in Autocracies Database (MMAD)

The data is coded based on news reports obtained from AP, the AFP and BBC Monitoring. The project pre-filters news reports using machine learning techniques. A codebook for the current version (MMAD Codebook for Version 4.0) is available, along with codebooks for previous versions.

## Mass Mobilization Data Project

The earlier version of the Mass Mobilization project used a different approach. Coders search Lexis-Nexis, "All News," using "advanced options" which permit selection of "major world publications," entry of date ranges, country name, and search terms. The main database contains information at the level of reports, which means that every mention of a political protest in a news report constitutes a new entry in the database.

When using the MMAD for your own work, please cite the codebook for the respective version, and detailed information about the variables contained in the MMAD and the numeric codes is available in the codebook.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "8ff3b6e8-03da-45b1-970a-f870b6762d92"
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-20T09:31:18.644Z_

<details><summary>↩ Tool result · `toolu_01Ntx5FFJkyg3kdUQCA2gJir`</summary>

```text
Web search results for query: "github emerging-welfare case-2021-shared-task task2 event subtypes list data format download"

Links: [{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Emerging Markets Welfare – CASE 2022","url":"https://emw.ku.edu.tr/case-2022/"},{"title":"case-2021-shared-task/task2/test_dataset/test_set_final_release_with_labels.tsv at main · emerging-welfare/case-2021-shared-task","url":"https://github.com/emerging-welfare/case-2021-shared-task/blob/main/task2/test_dataset/test_set_final_release_with_labels.tsv"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.researchgate.net/publication/353485828_Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"GitHub - emerging-welfare/case-2022-multilingual-event: The repository for the shared tasks Task 1 and Task 3 at CASE 2022 (to be held at EMNLP)","url":"https://github.com/emerging-welfare/case-2022-multilingual-event"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"},{"title":"emerging-welfare · GitHub","url":"https://github.com/emerging-welfare"}]

Based on the search results, I found information about the CASE 2021 shared task Task 2:

Task 2 focuses on evaluating generalized zero-shot learning event classification approaches to classify short text snippets reporting socio-political events with fine-grained event types using the Armed Conflict Location & Event Data Project (ACLED) event taxonomy, which consists of 25 event subtypes pertaining to political violence, demonstrations (rioting and protesting) and selected non-violent, politically important events.

The code and data samples and submission formats are available in the task2 folder on GitHub.

The test dataset includes labeled examples with event subtypes like MAN_MADE_DISASTER, AGREEMENT, VIOL_DEMONSTR (violent demonstrations), and MOB_VIOL (mob violence), stored in TSV format.

For training purposes, the task recommends using event-related textual data from ACLED (https://acleddata.com/), which can be obtained using their data export tool for academic purposes.

The GitHub repository for this shared task is located at: https://github.com/emerging-welfare/case-2021-shared-task, where you can access the task2 folder containing the datasets and submission formats.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5281758f-cb26-4ce3-bf02-e117547ecaa8"
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
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "description": "Searching for \"Mass Mobilization\" Clark Regan dataset \"news tex…",
  "usage": {
    "total_tokens": 32050,
    "tool_uses": 19,
    "duration_ms": 116546
  },
  "last_tool_name": "WebSearch",
  "uuid": "0aeb82c3-64ac-4114-9df3-612cedb016f7",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 202_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jd9s3kQPji516k4rD7PH9V`</summary>

```json
{
  "query": "\"Mass Mobilization\" Clark Regan dataset \"news text\" OR \"article text\" OR \"text column\" OR \"notes\" OR \"source text\" variables columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "1602596b-d841-48c2-a098-78e383cea439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqkoF4tnpucuztbxaTL6pC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 30512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 759,
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

_source line 203 · 2026-05-20T09:31:20.192Z_

<details><summary>↩ Tool result · `toolu_01GWXEMqFfng95ZLMfNcyrEh`</summary>

```text
Web search results for query: ""cross-context news corpus" protest event "gold standard" download zenodo github categories"

Links: [{"title":"(PDF) Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction","url":"https://www.researchgate.net/publication/352372953_Cross-Context_News_Corpus_for_Protest_Event-Related_Knowledge_Base_Construction"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base Construction | OpenReview","url":"https://openreview.net/forum?id=7NZkNhLCjp"},{"title":"Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction | Data Intelligence | MIT Press","url":"https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"(PDF) Cross-context News Corpus for Protest Events related Knowledge Base Construction","url":"https://www.researchgate.net/publication/343414342_Cross-context_News_Corpus_for_Protest_Events_related_Knowledge_Base_Construction"},{"title":"Cross-context News Corpus for Protest Events related ...","url":"https://openreview.net/pdf?id=7NZkNhLCjp"},{"title":"GitHub - emerging-welfare/glocongold: The repo is about how to get access to the gold standard corpus that is created and exploited to generate the Global Contention Dataset (GLOCON) · GitHub","url":"https://github.com/emerging-welfare/glocongold"}]

Based on the search results, I found information about the Cross-Context News Corpus for Protest Events:

## Overview

The corpus is a gold standard collection of protest events comprising various local and international English language sources from various countries, with document-, sentence-, and token-level annotations. The corpus consists of English news articles from various local and international sources from India, China, and South Africa.

## Purpose

This corpus facilitates creating machine learning models that automatically classify news articles and extract protest event-related information, constructing knowledge bases that enable comparative social and political science studies.

## Annotation Methodology

For each news source, the annotation starts with random samples of news articles and continues with samples drawn using active learning, with each batch annotated by two social and political scientists, adjudicated by an annotation supervisor, and improved by identifying annotation errors semi-automatically.

## Access

The corpus can be obtained by following the instructions on the Global Contentious Politics Gold Standard Data (GLOCON GOLD) repository at https://github.com/emerging-welfare/glocongold.

The search results don't show specific information about Zenodo download links or detailed category breakdowns, but the GitHub repository listed appears to be the primary access point for this resource.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "cf08faf5-0584-4bb9-b0b7-f5f6a2833d44"
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-20T09:31:22.383Z_

<details><summary>↩ Tool result · `toolu_01Maq8roQ33hULPTeDC1RrEb`</summary>

```text
Web search results for query: ""INDI-PROP" dataset protest India NLP classification download categories labels"

Links: [{"title":"Fine-grained Narrative Classification in Biased News Articles","url":"https://www.arxiv.org/pdf/2512.03582"},{"title":"Stance Prediction of Tweets on Farmers Protests in India","url":"https://www.ijraset.com/research-paper/stance-prediction-of-tweets-on-farmers-protests-in-india"},{"title":"H-Prop and H-Prop-News: Computational Propaganda Datasets in Hindi","url":"https://www.mdpi.com/2306-5729/7/3/29"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"bigscience-data/roots_indic-or_indic_nlp_corpus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/bigscience-data/roots_indic-or_indic_nlp_corpus"},{"title":"Sentiment analysis and classification of Indian farmers’ protest using twitter data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667096821000124"}]

Based on the web search results, here's what I found about the INDI-PROP dataset:

## INDI-PROP Dataset Overview

The INDI-PROP dataset comprises 1,266 articles focusing on two polarizing socio-political events in recent times: CAA and the Farmers' protest.

## Annotation Structure

Each article is annotated at two hierarchical levels: (i) ideological article-bias (pro-government, pro-opposition, neutral) and (ii) event-specific fine-grained narrative frames anchored in ideological polarity and communicative intent.

## Purpose and Application

The dataset is a narrative dataset with multi-level annotation for analyzing propaganda in Indian news media. A GPT-4o-mini guided multi-hop prompt-based reasoning framework called FANTA is proposed for bias and narrative classification.

The dataset appears to be designed for NLP tasks related to detecting propaganda and bias in news articles covering significant Indian socio-political events, with a focus on understanding different ideological narratives and framing strategies. The classification labels include pro-government, pro-opposition, and neutral categories at the article level, plus event-specific narrative frames at a finer granularity.

For access to download the dataset and complete technical details, you may want to consult the original research paper directly through the ArXiv PDF referenced in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2019c94b-e062-4d0e-a1c0-843128f85df4"
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-20T09:31:22.400Z_

<details><summary>↩ Tool result · `toolu_011Mtz3A8F8A2k9M6HjDvJdd`</summary>

```text
Web search results for query: "POLDEM protest event dataset 30 download categories action forms license"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"}]

Based on the search results, here's information about the POLDEM Protest Event Dataset 30:

## Overview
PolDem-Protest Dataset 30 covers 30 European countries with data collection relying on semi-automated coding of newswire reports, covering the time period from 2000 until 2015.

## Data Collection and Methodology
Protest event analysis is a form of content analysis that allows to systematically collect, quantify, and process large amounts of information on political protest across time and countries. The dataset includes 45,680 documents with about 642 working days invested in annotating the dataset.

## Categories and Variables
The dataset includes information on:
- Categories indicating whether an event is linked to other protest events that take place in the same country or in Europe
- Action forms and protest activities
- Organizations involved in protest events, coded according to their organizational background such as social movement organizations (SMOs), initiatives, and loose networks
- Information on whether there were people arrested or wounded

## Availability
The data and documentation can be downloaded at https://poldem.eui.eu/

The search results don't contain specific information about the license terms for the dataset. You may need to check the official PolDem website or the documentation downloads for license details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "949bba57-73e9-4d52-a80d-4574ab6cbb87"
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-20T09:31:23.871Z_

<details><summary>↩ Tool result · `toolu_01MGM8TJ9FFZmCFvm7wsBrQW`</summary>

```text
Web search results for query: "Lorenzini Kriesi Makarov Wüest 2022 "Protest Event Analysis" "semiautomated" NLP issue categories action form intercoder"

Links: [{"title":"A modular pipeline for the automation of protest event analysis","url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/90205C53AAAAA675F21AC19178418E68/S2049847025100137a.pdf/papea_a_modular_pipeline_for_the_automation_of_protest_event_analysis.pdf"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Protest-Event-Analysis:-Developing-a-Semiautomated-Lorenzini-Kriesi/0d5d4aa04657300bf641b01243d556a192bac7c1"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Peter Makarov's research works | University of Zurich and other places","url":"https://www.researchgate.net/scientific-contributions/2119894272_Peter_Makarov"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://agris.fao.org/search/en/providers/122535/records/65dfd44763b8185d9caf4ba9"},{"title":"PAPEA: A modular pipeline for the automation of protest event analysis | Political Science Research and Methods | Cambridge Core","url":"https://www.cambridge.org/core/journals/political-science-research-and-methods/article/papea-a-modular-pipeline-for-the-automation-of-protest-event-analysis/90205C53AAAAA675F21AC19178418E68"},{"title":"Protest event analysis: developin... | Archive ouverte UNIGE","url":"https://archive-ouverte.unige.ch/unige:152063"},{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://www.ovid.com/journals/absc/fulltext/10.1177/00027642211021650~protest-event-analysis-developing-a-semiautomated-nlp"},{"title":"Monthly number of protests (left) and 5-monthly moving averages (right)... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Monthly-number-of-protests-left-and-5-monthly-moving-averages-right-for-ICEWS-and-our_fig1_352087597"}]

I found the paper you're looking for! Here are the search results:

The 2022 paper by Lorenzini, Kriesi, Makarov, and Wüest titled "Protest event analysis: Developing a semiautomated NLP approach" was published in the American Behavioral Scientist, volume 66(5), pages 555–577.

The paper addresses how protest event analysis is a key method to study social movements but is time-consuming and resource intensive when done manually, and shows how advances in automated approaches offer opportunities to code multiple sources and create large datasets spanning many countries and years.

The research describes POLCON, a semi-automated process where event annotation is primarily performed by human coders, alongside computational tools.

The paper appears to be available through Cambridge University Press and various academic repositories. The full text should contain detailed discussions of the specific methodologies for coding issue categories, action forms, and intercoder reliability measures that you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "383edd70-ce82-477c-a749-8e281be90a5a"
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
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CASE 2021 task2 ACLED 25 event subtypes full list…",
  "usage": {
    "total_tokens": 40372,
    "tool_uses": 26,
    "duration_ms": 114530
  },
  "last_tool_name": "WebSearch",
  "uuid": "07e8e60b-c28b-4193-a696-6b91b2c3d466",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 208_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014i4MfRXjsrDFasm5apj6Hj`</summary>

```json
{
  "query": "CASE 2021 task2 ACLED 25 event subtypes full list categories \"Armed Clash\" \"Violent demonstration\" \"Peaceful protest\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "eb714a43-e89d-4b21-8063-b4e0170214cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gtXuPEYzjqYsUtmYo33kp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3214,
      "cache_read_input_tokens": 35926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3214,
        "ephemeral_1h_input_tokens": 0
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

_source line 209 · 2026-05-20T09:31:26.211Z_

<details><summary>↩ Tool result · `toolu_017hxKeyLrbHKxVdSBH9JzxU`</summary>

```text
# Protest Event Analysis: NLP Approach & Dataset Summary

## 1) Semi-Automated NLP Approach

The researchers developed a **multistep pipeline combining automated and manual methods**. The process includes:

- **Keyword searching** across 10 English-language newswire agencies (5.2M initial documents)
- **Duplicate removal** using SpotSigs algorithm (Jaccard similarity ≥0.75)
- **Location-based filtering** to retain only European events
- **Document classifier** trained on 7,500 manually classified documents (94% accuracy)
- **Event-trigger classifier** using 518 annotated documents to identify protest mentions
- **Manual coding** of remaining documents by human coders

Final dataset reduced to approximately 45,680 documents for manual coding, yielding 33,655 coded events.

## 2) Issue Categories

Complete list from Table 2:

- Economics (private) – firm/employer claims
- Economics (public) – public institution claims
- Environment – environmental protection, energy, infrastructure
- Cultural liberalism – peace, women's rights, LGBTQ, international solidarity, antiracism, migrants' rights
- Regionalism – separatism, regional independence
- Cultural conservatism – countermobilization to cultural liberalism
- Xenophobia – right-wing extremism, racist mobilization, anti-immigration
- Political – representation, corruption, electoral reforms
- Others – uncategorized issues

## 3) Action Form Categories

From Table 2:

- Strikes – industrial action, work stoppages, pickets
- Demonstrations – marches, rallies, camps, meetings, vigils, gatherings
- Petitions and related activities – consumer activism, boycotts, symbolic protests
- Violent protests – sabotage, riots, destruction, clashes with police
- Other protests – remaining action forms

## 4) Total Number of Events

The dataset contains **33,655 unique protest events** across 30 European countries from 2000-2015 (after removing duplicates and irrelevant documents).

## 5) Human Annotation Methodology & Intercoder Reliability

**Methodology:**
- 35 graduate students coded documents over 6 months (642 total working days)
- Coders identified events based on "unconventional or noninstitutionalized political action forms"
- Events defined as unique combinations of action form, timing, and city-level location

**Intercoder Reliability (14 coders, 65 documents):**

Researchers reported: "The averaged F1-score over all possible pairs of the 14 coders is 0.60 with a standard deviation of 0.06" for event identification.

For event attributes using Cohen's Kappa:
- Actors: 0.57 (SD 0.13)
- Issues: 0.53 (SD 0.13)
- Participant numbers: 0.45 (SD 0.06)

Authors note these "fair to good" values reflect task difficulty even for humans.

## 6) Gold-Standard Human Labels

**No.** The dataset is not presented as gold-standard. The authors acknowledge significant limitations:

- 26.3% of manually coded documents contained no events (false positives)
- 32.6% contained only duplicate events already reported
- Intercoder agreement scores were moderate, not high
- Authors describe the task as "difficult, even for human coders"

## 7) Dataset Size

- **Initial retrieval:** 5,251,894 documents
- **After location filtering:** 1,116,337 documents
- **After classifiers:** 101,877 documents
- **Sampled for manual coding:** 45,680 documents
- **Final coded events:** 33,655 unique protest events

## 8) Citation Information

**Full Citation:**

Lorenzini, J., Kriesi, H., Makarov, P., & Wüest, B. (2021). Protest event analysis: Developing a semiautomated NLP approach. *American Behavioral Scientist*, 66(5), 555-577. https://doi.org/10.1177/00027642211021650

**Publication Details:**
- First published online: June 2, 2021
- Issue published: May 2022
- License: Creative Commons Attribution 4.0 (CC BY 4.0)
- Journal Impact Factor: 1.5 (5-year: 2.6)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "22940f76-6b26-4c3a-886e-4961a43d54ba"
}
```

</details>

---

### System

_source line 210_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for GLOCON dataset download access \"event type\" categ…",
  "usage": {
    "total_tokens": 40423,
    "tool_uses": 27,
    "duration_ms": 118459
  },
  "last_tool_name": "WebSearch",
  "uuid": "90cc3244-804e-4a41-9d61-e5320aed3208",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 211_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSy4kFCy2JY74i8sZTCSjJ`</summary>

```json
{
  "query": "GLOCON dataset download access \"event type\" categories number samples size statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "d76570da-55c7-4269-b419-893028ece74d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gtXuPEYzjqYsUtmYo33kp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3214,
      "cache_read_input_tokens": 35926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3214,
        "ephemeral_1h_input_tokens": 0
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

_source line 212 · 2026-05-20T09:31:29.256Z_

<details><summary>↩ Tool result · `toolu_01Jd9s3kQPji516k4rD7PH9V`</summary>

```text
Web search results for query: ""Mass Mobilization" Clark Regan dataset "news text" OR "article text" OR "text column" OR "notes" OR "source text" variables columns"

Links: [{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"}]

Based on the search results, I found information about the Mass Mobilization dataset by Clark and Regan. Here's what the search revealed:

## Overview
The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018, containing events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events.

## Data Source
Lexis-Nexis was utilized as the source of information, searching for newspaper reports while focusing on four major publications: The New York Times, the Washington Post, the Christian Science Monitor and the Times of London.

## Variables and Columns
Each event records location, protest size, protester demands, and government responses. The MM data itemize what protesters demand across as many as seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions. The dataset also records up to seven types of government responses, including accommodation, arrests, beatings, crowd dispersal, ignore, killings, and shootings.

However, the search results do not specifically mention text columns or fields containing news article text, news text, or source text variables in the dataset. For detailed information about all available variables and columns, you may want to consult the project's official documentation or codebook at massmobilization.github.io or the Harvard Dataverse repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9c1554f6-0e65-4c15-a1fd-03839d384a88"
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
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for SPEED dataset Cline Center download event categor…",
  "usage": {
    "total_tokens": 40474,
    "tool_uses": 28,
    "duration_ms": 118785
  },
  "last_tool_name": "WebSearch",
  "uuid": "b83aeb2d-a6d2-4ba9-b515-d54b190a6a48",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 214_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016kKJb2nVBiazwmitjrdUya`</summary>

```json
{
  "query": "SPEED dataset Cline Center download event categories \"civil unrest\" \"political violence\" number of events format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "448726e7-4d91-458c-a340-cbe929331c25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gtXuPEYzjqYsUtmYo33kp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3214,
      "cache_read_input_tokens": 35926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3214,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 215_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/",
  "usage": {
    "total_tokens": 34250,
    "tool_uses": 22,
    "duration_ms": 131725
  },
  "last_tool_name": "WebFetch",
  "uuid": "66455ec6-8727-4310-bc60-0283d2305628",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 216_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SBoC9oGuYkSatzfAdYgc13`</summary>

```json
{
  "url": "https://poldem.eui.eu/",
  "prompt": "Extract: 1) Any download links for protest datasets (.dta, .csv, .xlsx). 2) Whether login/registration is required. 3) Terms of use or license mentioned anywhere on the page. 4) Any mention of \"free download\" or \"open access\". 5) All available dataset versions and links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9645ac60-0aa6-4257-97da-fea21e95ee14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYjp2SnmsukKBWftkTXYgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
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

### System

_source line 217_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Searching for poldem protest dataset download .dta .csv free op…",
  "usage": {
    "total_tokens": 34253,
    "tool_uses": 23,
    "duration_ms": 131910
  },
  "last_tool_name": "WebSearch",
  "uuid": "22d2863a-2c7a-4a72-b10b-928d6988c698",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 218_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XQQveFWwvhyMcRszkbohEP`</summary>

```json
{
  "query": "poldem protest dataset download .dta .csv free open access no registration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "dfbc6400-6b10-4510-9241-8af2115b4f76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYjp2SnmsukKBWftkTXYgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
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

_source line 219 · 2026-05-20T09:31:33.279Z_

<details><summary>↩ Tool result · `toolu_014i4MfRXjsrDFasm5apj6Hj`</summary>

```text
Web search results for query: "CASE 2021 task2 ACLED 25 event subtypes full list categories "Armed Clash" "Violent demonstration" "Peaceful protest""

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/acled-introduces-new-event-types-and-sub-event-types/"},{"title":"IBM MNLP IE at CASE 2021 Task 2: NLI Reranking for Zero ...","url":"https://aclanthology.org/2021.case-1.24.pdf"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"Classification of ACLED events by type. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Classification-of-ACLED-events-by-type_tbl1_356786131"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"}]

Based on the search results, I found information about the CASE 2021 Task 2 and the ACLED 25 event subtypes:

The objective of Task 2 is to evaluate zero-shot learning event classification approaches to classify short text snippets reporting socio-political events with fine-grained event types using the ACLED event taxonomy, which consists of 25 event subtypes pertaining to political violence, demonstrations (rioting and protesting) and selected non-violent, politically important events.

ACLED currently records six event types and 25 sub-event types, both violent and non-violent. Sub-event types are also categorized by three overarching disorder types to facilitate analysis: Political violence, Demonstrations, and Strategic developments.

The search results confirm that the CASE 2021 shared task uses the ACLED taxonomy with its 25 event subtypes, and the categories you mentioned ("Armed Clash," "Violent demonstration," and "Peaceful protest") fall within the broader categories of Political violence and Demonstrations. However, the search results do not provide the complete list of all 25 specific event subtypes with their exact names. 

For the full detailed list of all 25 event subtypes, annotation manuals for task 2 are available in the official CASE 2021 GitHub repository, and the complete list is referenced in the ACLED Codebook, though the specific subtype names are not fully enumerated in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "f0df93d5-50b7-4215-bfeb-f55ed8b23cf6"
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-20T09:31:36.083Z_

<details><summary>↩ Tool result · `toolu_016kKJb2nVBiazwmitjrdUya`</summary>

```text
Web search results for query: "SPEED dataset Cline Center download event categories "civil unrest" "political violence" number of events format"

Links: [{"title":"Social Political Economic Event Dataset (SPEED): Liberia ...","url":"https://databank.illinois.edu/datasets/IDB-7407320"},{"title":"The Social, Political and Economic Event Database Project (SPEED) | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED"},{"title":"Human-in-the-loop Event Data Projects | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects"},{"title":"(PDF) Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008) Codebook (v.1.0.0) About the Cline Center for Advanced Social Research | Dan Shalmon - Academia.edu","url":"https://www.academia.edu/40213536/Social_Political_Economic_Event_Dataset_SPEED_Liberia_Philippines_and_Sierra_Leone_1979_2008_Codebook_v_1_0_0_About_the_Cline_Center_for_Advanced_Social_Research"},{"title":"Cline Center Historical Phoenix Event Data. Cline Center for Advanced Social Research. v1.3.0. May 4 - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/cline-center-historical-phoenix-event-data-cline-center-for-advan-4/"},{"title":"Civil Unrest Event Data - dataset by history","url":"https://data.world/history/civil-unrest-event-data"},{"title":"Cline Center Coup d’État Project Dataset - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/cline-center-coup-d%C3%A9tat-project-dataset-10/"}]

Based on the search results, here's what I found about the SPEED dataset:

The SPEED (Social, Political and Economic Event Database) project is part of the Cline Center's ongoing work. Each observation represents an event involving civil unrest, repression, or political violence.

The protocols used in SPEED are category-specific electronic documents tailored to the information needs of particular event categories including civil unrest, property rights, and electoral processes. The destabilizing event ontology contains four Tier 1 categories: political expression events, politically motivated attacks, disruptive state acts, and political power reconfigurations.

Currently, two datasets have been produced through the SPEED Project: civil unrest event data and coup d'état event data.

The search results show information about SPEED datasets covering regions like Liberia, Philippines, and Sierra Leone from 1979-2008/2009, but they don't contain specific details about the total number of events across all SPEED datasets or the exact download format specifications. For more detailed information about event counts and available download formats, you may want to visit the Cline Center's official website or the University of Illinois data repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5f04deb5-3540-4e32-bb68-ba48d0d7f177"
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-20T09:31:37.797Z_

<details><summary>↩ Tool result · `toolu_01HSy4kFCy2JY74i8sZTCSjJ`</summary>

```text
Web search results for query: "GLOCON dataset download access "event type" categories number samples size statistics"

Links: [{"title":"GLOCON – About GLOCON","url":"https://glocon.ku.edu.tr/about-glocon/"},{"title":"Global Contentious Politics Dataset (GLOCON)","url":"https://glocon.ku.edu.tr/"},{"title":"New Dataset Collects Instances of ‘Contentious Politics’ Around the World - Social Science Space","url":"https://www.socialsciencespace.com/2023/12/new-dataset-collects-instances-of-contentious-politics-around-the-world/"},{"title":"GLOCON – Methodology","url":"https://glocon.ku.edu.tr/method/"},{"title":"GLOCON Database: Design Decisions and User Manual (v1.0)","url":"https://arxiv.org/pdf/2405.18613"},{"title":"Socio-political Events of Conflict and Unrest: A Survey of ...","url":"https://aclanthology.org/2024.case-1.5.pdf"},{"title":"GitHub - emerging-welfare/glocongold: The repo is about how to get access to the gold standard corpus that is created and exploited to generate the Global Contention Dataset (GLOCON) · GitHub","url":"https://github.com/emerging-welfare/glocongold"},{"title":"[2405.18613] GLOCON Database: Design Decisions and User Manual (v1.0)","url":"https://arxiv.org/abs/2405.18613"}]

Based on the web search results, here's information about the GLOCON dataset:

## Overview
GLOCON is the first multi-country protest event database for the Global South that uses local sources for automated data collection. It records diverse types of events, including but not limited to demonstrations, rallies, strikes, clashes, and political violence.

## Coverage and Size
The dataset currently contains protest event data from India, South Africa, Argentina, Brazil, and Turkey. As of the inauguration of the website, it contains 621,290 events from 9,509,193 news documents.

## Event Type Categories
Event categories are automatically predicted and include categories such as "Demonstration." The dataset includes various event types as indicators of contentious politics events.

## Data Access
To request access to raw data, users can follow the link to the Download section. The tool offers data visualizations drawn from categorical, geolocational, and temporal filters, and users can gain access to raw data via the download feature.

## Data Format
The data is released as JSON files organized as one separate file for each news source, with each JSON file consisting of JSON objects, one per each line, considered as .jsonl.

For more detailed specifications about event type categories and specific sample size statistics, you may need to consult the full documentation available at https://glocon.ku.edu.tr/ or their methodology section.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "d1069999-0598-49ad-8865-ceb072bc3308"
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-20T09:31:39.788Z_

<details><summary>↩ Tool result · `toolu_01XQQveFWwvhyMcRszkbohEP`</summary>

```text
Web search results for query: "poldem protest dataset download .dta .csv free open access no registration"

Links: [{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"PolData/PolData.csv at master · erikgahner/PolData","url":"https://github.com/erikgahner/PolData/blob/master/PolData.csv"},{"title":"Protest Events - PolDem","url":"https://poldem.eui.eu/download/protest-events/"},{"title":"Data Overview - PolDem - European University Institute","url":"https://poldem.eui.eu/data-overview/"}]

Based on the search results, here's what I found about the PolDem protest dataset:

The PolDem (Observatory for Political Conflict and Democracy) is a platform that produces and houses data on protest events, election campaigns, and issue-specific public contestation covering a wide-range of European countries over a long period of time. The core of PolDem includes data on protest events in 30 European countries obtained by coding media coverage.

**Download Location:**
The data and documentation can be downloaded at https://poldem.eui.eu/

**Dataset Details:**
The data collection relies on semi-automated coding of newswire reports and covers 30 European countries and the time period from 2000 until 2015. All of the datasets come with extensive documentation.

The main PolDem protest datasets include:
- **PolDem-Protest Dataset 30** (covering 30 European countries)
- **PolDem-Protest Dataset on EU issues** (covering 6 countries: Austria, France, Germany, Sweden, Switzerland, and the UK)

You can access the datasets and their codebooks directly from the PolDem portal at https://poldem.eui.eu/, where they appear to be available for download in various formats including .dta and .csv as open access research data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "8017f292-fc69-47d5-90aa-78c06081e0b4"
}
```

</details>

---

### System

_source line 223_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for ACLED sub-event types full list 25 \"Armed clash\" …",
  "usage": {
    "total_tokens": 43179,
    "tool_uses": 29,
    "duration_ms": 131125
  },
  "last_tool_name": "WebSearch",
  "uuid": "f0239fe0-598d-49ab-8653-25473abab1d9",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 224_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GXwRqDhFizdznUnq5wq41L`</summary>

```json
{
  "query": "ACLED sub-event types full list 25 \"Armed clash\" \"Government regains territory\" \"Non-state actor overtakes territory\" \"Peaceful protest\" \"Protest with intervention\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "4d44be26-a259-4a3c-92a6-2f264966663e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118asxP6uQRnhvBFtpAxUhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2598,
      "cache_read_input_tokens": 39140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2598,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 225_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CASE 2022 task1 subtask document classification p…",
  "usage": {
    "total_tokens": 43223,
    "tool_uses": 30,
    "duration_ms": 131470
  },
  "last_tool_name": "WebSearch",
  "uuid": "9b96d9a1-86f2-4270-92ec-b0329aca2a0f",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 226_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUe7C97tEJVCbFev7SR8Nw`</summary>

```json
{
  "query": "CASE 2022 task1 subtask document classification protest dataset languages sample size train test split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "1aa534f7-e53c-4b3e-96b5-c8372d56a19b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118asxP6uQRnhvBFtpAxUhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2598,
      "cache_read_input_tokens": 39140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2598,
        "ephemeral_1h_input_tokens": 0
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

_source line 227 · 2026-05-20T09:31:42.680Z_

<details><summary>↩ Tool result · `toolu_01SBoC9oGuYkSatzfAdYgc13`</summary>

```text
# PolDem Data Access Analysis

Based on the webpage content provided, here's what I found:

## 1. Download Links for Protest Datasets
The page references a "Download" section at `https://poldem.eui.eu/download/`, but **no direct file links (.dta, .csv, .xlsx) are displayed** on this homepage.

## 2. Login/Registration Requirements
**No information provided** about whether authentication is needed to access datasets.

## 3. Terms of Use or License
**Not mentioned** on this page. The footer only states "© 2026 - EUI & WZB. All rights reserved."

## 4. "Free Download" or "Open Access" Language
**Not present** on the homepage. The page uses neutral phrasing like "Download" and "Data Overview" without explicitly stating access restrictions or cost.

## 5. Dataset Versions Available
The page mentions these datasets:
- **poldem-protest_30** (Protest Event Dataset covering 30 European countries)
- **poldem-election_all** (Election Campaigns Dataset)

However, **no version numbers, dates, or direct download links are provided** on this page.

## Recommendation
To obtain actual dataset files and access terms, you would need to visit the linked "Download" or "Explore" pages directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "12dafdce-428c-4a7f-a5ec-dc400284e2a0"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Fetching https://poldem.eui.eu/download/protest-events/",
  "usage": {
    "total_tokens": 35735,
    "tool_uses": 24,
    "duration_ms": 145938
  },
  "last_tool_name": "WebFetch",
  "uuid": "a4e67170-3103-4414-a1f1-4ef2f433ee18",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 229_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CF5EwXa1wkc29Z99r69t7w`</summary>

```json
{
  "url": "https://poldem.eui.eu/download/protest-events/",
  "prompt": "Extract ALL information from this page: 1) All download links and file formats available. 2) Whether login/registration is required. 3) Terms of use or license. 4) Dataset versions. 5) Any instructions for downloading. 6) Direct URLs to data files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0561f622-4f89-4cb7-b561-01f36a28041a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAj9PndV1YY2CPMDiZJ6MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 1618,
      "cache_read_input_tokens": 32127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1618,
        "ephemeral_1h_input_tokens": 0
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

_source line 230 · 2026-05-20T09:31:49.248Z_

<details><summary>↩ Tool result · `toolu_01GXwRqDhFizdznUnq5wq41L`</summary>

```text
Web search results for query: "ACLED sub-event types full list 25 "Armed clash" "Government regains territory" "Non-state actor overtakes territory" "Peaceful protest" "Protest with intervention""

Links: [{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/acled-introduces-new-event-types-and-sub-event-types/"},{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"1 ACLED Definitions of Political Violence and Protest","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/2021/11/ACLED_Event-Definitions_v1_April-2019.pdf"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 2015","url":"https://www.strausscenter.org/wp-content/uploads/ACLED_Codebook_2015.pdf"},{"title":"Armed Conflict Location & Event Data CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2024/10/ACLED-Codebook-2024-7-Oct.-2024.pdf"},{"title":"Classification of ACLED events by type. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Classification-of-ACLED-events-by-type_tbl1_356786131"},{"title":"Armed Conflict Location & Event Data Project (ACLED) Humanitarian Data | 246 Datasets | HDX","url":"https://data.humdata.org/organization/acled"}]

Based on the search results, I found information about ACLED's sub-event types. ACLED currently records six event types and 25 sub-event types, both violent and non-violent. Sub-event types are also categorized by three overarching disorder types to facilitate analysis: 1) "Political violence," "Demonstrations," and "Strategic developments."

The search results include some of the specific sub-event types you mentioned. For example:
- "Armed clash: armed, organized groups engaging in a battle with no reports of a change in territorial control"
- "Non-state actor overtakes territory: when a non-state actor wins control and/or subdues government forces"

The results also reference other sub-event types like "Chemical weapon," "Air/drone strike," "Suicide bomb," "Shelling/artillery/missile attack," and various violence against civilians sub-types.

For the complete and authoritative list of all 25 sub-event types, an updated codebook reflecting these changes can be accessed here on the ACLED website. The most current version would be found in ACLED's official codebook, which appears to be the 2024 version based on the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "430e918a-b1f0-4d60-9f51-be1023a29220"
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-20T09:31:51.016Z_

<details><summary>↩ Tool result · `toolu_01CF5EwXa1wkc29Z99r69t7w`</summary>

```text
# PolDem Protest Events Dataset - Information Summary

## Download Links & File Formats
Three dataset versions are available with both CSV and Stata (.DTA) formats:

1. **poldem-protest_30**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta)
2. **poldem-protest_6**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_6.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_6.dta)
3. **poldem-protest_eu**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_eu.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_eu.dta)

## Login/Registration Requirement
**Not specified** - The page contains no mention of authentication requirements.

## Terms of Use or License
**Not provided** - No explicit license or terms of use are detailed on this page.

## Download Instructions
**None given** - The page offers direct download links without step-by-step guidance.

## Additional Information
- Contact: poldem@eui.eu (EUI) and poldem@wzb.eu (WZB Berlin)
- Related resources include codebooks, citation guidelines, and data exploration tools accessible through the main navigation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "08516f18-d59c-4547-bad8-adfe216c84b4"
}
```

</details>

---

### System

_source line 232_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8e25cafc895a96c2",
  "tool_use_id": "toolu_01RKjDE1P2EHBH2piAJtV2ws",
  "status": "completed",
  "output_file": "",
  "summary": "Search MMD dataset",
  "usage": {
    "total_tokens": 33125,
    "tool_uses": 19,
    "duration_ms": 148501
  },
  "uuid": "1615028f-0738-4042-9833-92f39fa31e84",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 233 · 2026-05-20T09:31:51.935Z_

<details><summary>↩ Tool result · `toolu_01RKjDE1P2EHBH2piAJtV2ws`</summary>

````text
Based on comprehensive web searches, here is the report:

```
数据集名称: Mass Mobilization Data Project (MMD / MMP)
         作者: David H. Clark (Binghamton University) & Patrick M. Regan (University of Notre Dame)

类别数 K: 
  - 抗议者诉求 (protester demand): 7 类
  - 政府响应 (government response): 7 类

类别列表:
  Protester demands: [labor/wages, land, police brutality, political process, prices/taxes, removal of politician, social restrictions]
  Government responses: [accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings]
  注意：每个事件可以同时有多个 demand 和多个 response（multi-label）

样本量: ~17,000+ 事件（162 个国家，1990–2020），每条记录对应一次 50 人以上的抗议事件

License: Harvard Dataverse 默认 CC0 Public Domain Dedication（该数据集未见特殊限制说明），可用于学术/ML 研究

下载方式: 
  - Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
  - 官网: https://massmobilization.github.io/
  - data.world 镜像: https://data.world/government/mass-mobilization-protest-data
  - 无需申请/审批，直接下载

Gold-standard human labels: 是
  标注方式：人工编码员从 Lexis-Nexis 检索新闻报道（主要来源为 NYT、Washington Post、Christian Science Monitor、Times of London），
  按 codebook 标准对每起抗议事件的诉求类型、政府响应、规模、地点等进行手工编码。

引用论文: 
  - 数据集引用: Clark, David H.; Regan, Patrick M., 2016, "Mass Mobilization Protest Data", 
    https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse
  - 相关分析论文: Klein, Graig R. and Patrick M. Regan. 2018. "Dynamics of Political Protests." 
    International Organization 72(2): 485-521.

备注:
  1. 该数据集是结构化事件数据（tabular），不含原始新闻文本。变量为编码后的分类标签（demand/response 为 0/1 二值列）、
     数值（protest size）和元数据（country, date, location）。如果用于 NLP 文本分类任务，
     需要自行匹配/获取原始新闻文本——数据集本身不提供 article text。
  2. Demand 和 response 都是 multi-label 设定（K=7 但非互斥），不是单标签 K 分类。
     作为 K>=3 的分类任务可行，但需注意 multi-label 性质。
  3. 另有 Mass Mobilization in Autocracies Database (MMAD, mmadatabase.org) 是独立扩展版，
     覆盖独裁国家，使用 AP/AFP/BBC Monitoring + ML 预筛选 + 人工编码，与 Clark/Regan 的 MMD 是不同数据集。
```

agentId: a8e25cafc895a96c2 (use SendMessage with to: 'a8e25cafc895a96c2' to continue this agent)
&lt;usage>total_tokens: 33265
tool_uses: 19
duration_ms: 148502&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "2f77a9a4-7eac-4732-98cf-df58d69cc67f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
    "agentId": "a8e25cafc895a96c2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on comprehensive web searches, here is the report:\n\n```\n数据集名称: Mass Mobilization Data Project (MMD / MMP)\n         作者: David H. Clark (Binghamton University) & Patrick M. Regan (University of Notre Dame)\n\n类别数 K: \n  - 抗议者诉求 (protester demand): 7 类\n  - 政府响应 (government response): 7 类\n\n类别列表:\n  Protester demands: [labor/wages, land, police brutality, political process, prices/taxes, removal of politician, social restrictions]\n  Government responses: [accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings]\n  注意：每个事件可以同时有多个 demand 和多个 response（multi-label）\n\n样本量: ~17,000+ 事件（162 个国家，1990–2020），每条记录对应一次 50 人以上的抗议事件\n\nLicense: Harvard Dataverse 默认 CC0 Public Domain Dedication（该数据集未见特殊限制说明），可用于学术/ML 研究\n\n下载方式: \n  - Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL\n  - 官网: https://massmobilization.github.io/\n  - data.world 镜像: https://data.world/government/mass-mobilization-protest-data\n  - 无需申请/审批，直接下载\n\nGold-standard human labels: 是\n  标注方式：人工编码员从 Lexis-Nexis 检索新闻报道（主要来源为 NYT、Washington Post、Christian Science Monitor、Times of London），\n  按 codebook 标准对每起抗议事件的诉求类型、政府响应、规模、地点等进行手工编码。\n\n引用论文: \n  - 数据集引用: Clark, David H.; Regan, Patrick M., 2016, \"Mass Mobilization Protest Data\", \n    https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse\n  - 相关分析论文: Klein, Graig R. and Patrick M. Regan. 2018. \"Dynamics of Political Protests.\" \n    International Organization 72(2): 485-521.\n\n备注:\n  1. 该数据集是结构化事件数据（tabular），不含原始新闻文本。变量为编码后的分类标签（demand/response 为 0/1 二值列）、\n     数值（protest size）和元数据（country, date, location）。如果用于 NLP 文本分类任务，\n     需要自行匹配/获取原始新闻文本——数据集本身不提供 article text。\n  2. Demand 和 response 都是 multi-label 设定（K=7 但非互斥），不是单标签 K 分类。\n     作为 K>=3 的分类任务可行，但需注意 multi-label 性质。\n  3. 另有 Mass Mobilization in Autocracies Database (MMAD, mmadatabase.org) 是独立扩展版，\n     覆盖独裁国家，使用 AP/AFP/BBC Monitoring + ML 预筛选 + 人工编码，与 Clark/Regan 的 MMD 是不同数据集。\n```"
      }
    ],
    "totalDurationMs": 148502,
    "totalTokens": 33265,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 31271,
      "output_tokens": 919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 919,
          "cache_read_input_tokens": 31271,
          "cache_creation_input_tokens": 1074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1074,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 19
    }
  }
}
````

</details>

---

### System

_source line 234_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Check HTTP headers to verify if CSV file is freely downloadable without auth",
  "usage": {
    "total_tokens": 36260,
    "tool_uses": 25,
    "duration_ms": 154774
  },
  "last_tool_name": "Bash",
  "uuid": "c2be014e-0a14-407f-b8b8-c78ce1cb81ee",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 235_

<details open><summary>🔧 Tool call — Bash · `toolu_01McG3mhGyMx4Lmk1FLyyZsp`</summary>

```json
{
  "command": "curl -sI \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -20",
  "description": "Check HTTP headers to verify if CSV file is freely downloadable without auth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ffd355a4-ebdf-43e5-b0b3-24393fd27ab8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja5k5uU6pfbu9L1gPNrZeg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 33745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
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

_source line 236 · 2026-05-20T09:31:56.347Z_

<details><summary>↩ Tool result · `toolu_01McG3mhGyMx4Lmk1FLyyZsp`</summary>

```text
HTTP/1.1 200 OK
Date: Wed, 20 May 2026 09:31:55 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Fri, 03 Apr 2020 11:32:14 GMT
ETag: "8899af-5a26144d6ab80"
Accept-Ranges: bytes
Content-Length: 8952239
Content-Type: text/csv
Set-Cookie: [REDACTED];Expires=Thu, 20 May 2027 09:31:56 GMT;Path=/;HttpOnly
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "9c647277-34e6-4161-9a9f-39fe852dd133"
}
```

</details>

---

### System

_source line 237_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Download first 5 lines of CSV to check column names and content",
  "usage": {
    "total_tokens": 36649,
    "tool_uses": 26,
    "duration_ms": 159172
  },
  "last_tool_name": "Bash",
  "uuid": "1c4c43de-0756-4876-9482-0121bca984f3",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 238_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXQnfuBJ4RAfncrJ7XfnoL`</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -5",
  "description": "Download first 5 lines of CSV to check column names and content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "ce2356db-4292-4ad7-b132-c8b51756b443",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ne7gLDWvvYkQGmqZsE9qY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 35108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 323,
        "ephemeral_1h_input_tokens": 0
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

_source line 239 · 2026-05-20T09:31:59.892Z_

<details><summary>↩ Tool result · `toolu_01GUe7C97tEJVCbFev7SR8Nw`</summary>

```text
Web search results for query: "CASE 2022 task1 subtask document classification protest dataset languages sample size train test split"

Links: [{"title":"NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models - ACL Anthology","url":"https://aclanthology.org/2022.case-1.23/"},{"title":"Extended Multilingual Protest News Detection - Shared Task 1, CASE 2021 and 2022 - ACL Anthology","url":"https://aclanthology.org/2022.case-1.31/"},{"title":"CEIA-NLP at CASE 2022 Task 1: Protest News Detection ...","url":"https://aclanthology.org/2022.case-1.26.pdf"},{"title":"ClassBases at the CASE-2022 Multilingual Protest Event Detection Task: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets - ACL Anthology","url":"https://aclanthology.org/2022.case-1.21/"},{"title":"ClassBases at the CASE-2022 Multilingual Protest Event ...","url":"https://aclanthology.org/2022.case-1.21.pdf"},{"title":"[2211.11360] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022","url":"https://arxiv.org/abs/2211.11360"},{"title":"[2301.06617] ClassBases at CASE-2022 Multilingual Protest Event Detection Tasks: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets","url":"https://arxiv.org/abs/2301.06617"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"}]

Let me search for more specific information about the dataset details, including languages, sample size, and train/test split.

Links: [{"title":"Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021   and 2022","url":"https://arxiv.org/pdf/2211.11360"},{"title":"Investigating data partitioning strategies for crosslinguistic   low-resource ASR evaluation","url":"https://arxiv.org/pdf/2208.12888"},{"title":"Train and Test Sets Split for Evaluating Learning To Rank Models","url":"https://sease.io/2022/07/how-to-split-your-dataset-into-train-and-test-sets-for-evaluating-learning-to-rank-models.html"},{"title":"Train-Test Split for Evaluating Machine Learning Algorithms - MachineLearningMastery.com","url":"https://machinelearningmastery.com/train-test-split-for-evaluating-machine-learning-algorithms/"},{"title":"Data augmentation and batch balancing for training multi-lingual model","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12530545"},{"title":"Splitting a Dataset into Train and Test Sets | Baeldung on Computer Science","url":"https://www.baeldung.com/cs/train-test-datasets-ratio"}]

Let me search more specifically for the CASE 2022 task description paper or dataset documentation.

Links: [{"title":"(PDF) NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models","url":"https://www.academia.edu/110108255/NSUT_NLP_at_CASE_2022_Task_1_Multilingual_Protest_Event_Detection_using_Transformer_based_Models"},{"title":"CamPros at CASE 2022 Task 1: Transformer-based Multilingual Protest News Detection - ACL Anthology","url":"https://aclanthology.org/2022.case-1.24/"},{"title":"(PDF) Multilingual Protest News Detection - Shared Task 1, CASE 2021","url":"https://www.academia.edu/64931265/Multilingual_Protest_News_Detection_Shared_Task_1_CASE_2021"},{"title":"(PDF) A Task Set Proposal for Automatic Protest Information Collection Across Multiple Countries","url":"https://www.academia.edu/39161444/A_Task_Set_Proposal_for_Automatic_Protest_Information_Collection_Across_Multiple_Countries"},{"title":"[2211.11360] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022","url":"https://arxiv.org/abs/2211.11360"},{"title":"(PDF) ClassBases at CASE-2022 Multilingual Protest Event Detection Tasks: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets","url":"https://www.researchgate.net/publication/367216659_ClassBases_at_CASE-2022_Multilingual_Protest_Event_Detection_Tasks_Multilingual_Protest_News_Detection_and_Automatically_Replicating_Manually_Created_Event_Datasets"},{"title":"Extended Multilingual Protest News Detection - Shared Task 1, CASE 2021 and 2022 - ACL Anthology","url":"https://aclanthology.org/2022.case-1.31/"},{"title":"Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021   and 2022","url":"https://arxiv.org/pdf/2211.11360"}]

Let me search for the specific data statistics from the official task description.

Links: [{"title":"Emerging Markets Welfare – CASE 2022","url":"https://emw.ku.edu.tr/case-2022/"},{"title":"[2210.09770] EventGraph at CASE 2021 Task 1: A General Graph-based Approach to Protest Event Extraction","url":"https://ar5iv.labs.arxiv.org/html/2210.09770"},{"title":"[2211.11360] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022","url":"https://arxiv.org/abs/2211.11360"},{"title":"(PDF) ClassBases at CASE-2022 Multilingual Protest Event Detection Tasks: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets","url":"https://www.researchgate.net/publication/367216659_ClassBases_at_CASE-2022_Multilingual_Protest_Event_Detection_Tasks_Multilingual_Protest_News_Detection_and_Automatically_Replicating_Manually_Created_Event_Datasets"},{"title":"ClassBases at the CASE-2022 Multilingual Protest Event Detection Task: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets - ACL Anthology","url":"https://aclanthology.org/2022.case-1.21/"},{"title":"Extended Multilingual Protest News Detection - Shared Task 1, CASE 2021 and 2022 - ACL Anthology","url":"https://aclanthology.org/2022.case-1.31/"},{"title":"Multilingual Protest News Detection - Shared Task 1, CASE 2021 | Request PDF","url":"https://www.researchgate.net/publication/353490567_Multilingual_Protest_News_Detection_-_Shared_Task_1_CASE_2021"},{"title":"Multilingual Protest News Detection - Shared Task 1, CASE 2021 - ACL Anthology","url":"https://aclanthology.org/2021.case-1.11/"}]

Based on the search results, I've found substantial information about CASE 2022 Task 1, Subtask 1 (document classification). Here's what I've found:

## CASE 2022 Task 1, Subtask 1: Document Classification Overview

**Task Description:**
CASE 2022 Task 1 consists of four subtasks including document classification, sentence classification, event sentence coreference identification, and event extraction.

**Languages:**
The training data consists of documents in English, Portuguese, and Spanish, while the evaluation texts are in English, Hindi, Mandarin, Portuguese, Spanish, Turkish, and Urdu.

**Dataset Split:**
The training data from CASE 2021 in English, Portuguese and Spanish were utilized. The CASE 2022 extension consists of expanding the test data with more data in previously available languages, namely, English, Hindi, Portuguese, and Spanish, and adding new test data in Mandarin, Turkish, and Urdu for Sub-task 1, document classification.

**Zero-Shot Setup:**
Predicting document labels in Hindi, Mandarin, Turkish, and Urdu occurs in a zero-shot setting.

**Data Source:**
The new document level data were randomly sampled from MOT v1.2 and were annotated by co-authors of the task organizers, with documents annotated by native speakers of the respective language.

Unfortunately, the search results do not contain specific information about the exact sample size (number of documents) or the precise train/test split percentages for the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "87ee4e1a-e9af-4ebb-9c43-ef963ed397f4"
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-20T09:32:00.307Z_

<details><summary>↩ Tool result · `toolu_01FXQnfuBJ4RAfncrJ7XfnoL`</summary>

```text
id_doc,id_coder,id_event,entry_time,doc_country,doc_publdate,doc_source,doc_probability,event_index,event_n,country_name,country_size,community,date,month,year,period,action_form,radical_action,part_all,big_event,issue_econ_private,issue_econ_public,issue_cult_lib,issue_environment,issue_political,issue_regional,issue_cult_cons,issue_xeno,issue_other,issue_dontknow,issue_missing,actor_party_left,actor_party_right,actor_party_unknown,actor_union_private,actor_union_public,actor_union_both,actor_union_unknown,actor_group_pens,actor_group_stud,actor_group_occup,actor_group_other,actor_other,actor_dontknow,actor_missing,weight_sample,weight_newswire,weight_country,weighted_event,weighted_part_all
924,13,3930,2016-05-03 19:59:46,norway,2000-09-12,DPA,.71601903,3,1,austria,8.6000004,vienna,2000-01-01,1,2000,normal times,demonstrations,not radical,1250,no,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.5,1,3.1517622,.63456565,793.20703
2072,30,19716,2016-05-07 18:26:15,austria,2001-06-20,CTK,.96823615,1,1,austria,8.6000004,austria (entire country),2000-01-01,1,2000,normal times,"petitions, symbolic actions",not radical,60000,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.25 sample,1,3.1517622,.31728283,19036.969
2490,30,19781,2016-05-08 21:44:48,austria,2001-10-21,CTK,.91951966,1,1,austria,8.6000004,weigetschlag,2000-01-01,1,2000,normal times,demonstrations,not radical,100,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.25 sample,1,3.1517622,.31728283,31.728281
30,1,10347,2016-04-21 23:15:29,slovenia,2000-01-13,CTK,.80277473,1,1,austria,8.6000004,vienna,2000-01-13,1,2000,normal times,"petitions, symbolic actions",not radical,4096,no,no,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,no,no,.25 sample,1,3.1517622,.31728283,1299.5905
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "f520e6be-f772-4f36-be5e-efa16af9bae2"
}
```

</details>

---

### System

_source line 241_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Count total rows in the poldem-protest_30 CSV",
  "usage": {
    "total_tokens": 37691,
    "tool_uses": 27,
    "duration_ms": 163381
  },
  "last_tool_name": "Bash",
  "uuid": "209e8169-60a1-4b99-b38c-d7fe0ac342a4",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 242_

<details open><summary>🔧 Tool call — Bash · `toolu_01LX1Dqg1AVWuD13PpY9DNaB`</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | wc -l",
  "description": "Count total rows in the poldem-protest_30 CSV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "70787779-021c-4c9d-91aa-71679aea959c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199opCtWfzVt9vsir6igdJH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 35431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 970,
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

### System

_source line 243_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for CASE 2021 shared task data statistics \"number of …",
  "usage": {
    "total_tokens": 46605,
    "tool_uses": 31,
    "duration_ms": 153361
  },
  "last_tool_name": "WebSearch",
  "uuid": "ee03f865-362a-4cea-8177-8a8ec7174fb7",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 244_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfuWEWbYnwwz8sJq8mafWx`</summary>

```json
{
  "query": "CASE 2021 shared task data statistics \"number of documents\" OR \"sample size\" task1 subtask1 English Hindi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "8561d95b-4af0-433c-a332-6b7c5b3a5d54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TMNKgfmsFXTewHyWhDaTQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 41738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4155,
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

_source line 245_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "description": "Searching for huggingface \"protest\" OR \"political event\" datase…",
  "usage": {
    "total_tokens": 46606,
    "tool_uses": 32,
    "duration_ms": 154298
  },
  "last_tool_name": "WebSearch",
  "uuid": "94b39667-9b1b-4991-a1e3-525adc41a6c7",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 246_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NrTcAfVYcYNMyPSbK3Lhqy`</summary>

```json
{
  "query": "huggingface \"protest\" OR \"political event\" dataset text classification multi-class labels",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "7c2536f9-67e8-441f-a3e7-744377361649",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TMNKgfmsFXTewHyWhDaTQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 41738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4155,
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

_source line 247_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "byqbx5z8r",
  "tool_use_id": "toolu_01LX1Dqg1AVWuD13PpY9DNaB",
  "description": "Count total rows in the poldem-protest_30 CSV",
  "task_type": "local_bash",
  "uuid": "fdd45985-a421-47a7-915a-670c27fca722",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 248 · 2026-05-20T09:32:10.038Z_

<details><summary>↩ Tool result · `toolu_01BfuWEWbYnwwz8sJq8mafWx`</summary>

```text
Web search results for query: "CASE 2021 shared task data statistics "number of documents" OR "sample size" task1 subtask1 English Hindi"

Links: [{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Multilingual Protest News Detection - Shared Task 1, CASE 2021 | Request PDF","url":"https://www.researchgate.net/publication/353490567_Multilingual_Protest_News_Detection_-_Shared_Task_1_CASE_2021"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"(PDF) Multilingual Protest News Detection - Shared Task 1, CASE 2021","url":"https://www.academia.edu/64931265/Multilingual_Protest_News_Detection_Shared_Task_1_CASE_2021"},{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.academia.edu/64357373/Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"Shared Task on Multilingual protest news detection CASE ...","url":"https://competitions.codalab.org/competitions/31247"},{"title":"Handshakes AI Research at CASE 2021 Task 1: Exploring different   approaches for multilingual tasks","url":"https://arxiv.org/pdf/2110.15599"},{"title":"CALCS 2021 Shared Task: Machine Translation for Code-Switched Data","url":"https://arxiv.org/pdf/2202.09625"}]

Based on the search results, I found relevant information about the CASE 2021 shared task. The results show information about Task 1 (Multilingual protest news detection) and its subtasks, but the specific data statistics you're looking for (number of documents or sample size for Task 1 Subtask 1 in English and Hindi) are not explicitly provided in these search results.

The search results confirm that:

- Task 1 includes Multilingual protest news detection with Subtask 1 being document classification
- The training dataset consisted of English, Spanish and Portuguese, while the test data were from English, Spanish, Portuguese, and Hindi

However, the exact number of documents or sample sizes for Task 1 Subtask 1 are not mentioned in these results. The information indicates that sample data, submission formats, scripts, baseline scores, and additional information will be shared on the dedicated online repository at the GitHub repository (https://github.com/emerging-welfare/case-2021-shared-task), which would likely contain the detailed data statistics you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3260bfac-39f5-4ee7-900e-f318688974ad"
}
```

</details>

---

### System

_source line 249_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "byqbx5z8r",
  "tool_use_id": "toolu_01LX1Dqg1AVWuD13PpY9DNaB",
  "status": "completed",
  "output_file": "",
  "summary": "Count total rows in the poldem-protest_30 CSV",
  "uuid": "4c9c397f-3818-4cc0-800f-dc4ce0ec17aa",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 250 · 2026-05-20T09:32:11.862Z_

<details><summary>↩ Tool result · `toolu_01LX1Dqg1AVWuD13PpY9DNaB`</summary>

```text
30853
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "45991e55-4641-4879-b825-1d63a9d69bc5"
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-20T09:32:13.569Z_

<details><summary>↩ Tool result · `toolu_01NrTcAfVYcYNMyPSbK3Lhqy`</summary>

```text
Web search results for query: "huggingface "protest" OR "political event" dataset text classification multi-class labels"

Links: [{"title":"cjerzak/TextQuantificationDatasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cjerzak/TextQuantificationDatasets"},{"title":"valurank/PoliticalBias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/valurank/PoliticalBias"},{"title":"cajcodes/political-bias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cajcodes/political-bias"},{"title":"fmplaza/offendes · Datasets at Hugging Face","url":"https://huggingface.co/datasets/fmplaza/offendes"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"},{"title":"README.md · cajcodes/political-bias at main","url":"https://huggingface.co/datasets/cajcodes/political-bias/blob/main/README.md"},{"title":"ethos · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ethos"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"mlburnham/Political_DEBATE_base_v1.0 · Hugging Face","url":"https://huggingface.co/mlburnham/Political_DEBATE_base_v1.0"}]

Based on my search results, here are some relevant Hugging Face datasets and resources for protest/political event text classification:

## Datasets Found:

1. **TextQuantificationDatasets** - A multi-class classification dataset tagged with text-classification, social-science, and politics.

2. **Political Bias Dataset** (cajcodes/political-bias) - Contains 658 synthetic statements annotated with bias ratings from 0 to 4, representing a spectrum from highly conservative to highly liberal.

3. **Offensive Language Detection** (fmplaza/offendes) - Intended for multi-class offensive classification and binary offensive classification, with categories including political ideology.

## Related Research:

The search also revealed academic work on protest detection:

- The CLEF 2019 ProtestNews Lab tasks participants to identify text relating to political protests within larger corpora of news data, with three tasks including article classification, sentence detection, and event extraction.

- A cross-context news corpus for protest events has been developed with variety and quality to develop and benchmark text classification and event extraction systems.

These resources offer varying approaches to multi-class text classification for political content, though none appeared specifically marketed as a "protest" dataset with multi-class labels on the Hugging Face platform based on these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0ce0cff3-9cce-489f-956b-87837d594992"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running List action_form and issue columns with their positions",
  "usage": {
    "total_tokens": 37995,
    "tool_uses": 28,
    "duration_ms": 175005
  },
  "last_tool_name": "Bash",
  "uuid": "adeae962-aece-4a00-997d-8aa4a12e7f51",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 253_

<details open><summary>🔧 Tool call — Bash · `toolu_013B65SaRdpF5jYYMfD3eZpW`</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -1 | tr ',' '\\n' | grep -n \"action_form\\|issue_\"",
  "description": "List action_form and issue columns with their positions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "e521a090-7075-473e-a6f4-234c0c993211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES736TUQYzVEq73ayKRoib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 36401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 235,
        "ephemeral_1h_input_tokens": 0
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

_source line 254 · 2026-05-20T09:32:16.184Z_

<details><summary>↩ Tool result · `toolu_013B65SaRdpF5jYYMfD3eZpW`</summary>

```text
18:action_form
22:issue_econ_private
23:issue_econ_public
24:issue_cult_lib
25:issue_environment
26:issue_political
27:issue_regional
28:issue_cult_cons
29:issue_xeno
30:issue_other
31:issue_dontknow
32:issue_missing
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5d8a541f-ae07-4628-b75f-bde1defaa142"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Count unique values in action_form column (column 18)",
  "usage": {
    "total_tokens": 38064,
    "tool_uses": 29,
    "duration_ms": 176059
  },
  "last_tool_name": "Bash",
  "uuid": "ff82906c-0eb8-4803-a182-33f6890f21f3",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 256_

<details open><summary>🔧 Tool call — Bash · `toolu_01BTzwGQuGNZp69X2bCncBVZ`</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | cut -d',' -f18 | sort | uniq -c | sort -rn",
  "description": "Count unique values in action_form column (column 18)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "53fabc65-61a2-4dd1-bf96-09cda78326f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES736TUQYzVEq73ayKRoib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 36401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 235,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 257_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bswn0k6qx",
  "tool_use_id": "toolu_01BTzwGQuGNZp69X2bCncBVZ",
  "description": "Count unique values in action_form column (column 18)",
  "task_type": "local_bash",
  "uuid": "272276ab-5982-413b-bd60-079ffcbba269",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 258_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bswn0k6qx",
  "tool_use_id": "toolu_01BTzwGQuGNZp69X2bCncBVZ",
  "status": "completed",
  "output_file": "",
  "summary": "Count unique values in action_form column (column 18)",
  "uuid": "c3e41b20-1403-4956-b325-a25f163dc520",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 259 · 2026-05-20T09:32:26.290Z_

<details><summary>↩ Tool result · `toolu_01BTzwGQuGNZp69X2bCncBVZ`</summary>

```text
  13327 demonstrations
   6224 violent protest
   5176 strikes
   2594 "confrontations
   2447 "petitions
   1080 other protest
      3 2006
      1 action_form
      1  baia mare
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "3e3c36b3-51a0-45a3-8604-d0f227788a64"
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
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Get clean action_form values with proper CSV parsing",
  "usage": {
    "total_tokens": 38595,
    "tool_uses": 30,
    "duration_ms": 194502
  },
  "last_tool_name": "Bash",
  "uuid": "778a9c8b-7833-4acb-abb7-f45f5ee9a91b",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 261_

<details open><summary>🔧 Tool call — Bash · `toolu_01DekeeLLePevQURkkiZte6N`</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | awk -F',' '{print $18}' | sed 's/^\"//;s/\"$//' | sort | uniq -c | sort -rn | head -20",
  "description": "Get clean action_form values with proper CSV parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "0561dc6a-575a-4ba7-8fad-2fe812275290",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHBysNznNqx3FY41NSoYDA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 36636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 459,
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

### System

_source line 262_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bestgrf0y",
  "tool_use_id": "toolu_01DekeeLLePevQURkkiZte6N",
  "description": "Get clean action_form values with proper CSV parsing",
  "task_type": "local_bash",
  "uuid": "e6ed28aa-bbe5-4fcf-b953-5f360bed00ea",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 263_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bestgrf0y",
  "tool_use_id": "toolu_01DekeeLLePevQURkkiZte6N",
  "status": "completed",
  "output_file": "",
  "summary": "Get clean action_form values with proper CSV parsing",
  "uuid": "f766a42f-3a71-4270-9eb7-ca030e63c22d",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 264 · 2026-05-20T09:32:45.013Z_

<details><summary>↩ Tool result · `toolu_01DekeeLLePevQURkkiZte6N`</summary>

```text
  13327 demonstrations
   6224 violent protest
   5176 strikes
   2594 confrontations
   2447 petitions
   1080 other protest
      3 2006
      1 action_form
      1  baia mare
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "eb7ea09a-3e2e-4586-bf59-9bb6b6a669c7"
}
```

</details>

---

### System

_source line 265_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "description": "Running Count binary issue category distributions",
  "usage": {
    "total_tokens": 38854,
    "tool_uses": 31,
    "duration_ms": 210950
  },
  "last_tool_name": "Bash",
  "uuid": "6ad66cc8-acae-4400-92ae-386edac2e8f9",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool call

_source line 266_

<details open><summary>🔧 Tool call — Bash · `toolu_013K5Ye3fo5mjrQFGF9j1ZWu`</summary>

```json
{
  "command": "# Check the issue columns: each is binary (yes/no), count how many events have each issue\ncurl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | python3 -c \"\nimport csv, sys\nreader = csv.DictReader(sys.stdin)\nissue_cols = ['issue_econ_private','issue_econ_public','issue_cult_lib','issue_environment','issue_political','issue_regional','issue_cult_cons','issue_xeno','issue_other','issue_dontknow','issue_missing']\ncounts = {c:0 for c in issue_cols}\ntotal = 0\nfor row in reader:\n    total += 1\n    for c in issue_cols:\n        if row.get(c,'').strip().lower() == 'yes':\n            counts[c] += 1\nprint(f'Total rows: {total}')\nfor c in issue_cols:\n    print(f'{c}: {counts[c]} ({100*counts[c]/total:.1f}%)')\n\"",
  "description": "Count binary issue category distributions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "82b6aff7-660a-4075-a097-e4236927bcac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTfharmL7ukqnbkZnNHYq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 37095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 223,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 267_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "brflzots3",
  "tool_use_id": "toolu_013K5Ye3fo5mjrQFGF9j1ZWu",
  "description": "Count binary issue category distributions",
  "task_type": "local_bash",
  "uuid": "96e3ae0b-9239-4bf2-9728-7959f0c41482",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### System

_source line 268_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "brflzots3",
  "tool_use_id": "toolu_013K5Ye3fo5mjrQFGF9j1ZWu",
  "status": "completed",
  "output_file": "",
  "summary": "Count binary issue category distributions",
  "uuid": "e9f4f09b-c46b-4353-a87f-7f6fbcc674a2",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 269 · 2026-05-20T09:32:58.759Z_

<details><summary>↩ Tool result · `toolu_013K5Ye3fo5mjrQFGF9j1ZWu`</summary>

```text
Total rows: 30852
issue_econ_private: 3769 (12.2%)
issue_econ_public: 9247 (30.0%)
issue_cult_lib: 5240 (17.0%)
issue_environment: 2051 (6.6%)
issue_political: 4678 (15.2%)
issue_regional: 2212 (7.2%)
issue_cult_cons: 903 (2.9%)
issue_xeno: 1806 (5.9%)
issue_other: 3339 (10.8%)
issue_dontknow: 21 (0.1%)
issue_missing: 1304 (4.2%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "5f861257-5e04-4d2f-9815-0f2233f5bd4e"
}
```

</details>

---

### System

_source line 270_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aaa88ae80b764645d",
  "tool_use_id": "toolu_01Cgb3VqR4Wn9RangSRTpyE5",
  "status": "completed",
  "output_file": "",
  "summary": "Search POLDEM dataset",
  "usage": {
    "total_tokens": 39376,
    "tool_uses": 31,
    "duration_ms": 259028
  },
  "uuid": "9c99aa23-b3a2-44f5-a085-6fb1f33c359d",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 271 · 2026-05-20T09:33:39.168Z_

<details><summary>↩ Tool result · `toolu_01Cgb3VqR4Wn9RangSRTpyE5`</summary>

````text
Now I have all the information needed. Here is the report:

---

```
数据集名称: PolDem – Protest Dataset 30 European Countries (poldem-protest_30), Version 1
类别数 K: 
  - action_form (抗议形式): 6 类
  - issue (议题): 9 实质类 + 2 缺失/不知道类 = 11 列 (binary multi-label)
类别列表:
  action_form:
    1. demonstrations (13,327 events, 43.2%)
    2. violent protest (6,224, 20.2%)
    3. strikes (5,176, 16.8%)
    4. confrontations (2,594, 8.4%)
    5. petitions, symbolic actions (2,447, 7.9%)
    6. other protest (1,080, 3.5%)
  issue (multi-label binary columns):
    1. issue_econ_private — 企业/雇主相关经济议题 (12.2%)
    2. issue_econ_public — 公共机构相关经济议题 (30.0%)
    3. issue_cult_lib — 文化自由主义 (和平/女权/LGBTQ/反种族主义/移民权利) (17.0%)
    4. issue_environment — 环境/能源/基础设施 (6.6%)
    5. issue_political — 政治议题 (腐败/选举改革/代表权) (15.2%)
    6. issue_regional — 地区主义/分离主义 (7.2%)
    7. issue_cult_cons — 文化保守主义 (2.9%)
    8. issue_xeno — 仇外/右翼极端主义/反移民 (5.9%)
    9. issue_other — 其他 (10.8%)
    10. issue_dontknow (0.1%)
    11. issue_missing (4.2%)
样本量: 30,852 行 (对应约 33,655 coded events，论文原文数字；CSV 去重后 30,852 条记录)
License: 未在网站明确标注。但方法论论文 (Lorenzini et al., 2022) 以 CC BY 4.0 发表。数据集本身在 poldem.eui.eu 上无登录即可直接下载，无明确 license 声明，页脚标注 "© EUI & WZB. All rights reserved."
下载方式: 免费直接下载，无需注册/登录/申请
  - CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv (约 8.5 MB)
  - Stata: https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta
  - Codebook: https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf
  - Documentation: https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf
  - 下载页面: https://poldem.eui.eu/download/protest-events/
Gold-standard human labels: 部分是，质量中等
  - 标注方式: 半自动流程 (semi-automated NLP pipeline)。先用关键词检索 520 万新闻文档，经去重/过滤/分类器筛选后，由 35 名研究生人工编码 45,680 篇文档（耗时 642 个工作日）
  - Intercoder reliability: 事件识别 F1 = 0.60 (SD 0.06)；议题 Cohen's κ = 0.53 (SD 0.13)；行动者 κ = 0.57；参与人数 κ = 0.45
  - 作者明确指出任务对人类编码者来说也"困难"，标注一致性属于 "fair to good"，并非高一致性 gold standard
引用论文:
  - 数据集: Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European Countries, Version 1.
  - 方法论文: Lorenzini, J., Kriesi, H., Makarov, P., & Wüest, B. (2022). Protest Event Analysis: Developing a Semiautomated NLP Approach. American Behavioral Scientist, 66(5), 555–577. https://doi.org/10.1177/00027642211021650
备注:
  - 覆盖 30 个欧洲国家，2000-2015 年
  - issue 列是 multi-label (一个事件可同时标记多个议题)，不是单标签分类
  - action_form 是单标签分类，K=6
  - 数据源为 10 家英文通讯社的新闻稿 (Reuters, AFP, DPA 等)
  - 另有两个子集: poldem-protest_6 (6国, 1975-2011) 和 poldem-protest_eu (6国EU议题, 1995-2010)
  - 如果要做 annotation error attribution 实验，action_form 是 K=6 的单标签分类任务，比较适合；issue 是 multi-label 二值标注，intercoder κ 仅 0.53，噪声较大
```

Sources:
- [PolDem Observatory Homepage](https://poldem.eui.eu/)
- [Protest Events Download Page](https://poldem.eui.eu/download/protest-events/)
- [PolDem-Protest 30 Codebook (PDF)](https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf)
- [PEA Documentation v1 (PDF)](https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf)
- [Lorenzini et al. (2022) - SAGE Journals](https://journals.sagepub.com/doi/10.1177/00027642211021650)
- [PolDem Data Overview - EUI](https://poldem.eui.eu/data-overview/)
- [VU Amsterdam Dataset Page](https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries)
- [Discuss-Data Repository](https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/)
- [WZB Berlin - PolDem Project](https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa)

agentId: aaa88ae80b764645d (use SendMessage with to: 'aaa88ae80b764645d' to continue this agent)
&lt;usage>total_tokens: 39758
tool_uses: 31
duration_ms: 259031&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "886d432b-417b-46e8-8932-ecdce36099ff",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
    "agentId": "aaa88ae80b764645d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the report:\n\n---\n\n```\n数据集名称: PolDem – Protest Dataset 30 European Countries (poldem-protest_30), Version 1\n类别数 K: \n  - action_form (抗议形式): 6 类\n  - issue (议题): 9 实质类 + 2 缺失/不知道类 = 11 列 (binary multi-label)\n类别列表:\n  action_form:\n    1. demonstrations (13,327 events, 43.2%)\n    2. violent protest (6,224, 20.2%)\n    3. strikes (5,176, 16.8%)\n    4. confrontations (2,594, 8.4%)\n    5. petitions, symbolic actions (2,447, 7.9%)\n    6. other protest (1,080, 3.5%)\n  issue (multi-label binary columns):\n    1. issue_econ_private — 企业/雇主相关经济议题 (12.2%)\n    2. issue_econ_public — 公共机构相关经济议题 (30.0%)\n    3. issue_cult_lib — 文化自由主义 (和平/女权/LGBTQ/反种族主义/移民权利) (17.0%)\n    4. issue_environment — 环境/能源/基础设施 (6.6%)\n    5. issue_political — 政治议题 (腐败/选举改革/代表权) (15.2%)\n    6. issue_regional — 地区主义/分离主义 (7.2%)\n    7. issue_cult_cons — 文化保守主义 (2.9%)\n    8. issue_xeno — 仇外/右翼极端主义/反移民 (5.9%)\n    9. issue_other — 其他 (10.8%)\n    10. issue_dontknow (0.1%)\n    11. issue_missing (4.2%)\n样本量: 30,852 行 (对应约 33,655 coded events，论文原文数字；CSV 去重后 30,852 条记录)\nLicense: 未在网站明确标注。但方法论论文 (Lorenzini et al., 2022) 以 CC BY 4.0 发表。数据集本身在 poldem.eui.eu 上无登录即可直接下载，无明确 license 声明，页脚标注 \"© EUI & WZB. All rights reserved.\"\n下载方式: 免费直接下载，无需注册/登录/申请\n  - CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv (约 8.5 MB)\n  - Stata: https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta\n  - Codebook: https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf\n  - Documentation: https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf\n  - 下载页面: https://poldem.eui.eu/download/protest-events/\nGold-standard human labels: 部分是，质量中等\n  - 标注方式: 半自动流程 (semi-automated NLP pipeline)。先用关键词检索 520 万新闻文档，经去重/过滤/分类器筛选后，由 35 名研究生人工编码 45,680 篇文档（耗时 642 个工作日）\n  - Intercoder reliability: 事件识别 F1 = 0.60 (SD 0.06)；议题 Cohen's κ = 0.53 (SD 0.13)；行动者 κ = 0.57；参与人数 κ = 0.45\n  - 作者明确指出任务对人类编码者来说也\"困难\"，标注一致性属于 \"fair to good\"，并非高一致性 gold standard\n引用论文:\n  - 数据集: Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European Countries, Version 1.\n  - 方法论文: Lorenzini, J., Kriesi, H., Makarov, P., & Wüest, B. (2022). Protest Event Analysis: Developing a Semiautomated NLP Approach. American Behavioral Scientist, 66(5), 555–577. https://doi.org/10.1177/00027642211021650\n备注:\n  - 覆盖 30 个欧洲国家，2000-2015 年\n  - issue 列是 multi-label (一个事件可同时标记多个议题)，不是单标签分类\n  - action_form 是单标签分类，K=6\n  - 数据源为 10 家英文通讯社的新闻稿 (Reuters, AFP, DPA 等)\n  - 另有两个子集: poldem-protest_6 (6国, 1975-2011) 和 poldem-protest_eu (6国EU议题, 1995-2010)\n  - 如果要做 annotation error attribution 实验，action_form 是 K=6 的单标签分类任务，比较适合；issue 是 multi-label 二值标注，intercoder κ 仅 0.53，噪声较大\n```\n\nSources:\n- [PolDem Observatory Homepage](https://poldem.eui.eu/)\n- [Protest Events Download Page](https://poldem.eui.eu/download/protest-events/)\n- [PolDem-Protest 30 Codebook (PDF)](https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf)\n- [PEA Documentation v1 (PDF)](https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf)\n- [Lorenzini et al. (2022) - SAGE Journals](https://journals.sagepub.com/doi/10.1177/00027642211021650)\n- [PolDem Data Overview - EUI](https://poldem.eui.eu/data-overview/)\n- [VU Amsterdam Dataset Page](https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries)\n- [Discuss-Data Repository](https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/)\n- [WZB Berlin - PolDem Project](https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa)"
      }
    ],
    "totalDurationMs": 259031,
    "totalTokens": 39758,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 37318,
      "output_tokens": 1921,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1921,
          "cache_read_input_tokens": 37318,
          "cache_creation_input_tokens": 518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 518,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 24
    }
  }
}
````

</details>

---

### System

_source line 272_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa45e88c0b435afd8",
  "tool_use_id": "toolu_0192Rf5hZwdGc442eWRxtvrU",
  "status": "completed",
  "output_file": "",
  "summary": "Search protest NLP datasets",
  "usage": {
    "total_tokens": 48501,
    "tool_uses": 32,
    "duration_ms": 278538
  },
  "uuid": "1e442fec-6ed3-46ef-801c-07914a022669",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 273 · 2026-05-20T09:34:09.188Z_

<details><summary>↩ Tool result · `toolu_0192Rf5hZwdGc442eWRxtvrU`</summary>

````text
Now I have enough information to compile a thorough report. Here are my findings:

---

## Protest/Political Event Multi-Class Text Classification Datasets

### 1. CASE 2021 Task 2 -- Fine-Grained Socio-Political Event Classification

```
数据集名称: CASE 2021 Shared Task 2 (Fine-Grained Event Classification)
类别数 K: 25 (main task) + 3 zero-shot + 2 surprise = 30 total
类别列表: ACLED 25 sub-event types, including Armed Clash, Government Regains Territory, 
  Non-state Actor Overtakes Territory, Violent Demonstration, Peaceful Protest, 
  Protest with Intervention, Excessive Force Against Protesters, Mob Violence, 
  Chemical Weapon, Air/Drone Strike, Suicide Bomb, Shelling/Artillery/Missile Attack, 
  Remote Explosive/Landmine/IED, Grenade, Sexual Violence, Attack, Abduction/Forced 
  Disappearance, Agreement, Arrests, Change to Group Activity, Disrupted Weapons Use, 
  Headquarters or Base Established, Looting/Property Destruction, 
  Non-violent Transfer of Territory, Other
样本量: ~600K short event descriptions (from ACLED text snippets)
License: 学术用途（需通过 ACLED 获取原始数据）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task2 文件夹含测试集 TSV)；
  训练数据需从 ACLED https://acleddata.com/ 获取
Gold-standard human labels: 是 (ACLED 专业编码员标注)
引用论文: Haneczok et al. "Fine-grained Event Classification in News-like Text Snippets - 
  Shared Task 2, CASE 2021" (ACL Anthology 2021.case-1.23)
备注: 测试集含标签可直接下载；训练数据建议从 ACLED 导出工具获取。K=25 是核心类别，
  非常适合多分类研究。涵盖政治暴力、示威、战略发展三大类。
```

### 2. CASE 2021/2022 Task 1 -- Multilingual Protest News Detection

```
数据集名称: CASE Shared Task 1 (Multilingual Protest News Detection)
类别数 K: Subtask 1 为二分类 (protest-related / not)；Subtask 2 为句子级二分类
类别列表: [protest-related, not protest-related] (文档级)；[event sentence, non-event sentence] (句子级)
样本量: Subtask 2 句子分类约 26,208 sentences；文档级数据涵盖多语言
License: 公开（GitHub 直接下载）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task1 文件夹)
  CASE 2022: https://github.com/emerging-welfare/case-2022-multilingual-event
Gold-standard human labels: 是 (政治学家标注，inter-annotator adjudication)
引用论文: Hürriyetoğlu et al. "Multilingual Protest News Detection - Shared Task 1, CASE 2021"
  (ACL Anthology 2021.case-1.11)
备注: ⚠️ K=2（二分类），不满足 K≥3 的要求。但与 Task 2 同源数据，可作为辅助。
  语言覆盖：English, Spanish, Portuguese, Hindi, Mandarin, Turkish, Urdu。
```

### 3. GLOCON Gold Standard Corpus (Cross-Context News Corpus)

```
数据集名称: GLOCON Gold Standard Corpus / Cross-Context News Corpus for Protest Events
类别数 K: 多层标注——文档级 (protest/non-protest)、句子级、token 级 (event trigger + arguments)
类别列表: 文档级二分类 + token级事件类型（protest event triggers with typed arguments）
样本量: 621,290 events from 9,509,193 news documents (自动预测);
  Gold standard 部分规模较小（需确认具体数量）
License: 需申请访问
下载方式: https://github.com/emerging-welfare/glocongold (申请流程说明)
  Dashboard: https://glocon.ku.edu.tr/
Gold-standard human labels: 是 (两位政治学家标注 + supervisor adjudication + 
  semi-automatic error detection)
引用论文: Hürriyetoğlu et al. "Cross-Context News Corpus for Protest Event-Related 
  Knowledge Base Construction" Data Intelligence 2021
备注: 覆盖 India, China, South Africa 新闻源。Gold standard 部分需要通过 GitHub 申请，
  不是完全免费下载。大规模自动标注数据可通过 dashboard 获取。
```

### 4. GLOCON Database (Full)

```
数据集名称: GLOCON (Global Contentious Politics Database)
类别数 K: 多类（事件类型包括 demonstrations, rallies, strikes, clashes, political violence 等）
类别列表: [Demonstration, Rally, Strike, Clash, Political Violence, ...] (具体完整列表需查文档)
样本量: 621,290 events（来自 India, South Africa, Argentina, Brazil, Turkey）
License: 公开下载（需在网站注册）
下载方式: https://glocon.ku.edu.tr/ (Download section) 
  数据格式: JSONL (每个新闻源一个文件)
Gold-standard human labels: 部分是（gold corpus 人工标注），大部分为自动预测标签
引用论文: Duruşan & Hürriyetoğlu "GLOCON Database: Design Decisions and User Manual (v1.0)" 
  arXiv:2405.18613
备注: 数据量大但标签为自动预测，非全部 gold-standard。适合大规模实验，
  但需注意标签噪声。覆盖全球南方五国。
```

### 5. ACLED (Armed Conflict Location & Event Data)

```
数据集名称: ACLED (Armed Conflict Location & Event Data Project)
类别数 K: 6 event types / 25 sub-event types / 3 disorder types
类别列表: 
  Disorder types: [Political Violence, Demonstrations, Strategic Developments]
  Event types: [Battles, Explosions/Remote Violence, Violence Against Civilians, 
    Riots, Protests, Strategic Developments]
  Sub-event types (25): [Armed Clash, Government Regains Territory, Non-state Actor
    Overtakes Territory, Chemical Weapon, Air/Drone Strike, Suicide Bomb, 
    Shelling/Artillery/Missile Attack, Remote Explosive/Landmine/IED, Grenade, 
    Sexual Violence, Attack, Abduction/Forced Disappearance, Violent Demonstration, 
    Mob Violence, Peaceful Protest, Protest with Intervention, Excessive Force 
    Against Protesters, Agreement, Arrests, Change to Group Activity, 
    Disrupted Weapons Use, HQ/Base Established, Looting/Property Destruction, 
    Non-violent Transfer of Territory, Other]
样本量: >1.3 million events (截至 2022)，实时更新
License: 开放访问（注册免费账户即可下载），学术/非营利用途免费
下载方式: https://acleddata.com/conflict-data/download-data/ (Data Export Tool / API)
  也可通过 HDX: https://data.humdata.org/organization/acled
Gold-standard human labels: 是 (专业编码员按 codebook 标注)
引用论文: Raleigh et al. "Introducing ACLED: An Armed Conflict Location and Event 
  Dataset" Journal of Peace Research 2010
备注: ⭐ 最佳候选之一。K=6 (event types) 或 K=25 (sub-event types)，样本量巨大，
  专业人工标注，免费注册下载。每条记录包含事件文本描述 (notes 字段) 可用于 NLP。
  注意：这不是"原始新闻文本"数据集，而是编码后的结构化事件数据（含短文本摘要）。
```

### 6. CEHA (Conflict Events in the Horn of Africa)

```
数据集名称: CEHA (Conflict Events in the Horn of Africa)
类别数 K: 4 (event types) + 2 (relevance classification)
类别列表: [Tribal/Communal/Ethnic Conflict, Religious Conflict, 
  Socio-political Violence Against Women, Climate-Related Security Risks]
样本量: 500 event descriptions
License: 公开 (GitHub)
下载方式: https://github.com/dataminr-ai/CEHA
Gold-standard human labels: 是 (subject matter experts 标注)
引用论文: CEHA: A Dataset of Conflict Events in the Horn of Africa (COLING 2025)
备注: ⚠️ 样本量仅 500，不满足 ≥1000 的要求。K=4 满足要求。
  数据来源于 ACLED 和 GDELT。适合低资源场景研究。
```

### 7. SPEED (Social, Political and Economic Event Database)

```
数据集名称: SPEED (Social Political Economic Event Dataset)
类别数 K: 4 Tier-1 categories + 多个子类
类别列表: Tier-1: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 Liberia, Philippines, Sierra Leone (1979-2008)，具体事件数未在搜索中确认
License: 公开下载
下载方式: https://databank.illinois.edu/datasets/IDB-7407320 
  官方: https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED
Gold-standard human labels: 是 (Cline Center 编码员标注)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: 结构化事件数据（非原始新闻文本）。覆盖时间较早(1979-2008)。
  K=4 满足要求。需确认是否包含可用于 NLP 的文本字段。
```

### 8. PolDem Protest Event Dataset 30

```
数据集名称: PolDem-Protest Dataset 30
类别数 K: 多类（action forms / organizational types 等多维标注）
类别列表: Action forms (多类), 组织类型 (SMOs, initiatives, loose networks 等),
  事件关联类型等
样本量: 45,680 documents (30 European countries, 2000-2015)
License: 需确认（网站下载）
下载方式: https://poldem.eui.eu/ (Downloads section)
Gold-standard human labels: 是 (semi-automated coding of newswire reports + 人工验证)
引用论文: PolDem documentation (EUI)
备注: 覆盖 30 个欧洲国家。数据基于新闻通讯社报道。标注维度丰富，
  不仅仅是事件类型，还有参与组织、暴力程度等。需要去网站确认具体类别数和下载条件。
```

### 9. HumAID (Human-Annotated Disaster Incidents Data)

```
数据集名称: HumAID
类别数 K: 11
类别列表: [Caution and Advice, Displaced People and Evacuations, 
  Don't Know or Can't Judge, Infrastructure and Utility Damage, 
  Injured or Dead People, Missing or Found People, Not Humanitarian, 
  Other Relevant Information, Requests or Urgent Needs, Rescue/Volunteering/Donation, 
  Sympathy and Support]
样本量: ~77,000 manually annotated tweets from 19 disaster events (2016-2019)
License: CC-BY-NC (学术用途)
下载方式: https://crisisnlp.qcri.org/humaid_dataset.html
  HuggingFace: https://huggingface.co/datasets/QCRI/HumAID-event-type
Gold-standard human labels: 是 (人工标注)
引用论文: Alam et al. "HumAID: Human-Annotated Disaster Incidents Data from Twitter" 
  ICWSM 2021
备注: ⚠️ 这是灾难事件数据集，不是抗议事件数据集。但方法论和任务类型相似，
  可作为参考。K=11, 样本量充足，完全公开下载。
```

### 10. CrisisNLP / CrisisLexT26

```
数据集名称: CrisisLexT26 / CrisisLexT6
类别数 K: 7 (information types including NOT RELATED)
类别列表: [Affected Individuals, Infrastructure/Utilities, Donations/Volunteering, 
  Caution/Advice, Sympathy, Information Source, Not Related]
样本量: CrisisLexT26 ~28,000 tweets from 26 events; CrisisLexT6 ~60,000 tweets from 6 events
License: 公开
下载方式: https://crisisnlp.qcri.org/
Gold-standard human labels: 是 (crowdsourced annotation)
引用论文: Olteanu et al. "CrisisLex: A Lexicon for Collecting and Filtering 
  Microblogged Communications in Crises" ICWSM 2014
备注: ⚠️ 同样是灾难/危机事件，非专门抗议事件。但标注框架可参考。
```

### 11. MPEDS (Machine-learning Protest Event Data System)

```
数据集名称: MPEDS
类别数 K: 多类（protest form categories）
类别列表: 包含多种抗议形式分类（具体列表需查看 codebook）
样本量: 需确认（系统用于生成抗议事件数据）
License: 公开 (GitHub + Zenodo)
下载方式: https://github.com/MPEDS/mpeds (需 Git LFS)
  Zenodo: https://zenodo.org/records/886459
  Annotation Interface: https://github.com/MPEDS/mpeds-coder
Gold-standard human labels: 是 (系统辅助 + 人工验证)
引用论文: Hanna "MPEDS: Automating the Generation of Protest Event Data" (2017)
备注: 更多是一个工具/系统而非固定数据集。需要深入查看 repo 确认是否有现成标注数据。
```

### 12. Crowd Counting Consortium (CCC)

```
数据集名称: Crowd Counting Consortium U.S. Protest Event Data
类别数 K: 494 discrete descriptive tags (多标签)
类别列表: 494 个标签涵盖抗议类型、议题、参与者等
样本量: 42,347 protest events (US, Jan 2017 - Jan 2021); 138,826 English articles
License: 公开
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H
  GitHub: https://github.com/rexdouglass/crowd-counting-consortium
Gold-standard human labels: 是 (人工标注)
引用论文: Pressman & Chenoweth, Harvard Kennedy School
备注: ⭐ 多标签（494 tags），非多分类。数据量大，完全公开（Harvard Dataverse）。
  包含新闻文章 URL，但原始文本需自行爬取。结构化标签数据直接可用。
```

### 13. INDI-PROP (Indian Propaganda Dataset)

```
数据集名称: INDI-PROP
类别数 K: 3 (article-level bias) + 多类 (narrative frames)
类别列表: Article-level: [Pro-Government, Pro-Opposition, Neutral]
  + event-specific fine-grained narrative frames
样本量: 1,266 articles (CAA protest + Farmers' protest)
License: 需确认（arXiv 论文附数据）
下载方式: 需查看论文附录/GitHub（arXiv:2512.03582）
Gold-standard human labels: 是 (人工标注 + GPT-4o-mini 辅助)
引用论文: "Fine-grained Narrative Classification in Biased News Articles" (arXiv:2512.03582)
备注: 专注于印度抗议事件新闻的偏见与叙事分类。K=3 满足，样本量 1,266 满足 ≥1000。
  但不是"事件类型"分类，而是"叙事立场"分类。
```

---

## 总结推荐（满足全部筛选条件：K≥3, gold labels, public download, ≥1000 samples）

| 排名 | 数据集 | K | 样本量 | 最适合用途 |
|------|--------|---|--------|-----------|
| 1 | **ACLED** | 6/25 | >1.3M | 政治暴力+抗议事件多分类，文本字段可用于 NLP |
| 2 | **CASE 2021 Task 2** | 25 | ~600K snippets | 细粒度社会政治事件分类，NLP 共享任务标准 |
| 3 | **CCC (Harvard)** | 494 tags (多标签) | 42K events | 美国抗议事件多标签分类 |
| 4 | **PolDem-30** | 多类 | 45K docs | 欧洲 30 国抗议事件，多维标注 |
| 5 | **GLOCON** | 多类 | 621K events | 全球南方五国，大规模自动标签 |
| 6 | **INDI-PROP** | 3+ | 1,266 | 印度抗议事件叙事分类 |

**首选推荐**：ACLED (K=25 sub-event types) 和 CASE 2021 Task 2 是最贴合需求的数据集 -- 专门面向抗议/政治事件、多分类、gold-standard 人工标注、公开下载、样本量远超 1000。

Sources:
- [CASE 2021 Shared Task GitHub](https://github.com/emerging-welfare/case-2021-shared-task)
- [CASE 2022 Multilingual Event GitHub](https://github.com/emerging-welfare/case-2022-multilingual-event)
- [ACLED Data Download](https://acleddata.com/conflict-data/download-data/)
- [ACLED Codebook](https://acleddata.com/methodology/acled-codebook/)
- [GLOCON Database](https://glocon.ku.edu.tr/)
- [GLOCON Gold Standard GitHub](https://github.com/emerging-welfare/glocongold)
- [GLOCON Annotation Manuals (Zenodo)](https://zenodo.org/records/6540579)
- [CEHA GitHub (Dataminr)](https://github.com/dataminr-ai/CEHA)
- [SPEED Dataset (UIUC)](https://databank.illinois.edu/datasets/IDB-7407320)
- [Cline Center SPEED Project](https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED)
- [PolDem Protest Event Dataset](https://poldem.eui.eu/)
- [CCC Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H)
- [CCC GitHub](https://github.com/rexdouglass/crowd-counting-consortium)
- [HumAID on HuggingFace](https://huggingface.co/datasets/QCRI/HumAID-event-type)
- [CrisisNLP](https://crisisnlp.qcri.org/)
- [MPEDS GitHub](https://github.com/MPEDS/mpeds)
- [MPEDS Zenodo](https://zenodo.org/records/886459)
- [Cross-Context News Corpus (MIT Press)](https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event)
- [CASE 2021 Task 2 Overview Paper](https://aclanthology.org/2021.case-1.23/)
- [INDI-PROP Paper](https://www.arxiv.org/pdf/2512.03582)
- [ACLED on HDX](https://data.humdata.org/organization/acled)

agentId: aa45e88c0b435afd8 (use SendMessage with to: 'aa45e88c0b435afd8' to continue this agent)
&lt;usage>total_tokens: 53511
tool_uses: 32
duration_ms: 278539&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "b21f7c90-b17c-41ee-8636-1e7c9c13910c",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found.",
    "agentId": "aa45e88c0b435afd8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a thorough report. Here are my findings:\n\n---\n\n## Protest/Political Event Multi-Class Text Classification Datasets\n\n### 1. CASE 2021 Task 2 -- Fine-Grained Socio-Political Event Classification\n\n```\n数据集名称: CASE 2021 Shared Task 2 (Fine-Grained Event Classification)\n类别数 K: 25 (main task) + 3 zero-shot + 2 surprise = 30 total\n类别列表: ACLED 25 sub-event types, including Armed Clash, Government Regains Territory, \n  Non-state Actor Overtakes Territory, Violent Demonstration, Peaceful Protest, \n  Protest with Intervention, Excessive Force Against Protesters, Mob Violence, \n  Chemical Weapon, Air/Drone Strike, Suicide Bomb, Shelling/Artillery/Missile Attack, \n  Remote Explosive/Landmine/IED, Grenade, Sexual Violence, Attack, Abduction/Forced \n  Disappearance, Agreement, Arrests, Change to Group Activity, Disrupted Weapons Use, \n  Headquarters or Base Established, Looting/Property Destruction, \n  Non-violent Transfer of Territory, Other\n样本量: ~600K short event descriptions (from ACLED text snippets)\nLicense: 学术用途（需通过 ACLED 获取原始数据）\n下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task2 文件夹含测试集 TSV)；\n  训练数据需从 ACLED https://acleddata.com/ 获取\nGold-standard human labels: 是 (ACLED 专业编码员标注)\n引用论文: Haneczok et al. \"Fine-grained Event Classification in News-like Text Snippets - \n  Shared Task 2, CASE 2021\" (ACL Anthology 2021.case-1.23)\n备注: 测试集含标签可直接下载；训练数据建议从 ACLED 导出工具获取。K=25 是核心类别，\n  非常适合多分类研究。涵盖政治暴力、示威、战略发展三大类。\n```\n\n### 2. CASE 2021/2022 Task 1 -- Multilingual Protest News Detection\n\n```\n数据集名称: CASE Shared Task 1 (Multilingual Protest News Detection)\n类别数 K: Subtask 1 为二分类 (protest-related / not)；Subtask 2 为句子级二分类\n类别列表: [protest-related, not protest-related] (文档级)；[event sentence, non-event sentence] (句子级)\n样本量: Subtask 2 句子分类约 26,208 sentences；文档级数据涵盖多语言\nLicense: 公开（GitHub 直接下载）\n下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task1 文件夹)\n  CASE 2022: https://github.com/emerging-welfare/case-2022-multilingual-event\nGold-standard human labels: 是 (政治学家标注，inter-annotator adjudication)\n引用论文: Hürriyetoğlu et al. \"Multilingual Protest News Detection - Shared Task 1, CASE 2021\"\n  (ACL Anthology 2021.case-1.11)\n备注: ⚠️ K=2（二分类），不满足 K≥3 的要求。但与 Task 2 同源数据，可作为辅助。\n  语言覆盖：English, Spanish, Portuguese, Hindi, Mandarin, Turkish, Urdu。\n```\n\n### 3. GLOCON Gold Standard Corpus (Cross-Context News Corpus)\n\n```\n数据集名称: GLOCON Gold Standard Corpus / Cross-Context News Corpus for Protest Events\n类别数 K: 多层标注——文档级 (protest/non-protest)、句子级、token 级 (event trigger + arguments)\n类别列表: 文档级二分类 + token级事件类型（protest event triggers with typed arguments）\n样本量: 621,290 events from 9,509,193 news documents (自动预测);\n  Gold standard 部分规模较小（需确认具体数量）\nLicense: 需申请访问\n下载方式: https://github.com/emerging-welfare/glocongold (申请流程说明)\n  Dashboard: https://glocon.ku.edu.tr/\nGold-standard human labels: 是 (两位政治学家标注 + supervisor adjudication + \n  semi-automatic error detection)\n引用论文: Hürriyetoğlu et al. \"Cross-Context News Corpus for Protest Event-Related \n  Knowledge Base Construction\" Data Intelligence 2021\n备注: 覆盖 India, China, South Africa 新闻源。Gold standard 部分需要通过 GitHub 申请，\n  不是完全免费下载。大规模自动标注数据可通过 dashboard 获取。\n```\n\n### 4. GLOCON Database (Full)\n\n```\n数据集名称: GLOCON (Global Contentious Politics Database)\n类别数 K: 多类（事件类型包括 demonstrations, rallies, strikes, clashes, political violence 等）\n类别列表: [Demonstration, Rally, Strike, Clash, Political Violence, ...] (具体完整列表需查文档)\n样本量: 621,290 events（来自 India, South Africa, Argentina, Brazil, Turkey）\nLicense: 公开下载（需在网站注册）\n下载方式: https://glocon.ku.edu.tr/ (Download section) \n  数据格式: JSONL (每个新闻源一个文件)\nGold-standard human labels: 部分是（gold corpus 人工标注），大部分为自动预测标签\n引用论文: Duruşan & Hürriyetoğlu \"GLOCON Database: Design Decisions and User Manual (v1.0)\" \n  arXiv:2405.18613\n备注: 数据量大但标签为自动预测，非全部 gold-standard。适合大规模实验，\n  但需注意标签噪声。覆盖全球南方五国。\n```\n\n### 5. ACLED (Armed Conflict Location & Event Data)\n\n```\n数据集名称: ACLED (Armed Conflict Location & Event Data Project)\n类别数 K: 6 event types / 25 sub-event types / 3 disorder types\n类别列表: \n  Disorder types: [Political Violence, Demonstrations, Strategic Developments]\n  Event types: [Battles, Explosions/Remote Violence, Violence Against Civilians, \n    Riots, Protests, Strategic Developments]\n  Sub-event types (25): [Armed Clash, Government Regains Territory, Non-state Actor\n    Overtakes Territory, Chemical Weapon, Air/Drone Strike, Suicide Bomb, \n    Shelling/Artillery/Missile Attack, Remote Explosive/Landmine/IED, Grenade, \n    Sexual Violence, Attack, Abduction/Forced Disappearance, Violent Demonstration, \n    Mob Violence, Peaceful Protest, Protest with Intervention, Excessive Force \n    Against Protesters, Agreement, Arrests, Change to Group Activity, \n    Disrupted Weapons Use, HQ/Base Established, Looting/Property Destruction, \n    Non-violent Transfer of Territory, Other]\n样本量: >1.3 million events (截至 2022)，实时更新\nLicense: 开放访问（注册免费账户即可下载），学术/非营利用途免费\n下载方式: https://acleddata.com/conflict-data/download-data/ (Data Export Tool / API)\n  也可通过 HDX: https://data.humdata.org/organization/acled\nGold-standard human labels: 是 (专业编码员按 codebook 标注)\n引用论文: Raleigh et al. \"Introducing ACLED: An Armed Conflict Location and Event \n  Dataset\" Journal of Peace Research 2010\n备注: ⭐ 最佳候选之一。K=6 (event types) 或 K=25 (sub-event types)，样本量巨大，\n  专业人工标注，免费注册下载。每条记录包含事件文本描述 (notes 字段) 可用于 NLP。\n  注意：这不是\"原始新闻文本\"数据集，而是编码后的结构化事件数据（含短文本摘要）。\n```\n\n### 6. CEHA (Conflict Events in the Horn of Africa)\n\n```\n数据集名称: CEHA (Conflict Events in the Horn of Africa)\n类别数 K: 4 (event types) + 2 (relevance classification)\n类别列表: [Tribal/Communal/Ethnic Conflict, Religious Conflict, \n  Socio-political Violence Against Women, Climate-Related Security Risks]\n样本量: 500 event descriptions\nLicense: 公开 (GitHub)\n下载方式: https://github.com/dataminr-ai/CEHA\nGold-standard human labels: 是 (subject matter experts 标注)\n引用论文: CEHA: A Dataset of Conflict Events in the Horn of Africa (COLING 2025)\n备注: ⚠️ 样本量仅 500，不满足 ≥1000 的要求。K=4 满足要求。\n  数据来源于 ACLED 和 GDELT。适合低资源场景研究。\n```\n\n### 7. SPEED (Social, Political and Economic Event Database)\n\n```\n数据集名称: SPEED (Social Political Economic Event Dataset)\n类别数 K: 4 Tier-1 categories + 多个子类\n类别列表: Tier-1: [Political Expression Events, Politically Motivated Attacks, \n  Disruptive State Acts, Political Power Reconfigurations]\n样本量: 覆盖 Liberia, Philippines, Sierra Leone (1979-2008)，具体事件数未在搜索中确认\nLicense: 公开下载\n下载方式: https://databank.illinois.edu/datasets/IDB-7407320 \n  官方: https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED\nGold-standard human labels: 是 (Cline Center 编码员标注)\n引用论文: Cline Center for Advanced Social Research, UIUC\n备注: 结构化事件数据（非原始新闻文本）。覆盖时间较早(1979-2008)。\n  K=4 满足要求。需确认是否包含可用于 NLP 的文本字段。\n```\n\n### 8. PolDem Protest Event Dataset 30\n\n```\n数据集名称: PolDem-Protest Dataset 30\n类别数 K: 多类（action forms / organizational types 等多维标注）\n类别列表: Action forms (多类), 组织类型 (SMOs, initiatives, loose networks 等),\n  事件关联类型等\n样本量: 45,680 documents (30 European countries, 2000-2015)\nLicense: 需确认（网站下载）\n下载方式: https://poldem.eui.eu/ (Downloads section)\nGold-standard human labels: 是 (semi-automated coding of newswire reports + 人工验证)\n引用论文: PolDem documentation (EUI)\n备注: 覆盖 30 个欧洲国家。数据基于新闻通讯社报道。标注维度丰富，\n  不仅仅是事件类型，还有参与组织、暴力程度等。需要去网站确认具体类别数和下载条件。\n```\n\n### 9. HumAID (Human-Annotated Disaster Incidents Data)\n\n```\n数据集名称: HumAID\n类别数 K: 11\n类别列表: [Caution and Advice, Displaced People and Evacuations, \n  Don't Know or Can't Judge, Infrastructure and Utility Damage, \n  Injured or Dead People, Missing or Found People, Not Humanitarian, \n  Other Relevant Information, Requests or Urgent Needs, Rescue/Volunteering/Donation, \n  Sympathy and Support]\n样本量: ~77,000 manually annotated tweets from 19 disaster events (2016-2019)\nLicense: CC-BY-NC (学术用途)\n下载方式: https://crisisnlp.qcri.org/humaid_dataset.html\n  HuggingFace: https://huggingface.co/datasets/QCRI/HumAID-event-type\nGold-standard human labels: 是 (人工标注)\n引用论文: Alam et al. \"HumAID: Human-Annotated Disaster Incidents Data from Twitter\" \n  ICWSM 2021\n备注: ⚠️ 这是灾难事件数据集，不是抗议事件数据集。但方法论和任务类型相似，\n  可作为参考。K=11, 样本量充足，完全公开下载。\n```\n\n### 10. CrisisNLP / CrisisLexT26\n\n```\n数据集名称: CrisisLexT26 / CrisisLexT6\n类别数 K: 7 (information types including NOT RELATED)\n类别列表: [Affected Individuals, Infrastructure/Utilities, Donations/Volunteering, \n  Caution/Advice, Sympathy, Information Source, Not Related]\n样本量: CrisisLexT26 ~28,000 tweets from 26 events; CrisisLexT6 ~60,000 tweets from 6 events\nLicense: 公开\n下载方式: https://crisisnlp.qcri.org/\nGold-standard human labels: 是 (crowdsourced annotation)\n引用论文: Olteanu et al. \"CrisisLex: A Lexicon for Collecting and Filtering \n  Microblogged Communications in Crises\" ICWSM 2014\n备注: ⚠️ 同样是灾难/危机事件，非专门抗议事件。但标注框架可参考。\n```\n\n### 11. MPEDS (Machine-learning Protest Event Data System)\n\n```\n数据集名称: MPEDS\n类别数 K: 多类（protest form categories）\n类别列表: 包含多种抗议形式分类（具体列表需查看 codebook）\n样本量: 需确认（系统用于生成抗议事件数据）\nLicense: 公开 (GitHub + Zenodo)\n下载方式: https://github.com/MPEDS/mpeds (需 Git LFS)\n  Zenodo: https://zenodo.org/records/886459\n  Annotation Interface: https://github.com/MPEDS/mpeds-coder\nGold-standard human labels: 是 (系统辅助 + 人工验证)\n引用论文: Hanna \"MPEDS: Automating the Generation of Protest Event Data\" (2017)\n备注: 更多是一个工具/系统而非固定数据集。需要深入查看 repo 确认是否有现成标注数据。\n```\n\n### 12. Crowd Counting Consortium (CCC)\n\n```\n数据集名称: Crowd Counting Consortium U.S. Protest Event Data\n类别数 K: 494 discrete descriptive tags (多标签)\n类别列表: 494 个标签涵盖抗议类型、议题、参与者等\n样本量: 42,347 protest events (US, Jan 2017 - Jan 2021); 138,826 English articles\nLicense: 公开\n下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H\n  GitHub: https://github.com/rexdouglass/crowd-counting-consortium\nGold-standard human labels: 是 (人工标注)\n引用论文: Pressman & Chenoweth, Harvard Kennedy School\n备注: ⭐ 多标签（494 tags），非多分类。数据量大，完全公开（Harvard Dataverse）。\n  包含新闻文章 URL，但原始文本需自行爬取。结构化标签数据直接可用。\n```\n\n### 13. INDI-PROP (Indian Propaganda Dataset)\n\n```\n数据集名称: INDI-PROP\n类别数 K: 3 (article-level bias) + 多类 (narrative frames)\n类别列表: Article-level: [Pro-Government, Pro-Opposition, Neutral]\n  + event-specific fine-grained narrative frames\n样本量: 1,266 articles (CAA protest + Farmers' protest)\nLicense: 需确认（arXiv 论文附数据）\n下载方式: 需查看论文附录/GitHub（arXiv:2512.03582）\nGold-standard human labels: 是 (人工标注 + GPT-4o-mini 辅助)\n引用论文: \"Fine-grained Narrative Classification in Biased News Articles\" (arXiv:2512.03582)\n备注: 专注于印度抗议事件新闻的偏见与叙事分类。K=3 满足，样本量 1,266 满足 ≥1000。\n  但不是\"事件类型\"分类，而是\"叙事立场\"分类。\n```\n\n---\n\n## 总结推荐（满足全部筛选条件：K≥3, gold labels, public download, ≥1000 samples）\n\n| 排名 | 数据集 | K | 样本量 | 最适合用途 |\n|------|--------|---|--------|-----------|\n| 1 | **ACLED** | 6/25 | >1.3M | 政治暴力+抗议事件多分类，文本字段可用于 NLP |\n| 2 | **CASE 2021 Task 2** | 25 | ~600K snippets | 细粒度社会政治事件分类，NLP 共享任务标准 |\n| 3 | **CCC (Harvard)** | 494 tags (多标签) | 42K events | 美国抗议事件多标签分类 |\n| 4 | **PolDem-30** | 多类 | 45K docs | 欧洲 30 国抗议事件，多维标注 |\n| 5 | **GLOCON** | 多类 | 621K events | 全球南方五国，大规模自动标签 |\n| 6 | **INDI-PROP** | 3+ | 1,266 | 印度抗议事件叙事分类 |\n\n**首选推荐**：ACLED (K=25 sub-event types) 和 CASE 2021 Task 2 是最贴合需求的数据集 -- 专门面向抗议/政治事件、多分类、gold-standard 人工标注、公开下载、样本量远超 1000。\n\nSources:\n- [CASE 2021 Shared Task GitHub](https://github.com/emerging-welfare/case-2021-shared-task)\n- [CASE 2022 Multilingual Event GitHub](https://github.com/emerging-welfare/case-2022-multilingual-event)\n- [ACLED Data Download](https://acleddata.com/conflict-data/download-data/)\n- [ACLED Codebook](https://acleddata.com/methodology/acled-codebook/)\n- [GLOCON Database](https://glocon.ku.edu.tr/)\n- [GLOCON Gold Standard GitHub](https://github.com/emerging-welfare/glocongold)\n- [GLOCON Annotation Manuals (Zenodo)](https://zenodo.org/records/6540579)\n- [CEHA GitHub (Dataminr)](https://github.com/dataminr-ai/CEHA)\n- [SPEED Dataset (UIUC)](https://databank.illinois.edu/datasets/IDB-7407320)\n- [Cline Center SPEED Project](https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED)\n- [PolDem Protest Event Dataset](https://poldem.eui.eu/)\n- [CCC Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H)\n- [CCC GitHub](https://github.com/rexdouglass/crowd-counting-consortium)\n- [HumAID on HuggingFace](https://huggingface.co/datasets/QCRI/HumAID-event-type)\n- [CrisisNLP](https://crisisnlp.qcri.org/)\n- [MPEDS GitHub](https://github.com/MPEDS/mpeds)\n- [MPEDS Zenodo](https://zenodo.org/records/886459)\n- [Cross-Context News Corpus (MIT Press)](https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event)\n- [CASE 2021 Task 2 Overview Paper](https://aclanthology.org/2021.case-1.23/)\n- [INDI-PROP Paper](https://www.arxiv.org/pdf/2512.03582)\n- [ACLED on HDX](https://data.humdata.org/organization/acled)"
      }
    ],
    "totalDurationMs": 278539,
    "totalTokens": 53511,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1894,
      "cache_read_input_tokens": 45893,
      "output_tokens": 5723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5723,
          "cache_read_input_tokens": 45893,
          "cache_creation_input_tokens": 1894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1894,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 32
    }
  }
}
````

</details>

---

### Assistant

_source line 274_

<details><summary>Logged reasoning block</summary>

```text
Let me synthesize the results from all three agents. I need to carefully evaluate which datasets actually meet ALL the criteria:

1. K ≥ 3 (multi-class)
2. Gold-standard human labels
3. Fully public download (no approval needed)
4. English or multilingual
5. Sample size ≥ 1000

Key concern: The user explicitly mentioned ACLED was excluded due to ToS prohibiting ML use. So ACLED and CASE 2021 Task 2 (which uses ACLED data for training) are both problematic.


Now I'm examining the specific candidates more closely. POLDEM Protest Dataset 30 has six action categories with nearly 31,000 events and free access, but the gold labels come from semi-automated methods with moderate intercoder agreement, and the copyright notice raises licensing concerns. The Mass Mobilization Project offers seven categories for both protester demands and government responses across 17,000+ events on Harvard Dataverse, though I need to verify the full accessibility and labeling quality.

CASE 2021 Task 2 provides 25 sub-event types across 600K snippets but requires access to ACLED data for training, creating the same licensing barrier. The Crowd Counting Consortium has 42K events but uses 494 multi-label tags rather than discrete classes, and the text data isn't directly available. SPEED covers four categories with public access but appears to be structured data from an older period (1979-2008) without clear text fields. GLOCON requires an application to access.

Looking at other candidates, CEHA only has 500 samples which is too small, while MPEDS functions more as a tool than a dataset. INDI-PROP focuses on narrative bias rather than event classification, and though HumAID has 11 categories across 77K tweets with public access and gold labels, it covers disaster events rather than protest-specific ones. CrisisLexT26 similarly addresses crisis events with 7 categories and 28K tweets but again isn't protest-focused.

The strongest option remains PolDem-30, which offers six action form categories across roughly 30K events with free download and human-coded labels, though the annotation quality is moderate.

But I'm realizing a critical issue: for this annotation error attribution project, I actually need raw text paired with labels for NLP classification tasks. Most of these political event datasets are structured coded data extracted from newswires without the original text included. PolDem and MMD both fall into this trap—they're event metadata rather than text corpora. So I need to refocus on datasets that actually contain the source text alongside their labels, which narrows things down significantly.

Looking at what's viable, CASE 2021 Task 2 has text snippets with event type labels, though it depends on ACLED for training data which has licensing concerns—though the test set is publicly available on GitHub. PolDem-30 might have some text fields embedded in its CSV. If neither of these work out, I could pivot to crisis-related tweet datasets like HumAID or CrisisLexT26, or shift to entirely different classification domains like emotion or intent detection. Let me organize what I've found into a clear recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "dd1fa13d-c03d-441e-9b13-40a4d0f9fe7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DwAeG5uacN2zHE6mvucBP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9932,
      "cache_read_input_tokens": 23653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9932
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

_source line 275_

## 搜索结果汇总

**关键前提**：ACLED ToS 禁止 ML 用途，因此 ACLED 本身和依赖 ACLED 训练数据的 CASE 2021 Task 2 均排除。

---

### 符合条件的候选

#### 1. PolDem Protest Dataset 30
```
数据集名称: PolDem-Protest Dataset 30 (poldem-protest_30)
类别数 K: action_form = 6 (单标签); issue = 9 (多标签)
类别列表 (action_form): [demonstrations, violent protest, strikes, confrontations, 
  petitions/symbolic actions, other protest]
样本量: 30,852 events (30 European countries, 2000-2015)
License: 未明确标注，页脚 "© EUI & WZB. All rights reserved."
下载方式: 直接下载，无需注册
  CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv
Gold-standard human labels: 半自动流程 + 35名编码员人工标注
  intercoder: 事件识别 F1=0.60, 议题 κ=0.53
引用论文: Lorenzini et al. (2022) American Behavioral Scientist
备注: 
  ⚠️ 结构化事件数据，不含原始新闻全文（来源为通讯社 newswire，但 CSV 中可能只有编码字段）
  ⚠️ License 模糊，"All rights reserved" 有风险
  ✅ action_form K=6 单标签分类，标注质量中等，适合研究标注噪声
```

#### 2. Mass Mobilization Project (MMD)
```
数据集名称: Mass Mobilization Data Project
类别数 K: protester demand = 7 (多标签); government response = 7 (多标签)
类别列表 (demand): [labor/wages, land, police brutality, political process, 
  prices/taxes, removal of politician, social restrictions]
样本量: ~17,000 events (162 countries, 1990-2020)
License: Harvard Dataverse (CC0 Public Domain)
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
Gold-standard human labels: 是，人工编码员从 Lexis-Nexis 新闻编码
引用论文: Clark & Regan (2016), Harvard Dataverse
备注:
  ⚠️ 结构化事件数据，不含原始新闻文本
  ⚠️ Demand/response 为多标签 (0/1 binary columns)，非单标签多分类
  ✅ License 好 (CC0)，完全公开
```

#### 3. SPEED (Social Political Economic Event Database)
```
数据集名称: SPEED
类别数 K: 4 Tier-1 categories
类别列表: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 3 国 (1979-2008)，具体数量待确认
License: 公开
下载方式: https://databank.illinois.edu/datasets/IDB-7407320
Gold-standard human labels: 是 (Cline Center 编码员)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: ⚠️ 同样是结构化事件数据，非 NLP 文本分类格式
```

---

### 不满足条件的排除项

| 数据集 | 排除原因 |
|--------|---------|
| ACLED / CASE 2021 Task 2 | ToS 禁止 ML 用途（训练数据来自 ACLED） |
| GLOCON Gold | 需邮件申请 |
| CEHA | 样本量仅 500 |
| CCC | 494 多标签 tags，无原始文本 |
| CASE Task 1 | K=2 二分类 |
| MPEDS | 工具/系统，非固定数据集 |

---

### 核心问题

**protest/political event 领域没有理想的公开 NLP 文本分类数据集。** 上述候选全部是结构化编码数据（tabular），不含可直接用于文本分类的原始新闻文本。要做 NLP 实验需要自行匹配/爬取新闻，这引入额外复杂度和版权问题。

---

### 建议

如果坚持 protest 领域确实困难，建议考虑换到有成熟公开 NLP 数据集的任务类型：

| 替代方向 | 数据集 | K | 样本量 | 特点 |
|---------|--------|---|--------|------|
| **危机事件分类** | HumAID | 11 | ~77K tweets | CC-BY-NC, HuggingFace 直接下载，gold labels |
| **情感分类** | GoEmotions | 27/28 | 58K | Reddit 文本，多标签，Google 标注 |
| **意图分类** | CLINC150 / BANKING77 | 150/77 | 23K/13K | 对话意图，完全公开 |
| **新闻主题** | AG News | 4 | 120K | 经典 benchmark |

其中 **HumAID** 最接近 protest 领域（crisis/disaster events），K=11，标注质量好，且项目本身研究标注错误归因，crisis event 分类的标注难度和噪声模式与 protest 类似。

是否要：(1) 用 PolDem action_form 做实验（接受 license 风险 + 无原始文本限制），(2) 转向 HumAID 等 crisis 数据集，还是 (3) 申请 GLOCON？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "uuid": "43ac48c7-8d1c-4192-9187-cf0e13bce4a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DwAeG5uacN2zHE6mvucBP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9932,
      "cache_read_input_tokens": 23653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9932
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

_source line 276_

## 搜索结果汇总

**关键前提**：ACLED ToS 禁止 ML 用途，因此 ACLED 本身和依赖 ACLED 训练数据的 CASE 2021 Task 2 均排除。

---

### 符合条件的候选

#### 1. PolDem Protest Dataset 30
```
数据集名称: PolDem-Protest Dataset 30 (poldem-protest_30)
类别数 K: action_form = 6 (单标签); issue = 9 (多标签)
类别列表 (action_form): [demonstrations, violent protest, strikes, confrontations, 
  petitions/symbolic actions, other protest]
样本量: 30,852 events (30 European countries, 2000-2015)
License: 未明确标注，页脚 "© EUI & WZB. All rights reserved."
下载方式: 直接下载，无需注册
  CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv
Gold-standard human labels: 半自动流程 + 35名编码员人工标注
  intercoder: 事件识别 F1=0.60, 议题 κ=0.53
引用论文: Lorenzini et al. (2022) American Behavioral Scientist
备注: 
  ⚠️ 结构化事件数据，不含原始新闻全文（来源为通讯社 newswire，但 CSV 中可能只有编码字段）
  ⚠️ License 模糊，"All rights reserved" 有风险
  ✅ action_form K=6 单标签分类，标注质量中等，适合研究标注噪声
```

#### 2. Mass Mobilization Project (MMD)
```
数据集名称: Mass Mobilization Data Project
类别数 K: protester demand = 7 (多标签); government response = 7 (多标签)
类别列表 (demand): [labor/wages, land, police brutality, political process, 
  prices/taxes, removal of politician, social restrictions]
样本量: ~17,000 events (162 countries, 1990-2020)
License: Harvard Dataverse (CC0 Public Domain)
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
Gold-standard human labels: 是，人工编码员从 Lexis-Nexis 新闻编码
引用论文: Clark & Regan (2016), Harvard Dataverse
备注:
  ⚠️ 结构化事件数据，不含原始新闻文本
  ⚠️ Demand/response 为多标签 (0/1 binary columns)，非单标签多分类
  ✅ License 好 (CC0)，完全公开
```

#### 3. SPEED (Social Political Economic Event Database)
```
数据集名称: SPEED
类别数 K: 4 Tier-1 categories
类别列表: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 3 国 (1979-2008)，具体数量待确认
License: 公开
下载方式: https://databank.illinois.edu/datasets/IDB-7407320
Gold-standard human labels: 是 (Cline Center 编码员)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: ⚠️ 同样是结构化事件数据，非 NLP 文本分类格式
```

---

### 不满足条件的排除项

| 数据集 | 排除原因 |
|--------|---------|
| ACLED / CASE 2021 Task 2 | ToS 禁止 ML 用途（训练数据来自 ACLED） |
| GLOCON Gold | 需邮件申请 |
| CEHA | 样本量仅 500 |
| CCC | 494 多标签 tags，无原始文本 |
| CASE Task 1 | K=2 二分类 |
| MPEDS | 工具/系统，非固定数据集 |

---

### 核心问题

**protest/political event 领域没有理想的公开 NLP 文本分类数据集。** 上述候选全部是结构化编码数据（tabular），不含可直接用于文本分类的原始新闻文本。要做 NLP 实验需要自行匹配/爬取新闻，这引入额外复杂度和版权问题。

---

### 建议

如果坚持 protest 领域确实困难，建议考虑换到有成熟公开 NLP 数据集的任务类型：

| 替代方向 | 数据集 | K | 样本量 | 特点 |
|---------|--------|---|--------|------|
| **危机事件分类** | HumAID | 11 | ~77K tweets | CC-BY-NC, HuggingFace 直接下载，gold labels |
| **情感分类** | GoEmotions | 27/28 | 58K | Reddit 文本，多标签，Google 标注 |
| **意图分类** | CLINC150 / BANKING77 | 150/77 | 23K/13K | 对话意图，完全公开 |
| **新闻主题** | AG News | 4 | 120K | 经典 benchmark |

其中 **HumAID** 最接近 protest 领域（crisis/disaster events），K=11，标注质量好，且项目本身研究标注错误归因，crisis event 分类的标注难度和噪声模式与 protest 类似。

是否要：(1) 用 PolDem action_form 做实验（接受 license 风险 + 无原始文本限制），(2) 转向 HumAID 等 crisis 数据集，还是 (3) 申请 GLOCON？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 354198,
  "duration_api_ms": 1057130,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "total_cost_usd": 4.023937999999999,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 21744,
    "cache_read_input_tokens": 35494,
    "output_tokens": 3848,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21744,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2777,
        "cache_read_input_tokens": 23653,
        "cache_creation_input_tokens": 9932,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9932
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1217820,
      "outputTokens": 30723,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 80,
      "costUSD": 2.1714349999999993,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9299,
      "outputTokens": 19228,
      "cacheReadInputTokens": 1110466,
      "cacheCreationInputTokens": 123212,
      "webSearchRequests": 0,
      "costUSD": 1.852503,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f14c7937-3b1b-40d5-a322-07869c8180b2"
}
```

</details>

---
